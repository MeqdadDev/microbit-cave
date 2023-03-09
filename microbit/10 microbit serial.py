####################
# CAUTION: mciro:bit serial runs on standard Python, not MicroPython.
# Which means it only runs on your computer, and micro:bit should send the serial messages.
####################
# pip install pyserial
import serial
from time import sleep

encoding = 'utf-8'
port = "COM19"  # checkout your port
baud = 115200
s = serial.Serial(port)
s.baudrate = baud

if not s.isOpen():
    s.open()


def take_action(result):
    if result == 0:
        return "OK"

    if result == 1:
        return "Not OK"
    # s.reset_output_buffer()
    # s.reset_input_buffer()


def get_microbit_msg():
    while True:
        i = s.read()
        msg = i.decode(encoding)
        print("msg from micro:bit:::", msg)
        take_action(msg)


if __name__ == "__main__":
    get_microbit_msg()
