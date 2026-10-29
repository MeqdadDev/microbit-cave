'''
Example: Clap switch with the built-in microphone in micro:bit V2
By: Meqdad Darwish
'''
from microbit import *

LAMP = Image("99999:"
             "99999:"
             "99999:"
             "99999:"
             "99999")

# 0-255: raise it if the lamp toggles by itself in a noisy room
microphone.set_threshold(SoundEvent.LOUD, 150)

lamp_on = False
display.set_pixel(2, 2, 2)  # dim dot = listening

while True:
    if microphone.was_event(SoundEvent.LOUD):
        lamp_on = not lamp_on
        if lamp_on:
            display.show(LAMP)
        else:
            display.clear()
            display.set_pixel(2, 2, 2)
        sleep(300)
        microphone.was_event(SoundEvent.LOUD)  # forget the tail of this clap
    sleep(10)
