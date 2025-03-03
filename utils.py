import random
import os

# Generates a random position in the matrix
def generate_random_position(rows, cols):
    x = random.randint(0, rows - 1)
    y = random.randint(0, cols - 1)
    return (x, y)


# Just a simple function to clear the screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    