import time
import random
import numpy as np

from initialization import init_function
from utils import clear_screen



def main():
    rows, cols = 8, 8  # City size
    refresh_rate = 1  # Seconds between each update
    pop_num = 20   # Initial population

    random.seed(22)

    world_time, city = init_function(rows, cols, pop_num)

    while True:
        clear_screen()  # Clear the screen
        city.update_city()  # Updates the city matrix
        world_time.update_time()  # Updates the world time
        city.print_city_matrix()  # Print the updated city matrix
        city.save_city_matrix()
        time.sleep(refresh_rate)  # Wait before the next update

if __name__ == "__main__":
    main()
