'''
Example: Display DIY Images on LED matrix in micro:bit
By: Meqdad Darwish
Ref: https://microbit-micropython.readthedocs.io/en/latest/tutorials/images.html#diy-images
'''
from microbit import *

boat = Image("06050:"
             "07040:"
             "08030:"
             "99999:"
             "09990")

display.show(boat)
