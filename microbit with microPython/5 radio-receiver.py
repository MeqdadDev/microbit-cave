'''
Example: Radio Messaging example using micro:bit (Receiver Side)
By: Meqdad Darwish
'''

# Receiver
from microbit import *
import radio
radio.config(group=5)
radio.on()
while True:
    message = radio.receive()
    if message == 'A is pressed':
        display.scroll(message)
