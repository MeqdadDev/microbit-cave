'''
Example: Measure distance using Ultrasonic sensor and display results on LED matrix in micro:bit
By: Meqdad Darwish
'''
from microbit import *
<<<<<<< HEAD
from ultrasonic import Ultrasonic

# default pins in Ultrasonic class are:
# trigger: pin13
# echo: pin15

ultrasonic_sensor = Ultrasonic()
# or
# ultrasonic_sensor = Ultrasonic(trig=pin13, echo=pin15)

while True:
    distance_value = ultrasonic_sensor.measure_distance_cm()
=======
from machine import time_pulse_us

TRIGGER = pin13
ECHO = pin15

def measure_distance():
    # Send a pulse to trigger ultrasonic burst
    TRIGGER.write_digital(1)
    TRIGGER.write_digital(0)
    # Measure the input echo pulse in microseconds and then convert to seconds
    msec = time_pulse_us(ECHO, 1)
    echo_time = msec / 1000000
    # Calculate distance in cm using distance equation with sound velocity
    dist_cm = (echo_time / 2) * 34300
    return dist_cm

TRIGGER.write_digital(0)
ECHO.read_digital()

while True:
    distance_value = measure_distance()
>>>>>>> db6551813e487b5a9dbf27f6126d0cbf0314043f
    display.scroll(str(int(distance_value)))
    sleep(2000)
