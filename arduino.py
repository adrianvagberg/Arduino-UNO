import pyfirmata2
import upload_firmata

# Upload the Standard Firmata sketch to the Arduino
# (necessary for controlling it from Python)
PORT = upload_firmata.run()

# Initialize the Arduino in pyFirmata
board = pyfirmata2.Arduino(f'{PORT}')

# Assign the 2nd pin as digital output
digitalOut = board.get_pin('d:2:o')

# digitalOut.write(True) sets the logic signal ON
# digitalOut.write(False) sets the logic signal OFF

board.exit()