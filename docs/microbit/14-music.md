---
title: "Music Jukebox"
description: "Play a built-in melody, your own tune and a siren with the music module."
tags:
  - Sound
  - Music
  - Buttons
  - Beginner
level: Beginner
board: "V1 & V2"
parts:
  - "micro:bit"
  - "V1 only: buzzer or headphones on pin 0 and GND"
source:
  - "microbit/14 music.py"
wiring:
  - part: "Buzzer or headphones"
    pins:
      "+": P0
      "−": GND
---

## What you'll build

A pocket jukebox:

| Input | Plays |
|-------|-------|
| Button **A** | Beethoven's *Ode to Joy* (built in) |
| Button **B** | *Frère Jacques*, written as a list of notes |
| **Shake** | A siren that sweeps up and down |

## Wiring

**micro:bit V2** plays through its built-in speaker, so you don't need to wire anything.

**micro:bit V1** has no speaker. Connect a buzzer or headphones between `P0` and `GND`:

<!-- wiring -->

## Code

```python title="14 music.py" linenums="1"
--8<-- "microbit/14 music.py"
```

## How it works

- `music.play()` plays a list of notes, or one of the built-in tunes like `music.ODE`, `music.NYAN` or `music.BIRTHDAY`.
- Each note is written `"C4:4"`: the note (`C`), the octave (`4`) and the length in **ticks** (`4`). At the default
  tempo a tick is 125 ms, so `:4` lasts half a second and `:8` a whole second.
- `music.pitch(frequency, duration)` plays any frequency in Hz. The siren loops from 880 Hz to 1760 Hz and back
  in 6 ms steps.

## Try this next

- Write your own tune, or slow it down with `music.set_tempo(bpm=80)`.
- Play a different note for each tilt direction, like a theremin, using `accelerometer.get_x()`.
- Build a [Fruit Piano](15-fruit-piano.md) to play notes by touch.
