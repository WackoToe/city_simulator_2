
class Underground:
    def __init__(self, line_name, names, locations):

        if len(names) != len(locations):
            print("[ERR] Names and locations must have the same length")
            exit(1)

        self.line_name = line_name
        self.names = names
        self.locations = locations

    def get_station_names_and_locations(self):
        return self.names, self.locations
    
    def print_station_names_and_locations(self):
        print("Line: {}".format(self.line_name))
        for i in range(len(self.names)):
            print("{}: {}".format(self.names[i], self.locations[i]))

    def next_station(self, current_station, direction):
        if current_station not in self.names:
            print("[ERR] Station not found")
            exit(1)
        station_index = self.names.index(current_station)
        if direction == self.names[0]:
            return self.names[station_index - 1], self.locations[station_index - 1]
        elif direction == self.names[-1]:
            return self.names[station_index + 1], self.locations[station_index + 1]
        else:
            print("[ERR] Invalid direction")
            exit(1)
