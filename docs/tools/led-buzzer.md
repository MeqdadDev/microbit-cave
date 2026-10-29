---
title: "LED and Buzzer"
description: "Turn an LED or buzzer on and off from pin 0 with button A."
tags:
  - Actuators
  - Sound
  - Buttons
  - Beginner
level: Beginner
board: "V1 & V2"
parts:
  - "micro:bit"
  - "LED + 220 Ω resistor or active buzzer"
  - "Jumper wires / crocodile clips"
source:
  - "microbit_tools/LED and Buzzer/led-buzzer-example.py"
wiring:
  - part: "LED or active buzzer"
    pins:
      "+ (long leg)": "P0 (through a 220 Ω resistor for an LED)"
      "− (short leg)": GND
---

## What you'll build

Hold button A to switch on an LED (or sound a buzzer) connected to pin 0.

## Wiring

<!-- wiring -->

## Code

```python title="led-buzzer-example.py" linenums="1"
--8<-- "microbit_tools/LED and Buzzer/led-buzzer-example.py"
```

## How it works

`pin0.write_digital(1)` sets pin 0 to 3 V (on); `write_digital(0)` sets it to 0 V (off).
The same code drives an LED or an **active** buzzer, since both just need power to work.

## Try this next

- Blink the LED with `sleep()` instead of holding the button.
- Use `pin0.write_analog(0–1023)` to dim the LED.
- Combine with the [PIR sensor](pir-sensor.md) to make a motion alarm.
