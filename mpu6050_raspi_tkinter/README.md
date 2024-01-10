# MPU6050 Rotation Display with Raspberry Pi and Tkinter

This project involves reading data from an MPU6050 sensor connected to a Raspberry Pi and displaying the rotation angles on a simple tkinter window. The script calculates the roll and pitch angles based on the accelerometer data from the MPU6050.

## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Hardware Setup](#hardware-setup)
- [Usage](#usage)
- [Customisation](#customisation)
- [License](#license)

## Requirements

- Raspberry Pi with Raspbian OS
![Raspberry Pi 4](/mpu6050_raspi_tkinter/misc/raspberry-pi-4.png)
- MPU6050 sensor
![MPU6050 Sensor](/mpu6050_raspi_tkinter/misc/MPU6050-Pinout.png)
- Python 3
- `smbus` library for I2C communication
- `tkinter` library for GUI

## Installation

1. **Install Required Libraries:**

   ```bash
   sudo apt-get update
   sudo apt-get install python3-smbus
   sudo apt-get install python3-tk
   pip install mpu6050-raspberrypi
   pip install matplotlib
   ```

2. **Clone the Repository:**

    ```bash
    git clone https://github.com/TateSamuD/RasPi.git
    cd RasPi/tkinter_mpu6050/mpu6050_raspi_tkinter
    ```

3. **Run the Script:**

    ```bash
    python3 mpu6050_tkinter.py
    ```

## Hardware Setup

![Raspberry Pi to MPU6050 snesor Connection](/mpu6050_raspi_tkinter/misc/mpu6050_raspi_connection.png)

1. Connect the MPU6050 sensor to the Raspberry Pi using the I2C interface. Double-check the wiring to ensure proper connections.
2. Power up the Raspberry Pi.

## Usage

1. Run the script using the command mentioned in the installation section.
2. The tkinter window will display the roll and pitch angles calculated from the MPU6050 sensor data.
3. The angles will be updated continuously in real-time.

## Customisation

You can customise the script and GUI according to your preferences:

- Adjust the update the `after()` function to control how often the angles are updated.
- Modify the GUI layout, font and style to match your design preferences.
- Add additional features or data visualistaions based on the MPU6050 data.

## License

This project is licensed under the [MIT License](/LICENSE).
