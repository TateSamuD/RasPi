import tkinter as tk
from smbus import SMBus
import time
import math

# MPU6050 address and register constants
MPU6050_ADDR = 0x68
MPU6050_REG_X = 0x3B
MPU6050_SCALE_FACTOR = 16384.0

def read_mpu6050_data(bus):
    data = bus.read_i2c_block_data(MPU6050_ADDR, MPU6050_REG_X, 6)
    raw_accel_x = (data[0] << 8) | data[1]
    raw_accel_y = (data[2] << 8) | data[3]
    raw_accel_z = (data[4] << 8) | data[5]

    accel_x = raw_accel_x / MPU6050_SCALE_FACTOR
    accel_y = raw_accel_y / MPU6050_SCALE_FACTOR
    accel_z = raw_accel_z / MPU6050_SCALE_FACTOR

    return accel_x, accel_y, accel_z

def update_rotation_label():
    accel_x, accel_y, accel_z = read_mpu6050_data(bus)

    # Calculate rotation angles
    roll = math.atan2(accel_y, accel_z) * (180.0 / math.pi)
    pitch = math.atan2(-accel_x, math.sqrt(accel_y ** 2 + accel_z ** 2)) * (180.0 / math.pi)

    # Update label text
    label_var.set(f"Roll: {roll:.2f} degrees\nPitch: {pitch:.2f} degrees")

    # Call this function after a delay
    root.after(100, update_rotation_label)

# Initialize tkinter
root = tk.Tk()
root.title("MPU6050 Rotation Display")

# Create a label to display rotation
label_var = tk.StringVar()
label = tk.Label(root, textvariable=label_var, font=("Helvetica", 14))
label.pack(pady=20)

# Initialize I2C bus
bus = SMBus(1)

# Call the update function
update_rotation_label()

# Start the tkinter main loop
root.mainloop()
