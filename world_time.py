class World_Time():
    def __init__(self):
        self.time = 6
        self.day = 0

    def get_day(self):
        return self.day

    def get_time(self):
        return self.time
    
    def update_time(self):
        self.time += 1
        self.check_new_day()
        return
    
    def check_new_day(self):
        if self.time == 24:
            self.time = 0
            self.day += 1
        return