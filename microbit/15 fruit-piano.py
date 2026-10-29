'''
Example: Fruit piano with touch pins and the touch logo in micro:bit V2
By: Meqdad Darwish
'''
# Note: clip pin1 and pin2 to two pieces of fruit, and hold the GND pad
# (or a clip from GND) with your other hand while you touch them.

from microbit import *
import music

KEYS = [
    (pin1, "C4:2"),
    (pin2, "E4:2"),
    (pin_logo, "G4:2"),
]

while True:
    for key, note in KEYS:
        if key.is_touched():
            display.show(note[0])  # the note's letter
            music.play(note)
            display.clear()
    sleep(10)
