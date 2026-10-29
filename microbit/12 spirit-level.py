'''
Example: Rolling-ball spirit level with the accelerometer in micro:bit
By: Meqdad Darwish
'''
from microbit import *

LEVEL = Image("00000:"
              "03330:"
              "03930:"
              "03330:"
              "00000")


def to_led(reading):
    # Tilt in milli-g (about -1024 to 1024) -> LED column/row 0-4, flat = 2
    return min(4, max(0, 2 + (reading + 150) // 300))


while True:
    x = to_led(accelerometer.get_x())
    y = to_led(accelerometer.get_y())

    if x == 2 and y == 2:
        display.show(LEVEL)
    else:
        display.clear()
        display.set_pixel(x, y, 9)
    sleep(50)
