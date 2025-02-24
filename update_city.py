import numpy as np

def update_city(rows, cols, population):
    city_matrix = np.zeros((rows, cols), dtype=int)  # Matrice di zeri
    for agent in population:
        dx, dy = agent.decision()
        agent.move(dx, dy, rows, cols)
        x, y = agent.get_position()
        city_matrix[x][y] += 1
    # return new_world_matrix
    return city_matrix, population