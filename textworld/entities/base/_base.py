from textworld.models import Coords, Tile

class BaseEntity():

    x: int = 0
    y: int = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def get_position(self):
        return (self.x, self.y)

    def up(self):
        self.y -= 1

    def down(self):
        self.y += 1

    def left(self):
        self.x -= 1

    def right(self):
        self.x += 1
    
    def update(self):
        pass