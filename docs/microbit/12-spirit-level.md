---
title: "Spirit Level"
description: "A rolling-ball level: tilt the micro:bit and an LED rolls downhill using the accelerometer's x and y axes."
tags:
  - Accelerometer
  - Display
  - Beginner
level: Beginner
board: "V1 & V2"
parts:
  - "micro:bit"
source:
  - "microbit/12 spirit-level.py"
---

## What you'll build

Tilt the micro:bit and a bright LED rolls to the lowest side, like a ball on a tray. When the board is flat,
a target appears in the middle.

## Code

```python title="12 spirit-level.py" linenums="1"
--8<-- "microbit/12 spirit-level.py"
```

## How it works

- `accelerometer.get_x()` and `get_y()` measure tilt in **milli-g**: about 0 when flat and ±1024 when that edge
  points straight down. Tilt right and x goes positive. Tilt the pin edge down and y goes positive.
- `to_led()` turns each reading into an LED position: every 300 milli-g of tilt moves the ball one LED from the
  middle, and `min`/`max` keep it on the 5×5 grid.
- `display.set_pixel(x, y, 9)` lights one LED at full brightness. When the ball is centred, the custom `LEVEL`
  image shows a dim ring around it.

## Try this next

- Make it more sensitive by changing `300` to `150`.
- Turn it into a maze game: avoid "wall" pixels while you roll the ball to a goal.
- Use `accelerometer.was_gesture("face down")` to switch the level off when the board is turned over.
