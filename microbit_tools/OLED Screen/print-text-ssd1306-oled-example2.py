'''
Example: Test how text is placed and clipped on OLED Screen (ssd1306) connected to micro:bit
By: Meqdad Darwish
'''
# Note: The screen should be connected to the default I2C pins of the micro:bit.
# You should connect the device's SCL pin to micro:bit pin 19
# and the device's SDA pin to micro:bit pin 20.

from microbit import *
from ssd1306 import initialize, clear_oled
from ssd1306_text import add_text

initialize()
clear_oled()

add_text(0, 0, "")                  # draws nothing
add_text(12, 0, "Hi")               # off-screen: draws nothing
add_text(0, 1, "HHH")               # check the last H is complete
add_text(0, 2, "ABCDEFGHIJKLMNOP")  # clipped to 12 characters
add_text(9, 3, "12345")             # clipped at the right edge

display.show(Image.YES)
