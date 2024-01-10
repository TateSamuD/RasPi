import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Rotating 3D Object")

clock = pygame.time.Clock()

# Function to draw a cube
def draw_cube(surface, size, angle):
    half_size = size // 2
    points = [
        (half_size, -half_size),
        (-half_size, -half_size),
        (-half_size, half_size),
        (half_size, half_size),
        (half_size, -half_size),
        (half_size, -half_size + size),
        (-half_size, -half_size + size),
        (-half_size, half_size + size),
        (half_size, half_size + size),
        (half_size, -half_size + size),
        (-half_size, -half_size + 2 * size),
        (-half_size, half_size + 2 * size),
        (half_size, half_size + 2 * size),
        (half_size, -half_size + 2 * size),
    ]

    rotated_points = [
        (
            x * math.cos(math.radians(angle)) - y * math.sin(math.radians(angle)),
            x * math.sin(math.radians(angle)) + y * math.cos(math.radians(angle)),
        )
        for x, y in points
    ]

    translated_points = [
        (x + width // 2, y + height // 2) for x, y in rotated_points
    ]

    pygame.draw.lines(surface, (255, 255, 255), True, translated_points, 2)

# Main loop
angle = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0, 0, 0))

    draw_cube(screen, 50, angle)

    pygame.display.flip()
    clock.tick(60)  # Set the frames per second
    angle += 1  # Adjust rotation speed as needed
