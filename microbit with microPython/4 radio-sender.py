'''
Example: Radio Messaging example using micro:bit (Sender Side)
By: Meqdad Darwish
'''

# Sender
from microbit import *
import radio
radio.config(group=5)
radio.on()

while True:
    if button_a.is_pressed():
        radio.send('A is pressed')
