'''
Example: Measure distance using Ultrasonic sensor and display results on LED matrix in micro:bit
By: Meqdad Darwish
'''
from microbit import *
from ultrasonic import Ultrasonic

# default pins in Ultrasonic class are:
# trigger: pin13
# echo: pin15

ultrasonic_sensor = Ultrasonic()
# or
# ultrasonic_sensor = Ultrasonic(trig=pin13, echo=pin15)

MAX_RANGE_CM = 400  # HC-SR04 range is about 2-400 cm

while True:
    distance_value = ultrasonic_sensor.measure_distance_cm()
    if 0 < distance_value <= MAX_RANGE_CM:
        display.scroll(str(int(distance_value)))
    else:
        # No echo came back: nothing in range, or check the wiring
        display.show("?")
    sleep(2000)
