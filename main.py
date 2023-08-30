class Spacecraft:

    def __init__(self,initial_position,initial_direction):
        self.position = initial_position
        self.direction = initial_direction

    def move_forward(self,command):
        if command == 'F':
            if self.direction == 'E':
                self.position = (self.position[0],self.position[1]+2,self.position[2])

    def move_backward(self,command):
        if command == 'B':
            if self.direction == 'W':
                self.position = (self.position[0],self.position[1]-2,self.position[2])

    def turn_left(self,command):
        if command == 'R':
            if self.direction == 'N':
                self.position = (self.position[0]+2,self.position[1],self.position[2])

    def turn_right(self,command):
        if command == 'L':
            if self.direction == 'S':
                self.position = (self.position[0]-2,self.position[1],self.position[2])

    def turn_Up(self,command):
        if command == 'U':
            if self.direction == 'Up':
                self.position = (self.position[0],self.position[1],self.position[2]+2)

    def turn_Down(self,command):
        if command == 'D':
            if self.direction == 'Down':
                self.position = (self.position[0],self.position[1],self.position[2]-2)

    def getPosition(self):
        return list(self.position)