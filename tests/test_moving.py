import unittest
import os
import sys

script_dir = os.path.dirname(os.path.abspath(__file__))
module_path = os.path.join(script_dir, '..')  

sys.path.append(module_path)

from main import Spacecraft  

class TestSpacecraftMovement(unittest.TestCase):
     space_craft = Spacecraft((0, 0, 0), 'n')

     def test_move_forward(self):    
        self.space_craft.move_forward('f')
        self.assertEqual(self.space_craft.getPosition(), (0, 0, 0))

     def test_move_backward(self):
        self.space_craft.move_backward('b')
        self.assertEqual(self.space_craft.getPosition(), (0, -2, 0))

     def test_turn_right(self):
        self.space_craft.turn_right('r')
        self.assertEqual(self.space_craft.getPosition(), (0, 0, 0))

     def test_turn_left(self):
        self.space_craft.turn_left('l')
        self.assertEqual(self.space_craft.getPosition(), (0, 0, 0))

     def test_turn_Up(self):
        self.space_craft.turn_Up('u')
        self.assertEqual(self.space_craft.getPosition(), (0, 0, 0))

     def test_turn_Down(self):
        self.space_craft.turn_Down('d')
        self.assertEqual(self.space_craft.getPosition(), (0, 0, -2))


if __name__ == '__main__':
    unittest.main()