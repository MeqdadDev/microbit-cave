---
title: Getting Started
description: Flash your first MicroPython program onto a BBC micro:bit.
---

## What you need

- A **BBC micro:bit** — every project is tested on **V2**; most also run on V1 (each page says which).
- A **micro-USB cable** that carries data, not just power.
- A computer with a modern browser — no installs needed for most projects.

## Flash your first program

1. Open the **[micro:bit Python Editor](https://python.microbit.org/)**.
2. Replace the starter code with this:

    ```python
    from microbit import *

    while True:
        display.scroll('Hello!')
        display.show(Image.HEART)
        sleep(2000)
    ```

3. Plug in the micro:bit and click **Send to micro:bit** (or **Save** and drag the `.hex` file onto the `MICROBIT` drive).
4. Watch the LEDs scroll your message. :tada:

!!! tip "Prefer a desktop editor?"
    [Thonny](https://thonny.org/) and [Mu](https://codewith.mu/) both support the micro:bit
    and give you a REPL to try code line by line.

## Copying helper libraries

Many [Sensors & Modules](tools/index.md) projects import a helper file such as `servo.py` or `ultrasonic.py`.
That file must be on the micro:bit **before** you run the example:

=== "Python Editor"

    Click **Open…**, choose the library `.py` file and pick **Add file** — then flash as usual.
    The editor bundles both files into one download.

=== "Command line (ufs)"

    ```bash
    pip install microfs
    ufs put servo.py
    ```

=== "Thonny"

    Open the library, then **File → Save as… → micro:bit** and keep the same file name.

## micro:bit V1 vs V2

| Feature | V1 | V2 |
|---------|----|----|
| Speaker & microphone | — | :white_check_mark: |
| Data logging (`log` module) | — | :white_check_mark: |
| Touch-sensitive logo | — | :white_check_mark: |
| More memory for larger programs | — | :white_check_mark: |

Every example page shows a **Board** field so you know what will run on your micro:bit.

## Next steps

Start with [Display Text on the LED Matrix](microbit/01-display-text.md), then work your way through the
[micro:bit Built-ins](microbit/index.md) before wiring up [Sensors & Modules](tools/index.md).
