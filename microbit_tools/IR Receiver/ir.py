'''
IR Remote with IR Receiver - A Module in microPython for micro:bit
Author: Meqdad Dev (Meqdad Darwish)
GitHub: @MeqdadDev
https://github.com/MeqdadDev/
'''
from microbit import pin16
import utime

class MicrobitIRReceiver:
    '''
    A module to interface IR Remote with IR Receiver in microPython with micro:bit.
    Example:
    ```
    from microbit import *
    import ir
    
    # Initialize IR receiver on pin16
    ir_receiver = ir.MicrobitIRReceiver()
    
    def display_signal(signal):
        display.scroll(str(signal))
    
    while True:
        if ir_receiver.get_signal():
            display_signal(ir_receiver.get_signal())
    ```
    '''
    def __init__(self):
        self.pin = pin16
        self.last_time = 0
        self.last_code = None

    def get_signal(self):
        pin_val = pin16.read_digital()
        curr_time = utime.ticks_us()

        if pin_val == 0 and self.last_time == 0:
            self.last_time = curr_time
            return None

        if pin_val == 1 and self.last_time != 0:
            elapsed_time = curr_time - self.last_time

            if elapsed_time > 1500:
                self.last_code = None
            elif elapsed_time > 800:
                if self.last_code is not None:
                    return self.last_code
            else:
                self.last_code = 0

            self.last_time = 0
        elif pin_val == 0 and self.last_time != 0:
            elapsed_time = curr_time - self.last_time

            if elapsed_time > 1500:
                self.last_code = None
            elif elapsed_time > 800:
                if self.last_code is not None:
                    self.last_code = (self.last_code << 1) | 1
            else:
                if self.last_code is not None:
                    self.last_code = self.last_code << 1

            self.last_time = curr_time

        return None
