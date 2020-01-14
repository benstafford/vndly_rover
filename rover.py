class Rover:
    def __init__(self, starting_position):
        parsed_position = starting_position.split(" ")
        self.x = int(parsed_position[0])
        self.y = int(parsed_position[1])
        self.heading = parsed_position[2]
        self.directions = ['N', 'E', 'S', 'W']
        self.move_list = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def get_position(self):
        return (self.x, self.y)

    def get_heading(self):
        return self.heading

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
        self.heading = self.directions[curr_index + 1]

    def move(self):
        current = self.get_heading()
        curr_index = self.directions.index(current)

        self.x = self.x + self.move_list[curr_index][0]
        self.y = self.y + self.move_list[curr_index][1]