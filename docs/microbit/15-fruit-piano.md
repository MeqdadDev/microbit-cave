---
title: "Fruit Piano"
description: "Turn fruit into piano keys with the micro:bit's touch pins and touch logo."
tags:
  - Touch
  - Sound
  - Music
  - Beginner
level: Beginner
board: "V2 only"
parts:
  - "micro:bit V2"
  - "2 pieces of fruit (bananas, apples...)"
  - "3 crocodile clip leads"
source:
  - "microbit/15 fruit-piano.py"
wiring:
  - part: "Fruit 1 (key C)"
    pins:
      clip: P1
  - part: "Fruit 2 (key E)"
    pins:
      clip: P2
  - part: "You (other hand)"
    pins:
      hold: GND
---

## What you'll build

A three-key piano. Touch the fruit on pin 1 for **C**, the fruit on pin 2 for **E**, and the gold **touch logo** for **G**.
The note's letter appears on the display while it plays.

## Wiring

<!-- wiring -->

The touch logo on the front needs no wiring.

## Code

```python title="15 fruit-piano.py" linenums="1"
--8<-- "microbit/15 fruit-piano.py"
```

## How it works

- `pin1.is_touched()` works by noticing a tiny current flowing from the pin, through you, to `GND`. That's why you
  hold the GND clip, and why anything that conducts, like fruit, plants or water, can be a key.
- `pin_logo.is_touched()` senses your finger **capacitively**, so it needs no GND connection.
- The `KEYS` list pairs each touch input with a note, so adding a key is one extra line.
  `note[0]` is the note's first letter, which is shown while it plays.
- `music.play("C4:2")` plays a short note (250 ms), so holding a key repeats it.

!!! note "Why not pin 0?"
    The `music` module also sends sound out of pin 0, which would interfere with using it as a key.

## Try this next

- Add more keys with an edge connector breakout: other pins can be touch keys too.
- Play a chord when two fruits are touched together.
- Record what you play into a list and replay it with button A.
