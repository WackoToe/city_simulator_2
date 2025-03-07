import random
import numpy as np

from stats import stat_dict
class Agent:
    def __init__(self, world_time, home_pos, work_pos, everyday_work_hours):
        # Initialize the agent's position and status
        self.world_time = world_time
        self.home = (home_pos[0], home_pos[1])
        self.to_home = True

        self.workplace = (work_pos[0], work_pos[1])
        self.work_time_start = 8
        self.work_time_end = 17
        self.to_work = False

        self.everyday_work_hours = everyday_work_hours

        self.sleeping = False

        # print(home_pos)
        num = random.uniform(0, 1)
        num = 0
        # print(num)
        self.got_car = num < stat_dict["car_own"]
        self.car_speed = 5

        self.x, self.y = self.home[0], self.home[1]

    def walk(self, direction):
        if direction[0] is not 0:
            dx = int(direction[0]/np.abs(direction[0]))
            dy = 0
        elif direction[1] is not 0:
            dx = 0
            dy = int(direction[1]/np.abs(direction[1]))
        else:
            dx, dy = 0, 0

        return dx, dy
    
    def car(self, direction):
        if np.abs(direction[0]) + np.abs(direction[1]) <= self.car_speed:
            return direction[0], direction[1]
        
        if direction[0] == 0:
            return 0, np.sign(direction[1])*self.car_speed
        if direction[1] == 0:
            return np.sign(direction[0])*self.car_speed, 0
        
        moves = [0 for i in range(np.abs(direction[0]))] + [1 for j in range(np.abs(direction[1]))]
        selected_moves = random.sample(moves, self.car_speed)

        dx = int(selected_moves.count(0)/np.sign(direction[0]))
        dy = int(selected_moves.count(1)/np.sign(direction[1]))
        return dx, dy

    def decision(self):
        if self.x == self.workplace[0] and self.y == self.workplace[1]:
            if self.world_time.get_time() == self.work_time_end:
                self.to_work = False
                self.to_home = True
            else: return 0, 0
        elif self.x == self.home[0] and self.y == self.home[1]:
            if self.world_time.get_time() == self.work_time_start:
                self.to_home = False
                self.to_work = True
            else: return 0, 0

        if self.to_work:
            if self.got_car:
                dx, dy = self.car((self.workplace[0] - self.x, self.workplace[1] - self.y))
            else:
                dx, dy = self.walk((self.workplace[0] - self.x, self.workplace[1] - self.y))
        elif self.to_home:
            if self.got_car:
                dx, dy = self.car((self.home[0] - self.x, self.home[1] - self.y))
            else:
                dx, dy = self.walk((self.home[0] - self.x, self.home[1] - self.y))
            # if dx == 0 and dy == 0:
            #     self.to_home = not self.to_home
            #     self.to_work = not self.to_work
        return dx, dy

    def move(self, dx, dy, max_x, max_y):
        """
        Sposta l'agente di (dx, dy), garantendo che rimanga nei limiti della matrice.
        :param dx: Spostamento lungo l'asse x.
        :param dy: Spostamento lungo l'asse y.
        :param max_x: Larghezza massima della matrice.
        :param max_y: Altezza massima della matrice.
        """
        new_x = max(0, min(self.x + dx, max_x - 1))
        new_y = max(0, min(self.y + dy, max_y - 1))

        self.x, self.y = new_x, new_y

    def get_position(self):
        """Restituisce la posizione corrente dell'agente."""
        return self.x, self.y