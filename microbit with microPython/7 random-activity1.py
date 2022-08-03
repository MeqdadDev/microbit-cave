'''
Example: Dice with random library example using micro:bit
By: Meqdad Darwish
'''
from microbit import *
import random

while True:
    if accelerometer.was_gesture('shake'):
        display.scroll('..')
        sleep(500)
        display.show(random.randint(1, 6))
