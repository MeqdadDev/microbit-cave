'''
Example: Detecting motion with PIR sensor and buzzer connected to micro:bit
By: Meqdad Darwish
'''
# Note: PIR sensor is connected to pin2.
# Note: Buzzer is connected to pin1.

from microbit import *

while True:
    motion = pin2.read_digital()
    if motion == 1:
        pin1.write_digital(1)
    else:
        pin1.write_digital(0)
