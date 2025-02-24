import numpy as np
from agent import Agent
from utils import generate_random_position

def setup_agents(rows, cols, pop_num):
    agents = []
    for i in range(pop_num):
        home_pos = generate_random_position(rows, cols)
        work_pos = generate_random_position(rows, cols)
        work_hours = 3
        agents.append(Agent(home_pos, work_pos, work_hours))
    return agents

def generate_matrix(rows, cols, population):
    city_matrix = np.zeros((rows, cols), dtype=int)  # Matrice di zeri
    for i, agent in enumerate(population):
        city_matrix[agent.home[0]][agent.home[1]] += 1
    return city_matrix

def setup_stations():
    return

def init_function(rows, cols, pop_num):
    population = setup_agents(rows, cols, pop_num)
    setup_stations()
    
    city_matrix = generate_matrix(rows, cols, population)
    return city_matrix, population