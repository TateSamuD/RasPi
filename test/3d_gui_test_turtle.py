import turtle
import time
import math

# Set up the turtle
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Rotating 3D Object")

pen = turtle.Turtle()
pen.speed(0)  # Set the drawing speed (0 is the fastest)

# Function to draw a square
def draw_square(size):
    for _ in range(4):
        pen.forward(size)
        pen.right(90)

# Function to draw a 3D-like object
def draw_3d_object(size, num_sides):
    for _ in range(num_sides):
        draw_square(size)
        pen.forward(size)
        pen.right(360 / num_sides)

# Function to rotate the object
def rotate_object(angle):
    pen.left(angle)

# Main loop
while True:
    pen.clear()  # Clear the previous frame
    draw_3d_object(50, 8)  # Adjust size and number of sides as needed
    rotate_object(1)  # Adjust rotation speed as needed
    screen.update()  # Update the screen
    time.sleep(0.02)  # Adjust the delay to control the rotation speed
