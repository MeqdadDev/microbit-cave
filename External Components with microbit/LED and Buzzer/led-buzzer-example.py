'''
Example: Control LED or Buzzer (On/Off), connected with Pin0 in micro:bit
By: Meqdad Darwish
'''
from microbit import *

while True:
    if button_a.is_pressed():
        pin0.write_digital(1)
        sleep(2000)
    else:
        pin0.write_digital(0)
