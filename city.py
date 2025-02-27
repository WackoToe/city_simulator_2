import numpy as np

from colorama import Fore, Style

class City:
    def __init__(self, rows, cols, population):
        self.time = 8
        self.rows = rows
        self.cols = cols
        self.population = population
        self.city_matrix = self.generate_matrix()

    def generate_matrix(self):
        city_matrix = np.zeros((self.rows, self.cols), dtype=int)  # Matrice di zeri
        for i, agent in enumerate(self.population):
            city_matrix[agent.home[0]][agent.home[1]] += 1
        return city_matrix
    
    def check_new_day(self):
        if self.time == 24:
            self.time = 0
        return

    def update_city(self):
        new_city_matrix = np.zeros((self.rows, self.cols), dtype=int)  # Matrice di zeri
        for agent in self.population:
            dx, dy = agent.decision()
            agent.move(dx, dy, self.rows, self.cols)
            x, y = agent.get_position()
            new_city_matrix[x][y] += 1
        self.city_matrix = new_city_matrix
        self.time += 1
        self.check_new_day()

    def print_city_matrix(self):
        # First, we print the current time
        print(Fore.CYAN + f"Time: {self.time}")

        # Print the city mmatrix at every iteration
        homes = []
        workplaces = []
        for agent in self.population:
            homes.append(agent.home)
            workplaces.append(agent.workplace)

        for i, row in enumerate(self.city_matrix):
            for j, num in enumerate(row):
                if (i, j) in homes:
                    color = Fore.GREEN
                    print(color + str(num), end=" ")  # Stampa colorato
                elif (i, j) in workplaces:
                    color = Fore.RED
                    print(color + str(num), end=" ")
                else:
                    print(str(num), end=" ")  # Stampa normale
            print()  # Vai a capo dopo ogni riga