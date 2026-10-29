---
title: "Clap Switch"
description: "Clap to turn an LED lamp on and off using the micro:bit V2's built-in microphone."
tags:
  - Microphone
  - Sound
  - Sensors
  - Beginner
level: Beginner
board: "V2 only"
parts:
  - "micro:bit V2"
source:
  - "microbit/13 clap-switch.py"
---

## What you'll build

A clap-controlled lamp: clap once and every LED turns on, clap again and it goes off. A dim dot in the middle shows
it's listening.

## Code

```python title="13 clap-switch.py" linenums="1"
--8<-- "microbit/13 clap-switch.py"
```

## How it works

- The microphone sits behind the small hole next to the touch logo. The LED beside it lights up while it's in use.
- `microphone.set_threshold(SoundEvent.LOUD, 150)` sets how loud (0–255) a sound must be to count as `LOUD`.
- `microphone.was_event(SoundEvent.LOUD)` is `True` if a loud sound happened since the last check.
- After a clap, the program waits 300 ms and checks again to throw away the rest of the same clap, so a single
  clap never toggles the lamp twice.

!!! tip "Tuning"
    If the lamp toggles by itself, raise the threshold. If it misses your claps, lower it.
    Scroll `microphone.sound_level()` to see how loud your room is.

## Try this next

- Require **two claps** within a second to toggle, so talking doesn't trigger it.
- Show a live sound meter: map `microphone.sound_level()` to a bar of LEDs.
- Send the on/off state to another micro:bit over [radio](04-radio-messaging.md) to control a real lamp.
