'''
Example: Data Logger example using micro:bit
By: Meqdad Darwish
'''
from microbit import *
import log

log.set_labels("temperature")

while True:
    log.add({'temperature': temperature()})
    display.show(Image.HEART)
    sleep(500)
    display.show(Image.HEART_SMALL)
    sleep(500)
    display.clear()
