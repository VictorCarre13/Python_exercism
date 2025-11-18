# Globals for the directions
# Change the values as you see fit
WEST = 1
NORTH = 2
EAST = 3
SOUTH = 4


class Robot:
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        self.direction=direction
        self.x=x_pos
        self.y=y_pos
        self.coordinates=(self.x, self.y)
    def move(self, orders):
        for order in orders:
            if order not in "RAL":
                raise ValueError ("Incorrect order was given. Must R, A or L.")
            if order=="R":
                if self.direction != 4:
                    self.direction+=1
                else:
                    self.direction=1
            if order=="L":
                if self.direction != 1:
                    self.direction-=1
                else:
                    self.direction=4
            if order=="A":
                if self.direction==WEST:
                    self.x-=1
                if self.direction==NORTH:
                    self.y+=1
                if self.direction==EAST:
                    self.x+=1
                if self.direction==SOUTH:
                    self.y-=1
        self.coordinates=(self.x, self.y)