---
title: "Display Text on the LED Matrix"
description: "Scroll a message and show a heart on the micro:bit's 5×5 LED display."
tags:
  - Display
  - Beginner
level: Beginner
board: "V1 & V2"
parts:
  - "micro:bit"
source:
  - "microbit/1 display string.py"
---

## What you'll build

Your first micro:bit program: scroll a greeting across the 5×5 LED matrix, then flash a heart — forever.

## Code

```python title="1 display string.py" linenums="1"
--8<-- "microbit/1 display string.py"
```

## How it works

- `display.scroll()` slides a string across the LEDs one column at a time and returns when the text has passed.
- `display.show(Image.HEART)` draws one of the built-in images instantly.
- `sleep(2000)` pauses for 2000 milliseconds (2 seconds) before the loop starts again.

## Try this next

- Change the message to your own name.
- Pass `delay=60` to `display.scroll()` to make the text scroll faster.
- Show a different built-in image — see [Display Built-in Images](02-display-images.md).
