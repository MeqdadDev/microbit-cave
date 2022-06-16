'''
Ultrasonic sensor (HC-SR04) library  in microPython for the microcontrollers like micro:bit
Author: Meqdad Darwish
GitHub: @MeqdadDev
https://github.com/MeqdadDev/
'''

from microbit import *
from machine import time_pulse_us

class Ultrasonic:
    '''
    A library to interface Ultrasonic HC-SR04 sensor in microPython with micro:bit and other controllers.

    Example:
    ```
    from microbit import *
    from ultrasonic import Ultrasonic

    ultrasonic_sensor = Ultrasonic()

    while True:
        distance_value = ultrasonic_sensor.measure_distance_cm()
        display.scroll(str(int(distance_value)))
    ```
    '''
    def __init__(self, trig=pin13, echo=pin15):
        self.trigger = trig
        self.echo = echo
        self.trigger.write_digital(0)
        self.echo.read_digital()

    def measure_distance_cm(self):
        self.trigger.write_digital(1)
        self.trigger.write_digital(0)
        msec = time_pulse_us(self.echo, 1)
        echo_time = msec / 1000000
        dist_cm = (echo_time / 2) * 34300
        return dist_cm

