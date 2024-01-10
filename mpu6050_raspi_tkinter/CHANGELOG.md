<!-- markdownlint-disable MD024 -->
# CHANGELOG

## Version Table of Content

- [Version 0.1.0](#version-010-2024-01-01)
- [Version 0.1.1](#verison-011-2024-01-01)
- [Version 0.1.2](#version-012-2024-01-03)
- [Version 0.2.0](#version-020-2024-01-09)

## Version 0.1.0 (2024-01-01)

### Overview

This is the initialisation of this project with rough code.

### Features

- Added: initial code which connects the sensor to the script.
- Added: tkinter dialogue box to display data shifts.

## Verison 0.1.1 (2024-01-01)

### Changes

- Updating script structure to use more recognisable libraries.
- Added 3 methods, `read_mpu_accel_data()`, `read_mpu_gyro_data()` and `update_mpu_rotation()`
  - `read_mpu_accel_data()`: This reads the current accelerometer data from the sensor returning it into a local dictionary.
  - `read_mpu_gyro_data()`: This reads the current gyroscope data from the sensor returning it into a local dicitonary.
  - `update_mpu_rotation()`: This calls the 2 functions above and calculates the roll and pitch using the accelerometer data for which the new values update a tkinter label.
- Added [TODO.md](/mpu6050_raspi_tkinter/TODO.md) file to project to hold noted expected changes
- Directory restructured

## Version 0.1.2 (2024-01-03)

### Additions

- Added module to display GUI over SSH

### Changes

- `read_mpu_accel_data()` and `read_mpu_gyro_data()` have been rewritten to have them pull the data straight from the sensor addresses for the respective axis

## Version 0.2.0 (2024-01-09)

### Changes

- Crossing over to 3D plot diagram
- Code cleanup (minor)
