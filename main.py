class Spacecraft:
    @staticmethod
    def main():
        position = [0,0,0]
        direction = 'N' #use  only UPPER CASE letters
        commands = ['f','r','u','b','l']
        array_of_directions = [direction]
        last_direction = direction
        
        for cmd in commands:
            if cmd == 'f':
                Spacecraft.move_forward(direction, position)
            elif cmd == 'b':
                Spacecraft.move_backward(direction, position)
            elif cmd == 'r':
                last_direction = Spacecraft.find_last_direction(array_of_directions, len(array_of_directions))
                direction = Spacecraft.turn_right(direction, last_direction)
                array_of_directions.append(direction)
            elif cmd == 'l':
                last_direction = Spacecraft.find_last_direction(array_of_directions, len(array_of_directions))
                direction = Spacecraft.turn_left(direction, last_direction)
                array_of_directions.append(direction)
            elif cmd == 'u':
                direction = Spacecraft.turn_up(direction)
                array_of_directions.append(direction)
            elif cmd == 'd':
                direction = Spacecraft.turn_down(direction)
                array_of_directions.append(direction)
        
        print(f"Final Direction: {direction}")
        print(f"Final Position: ({position[0]}, {position[1]}, {position[2]})")

    @staticmethod
    def move_forward(direction, position):
        if direction == 'N':
            position[1] += 1
        elif direction == 'S':
            position[1] -= 1
        elif direction == 'E':
            position[0] += 1
        elif direction == 'W':
            position[0] -= 1
        elif direction == 'U':
            position[2] += 1
        elif direction == 'D':
            position[2] -= 1

    @staticmethod
    def move_backward(direction, position):
        if direction == 'N':
            position[1] -= 1
        elif direction == 'S':
            position[1] += 1
        elif direction == 'E':
            position[0] -= 1
        elif direction == 'W':
            position[0] += 1
        elif direction == 'U':
            position[2] -= 1
        elif direction == 'D':
            position[2] += 1

    @staticmethod
    def turn_right(direction, last_direction):
        if direction == 'N':
            return 'E'
        elif direction == 'S':
            return 'W'
        elif direction == 'E':
            return 'S'
        elif direction == 'W':
            return 'N'
        elif direction == 'U':
            if last_direction == 'E':
                return 'S'
            elif last_direction == 'W':
                return 'N'
            elif last_direction == 'N':
                return 'E'
            elif last_direction == 'S':
                return 'W'
            else:
                return direction
        elif direction == 'D':
            if last_direction == 'E':
                return 'S'
            elif last_direction == 'W':
                return 'N'
            elif last_direction == 'N':
                return 'E'
            elif last_direction == 'S':
                return 'W'
            else:
                return direction
        else:
            return direction

    @staticmethod
    def turn_left(direction, last_direction):
        if direction == 'N':
            return 'W'
        elif direction == 'S':
            return 'E'
        elif direction == 'E':
            return 'N'
        elif direction == 'W':
            return 'S'
        elif direction == 'U':
            if last_direction == 'E':
                return 'N'
            elif last_direction == 'W':
                return 'S'
            elif last_direction == 'N':
                return 'W'
            elif last_direction == 'S':
                return 'E'
        elif direction == 'D':
            if last_direction == 'E':
                return 'N'
            elif last_direction == 'W':
                return 'S'
            elif last_direction == 'N':
                return 'W'
            elif last_direction == 'S':
                return 'E'
        else:
            return direction

    @staticmethod
    def turn_up(direction):
        if direction in ['N', 'S', 'E', 'W']:
            return 'U'
        else:
            return direction

    @staticmethod
    def turn_down(direction):
        if direction in ['N', 'S', 'E', 'W']:
            return 'D'
        else:
            return direction

    @staticmethod
    def find_last_direction(array_of_directions, i):
        for j in range(i - 1, -1, -1):
            temp = array_of_directions[j]
            if temp != 'U' and temp != 'D':
                return temp
        return array_of_directions[i - 1]

# Run the main method when the script is executed
Spacecraft.main()