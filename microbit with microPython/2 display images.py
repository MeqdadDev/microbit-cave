'''
Example: Print built-in Images on LED matrix in micro:bit
By: Meqdad Darwish
Ref: https://microbit-micropython.readthedocs.io/en/latest/tutorials/images.html
'''
from microbit import *

while True:
    display.show(Image.HEART)
    sleep(1000)  # 2000 = 2 sec.
    display.show(Image.HEART_SMALL)
    sleep(1000)
    display.show(Image.HAPPY)
    sleep(1000)
    display.show(Image.SMILE)
    sleep(1000)
    display.show(Image.SAD)
    sleep(1000)
    display.show(Image.CONFUSED)
    sleep(1000)
    display.show(Image.ANGRY)
    sleep(1000)
    display.show(Image.ASLEEP)
    sleep(1000)
    display.show(Image.SURPRISED)
    sleep(1000)
