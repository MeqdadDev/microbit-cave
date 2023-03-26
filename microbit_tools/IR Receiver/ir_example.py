from microbit import *
import ir

# Initialize IR receiver on pin16
ir_receiver = ir.MicrobitIRReceiver()

def display_signal(signal):
    display.scroll(str(signal))

while True:
    # Check if a signal has been received
    if ir_receiver.get_signal():
        # Display the received signal
        display_signal(ir_receiver.get_signal())
        
