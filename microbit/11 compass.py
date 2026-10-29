'''
Example: Digital compass with the built-in magnetometer in micro:bit
By: Meqdad Darwish
'''
from microbit import *

DIRECTIONS = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]

while True:
    # The first reading starts calibration: tilt the board until every LED is lit
    heading = compass.heading()  # 0-359 degrees, 0 = north

    if button_a.was_pressed():
        display.scroll(str(heading))
    elif button_b.was_pressed():
        display.scroll(DIRECTIONS[((heading + 22) // 45) % 8])
    else:
        # Pick the clock hand that points north
        needle = ((15 - heading) // 30) % 12
        display.show(Image.ALL_CLOCKS[needle])
        sleep(100)
