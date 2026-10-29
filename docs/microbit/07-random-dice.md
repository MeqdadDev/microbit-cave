---
title: "Random Activity: Dice"
description: "Shake the micro:bit to roll a dice using the random library and accelerometer."
tags:
  - Random
  - Accelerometer
  - Beginner
level: Beginner
board: "V1 & V2"
parts:
  - "micro:bit"
source:
  - "microbit/7 random-lib1.py"
---

## What you'll build

Turn your micro:bit into a dice: shake it and it shows a random number from 1 to 6.

## Code

```python title="7 random-lib1.py" linenums="1"
--8<-- "microbit/7 random-lib1.py"
```

## How it works

- `accelerometer.was_gesture('shake')` is `True` if the board was shaken since the last check.
- `random.randint(1, 6)` picks a whole number between 1 and 6, inclusive.

## Try this next

- Show dice dot patterns as DIY images instead of digits.
- Roll two dice and show the total.
- Use button A for a coin flip with `random.choice(['H', 'T'])`.
