---
title: "IR Receiver (Remote Control)"
description: "Decode signals from an infrared remote control with an IR receiver."
tags:
  - Sensors
  - Remote
  - Intermediate
level: Intermediate
board: "V1 & V2"
parts:
  - "micro:bit"
  - "IR receiver module (e.g. VS1838B)"
  - "IR remote control"
  - "Edge connector breakout"
source:
  - "microbit_tools/IR Receiver/ir_example.py"
  - "microbit_tools/IR Receiver/ir.py"
libraries:
  - "microbit_tools/IR Receiver/ir.py"
wiring:
  - part: "IR receiver"
    pins:
      OUT: P16
      VCC: 3V
      GND: GND
---

## What you'll build

Point an IR remote at the receiver and the micro:bit scrolls the code of the button you pressed.
Most small remotes (TV, LED-strip and kit remotes) use the **NEC protocol**, which this module decodes.

## Wiring

<!-- wiring -->

Pin 16 is only reachable through an **edge connector breakout board**.

- `get_signal()` returns straight away with `None` unless a leader has started. When one has, it times every
  pulse with `machine.time_pulse_us` (about 70 ms per frame) and builds the 32-bit code from the length of each gap.
- The frame carries the command twice, once inverted. If the two copies don't match, the frame is ignored,
  so noise never turns into a fake button.
- It returns the **command** (0–255). The remote's address is kept in `remote.address`.
- Call `get_signal(repeat=True)` to keep getting the command while a button is held, which is handy for volume or motors.
- `display.scroll(..., wait=False)` scrolls in the background, so the loop keeps listening for the next press.

!!! tip "Find your remote's codes"
    Every remote model uses its own numbers. Run the example, press each button and write down its code,
    then use those numbers in your own `if command == ...:` checks.

## Try this next

- Map remote buttons to actions, like moving the [servo](servo-motor.md).
- Use the remote to choose which image to display, e.g. `if command == 69: display.show(Image.HEART)`.
- Build a remote-controlled radio messenger.
