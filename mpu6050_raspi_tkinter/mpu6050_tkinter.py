import tkinter as tk
import smbus2
import math
import os
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

# MPU6050 address
MPU6050_ADDR = 0x68

#MPU6050 Registers
GYRO_XOUT_H = 0x43
GYRO_YOUT_H = 0x45
GYRO_ZOUT_H = 0x47
ACCEL_XOUT_H = 0x3B
ACCEL_YOUT_H = 0x3D
ACCEL_ZOUT_H = 0x3F

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

def update_rotation_3D():
    accel_x, accel_y, accel_z = read_mpu_accel_data()

    roll = math.atan2(accel_y, accel_z) * (180.0 / math.pi)
    pitch = math.atan2(-accel_x, math.sqrt(accel_y**2 + accel_z**2)) * (180.0 / math.pi)

    # Update 3D plot
    ax.cla()
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_zlim(-1, 1)
    ax.set_title('MPU6050 Rotation Display')

    # 3D Object Rotation
    rotation_matrix_roll = np.array([
        [1,0,0],
        [0,math.cos(math.radians(roll)), -math.sin(math.radians(roll))],
        [0,math.sin(math.radians(roll)), math.cos(math.radians(roll))]
    ])

    rotation_matrix_pitch = np.array([
        [math.cos(math.radians(pitch)), 0, math.sin(math.radians(pitch))],
        [0,1,0],
        [-math.sin(math.radians(pitch)), 0, math.cos(math.radians(pitch))]
    ])

    rotation_matrix = np.dot(rotation_matrix_pitch, rotation_matrix_roll)

    plane_vertices = np.array([
        [-0.5, -0.5, 0],
        [0.5, -0.5, 0],
        [0.5, 0.5, 0],
        [-0.5, 0.5, 0]
    ])

    rotated_plane = np.dot(plane_vertices, rotation_matrix)

    rotated_plane = rotated_plane.reshape((4, 3))

    ax.plot(rotated_plane[:,0], rotated_plane[:,1],rotated_plane[:, 2], color='b', alpha=0.6)

    canvas.draw()
    root.after(100, update_rotation_3D)

if os.environ.get('DISPLAY', '') == '':
    print('No Display Found.\nUsing: 0.0')
    os.environ.__setitem__('DISPLAY', ':0.0')

# Initialize tkinter
root = tk.Tk()
root.title("MPU6050 3D Rotation Display")

# Initialize I2C bus
bus = smbus2.SMBus(1)

fig = plt.figure()
ax =p3.Axes3D(fig)

# Tkinter Canvas
canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Call the update function
update_rotation_3D()

# Start the tkinter main loop
root.mainloop()
