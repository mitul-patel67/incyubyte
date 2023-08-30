class Spacecraft:

    def __init__(self,initial_position,initial_direction):
        self.position = initial_position
        self.direction = initial_direction

    def move(self,command):
        if command == 'f':
            if self.direction == 'n':
                self.position = (self.position[0],self.position[1]+2,self.position[2])
    def getPosition(self):
        return self.position