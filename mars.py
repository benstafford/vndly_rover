class Mars:
    def __init__(self, map):
        parsed_map = map.split(" ")
        self.maximum_x = int(parsed_map[0])
        self.maximum_y = int(parsed_map[1])
        self.rovers = []

    def get_rovers(self):
        return self.rovers

    def place_rover(self, rover):
        if self.is_valid_position(rover):
            self.rovers.append(rover)

    def is_valid_position(self, rover):
        rover_position = rover.get_position()
        return rover_position[0] <= self.maximum_x and rover_position[1] <= self.maximum_y