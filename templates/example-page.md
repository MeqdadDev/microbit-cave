---
title: "Short Descriptive Title"
description: "One sentence shown on the section cards and in search results."
tags:
  - Sensors
  - Beginner
level: Beginner            # Beginner | Intermediate | Advanced
board: "V1 & V2"           # V1 & V2 | V2 only | V2 (tested)
parts:
  - micro:bit
  - "Your sensor or module"
source:                    # paths from the repo root; first file is the main example
  - "microbit_tools/Your Module/your-example.py"
  - "microbit_tools/Your Module/your_library.py"
libraries:                 # helper files readers must copy onto the micro:bit first; omit if none
  - "microbit_tools/Your Module/your_library.py"
wiring:                    # drawn as a table + diagram where <!-- wiring --> appears; omit if nothing is wired
  - part: "Your sensor or module"
    pins:                  # part pin: micro:bit pin, optionally followed by a note
      SIGNAL: P0
      VCC: 3V                # or 5V for an external 5 V supply; see the Ultrasonic page
      GND: GND
---

## What you'll build

One or two sentences describing what the project does.

## Wiring

<!-- wiring -->

## Code

=== "Example"

    ```python title="your-example.py" linenums="1"
    --8<-- "microbit_tools/Your Module/your-example.py"
    ```

=== "your_library.py (library)"

    ```python title="your_library.py" linenums="1"
    --8<-- "microbit_tools/Your Module/your_library.py"
    ```

## How it works

Explain the key lines in plain language.

## Try this next

- An idea to extend the project.
- Another idea, linking to a related example.
