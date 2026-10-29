"""MkDocs hook: turn a page's `wiring:` front matter into a wiring table and an SVG diagram.

A line `<!-- wiring -->` is replaced with the table and diagram:

    wiring:
      - part: "HC-SR04 (5 V)"
        pins:
          VCC: 5V                                   # +5V of an external supply (shares GND)
          Trig: P13
          Echo: {to: P15, divider: "1 kΩ / 2 kΩ"}   # 5 V signal brought down to ~3.3 V
          GND: "GND (text after the pin is a note shown in the table)"

Pages with a divider or an external supply get a GND-rail layout so every ground joins visibly.
For several wiring options, make `wiring` a mapping of name -> list and use `<!-- wiring NAME -->`.
"""
import logging
import re
from html import escape

log = logging.getLogger("mkdocs.hooks.wiring")

MARKER = re.compile(r"^([ \t]*)<!-- wiring(?: (\S+))? -->$", re.M)  # only on a line of its own
ROW = 30
BOARD_X, BOARD_W = 16, 150
PAD_X = BOARD_X + BOARD_W
PART_X, PART_W = 420, 190
WIDTH = 640
POWER = ("3V", "3V3")
SUPPLY = "5V"


def _connections(part):
    for pin, value in part["pins"].items():
        if isinstance(value, dict):
            target, divider = str(value["to"]), value.get("divider")
        else:
            target, divider = str(value), None
        name, _, note = target.partition(" ")
        yield str(pin), name, note, divider


def _table(parts):
    rows = ["| Part | Part pin | micro:bit pin |", "|------|----------|---------------|"]
    for part in parts:
        for pin, name, note, divider in _connections(part):
            cell = "`+5V` of an external 5 V supply" if name == SUPPLY else "`%s`" % name
            if divider:
                first, _, second = (s.strip() for s in divider.partition("/"))
                cell += " through %s; a %s resistor also links `%s` to `GND`" % (first, second, name)
            if note:
                cell += " " + note
            rows.append("| %s | %s | %s |" % (part["part"], pin, cell))
    return "\n".join(rows)


def _zigzag(x, y, length, horizontal):
    pts = []
    for i in range(9):
        offset = 0 if i in (0, 8) else (-7 if i % 2 else 7)
        along = length * i / 8
        pts.append("%.1f %.1f" % ((x + along, y + offset) if horizontal else (x + offset, y + along)))
    return '<polyline class="mc-wd-resistor" points="%s"/>' % " ".join(pts)


def _dot(cls, x, y, r=4.5):
    return '<circle class="mc-wire-end %s" cx="%.1f" cy="%.1f" r="%s"/>' % (cls, x, y, r)


