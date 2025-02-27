import numpy as np
from world_time import World_Time
from agent import Agent
from city import City
from utils import generate_random_position

from colorama import init

def setup_agents(world_time, rows, cols, pop_num):
    agents = []
    for i in range(pop_num):
        home_pos = generate_random_position(rows, cols)
        work_pos = generate_random_position(rows, cols)
        work_hours = 3
        agents.append(Agent(world_time, home_pos, work_pos, work_hours))
    return agents



def setup_stations():
    return

def init_function(rows, cols, pop_num):
    # Initialize Colorama (required for Windows)
    init(autoreset=True)

    # Initialize the world time
    world_time = World_Time()

    # Initialize the population
    population = setup_agents(world_time, rows, cols, pop_num)

    # Initialize the stations. Empty now!
    setup_stations()
    
    # Initialize the city matrix
    city = City(world_time, rows, cols, population)
    return world_time, city