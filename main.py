import os
import time
import random
import numpy as np

from colorama import Fore, Style, init

from initialization import init_function
from update_city import update_city



# Inizializza Colorama (necessario per Windows)
init(autoreset=True)

def clear_screen():
    """Pulisce la schermata del terminale."""
    os.system('cls' if os.name == 'nt' else 'clear')



def print_matrix(matrix, population):
    """Stampa la matrice con alcuni numeri colorati."""
    homes = []
    workplaces = []
    for agent in population:
        homes.append(agent.home)
        workplaces.append(agent.workplace)

    for i, row in enumerate(matrix):
        for j, num in enumerate(row):
            # Assegna un colore casuale solo al 50% dei numeri
            if (i, j) in homes:
                # color = random.choice([Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN])
                color = Fore.GREEN
                print(color + str(num), end=" ")  # Stampa colorato
            elif (i, j) in workplaces:
                color = Fore.RED
                print(color + str(num), end=" ")
            else:
                print(str(num), end=" ")  # Stampa normale
        print()  # Vai a capo dopo ogni riga

def main():
    rows, cols = 8, 8  # Dimensioni della matrice
    refresh_rate = 1  # Secondi tra un aggiornamento e l'altro
    pop_num = 2   # Numero di abitanti all'inizio

    random.seed(22)

    city_matrix, population = init_function(rows, cols, pop_num)

    while True:
        clear_screen()  # Pulisce lo schermo
        city_matrix, population = update_city(rows, cols, population)  # Genera una nuova matrice
        print_matrix(city_matrix, population)  # Stampa la matrice con colori
        time.sleep(refresh_rate)  # Aspetta prima del prossimo aggiornamento

if __name__ == "__main__":
    main()
