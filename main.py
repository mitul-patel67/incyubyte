class Spacecraft:

    def __init__(self,initial_position,initial_direction):
        self.position = initial_position
        self.direction = initial_direction

    def move_forward(self,command):
        if command == 'f':
            if self.direction == 'n':
                self.position = (self.position[0],self.position[1]+2,self.position[2])

    def move_backward(self,command):
        if command == 'b':
            if self.direction == 'n':
                self.position = (self.position[0],self.position[1]-2,self.position[2])

    def turn_left(self,command):
        if command == 'r':
            if self.direction == 'n':
                self.position = (self.position[0]+2,self.position[1],self.position[2])

    def turn_right(self,command):
        if command == 'l':
            if self.direction == 'n':
                self.position = (self.position[0]-2,self.position[1],self.position[2])

    def turn_Up(self,command):
        if command == 'u':
            if self.direction == 'n':
                self.position = (self.position[0],self.position[1],self.position[2]+2)

    def turn_Down(self,command):
        if command == 'd':
            if self.direction == 'n':
                self.position = (self.position[0],self.position[1],self.position[2]-2)

    def getPosition(self):
        return self.position