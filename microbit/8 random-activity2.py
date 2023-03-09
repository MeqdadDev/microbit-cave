from microbit import *
import random

challenges = ["joke", "jump", "truth/dare", "drink"]

while True:
    if button_a.is_pressed():
        display.scroll(random.choice(challenges))
