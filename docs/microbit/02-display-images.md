---
title: "Display Built-in Images"
description: "Cycle through the micro:bit's built-in images: hearts, faces and moods."
tags:
  - Display
  - Beginner
level: Beginner
board: "V1 & V2"
parts:
  - "micro:bit"
source:
  - "microbit/2 display images.py"
---

## What you'll build

Animate the LED matrix by stepping through nine built-in images, one per second.

## Code

```python title="2 display images.py" linenums="1"
--8<-- "microbit/2 display images.py"
```

## How it works

MicroPython ships with dozens of ready-made 5×5 images on the `Image` class (`Image.HEART`, `Image.HAPPY`, `Image.SAD`, …).
Each `display.show()` replaces what is on screen, and `sleep(1000)` holds it for a second.

See the full list in the [MicroPython images tutorial](https://microbit-micropython.readthedocs.io/en/latest/tutorials/images.html).

## Try this next

- Put the images in a list and loop over it instead of repeating `show`/`sleep`.
- Pass the whole list to `display.show(images, delay=500)` to animate in one line.
- Design your own image — see [Display DIY Images](03-display-diy-images.md).
