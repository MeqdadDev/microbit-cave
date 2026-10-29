---
title: "Random Activity: Challenges"
description: "Press button A to pick a random challenge from a list."
tags:
  - Random
  - Buttons
  - Beginner
level: Beginner
board: "V1 & V2"
parts:
  - "micro:bit"
source:
  - "microbit/8 random-lib2.py"
---

## What you'll build

A party-game picker: press button A and the micro:bit scrolls a random challenge.

## Code

```python title="8 random-lib2.py" linenums="1"
--8<-- "microbit/8 random-lib2.py"
```

## How it works

`random.choice(list)` returns one item from the list at random. Edit the `challenges` list to make your own game.

## Try this next

- Add your own challenges to the list.
- Use `button_a.was_pressed()` so one press gives exactly one challenge.
- Send the challenge to a friend's micro:bit over [radio](04-radio-messaging.md).
