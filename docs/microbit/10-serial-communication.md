---
title: "micro:bit Serial Communication"
description: "Stream sensor readings and button events from the micro:bit to your computer over USB, and send a status back."
tags:
  - Serial
  - Computer
  - Sensors
  - Buttons
  - Intermediate
level: Intermediate
board: "V1 & V2"
runs_on: "micro:bit + your computer (standard Python)"
parts:
  - "micro:bit"
  - "USB data cable"
  - "Computer with Python 3"
source:
  - "microbit/10 microbit serial sender.py"
  - "microbit/10 microbit serial.py"
---

## What you'll build

A two-way link over the USB cable. The micro:bit becomes a **sensor station**: it streams its temperature and
light level every second and reports button presses and shakes. A Python script on your **computer** turns those
messages into a readable live log, decides whether it is too hot, and replies. The micro:bit then shows a
tick (:white_check_mark:) or a cross (:x:).

```text
Listening to the micro:bit on COM19 (Ctrl+C to stop)
Temperature: 24 C | Light: 132 (dim) -> OK
Button A pressed
Temperature: 29 C | Light: 210 (bright) -> ALERT
Gesture detected: shake
```

## The message format

Both sides agree on a tiny text protocol: **one message per line, fields separated by commas**.

| Direction | Message | Meaning |
|-----------|---------|---------|
| micro:bit → computer | `SENSORS,24,132` | Temperature in °C, light level 0–255 (every second) |
| micro:bit → computer | `BUTTON,A` / `BUTTON,B` | A button was pressed |
| micro:bit → computer | `GESTURE,shake` | The micro:bit was shaken |
| computer → micro:bit | `OK` | Temperature is fine: show a tick |
| computer → micro:bit | `ALERT` | Temperature ≥ 28 °C: show a cross |

## Code

=== "micro:bit side"

    Flash this to the micro:bit.

    ```python title="10 microbit serial sender.py" linenums="1"
    --8<-- "microbit/10 microbit serial sender.py"
    ```

=== "Computer side"

    Run this on your computer with standard Python.

    ```python title="10 microbit serial.py" linenums="1"
    --8<-- "microbit/10 microbit serial.py"
    ```

!!! warning "Run it in this order"
    1. Flash **10 microbit serial sender.py** to the micro:bit.
    2. On your computer: `pip install pyserial`, then set `PORT` to your micro:bit's port —
       `COM3`-style on Windows (Device Manager → Ports), `/dev/ttyACM0` on Linux, `/dev/cu.usbmodem…` on macOS.
    3. **Close the Python Editor's serial monitor** (or any other program using the port), then run
       `python "10 microbit serial.py"`. Only one program can open the serial port at a time.

## How it works

**On the micro:bit**

- `print()` sends text over the USB cable at 115200 baud and adds a line ending, so every `print` is one message.
- `running_time()` tracks milliseconds, so sensors are reported once per second without `sleep(1000)`
  blocking the button and shake checks.
- `uart.any()` checks for a reply without waiting; `uart.readline()` reads it as bytes, which
  `str(reply, "utf-8").strip()` turns into `"OK"` or `"ALERT"`.

**On the computer**

- `port.readline()` waits (up to the 1-second `timeout`) for a complete line, so messages are never split.
- `handle_message()` splits the line at the first comma to find the message type, then handles each type.
  Malformed lines are reported instead of crashing the script.
- `take_action()` holds the decision: change `HOT_TEMPERATURE` to set when the alert fires.
- `port.write(b"OK\n")` sends the reply back down the same cable.

!!! note "About the temperature"
    `temperature()` reads the micro:bit's processor, which runs a few degrees warmer than the room —
    adjust `HOT_TEMPERATURE` to suit your board.

## Try this next

- Save every `SENSORS` reading to a CSV file and plot it with a spreadsheet or `matplotlib`.
- Add a `SOUND` message using the V2 microphone's `microphone.sound_level()`.
- Let button B ask the computer for the time and scroll the reply on the micro:bit.
- Combine with [Radio Messaging](04-radio-messaging.md): one micro:bit plugged into the computer relays readings
  from wireless micro:bits around the room.
