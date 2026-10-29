---
title: "OLED Screen (SSD1306)"
description: "Print text on a 128×64 SSD1306 OLED display over I²C."
tags:
  - Display
  - I2C
  - Intermediate
level: Intermediate
board: "V1 & V2"
parts:
  - "micro:bit"
  - "SSD1306 128×64 I²C OLED"
  - "Edge connector breakout"
  - "Jumper wires"
source:
  - "microbit_tools/OLED Screen/print-text-ssd1306-oled-example1.py"
  - "microbit_tools/OLED Screen/ssd1306.py"
  - "microbit_tools/OLED Screen/ssd1306_text.py"
libraries:
  - "microbit_tools/OLED Screen/ssd1306.py"
  - "microbit_tools/OLED Screen/ssd1306_text.py"
wiring:
  - part: "SSD1306 OLED"
    pins:
      SCL: P19
      SDA: P20
      VCC: 3V
      GND: GND
---

## What you'll build

Give your micro:bit a bigger screen: write lines of text on an SSD1306 OLED.

## Wiring

<!-- wiring -->

The OLED uses the micro:bit's default I²C pins, reachable through an **edge connector breakout board**.

## Code

=== "Example"

    ```python title="print-text-ssd1306-oled-example1.py" linenums="1"
    --8<-- "microbit_tools/OLED Screen/print-text-ssd1306-oled-example1.py"
    ```

=== "ssd1306.py (library)"

    ```python title="ssd1306.py" linenums="1"
    --8<-- "microbit_tools/OLED Screen/ssd1306.py"
    ```

=== "ssd1306_text.py (library)"

    ```python title="ssd1306_text.py" linenums="1"
    --8<-- "microbit_tools/OLED Screen/ssd1306_text.py"
    ```

## How it works

- `initialize()` sends the start-up commands to the OLED at I²C address `0x3C`; `clear_oled()` blanks it.
- `add_text(x, y, text)` writes text at column `x`, row `y` (rows are 8 pixels tall).

## Try this next

- Show live sensor readings, like temperature or distance.
- Display the last message received over [radio](../microbit/04-radio-messaging.md).
- Build a scoreboard updated with buttons A and B.
