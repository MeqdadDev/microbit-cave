'''
IR Remote with IR Receiver - A Module in microPython for micro:bit
Decodes the NEC protocol used by most small IR remote controls.
Author: Meqdad Dev (Meqdad Darwish)
GitHub: @MeqdadDev
https://github.com/MeqdadDev/
'''
from microbit import pin16
from machine import time_pulse_us

# NEC timings in microseconds. The receiver output is LOW while the remote's LED is on.
LEADER_MIN = 4000         # 9 ms low pulse (we may catch it a little late)
LEADER_MAX = 10500
FRAME_SPACE_MIN = 3500    # 4.5 ms high: a new button code follows
REPEAT_SPACE_MIN = 1700   # 2.25 ms high: button is being held down
ONE_THRESHOLD = 1100      # data space: ~560 us = 0, ~1690 us = 1


class MicrobitIRReceiver:
    '''
    A module to interface IR Remote with IR Receiver in microPython with micro:bit.
    Example:
    ```
    from microbit import *
    import ir

    remote = ir.MicrobitIRReceiver(pin16)

    while True:
        command = remote.get_signal()
        if command is not None:
            display.scroll(str(command), wait=False)
    ```
    '''
    def __init__(self, pin=pin16):
        self.pin = pin
        self.address = None
        self.last_command = None

    def get_signal(self, repeat=False):
        '''
        Return the command (0-255) of the button pressed, or None.
        Returns immediately when no signal is arriving; decoding a frame takes about 70 ms.
        With repeat=True, holding a button keeps returning its command.
        '''
        if self.pin.read_digital() != 0:
            return None

        leader = time_pulse_us(self.pin, 0, LEADER_MAX + 1000)
        if not LEADER_MIN <= leader <= LEADER_MAX:
            return None

        space = time_pulse_us(self.pin, 1, 6000)
        if space >= FRAME_SPACE_MIN:
            return self._read_frame()
        if space >= REPEAT_SPACE_MIN and repeat:
            return self.last_command
        return None

    def _read_frame(self):
        # Locals keep the Python work between pulses short; two 16-bit halves avoid
        # allocating a big integer (micro:bit small ints stop at 2**30) mid-frame.
        pin, pulse, threshold = self.pin, time_pulse_us, ONE_THRESHOLD
        halves = [0, 0]
        for bit in range(32):
            # Waits out the ~560 us low pulse, then times the high gap that encodes the bit.
            space = pulse(pin, 1, 2500)
            if space < 0:
                return None
            if space > threshold:
                halves[bit >> 4] |= 1 << (bit & 15)

        low, high = halves
        address, address_check = low & 0xFF, low >> 8
        command, command_check = high & 0xFF, high >> 8

        if command ^ command_check != 0xFF:
            return None

        # Extended NEC remotes use a 16-bit address with no inverted copy.
        self.address = address if address ^ address_check == 0xFF else low
        self.last_command = command
        return command
