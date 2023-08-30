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
        self.space_craft.move('f')
        self.assertEqual(self.space_craft.getPosition(), (0, 1, 0))

if __name__ == '__main__':
    unittest.main()
