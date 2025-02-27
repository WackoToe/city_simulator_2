import numpy as np
from agent import Agent
from city import City
from utils import generate_random_position

from colorama import init

def setup_agents(rows, cols, pop_num):
    agents = []
    for i in range(pop_num):
        home_pos = generate_random_position(rows, cols)
        work_pos = generate_random_position(rows, cols)
        work_hours = 3
        agents.append(Agent(home_pos, work_pos, work_hours))
    return agents



def setup_stations():
    return

def init_function(rows, cols, pop_num):
    # Inizializza Colorama (necessario per Windows)
    init(autoreset=True)

    # Initialize the population
    population = setup_agents(rows, cols, pop_num)

    # Initialize the stations. Empty now!
    setup_stations()
    
    # Initialize the city matrix
    city = City(rows, cols, population)
    return city