def _svg(parts, title):
    conns_all = [c for part in parts for c in _connections(part)]
    rail = any(divider or name == SUPPLY for _, name, _, divider in conns_all)
    shapes, wires, labels = [], [], []

    # Optional 5 V supply above the parts (rail layout only).
    y, supply = 46, None  # supply = bottom edge of the supply box
    if rail and any(name == SUPPLY for _, name, _, _ in conns_all):
        s_top, s_bottom = 30, 84
        supply = s_bottom
        plus_x, gnd_x = PART_X + 40, PART_X + PART_W - 40
        shapes.append('<rect class="mc-wd-box" x="%d" y="%d" width="%d" height="%d" rx="10"/>' % (PART_X, s_top, PART_W, s_bottom - s_top))
        labels.append('<text class="mc-wd-part" x="%d" y="%d">5 V supply</text>' % (PART_X + 14, s_top + 22))
        for text, x in (("+5V", plus_x), ("GND", gnd_x)):
            shapes.append('<rect class="mc-wd-pad" x="%d" y="%d" width="22" height="16" rx="4"/>' % (x - 11, s_bottom - 8))
            labels.append('<text class="mc-wd-label mc-wd-label--center" x="%d" y="%d">%s</text>' % (x, s_bottom - 14, text))
        y = s_bottom + 50

    # Parts on the right.
    links, grounds, powered = [], [], []  # (pad, y, divider) / part GND pin ys / 5V pin ys
    for part in parts:
        conns = list(_connections(part))
        height = len(conns) * ROW + 12
        labels.append('<text class="mc-wd-part" x="%d" y="%d">%s</text>' % (PART_X, y - 10, escape(part["part"])))
        shapes.append('<rect class="mc-wd-box" x="%d" y="%d" width="%d" height="%d" rx="10"/>' % (PART_X, y, PART_W, height))
        for i, (pin, name, _, divider) in enumerate(conns):
            py = y + 6 + ROW // 2 + i * ROW
            labels.append('<text class="mc-wd-label" x="%d" y="%d">%s</text>' % (PART_X + 16, py + 4, escape(pin)))
            if rail and name == "GND":
                grounds.append(py)
            elif name == SUPPLY:
                powered.append(py)
            else:
                links.append((name, py, divider))
        y += height + 40
    parts_bottom = y - 40

    # micro:bit pads, each level with the pins it feeds; in the rail layout GND is always present and last.
    targets = {}
    for name, py, _ in links:
        targets.setdefault(name, []).append(py)
    if rail:
        targets.pop("GND", None)

    pad_y, last = {}, 80 - ROW
    for pin in sorted(targets, key=lambda p: sum(targets[p]) / len(targets[p])):
        pad_y[pin] = max(sum(targets[pin]) / len(targets[pin]), last + ROW)
        last = pad_y[pin]
    if rail:
        pad_y["GND"] = last + ROW

    board_top, board_bottom = max(22, min(pad_y.values()) - 64), max(pad_y.values()) + 24
    shapes.append('<rect class="mc-wd-board" x="%d" y="%d" width="%d" height="%d" rx="18"/>'
                  % (BOARD_X, board_top, BOARD_W, board_bottom - board_top))
    labels.append('<text class="mc-wd-board-label" x="%d" y="%d">micro:bit</text>' % (BOARD_X + 16, board_top + 26))
    for pin, py in pad_y.items():
        shapes.append('<rect class="mc-wd-pad" x="%d" y="%.1f" width="22" height="18" rx="4"/>' % (PAD_X - 22, py - 9))
        labels.append('<text class="mc-wd-pin" x="%d" y="%.1f">%s</text>' % (PAD_X - 30, py + 4, escape(pin)))

    classes, signals = {}, 0
    for pin in sorted(pad_y, key=lambda p: pad_y[p]):
        if pin == "GND":
            classes[pin] = "mc-wire--gnd"
        elif pin in POWER:
            classes[pin] = "mc-wire--power"
        else:
            classes[pin] = "mc-wire--s%d" % (signals % 5)
            signals += 1

    rail_y = max(board_bottom, parts_bottom) + 36
    mid = (PAD_X + PART_X) / 2
    node_x, r1_x = 262, 318
    for name, y2, divider in links:
        cls, y1 = classes[name], pad_y[name]
        if not divider:
            wires.append('<path class="mc-wire %s" d="M%d %.1f C%.1f %.1f %.1f %d %d %d"/>' % (cls, PAD_X, y1, mid, y1, mid, y2, PART_X, y2))
        else:
            first, _, second = (s.strip() for s in divider.partition("/"))
            wires.append('<path class="mc-wire %s" d="M%d %.1f C%.1f %.1f %.1f %d %d %d H%d M%d %d H%d"/>'
                         % (cls, PAD_X, y1, (PAD_X + node_x) / 2, y1, (PAD_X + node_x) / 2, y2, node_x, y2, r1_x, r1_x + 64, y2, PART_X))
            wires.append(_zigzag(r1_x, y2, 64, True))
            labels.append('<text class="mc-wd-note mc-wd-note--center mc-wd-value" x="%d" y="%d">%s</text>' % (r1_x + 32, y2 - 13, escape(first)))
            wires.append('<path class="mc-wire mc-wire--gnd" d="M%d %d V%d M%d %d V%.1f"/>' % (node_x, y2, y2 + 12, node_x, y2 + 64, rail_y))
            wires.append(_zigzag(node_x, y2 + 12, 52, False))
            labels.append('<text class="mc-wd-note mc-wd-value" x="%d" y="%d">%s</text>' % (node_x + 14, y2 + 42, escape(second)))
            wires.append('<circle class="mc-wd-node" cx="%d" cy="%d" r="5"/>' % (node_x, y2))
            wires.append(_dot("mc-wire--gnd", node_x, rail_y, 4))
        wires.append(_dot(cls, PART_X, y2))

    if rail:
        gnd_drop = PAD_X + 24
        wires.append('<path class="mc-wire mc-wire--gnd" d="M%d %.1f H%d V%.1f"/>' % (PAD_X, pad_y["GND"], gnd_drop, rail_y))
        wires.append(_dot("mc-wire--gnd", gnd_drop, rail_y, 4))
        rail_end = PART_X - 24
        for gy in grounds:
            wires.append('<path class="mc-wire mc-wire--gnd" d="M%d %d H%d V%.1f"/>' % (PART_X, gy, PART_X - 24, rail_y))
            wires.append(_dot("mc-wire--gnd", PART_X, gy))
            wires.append(_dot("mc-wire--gnd", PART_X - 24, rail_y, 4))
        if supply:
            top_lane = supply + 16
            for vy in powered:
                wires.append('<path class="mc-wire mc-wire--power" d="M%d %d V%d H%d V%d H%d"/>'
                             % (plus_x, supply + 8, top_lane, PART_X - 14, vy, PART_X))
                wires.append(_dot("mc-wire--power", PART_X, vy))
            rail_end = PART_X + PART_W + 18
            wires.append('<path class="mc-wire mc-wire--gnd" d="M%d %d V%d H%d V%.1f"/>'
                         % (gnd_x, supply + 8, top_lane, rail_end, rail_y))
            wires.append(_dot("mc-wire--gnd", rail_end, rail_y, 4))
        shapes.append('<path class="mc-wd-rail" d="M%d %.1f H%d"/>' % (gnd_drop, rail_y, rail_end))
        labels.append('<text class="mc-wd-note" x="%d" y="%.1f">GND rail: all grounds join here</text>' % (gnd_drop + 10, rail_y + 18))

    height = (rail_y + 30) if rail else (max(board_bottom, parts_bottom) + 18)
    return ('<div class="mc-wiring"><svg viewBox="0 0 %d %d" role="img" aria-label="%s">%s</svg></div>'
            % (WIDTH, height, escape(title), "".join(shapes + wires + labels)))


def on_page_markdown(markdown, page, config, files):
    if not MARKER.search(markdown):
        return markdown
    wiring = page.meta.get("wiring")

    def replace(match):
        indent, variant = match.group(1), match.group(2)
        if isinstance(wiring, dict):
            parts = wiring.get(variant)
        else:
            parts = wiring if variant is None else None
        if not parts:
            log.warning("%s: no wiring found for %s", page.file.src_uri, match.group(0).strip())
            return match.group(0)
        title = "Wiring diagram for %s%s" % (page.title, " (%s)" % variant if variant else "")
        block = _table(parts) + "\n\n" + _svg(parts, title)
        return "\n".join(indent + line if line else line for line in block.split("\n"))

    return MARKER.sub(replace, markdown)
