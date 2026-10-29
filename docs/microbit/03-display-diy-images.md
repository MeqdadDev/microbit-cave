---
title: "Display DIY Images"
description: "Draw your own picture on the LED matrix pixel by pixel, with brightness levels."
tags:
  - Display
  - Beginner
level: Beginner
board: "V1 & V2"
parts:
  - "micro:bit"
source:
  - "microbit/3 display DIY images.py"
---

## What you'll build

Design a custom image — a little boat — by describing the brightness of every LED.

## Code

```python title="3 display DIY images.py" linenums="1"
--8<-- "microbit/3 display DIY images.py"
```

## How it works

An `Image` can be built from a string of five rows separated by `:`. Each digit is one LED's brightness,
from `0` (off) to `9` (brightest), so `"99999"` is a fully lit row and `"06050"` lights two LEDs dimly.

## Try this next

- Draw your initials or a small animal.
- Make two frames and alternate them to animate the boat rocking.
- Use `display.set_pixel(x, y, brightness)` to change a single LED.
