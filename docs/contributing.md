---
title: Contributing
description: How to add a new tested example to micro:bit cave.
---

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.
Before adding a project, check the existing examples to avoid duplicates, and **test your code on a real micro:bit**.

## Adding a new example

Every example is two files: the **code** and a **docs page**. The docs page embeds the code directly
from the `.py` file, so the website always shows exactly what is in the repository.

### 1. Add the code

| Your example uses… | Put the code in… |
|--------------------|------------------|
| Only the micro:bit (display, radio, buttons, sensors on the board) | `microbit/<number> <name>.py` |
| External hardware (sensor, display, motor…) | `microbit_tools/<Module Name>/` — the example plus any library file |

### 2. Add the docs page

Copy [`templates/example-page.md`](https://github.com/MeqdadDev/microbit-cave/blob/main/templates/example-page.md)
into the matching docs folder and fill it in:

| Code folder | Docs page |
|-------------|-----------|
| `microbit/` | `docs/microbit/<NN>-<short-name>.md` — the number keeps the sidebar in order |
| `microbit_tools/` | `docs/tools/<short-name>.md` |

That's it — **no navigation file to edit**. New pages appear in the sidebar, on the section's card grid
and on the [Tags](tags.md) page automatically.

### The page template

Front matter from [`templates/example-page.md`](https://github.com/MeqdadDev/microbit-cave/blob/main/templates/example-page.md):

```yaml
--8<-- "templates/example-page.md:2:22"
```

Then these sections: **What you'll build**, **Wiring** (skip for built-in-only examples), **Code**, **How it works**, **Try this next**.

The front matter fields render as the info card at the top of each page. List helper files under
`libraries`: the card tells readers to copy them onto the micro:bit first.
If the example needs wiring, describe it once in `wiring:` and put `<!-- wiring -->` under the
**Wiring** heading: the site draws the wiring table and a diagram from it. Pads on the diagram follow the order you list
each part's pins in, so list them in the module's real pin order (swap two if wires cross).
Keep text values in double quotes — a title like `Radio: Sender` breaks the page without them.
Embed code with a snippet line inside a fenced block — for a single file:

````markdown
```python title="your-example.py" linenums="1"
;--8<-- "microbit_tools/Your Module/your-example.py"
```
````

If the example needs a library, put each file in its own `=== "Tab name"` block, as in the template.

### 3. Preview locally (optional)

```bash
pip install -r requirements-docs.txt
mkdocs serve
```

Open <http://127.0.0.1:8000> — the site reloads as you edit.

## What happens when you open a PR

- A **docs check** builds the site with `mkdocs build --strict`. It fails on links to missing pages, code files
  that don't exist, and example pages with incomplete front matter (missing fields, unquoted `:`, a level that
  isn't in the tags). `mkdocs serve` shows the same warnings while you edit.
- Once the PR is **merged into `main`**, the site is rebuilt and deployed to GitHub Pages automatically.
