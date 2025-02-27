import random
import os

def generate_random_position(rows, cols):
    # Generates a random position in the matrix
    x = random.randint(0, rows - 1)
    y = random.randint(0, cols - 1)
    return (x, y)

def clear_screen():
    # Just a simple function to clear the screen
    os.system('cls' if os.name == 'nt' else 'clear')