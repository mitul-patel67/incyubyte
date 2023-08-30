import unittest
import os
import sys

script_dir = os.path.dirname(os.path.abspath(__file__))
module_path = os.path.join(script_dir, '..')  

sys.path.append(module_path)

from main import Spacecraft  

class TestSpacecraftMovement(unittest.TestCase):
     initial_direction = input("Enter initial direction: Choose from 'N', 'S', 'E', 'W', 'Up', 'Down' :: ")
     initial_position = [int(x) for x in input("Enter initial position (x y z): ").split()]
     space_craft = Spacecraft(initial_position, initial_direction.title()) 

     def test_move_forward(self):    
        self.space_craft.move_forward('F')
        self.assertEqual(self.space_craft.getPosition(), [0, 2, 0])

     def test_move_backward(self):
        self.space_craft.move_backward('B')
        self.assertEqual(self.space_craft.getPosition(), [0, 0, 0])

     def test_turn_right(self):
        self.space_craft.turn_right('R')
        self.assertEqual(self.space_craft.getPosition(), [0, 2, 0])

     def test_turn_left(self):
        self.space_craft.turn_left('L')
        self.assertEqual(self.space_craft.getPosition(), [0, 2, 0])

     def test_turn_Up(self):
        self.space_craft.turn_Up('U')
        self.assertEqual(self.space_craft.getPosition(), [0, 2, 0])

     def test_turn_Down(self):
        self.space_craft.turn_Down('')
        self.assertEqual(self.space_craft.getPosition(), [0, 2, 0])


if __name__ == '__main__':
    unittest.main()