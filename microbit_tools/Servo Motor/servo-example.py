'''
Example: Controlling Servo Motor 9g example using micro:bit
By: Meqdad Darwish
'''
from microbit import *
from servo import Servo

my_servo = Servo(pin0)

while True:
    if button_a.was_pressed():
        my_servo.set_angle(90)
        display.scroll(90)
    if button_b.was_pressed():
        my_servo.set_angle(0)
        display.scroll(0)
