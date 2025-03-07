import time
import random
import numpy as np

from initialization import init_function
from utils import clear_screen



def main():
    rows, cols = 10, 10  # City size
    refresh_rate = 0.5  # Seconds between each update
    pop_num = 2   # Initial population
    lines_num = 1  # Number of bus lines

    # random.seed(22)
    # random.seed(7)
    random.seed(10)

    world_time, city = init_function(rows, cols, pop_num, lines_num)

    while True:
        clear_screen()  # Clear the screen
        city.update_city()  # Updates the city matrix
        world_time.update_time()  # Updates the world time
        city.print_city_matrix()  # Print the updated city matrix
        city.save_city_matrix()
        time.sleep(refresh_rate)  # Wait before the next update

if __name__ == "__main__":
    main()
