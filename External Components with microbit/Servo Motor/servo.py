'''
Servo Motor (9g) Module in microPython for the microcontrollers like micro:bit
Author: Meqdad Darwish
GitHub: @MeqdadDev
https://github.com/MeqdadDev/
'''

from microbit import *


class Servo:
    '''
    A library to interface Servo motor 9g in microPython with micro:bit.

    Example:
    ```py
    from microbit import *
    from servo import Servo

    my_servo = Servo(pin0)
    my_servo.set_angle(90)
    ```
    '''

    def __init__(self, pin=pin0):
        self.pin = pin

    def set_angle(self, angle=0):
        duty = 26 + (angle * 102) / 180
        self.pin.write_analog(duty)
