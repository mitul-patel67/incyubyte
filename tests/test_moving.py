import unittest
import os
import sys

script_dir = os.path.dirname(os.path.abspath(__file__))
module_path = os.path.join(script_dir, '..')  

sys.path.append(module_path)

from main import Spacecraft  

class TestSpacecraftMovement(unittest.TestCase):

    def get_valid_direction(self):
        while True:
            initial_direction = input("Enter initial direction: Choose from 'N', 'S', 'E', 'W', 'Up', 'Down' :: ").strip().title()
            if initial_direction in ['N', 'S', 'E', 'W', 'Up', 'Down']:
                return initial_direction
            else:
                print("Invalid direction. Choose from 'N', 'S', 'E', 'W', 'Up', 'Down'.")

    def get_valid_position(self):
        while True:
            try:
                initial_position = [int(x) for x in input("Enter initial position (x y z): ").split()]
                if len(initial_position) == 3:
                    return initial_position
                else:
                    print("Invalid input. Enter three integers separated by spaces.")
            except ValueError:
                print("Invalid input. Enter three integers separated by spaces.")

    def get_valid_commands(self):
        while True:
            command_str = input("Enter commands (e.g. 'f r u b l d'): ").upper()
            commands = command_str.split()
            valid_commands = {'F', 'B', 'R', 'L', 'U', 'D'}
            if all(command in valid_commands for command in commands):
                return commands
            else:
                print("Invalid commands. Use only 'F', 'B', 'R', 'L', 'U', 'D'.")

    def execute_commands(self, commands):
        def execute_commands(self, commands):
         for command in commands:
            if command == 'F':
                self.space_craft.move_forward('F')
            elif command == 'B':
                self.space_craft.move_backward('B')
            elif command == 'R':
                self.space_craft.turn_right('R')
            elif command == 'L':
                self.space_craft.turn_left('L')
            elif command == 'U':
                self.space_craft.turn_up('U')
            elif command == 'D':
                self.space_craft.turn_down('D')

    def test_execute_commands(self):
        initial_direction = self.get_valid_direction()
        initial_position = self.get_valid_position()
        commands = self.get_valid_commands()

        space_craft = Spacecraft(initial_position, initial_direction)

        self.execute_commands(commands)
        self.assertEqual(space_craft.getPosition(), [1, 0, 0])

if __name__ == '__main__':
    unittest.main()
