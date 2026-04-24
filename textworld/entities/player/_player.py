from textworld.entities.base import BaseEntity

class Player(BaseEntity):

    chunk_x: int
    chunk_y: int

    def __init__(self, x, y, chunk_x, chunk_y):
        super().__init__(x, y)
        self.chunk_x = chunk_x
        self.chunk_y = chunk_y
    
    def get_position(self):
        return (self.x, self.y, self.chunk_x, self.chunk_y)
    
    def chunk_up(self):
        self.chunk_y -= 1

    def chunk_down(self):
        self.chunk_y += 1

    def chunk_left(self):
        self.chunk_x -= 1

    def chunk_right(self):
        self.chunk_x += 1