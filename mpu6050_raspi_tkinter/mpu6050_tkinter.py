import pygame
import smbus2
import math
import os
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

def draw_rotated_rect(screen, color, rect, angle):
    rotated_rect = pygame.transform.rotate(rect, angle)
    new_rect = rotated_rect.get_rect(center=rect.center)
    screen.blit(rotated_rect, new_rect.topleft)

if os.environ.get('DISPLAY', '') == '':
    print('No Display Found.\nUsing: 0.0')
    os.environ.__setitem__('DISPLAY', ':0.0')

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("MPU6050 3D Rotation Display")

# Initialize I2C bus
bus = smbus2.SMBus(1)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    accel_x, accel_y, _ = read_mpu_accel_data()
    roll = math.atan2(accel_y, 9.8) * (180.0 / math.pi)

    # Clear the screen
    screen.fill((255, 255, 255))

    # Create a rectangle using Numpy
    rect_size = (100, 50)
    rect = pygame.Surface(rect_size)
    rect.fill((0, 0, 255))
    rect_center = np.array([width // 2, height // 2])
    rect_pos = rect_center - np.array([rect_size[0] // 2, rect_size[1] // 2])
    rect_rect = pygame.Rect(rect_pos[0], rect_pos[1], rect_size[0], rect_size[1])

    # Draw the rotated rectangle
    draw_rotated_rect(screen, (0, 0, 255), rect, roll)

    pygame.display.flip()
    clock.tick(60)
