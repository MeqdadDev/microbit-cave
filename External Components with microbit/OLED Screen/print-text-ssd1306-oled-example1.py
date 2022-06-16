'''
Example: Print text on OLED Screen (ssd1306) connected to micro:bit
By: Meqdad Darwish
'''
# Note: The screen should be connected to the default I2C pins of the micro:bit.
# You should connect the device’s SCL pin to micro:bit pin 19
# and the device’s SDA pin to micro:bit pin 20.

from microbit import *
from ssd1306 import initialize, clear_oled
from ssd1306_text import add_text

initialize()
clear_oled()
sleep(1000)
add_text(0, 0, "------")
add_text(0, 1, "Hi")
add_text(0, 2, "------")
add_text(0, 3, "Meqdad")
