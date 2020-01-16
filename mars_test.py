import unittest

from mars import Mars
from rover import Rover

class MarsTest(unittest.TestCase):
    def test_place_rover(self):
        mars = Mars("5 5")

        rover = Rover("1 1 N")
        mars.place_rover(rover)

        self.assertEqual([rover], mars.get_rovers())

        rover2 = Rover("6 1 N")
        mars.place_rover(rover2)

        self.assertEqual([rover], mars.get_rovers())