---
title: "Digital Compass"
description: "Use the built-in magnetometer to point north, and show the heading in degrees or as a direction."
tags:
  - Sensors
  - Compass
  - Buttons
  - Beginner
level: Beginner
board: "V1 & V2"
parts:
  - "micro:bit"
source:
  - "microbit/11 compass.py"
---

## What you'll build

A compass needle on the LED matrix that always points **north**. Press **A** to scroll the heading in degrees,
or **B** to scroll the direction (`N`, `NE`, `E`...).

## Code

```python title="11 compass.py" linenums="1"
--8<-- "microbit/11 compass.py"
```

!!! tip "Calibrating"
    The first time it runs, the micro:bit asks you to **tilt it to fill the screen**: roll it around until
    every LED is lit. Calibrate again with `compass.calibrate()` if the readings drift or you move near metal.

## How it works

- `compass.heading()` returns 0–359°, the direction the top of the board (the edge opposite the pins) faces.
  0° is north, 90° is east.
- `Image.ALL_CLOCKS` is a list of 12 clock-hand images, one every 30°. `((15 - heading) // 30) % 12` picks the
  hand pointing back towards north: turn to face east (90°) and the needle points left, to 9 o'clock.
- `(heading + 22) // 45` splits the circle into eight 45° slices, centred on N, NE, E and so on.

Keep the board **flat**: the heading is only accurate when the micro:bit is level.

## Try this next

- Show an arrow that points to a chosen direction, like your front door.
- Use `compass.get_field_strength()` to make a metal detector.
- Pair it with the [Spirit Level](12-spirit-level.md) so you know when the board is flat enough.
