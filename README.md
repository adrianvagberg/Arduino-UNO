# Arduino UNO
A small repo for controlling an Arduino UNO from Python.
- ```arduino.py``` is the main file, modify it as needed.
- ```upload_firmata.py``` serves to install the Arduino Command Line Interface (CLI) and then upload the ```StandardFirmata``` sketch to the Arduino.

## Setup
### Clone repo and setup environment
- Clone the repository in your preferred way. For example in the command line:
    ```bash
    git clone https://github.com/adrianvagberg/Arduino-UNO.git
    cd Arduino-UNO
   ```
- Create a virtual environment and install dependencies.
    ```bash
    python -m venv venv
    source venv/bin/activate  # For macOS/Linux
    # or
    venv\Scripts\activate     # For Windows
    pip install -r requirements.txt
   ```
- Alternatively, install pyfirmata2 directly and write your own code using:
   ```bash
  pip install pyfirmata2 [--user] [--upgrade]
   ```
  
### Connect Arduino
- Use the USB-port to connect the Arduino to your PC. No other power cord is needed.
  
### If upload_firmata.py fails:
1. Consult Chat GPT :)
2. Download and install the Arduino IDE [here](https://www.arduino.cc/en/software).
   1. In the Arduino IDE, select your Arduino board under "Tools"
   2. Upload the ```File -> Examples -> Firmata -> Standard Firmata``` sketch. You may need to download the ```Firmata``` and ```Servo``` packages.
   3. Hardcode the value of ```PORT``` in ```arduino.py``` to the port identified in the Arduino IDE (usually COM3, COM4, or COM5 on PCs)

## Documentation
- [pyFirmata2](https://github.com/berndporr/pyFirmata2/blob/master/README.md)
- [Arduino CLI](https://github.com/arduino/arduino-cli/releases)
