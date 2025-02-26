import pyfirmata2
import upload_firmata
import time

# Upload the Standard Firmata sketch to the Arduino
# (necessary for controlling it from Python)
PORT = upload_firmata.run()

# Initialize the Arduino in pyFirmata
board = pyfirmata2.Arduino(f'{PORT}')

# Assign the 2nd pin as digital output
digitalOut = board.get_pin('d:2:o')

# Testing if it works
for i in range(10):
    digitalOut.write(True) # sets the logic signal ON
    time.sleep(0.5)
    digitalOut.write(False) # sets the logic signal OFF
    time.sleep(0.5)

board.exit()