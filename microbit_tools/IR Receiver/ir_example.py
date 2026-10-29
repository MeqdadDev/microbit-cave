'''
Example: Show the code of each IR remote button on the LED matrix
By: Meqdad Darwish
'''
# Note: IR receiver OUT is connected to pin16.

from microbit import *
import ir

remote = ir.MicrobitIRReceiver(pin16)

while True:
    command = remote.get_signal()
    if command is not None:
        # wait=False keeps the loop polling the receiver while the number scrolls
        display.scroll(str(command), wait=False)
    sleep(2)  # the 9 ms start pulse is still caught, without running flat out
