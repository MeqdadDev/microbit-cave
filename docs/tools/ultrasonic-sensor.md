---
title: "Ultrasonic Sensor"
description: "Measure distance in centimetres with an HC-SR04 ultrasonic sensor."
tags:
  - Sensors
  - Display
  - Intermediate
level: Intermediate
board: "V1 & V2"
parts:
  - "micro:bit"
  - "HC-SR04P (3 V) or HC-SR04 (5 V) ultrasonic sensor"
  - "5 V module only: 1 kΩ and 2 kΩ resistors, and a 5 V supply"
  - "Edge connector breakout"
  - "Jumper wires"
source:
  - "microbit_tools/Ultrasonic Sensor/ultrasonic-example-1.py"
  - "microbit_tools/Ultrasonic Sensor/ultrasonic.py"
libraries:
  - "microbit_tools/Ultrasonic Sensor/ultrasonic.py"
wiring:
  3v:
    - part: "HC-SR04P (3 V)"
      pins:
        Trig: P13
        Echo: P15
        VCC: 3V
        GND: GND
  5v:
    - part: "HC-SR04 (5 V)"
      pins:
        VCC: 5V
        Trig: P13
        Echo: {to: P15, divider: "1 kΩ / 2 kΩ"}
        GND: GND
---

## What you'll build

Measure the distance to an object using sound pulses and scroll it on the display.

## Wiring

Pins 13 and 15 are only reachable through an **edge connector breakout board**. Pick the tab for your module.
The **HC-SR04P** runs on 3 V; the classic **HC-SR04** needs 5 V (check the label or the seller's listing).

=== "3 V module (HC-SR04P)"

    <!-- wiring 3v -->

=== "5 V module (HC-SR04)"

    !!! danger "Never connect a 5 V Echo straight to the micro:bit"
        A 5 V HC-SR04 sends 5 V out of **Echo**, but micro:bit pins only tolerate about 3.6 V.
        Wired directly, it can damage the micro:bit. Two resistors, a **voltage divider**, bring the signal down to
        5 V × 2 kΩ / (1 kΩ + 2 kΩ) ≈ **3.3 V**. No 2 kΩ resistor? Use two 1 kΩ in series, or 2.2 kΩ (≈ 3.4 V).

    The micro:bit has no 5 V pin, so power the sensor from a separate **5 V supply**, such as a breakout board with
    a 5 V rail, or a USB power bank through a USB breakout. **Connect the supply's GND to the micro:bit's GND**:
    without a shared ground, the signals have nothing to be measured against. **Trig** can be wired directly,
    because 3 V is high enough for the sensor to read.

    <!-- wiring 5v -->

## Code

=== "Example"

    ```python title="ultrasonic-example-1.py" linenums="1"
    --8<-- "microbit_tools/Ultrasonic Sensor/ultrasonic-example-1.py"
    ```

=== "ultrasonic.py (library)"

    ```python title="ultrasonic.py" linenums="1"
    --8<-- "microbit_tools/Ultrasonic Sensor/ultrasonic.py"
    ```

## How it works

The sensor sends an ultrasonic ping from **Trig** and holds **Echo** high until the echo returns.
The library times that pulse with `time_pulse_us` and converts it to centimetres using the speed of sound.
Pass `Ultrasonic(trig=..., echo=...)` to use other pins.

If no echo returns (nothing within about 4 m, or a wiring problem), the reading is zero or negative,
so the example shows `?` instead of a misleading number. Waiting for a missing echo takes up to one second.

## Try this next

- Make a parking sensor that beeps faster as objects get closer.
- Show distance as a bar graph on the LED matrix.
- Combine with the [servo](servo-motor.md) to build a sweeping radar.
