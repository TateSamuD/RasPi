import tkinter as tk
import smbus2
import time
import math
from mpu6050 import mpu6050
import os
import sys

# MPU6050 address
MPU6050_ADDR = 0x68

#MPU6050 Registers
GYRO_XOUT_H = 0x43
GYRO_YOUT_H = 0x45
GYRO_ZOUT_H = 0x47
ACCEL_XOUT_H = 0x3B
ACCEL_YOUT_H = 0x3D
ACCEL_ZOUT_H = 0x3F

# Initialise mpu6050
sensor = mpu6050(0x68)

# Initialize I2C bus
bus = smbus2.SMBus(1)

def read_word(reg):
    high = bus.read_byte_data(MPU6050_ADDR, reg)
    low = bus.read_byte_data(MPU6050_ADDR, reg +1)
    value = (high << 8) + low
    if (value >= 0x8000):
        return  -((65535 - value) +1)
    else:
        return value

def read_mpu_accel_data():
    accel_x = read_word(ACCEL_XOUT_H)
    accel_y = read_word(ACCEL_YOUT_H)
    accel_z = read_word(ACCEL_ZOUT_H)
    return accel_x, accel_y, accel_z

def read_mpu_gyro_data():
    gyro_x = read_word(GYRO_XOUT_H)
    gyro_y = read_word(GYRO_YOUT_H)
    gyro_z = read_word(GYRO_ZOUT_H)
    return gyro_x, gyro_y, gyro_z

# def update_rotation_label():
#     accel_x, accel_y, accel_z = read_mpu6050_data(bus)

#     # Calculate rotation angles
#     roll = math.atan2(accel_y, accel_z) * (180.0 / math.pi)
#     pitch = math.atan2(-accel_x, math.sqrt(accel_y ** 2 + accel_z ** 2)) * (180.0 / math.pi)

#     # Update label text
#     label_var.set(f"Roll: {roll:.2f} degrees\nPitch: {pitch:.2f} degrees")

#     # Call this function after a delay
#     root.after(100, update_rotation_label)

def update_mpu_rotation():
    accel_x, accel_y, accel_z = read_mpu_accel_data()
    # gyro_x, gyro_y, gyro_z = read_mpu_gyro_data()

    roll = math.atan2(accel_y, accel_z) * (180.0 / math.pi)
    pitch = math.atan2(-accel_x, math.sqrt(accel_y**2 + accel_z**2)) * (180.0 / math.pi)

    label_var.set(f"Roll: {roll:.2f} degrees\nPitch: {pitch:.2f} degrees")

    root.after(100, update_mpu_rotation)

if os.environ.get('DISPLAY', '') == '':
    print('No Display Found.\nUsing: 0.0')
    os.environ.__setitem__('DISPLAY', ':0.0')

# Initialize tkinter
root = tk.Tk()
root.title("MPU6050 Rotation Display")

# Create a label to display rotation
label_var = tk.StringVar()
label = tk.Label(root, textvariable=label_var, font=("Helvetica", 14))
label.pack(pady=20)


# Call the update function
update_mpu_rotation()
# update_rotation_label()


# Start the tkinter main loop
root.mainloop()
