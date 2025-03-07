import random
import os

# Generates a random position in the matrix
def generate_random_position(rows, cols):
    x = random.randint(0, rows - 1)
    y = random.randint(0, cols - 1)
    return (x, y)

# Generates a list of stations having some constraints
# Stations are randomly placed, but they follow a logical path.
# They don't go back on themselves.
# They follow a senseful path (e.g. a horizontal, vertical or gently curved line).
# def generate_stations(rows, cols, num_stations):
#     stations = []
#     row_modifier = 1 if random.random() < 0.5 else -1
#     row_adder = rows*(0.35 + random.random() * 0.1)
#     col_modifier = 1 if random.random() < 0.5 else -1
#     col_adder = cols*(0.35 + random.random() * 0.1)
#     start_row = int(rows / 2) + row_modifier * int(row_adder)
#     start_col = int(cols / 2) + col_modifier * int(col_adder)
#     stations.append((start_row, start_col))
#     print(stations)

#     # Determine the direction of the stations. If the starting station is in the upper half of the matrix,
#     # the stations will go down. If the starting station is in the lower half, the stations will go up.
#     # Same for the columns.
#     if start_row < int(rows / 2): row_modifier = 1
#     else: row_modifier = -1
#     if start_col < int(cols / 2): col_modifier = 1
#     else: col_modifier = -1

#     num_stations = 5
#     row_starters = [start_row] + [(num_stations - 1) * row_modifier * i + start_row for i in range(1, num_stations)]
#     col_starters = [start_col] + [(num_stations - 1) * col_modifier * i + start_col for i in range(1, num_stations)]
#     print(row_starters)
#     print(col_starters)
#     exit()

#     print(num_stations)
#     for i in range(1, num_stations):
#         prev_row, prev_col = stations[i-1]
#         new_row, new_col = prev_row, prev_col

#         while new_row == prev_row and new_col == prev_col:
#             # Next station's row is gonna be a random number between 10% and 90% 
#             # of the total rows divided by the number of stations
#             row_adder = int(((0.2 + random.random() * 1.2) * rows)/num_stations)
#             print(row_adder)
#             new_row = prev_row + row_modifier * row_adder
#             if new_row >= rows: new_row = rows
#             if new_row < 0: new_row = 0

#             # Same for the columns
#             col_adder = int(((0.2 + random.random() * 1.2) * cols)/num_stations)
#             print(col_adder)
#             new_col = prev_col + col_modifier * col_adder
#             if new_col >= cols: new_col = cols
#             if new_col < 0: new_col = 0

#             new_station = (new_row, new_col)
#             stations.append(new_station)
#     # exit()
#     return stations

# Generates a list of stations having some constraints
# Stations are randomly placed, but they follow a logical path.
# They don't go back on themselves.
# They follow a senseful path (e.g. a horizontal, vertical or gently curved line).
def generate_stations(rows, cols, num_stations):
    interval_rows = rows / num_stations
    interval_cols = cols / num_stations
    stations_rows = [int(interval_rows * i) for i in range(num_stations)]
    stations_cols = [int(interval_cols * i) for i in range(num_stations)]

    stations = []

    print(stations_rows)
    for i in range(num_stations):
        row_modifier = random.randint(0, interval_rows-1)
        col_modifier = random.randint(0, interval_cols-1)
        stations_rows[i] = stations_rows[i] + row_modifier
        stations_cols[i] = stations_cols[i] + col_modifier
        stations.append((stations_rows[i], stations_cols[i]))
        
    return stations

# Just a simple function to clear the screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
