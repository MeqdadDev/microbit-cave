from microbit import *

while True:
    if display.read_light_level() < 150:
        display.scroll('Night')
    else:
        display.scroll('Day')
    sleep(2000)
