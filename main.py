import time
import random
import numpy as np

from initialization import init_function
from utils import clear_screen



def main():
    rows, cols = 8, 8  # City size
    refresh_rate = 1  # Seconds between each update
    pop_num = 2   # Initial population

    random.seed(22)

    city = init_function(rows, cols, pop_num)

    while True:
        clear_screen()  # Clear the screen
        city.update_city()  # Updates the city matrix
        city.print_city_matrix()  # Print the updated city matrix
        time.sleep(refresh_rate)  # Wait before the next update

if __name__ == "__main__":
    main()
