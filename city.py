import csv
import numpy as np

from rich.console import Console

class City:
    def __init__(self, world_time, rows, cols, population):
        self.world_time = world_time
        self.rows = rows
        self.cols = cols
        self.population = population
        self.city_matrix = self.generate_matrix()

    def generate_matrix(self):
        city_matrix = np.zeros((self.rows, self.cols), dtype=int)  # Matrice di zeri
        for i, agent in enumerate(self.population):
            city_matrix[agent.home[0]][agent.home[1]] += 1
        return city_matrix

    def update_city(self):
        new_city_matrix = np.zeros((self.rows, self.cols), dtype=int)  # Matrice di zeri
        for agent in self.population:
            dx, dy = agent.decision()
            agent.move(dx, dy, self.rows, self.cols)
            x, y = agent.get_position()
            new_city_matrix[x][y] += 1
        self.city_matrix = new_city_matrix

    def print_city_matrix(self):
        # First, we print the current time
        # print(Fore.CYAN + f"Day: {self.world_time.get_day()}\tTime: {self.world_time.get_time()}")
        console = Console()
        day_and_time_color = "ffb000"
        home_color = "#648fff"
        workplace_color = "#fe6100"

        console.print("[{}]Day: {}\tTime: {}".format(day_and_time_color, self.world_time.get_day(), self.world_time.get_time()))

        # Print the city matrix at every iteration
        homes = []
        workplaces = []
        for agent in self.population:
            homes.append(agent.home)
            workplaces.append(agent.workplace)

        for i, row in enumerate(self.city_matrix):
            for j, num in enumerate(row):
                if (i, j) in homes:
                    console.print("[{}]{}".format(home_color, num), end=" ")
                elif (i, j) in workplaces:
                    console.print("[{}]{}".format(workplace_color, num), end=" ")
                else:
                    print(str(num), end=" ")  # Print the number in white
            print()  # new line

    def save_city_matrix(self, filename="city_matrix.csv"):
        # Saves all the instance attributes in a CSV file
        attributes = vars(self)  # Obtain all the attributes of the instance

        # Writes the attributes in a CSV file
        with open(filename, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(attributes.keys())  # Headers, attribute names
            writer.writerow(attributes.values())  # Attribute values