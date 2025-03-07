import numpy as np
from world_time import World_Time
from agent import Agent
from city import City
from public_transport import Underground
from utils import generate_random_position, generate_stations

def setup_agents(world_time, rows, cols, pop_num):
    agents = []
    for i in range(pop_num):
        home_pos = generate_random_position(rows, cols)
        work_pos = generate_random_position(rows, cols)
        work_hours = 3
        agents.append(Agent(world_time, home_pos, work_pos, work_hours))
    return agents


def setup_lines(rows, cols, lines_num=1):
    lines = {}
    for i in range(lines_num):
        stations_num = np.random.randint(2, 5)
        stations_num = 5
        stations_names = []
        for j in range(stations_num):
            station_name = "station {}".format(j)
            stations_names.append(station_name)
        stations_locations = generate_stations(rows, cols, stations_num)
        
        line_name = "line {}".format(i)
        lines[line_name] = Underground(line_name, stations_names, stations_locations)
    
    for k in lines.keys():
        lines[k].print_station_names_and_locations()
            
    return lines



def setup_stations():
    return

def init_function(rows, cols, pop_num, lines_num):
    # Initialize the world time
    world_time = World_Time()

    # Initialize the population
    population = setup_agents(world_time, rows, cols, pop_num)

    # Initialize the stations. Empty now!
    public_transport = {}
    metro_lines = setup_lines(rows, cols, lines_num)
    public_transport["metro"] = metro_lines
    
    # Initialize the city matrix
    city = City(world_time, rows, cols, population, public_transport)
    return world_time, city