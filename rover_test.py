import unittest

from rover import Rover

class RoverTest(unittest.TestCase):
    def test_placement(self):
        rover = Rover("1 2 N")
        self.assertEqual((1, 2), rover.get_position())
        self.assertEqual("N", rover.get_heading())

    def test_instruction_set(self):
        rover = Rover("1 2 N")
        rover.send_instructions("LMLMLMLMM")
        self.assertEqual((1, 3), rover.get_position())
        self.assertEqual("N", rover.get_heading())

    def test_turn_left(self):
        rover = Rover("1 2 N")
        rover.send_instructions("L")
        self.assertEqual("W", rover.get_heading())
        rover.send_instructions("L")
        self.assertEqual("S", rover.get_heading())

    def test_turn_right(self):
        rover = Rover("1 2 N")
        rover.send_instructions("R")
        self.assertEqual("E", rover.get_heading())
        rover.send_instructions("R")
        self.assertEqual("S", rover.get_heading())

    def test_move_north(self):
        rover = Rover("1 2 N")
        rover.send_instructions("M")
        self.assertEqual((1, 3), rover.get_position())

    def test_move_south(self):
        rover = Rover("1 2 S")
        rover.send_instructions("M")
        self.assertEqual((1, 1), rover.get_position())

    def test_move_east(self):
        rover = Rover("1 2 E")
        rover.send_instructions("M")
        self.assertEqual((2, 2), rover.get_position())

    def test_move_west(self):
        rover = Rover("1 2 W")
        rover.send_instructions("M")
        self.assertEqual((0, 2), rover.get_position())
