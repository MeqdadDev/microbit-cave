'''
Example: Mini jukebox with the music module in micro:bit
By: Meqdad Darwish
'''
# Note: micro:bit V2 plays through its built-in speaker.
# On V1, connect a buzzer or headphones to pin0 and GND.

from microbit import *
import music

# "Frere Jacques": note + octave, then ":" and length in ticks
FRERE_JACQUES = ["C4:4", "D4:4", "E4:4", "C4:4",
                 "C4:4", "D4:4", "E4:4", "C4:4",
                 "E4:4", "F4:4", "G4:8",
                 "E4:4", "F4:4", "G4:8"]

while True:
    if button_a.was_pressed():
        display.show(Image.MUSIC_QUAVER)
        music.play(music.ODE)  # a built-in melody
        display.clear()
    elif button_b.was_pressed():
        display.show(Image.MUSIC_CROTCHET)
        music.play(FRERE_JACQUES)
        display.clear()
    elif accelerometer.was_gesture("shake"):
        display.show(Image.SURPRISED)
        for frequency in range(880, 1760, 16):  # siren up...
            music.pitch(frequency, 6)
        for frequency in range(1760, 880, -16):  # ...and down
            music.pitch(frequency, 6)
        display.clear()
    sleep(20)
