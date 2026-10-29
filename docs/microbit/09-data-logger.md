---
title: "Data Logging"
description: "Record temperature readings to the micro:bit's built-in data log."
tags:
  - Data
  - Sensors
  - Intermediate
level: Intermediate
board: "V2 only"
parts:
  - "micro:bit V2"
source:
  - "microbit/9 data-logger.py"
---

## What you'll build

Log the temperature every second into the micro:bit V2's on-board data log, with a heartbeat animation so you know it's recording.

## Code

```python title="9 data-logger.py" linenums="1"
--8<-- "microbit/9 data-logger.py"
```

## How it works

- `log.set_labels("temperature")` defines the columns of the log table.
- `log.add({...})` appends one row; `temperature()` reads the processor's temperature in °C.
- To view the data, plug the micro:bit into a computer and open the **MY_DATA.HTM** file on the MICROBIT drive.

## Try this next

- Add a second column with `display.read_light_level()`.
- Use `log.set_mirroring(True)` to also print each row over serial.
- Start and stop logging with button A.
