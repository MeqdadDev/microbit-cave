'''
Example: Print strings and shapes on LED matrix in micro:bit
By: Meqdad Darwish
'''
from microbit import *

while True:
    display.scroll('Hello Meqdad!')
    display.show(Image.HEART)
    sleep(2000)  # 2000 = 2 sec.
