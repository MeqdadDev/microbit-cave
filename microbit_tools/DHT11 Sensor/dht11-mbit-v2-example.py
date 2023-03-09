# Example: Interfacing dht11 sensor in micro:bit v2
# Example by: Meqdad Dev
# GitHub: https://github.com/MeqdadDev
# Repo. Link: https://github.com/MeqdadDev/microbit-micropython-samples
# License - MIT

from microbit import *
from dht11 import DHT11

# Tested on: P0, P1, P2 with micro:bit v2.0
sensor = DHT11(pin0)

while True:
    try:
        temp, humid = sensor.read()
        display.scroll(temp)
        sleep(500)
        display.scroll(humid)
    except:
        sleep(3000)
    else:
        sleep(1000)
