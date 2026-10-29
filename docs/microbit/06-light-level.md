---
title: "Light Sensor (built-in)"
description: "Use the LED matrix as a light sensor to tell day from night."
tags:
  - Sensors
  - Display
  - Beginner
level: Beginner
board: "V1 & V2"
parts:
  - "micro:bit"
source:
  - "microbit/6 light-level.py"
---

## What you'll build

The LED matrix can also *sense* light. Read the ambient light level and scroll **Day** or **Night**.

## Code

```python title="6 light-level.py" linenums="1"
--8<-- "microbit/6 light-level.py"
```

## How it works

`display.read_light_level()` returns a value from `0` (dark) to `255` (bright). Below `150` the program decides it is night.

## Try this next

- Scroll the raw light level to find a better threshold for your room.
- Turn the display into a night-light that glows when it gets dark.
- Log light levels over a day with [Data Logging](09-data-logger.md).
