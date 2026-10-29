'''
Example: micro:bit Serial Communication (computer side)
CAUTION: this runs on your computer with standard Python, NOT on the micro:bit.
Flash "10 microbit serial sender.py" to the micro:bit first, then run this script.

pip install pyserial
By: Meqdad Darwish
'''
import serial

PORT = "COM19"  # Windows: Device Manager > Ports | Linux: /dev/ttyACM0 | macOS: /dev/cu.usbmodem*
BAUD = 115200
HOT_TEMPERATURE = 28  # degrees C; at or above this the micro:bit shows a cross


def describe_light(level):
    if level < 50:
        return "dark"
    if level < 150:
        return "dim"
    return "bright"


def take_action(temperature):
    return "ALERT" if temperature >= HOT_TEMPERATURE else "OK"


def handle_message(line, port):
    kind, _, payload = line.partition(",")

    if kind == "SENSORS":
        try:
            temperature, light = (int(value) for value in payload.split(","))
        except ValueError:
            print("Malformed sensor reading:", line)
            return
        reply = take_action(temperature)
        print("Temperature: {} C | Light: {} ({}) -> {}".format(
            temperature, light, describe_light(light), reply))
        port.write((reply + "\n").encode("utf-8"))
    elif kind == "BUTTON":
        print("Button {} pressed".format(payload))
    elif kind == "GESTURE":
        print("Gesture detected: {}".format(payload))
    else:
        print("Unknown message:", line)


def main():
    with serial.Serial(PORT, BAUD, timeout=1) as port:
        print("Listening to the micro:bit on {} (Ctrl+C to stop)".format(PORT))
        while True:
            line = port.readline().decode("utf-8", errors="replace").strip()
            if line:
                handle_message(line, port)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nStopped.")
