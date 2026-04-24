from textworld.models import Coords, Tile

class BaseEntity():

    _move_table:dict = {'up': False, 'down': False, "left": False, "right": False}

    x: int = 0
    y: int = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def update_positon(self, up, down, left, right):
        self._move_table = {'up':up,'down':down,"left":left,"right":right}
        print(self._move_table)
    
    def get_position(self):
        return (self.x, self.y)
    
    def update(self):
        if self._move_table['up']:
            self.y -= 1
        if self._move_table['down']:
            self.y += 1
        if self._move_table['left']:
            self.x -= 1
        if self._move_table['right']:
            self.x += 1