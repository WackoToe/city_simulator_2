import numpy as np
class Agent:
    def __init__(self, home_pos, work_pos, everyday_work_hours):
        """Inizializza l'agente con una posizione nella matrice."""
        self.home = (home_pos[0], home_pos[1])
        self.x, self.y = self.home[0], self.home[1]
        self.to_home = False

        self.workplace = (work_pos[0], work_pos[1])
        self.everyday_work_hours = everyday_work_hours
        self.today_work_hours = everyday_work_hours
        self.to_work = True

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

    def decision(self):
        if self.x == self.workplace[0] and self.y == self.workplace[1]:
            if self.today_work_hours != 0:
                self.today_work_hours -= 1
                return 0, 0
            else:
                self.to_work = not self.to_work
                self.to_home = not self.to_home
                self.today_work_hours = self.everyday_work_hours

        if self.to_work:
            dx, dy = self.walk((self.workplace[0] - self.x, self.workplace[1] - self.y))
        elif self.to_home:
            dx, dy = self.walk((self.home[0] - self.x, self.home[1] - self.y))
            if dx == 0 and dy == 0:
                self.to_home = not self.to_home
                self.to_work = not self.to_work
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