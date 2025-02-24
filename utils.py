import random

def generate_random_position(rows, cols):
    x = random.randint(0, rows - 1)
    y = random.randint(0, cols - 1)
    return (x, y)