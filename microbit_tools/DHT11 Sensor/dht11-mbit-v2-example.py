# Example: Interfacing dht11 sensor in micro:bit v2
# Example by: Meqdad Dev
# GitHub: https://github.com/MeqdadDev
# Repo. Link: https://github.com/MeqdadDev/microbit-micropython-samples
# License - MIT

from microbit import *
from dht11 import DHT11, DataError

# Tested on: P0, P1, P2 with micro:bit v2.0
sensor = DHT11(pin0)

while True:
    try:
        temp, humid = sensor.read()
    except DataError:
        # An occasional bad reading is normal: show "?" and try again
        display.show("?")
        sleep(2000)
    except Exception as error:
        # Sensor not responding or unsupported pin: show why
        display.scroll("Error: " + str(error))
        sleep(3000)
    else:
        display.scroll("T " + str(temp) + "C")
        sleep(500)
        display.scroll("H " + str(humid) + "%")
        sleep(1000)
