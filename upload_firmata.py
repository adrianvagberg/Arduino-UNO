import subprocess
import os
import sys
import urllib.request
import zipfile
from pathlib import Path


# Function to check for errors and exit if necessary
def check_error(result, error_message):
    if result.returncode != 0:
        print(f"Error: {error_message}")
        sys.exit(1)


# Function to install Arduino CLI if not installed
def install_arduino_cli():
    print("Arduino CLI not found. Installing...")

    # Define the installation directory for Arduino CLI
    install_dir = os.path.join(os.getcwd(), 'Arduino CLI')

    # Check if the directory already exists
    if not os.path.exists(install_dir):
        os.makedirs(install_dir)

    # Download the Arduino CLI zip file for Windows
    url = "https://github.com/arduino/arduino-cli/releases/download/0.31.0/arduino-cli_0.31.0_Windows_64bit.zip"
    zip_path = "arduino-cli.zip"

    # Download the zip file
    urllib.request.urlretrieve(url, zip_path)

    # Extract the zip file
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(install_dir)

    # Delete the downloaded zip file
    os.remove(zip_path)

    print("Arduino CLI installed successfully.")


# Function to install a library using Arduino CLI
def install_library(library_name):
    print(f"Installing {library_name} library...")
    result = subprocess.run(["arduino-cli", "lib", "install", library_name], capture_output=True)
    check_error(result, f"Failed to install {library_name} library.")


# Function to detect the Arduino port
def detect_port():
    print("Detecting connected Arduino...")
    result = subprocess.run(["arduino-cli", "board", "list"], capture_output=True, text=True)
    check_error(result, "Failed to detect Arduino board.")

    ports = result.stdout.splitlines()
    for line in ports:
        if "Serial" in line:
            port = line.split()[0]
            print(f"Arduino detected on port {port}.")
            return port

    print("Error: Could not detect Arduino board. Please check the connection.")
    sys.exit(1)


def run():
    # Path to the sketch file (StandardFirmata example)
    home = Path.home()
    sketch_path = os.path.join(home, 'Documents', 'Arduino', 'libraries', 'Firmata', 'examples', 'StandardFirmata')

    # Set the board type
    board_type = "arduino:avr:uno"  # Change this to your board type (e.g., arduino:avr:mega)

    # Define the installation directory for Arduino CLI
    install_dir = os.path.join(os.getcwd(), 'Arduino CLI')
    arduino_cli_path = os.path.join(install_dir, 'arduino-cli.exe')

    # Check if Arduino CLI is installed in the correct directory
    if not os.path.exists(arduino_cli_path):
        install_arduino_cli()

    if arduino_cli_path not in os.environ["PATH"]:
        os.environ["PATH"] = f"{os.environ['PATH']};{install_dir}"

    # Install necessary libraries (Firmata and Servo)
    install_library("Firmata")
    install_library("Servo")

    # Detect the Arduino port
    port = detect_port()

    # Compile the sketch
    print("Compiling StandardFirmata...")
    result = subprocess.run(["arduino-cli", "compile", "--fqbn", board_type, sketch_path], capture_output=True)
    check_error(result, "Failed to compile StandardFirmata.")

    # Upload the sketch to the Arduino
    print(f"Uploading StandardFirmata to Arduino on port {port}...")
    result = subprocess.run(["arduino-cli", "upload", "--fqbn", board_type, "--port", port, sketch_path],
                            capture_output=True)
    check_error(result, "Failed to upload StandardFirmata to the board.")

    print("Successfully uploaded StandardFirmata to the board.")

    return port
