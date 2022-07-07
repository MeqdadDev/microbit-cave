'''
Example: Controlling Servo Motor 9g example using micro:bit
By: Meqdad Darwish
'''
from microbit import *


def servo_angle(pin=pin0, angle=0):
    duty = 26 + (angle * 102) / 180
    pin.write_analog(duty)


servo_angle(pin0, 0)

while True:
    if button_a.was_pressed():
        servo_angle(pin0, 90)
        display.scroll(90)
        servo_angle(pin0, 180)
        display.scroll(180)
    if button_b.was_pressed():
        servo_angle(pin0, 0)
        display.scroll(0)
