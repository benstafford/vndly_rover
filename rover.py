class Rover:
    def __init__(self, starting_position, map=None):
        parsed_position = starting_position.split(" ")
        self.x = int(parsed_position[0])
        self.y = int(parsed_position[1])
        self.heading = parsed_position[2]

        if map:
            parsed_map = map.split(" ")
            self.maximum_x = int(parsed_map[0])
            self.maximum_y = int(parsed_map[1])
        else:
            self.maximum_x = None
            self.maximum_y = None

        self.directions = ['N', 'E', 'S', 'W']
        self.move_list = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def get_position(self):
        return (self.x, self.y)

    def get_heading(self):
        return self.heading

    def get_readable_location(self):
        return f'{self.x} {self.y} {self.heading}'

    def send_instructions(self, instruction_set):
        for command in instruction_set:
            self.perform(command)

    def perform(self, command):
        if command == "L":
            self.turn_left()
        elif command == "R":
            self.turn_right()
        elif command == "M":
            self.move()
        else:
            pass

    def turn_left(self):
        current = self.get_heading()
        curr_index = self.directions.index(current)
        self.heading = self.directions[curr_index - 1]

    def turn_right(self):
        current = self.get_heading()
        curr_index = self.directions.index(current)
        self.heading = self.directions[(curr_index + 1) % 4]

    def move(self):
        current = self.get_heading()
        curr_index = self.directions.index(current)

        new_x = self.x + self.move_list[curr_index][0]
        new_y = self.y + self.move_list[curr_index][1]
    
        if self.valid_new_position(new_x, new_y):
            self.x = new_x
            self.y = new_y

    def valid_new_position(self, x, y):
        if self.maximum_x and self.maximum_y:
            on_map = x <= self.maximum_x and y <= self.maximum_y
        else:
            on_map = True
        return x >= 0 and y >= 0 and on_map