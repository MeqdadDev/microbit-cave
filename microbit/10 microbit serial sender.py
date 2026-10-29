'''
Example: micro:bit Serial Communication (micro:bit side)
Flash this to the micro:bit, then run "10 microbit serial.py" on your computer.

Every message is one line of comma-separated text:
    SENSORS,<temperature C>,<light 0-255>   every second
    BUTTON,A / BUTTON,B                     when a button is pressed
    GESTURE,shake                           when the micro:bit is shaken

The computer replies with one word per line, shown on the LED matrix:
    OK    -> tick       ALERT -> cross (too hot)

By: Meqdad Darwish
'''
from microbit import *

REPORT_EVERY_MS = 1000
last_report = running_time()

while True:
    if button_a.was_pressed():
        print("BUTTON,A")
    if button_b.was_pressed():
        print("BUTTON,B")
    if accelerometer.was_gesture("shake"):
        print("GESTURE,shake")

    if running_time() - last_report >= REPORT_EVERY_MS:
        print("SENSORS,{},{}".format(temperature(), display.read_light_level()))
        last_report = running_time()

    if uart.any():
        reply = uart.readline()
        if reply:
            command = str(reply, "utf-8").strip()
            if command == "OK":
                display.show(Image.YES)
            elif command == "ALERT":
                display.show(Image.NO)

    sleep(20)
