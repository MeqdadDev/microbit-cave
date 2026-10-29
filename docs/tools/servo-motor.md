---
title: "Servo Motor"
description: "Move a 9g servo between 0° and 90° with the micro:bit buttons."
tags:
  - Actuators
  - Buttons
  - Intermediate
level: Intermediate
board: "V1 & V2"
parts:
  - "micro:bit"
  - "SG90 (9g) servo motor"
  - "Jumper wires"
source:
  - "microbit_tools/Servo Motor/servo-example.py"
  - "microbit_tools/Servo Motor/servo.py"
libraries:
  - "microbit_tools/Servo Motor/servo.py"
wiring:
  - part: "SG90 servo"
    pins:
      "Signal (orange)": P0
      "Power (red)": "3V (or an external 5 V supply for heavier loads)"
      "Ground (brown)": GND
---

## What you'll build

Press button A to turn the servo to 90°, button B to return it to 0°.

## Wiring

<!-- wiring -->

## Code

=== "Example"

    ```python title="servo-example.py" linenums="1"
    --8<-- "microbit_tools/Servo Motor/servo-example.py"
    ```

=== "servo.py (library)"

    ```python title="servo.py" linenums="1"
    --8<-- "microbit_tools/Servo Motor/servo.py"
    ```

## How it works

Hobby servos read the width of a repeating pulse to choose their angle. `set_angle()` maps 0–180° onto an
analog duty value and writes it with `pin.write_analog()`.

## Try this next

- Sweep smoothly from 0° to 180° in a loop.
- Control the angle by tilting the board with `accelerometer.get_x()`.
- Build a pointer that shows the temperature on a dial.
