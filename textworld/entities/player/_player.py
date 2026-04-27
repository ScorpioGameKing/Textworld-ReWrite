from textworld.entities.base import BaseEntity

class Player(BaseEntity):

    chunk_x: int
    chunk_y: int
    _chunk_size: Size

    def __init__(self, x, y, chunk_x, chunk_y, _chunk_size):
        super().__init__(x, y)
        self.chunk_x = chunk_x
        self.chunk_y = chunk_y
        self._chunk_size = _chunk_size
    
    def get_position(self):
        return (self.x, self.y, self.chunk_x, self.chunk_y)
    
    def up(self):
        print(self.get_position())
        super().up()
        if self.y <= 0:
            self.chunk_y -= 1
            self.y = self._chunk_size.height - 1

    def down(self):
        print(self.get_position())
        super().down()
        if self.y >= self._chunk_size.height:
            self.chunk_y += 1
            self.y = 1

    def left(self):
        print(self.get_position())
        super().left()
        if self.x <= 0:
            self.chunk_x -= 1
            self.x = self._chunk_size.width - 1

    def right(self):
        print(self.get_position())
        super().right()
        if self.x >= self._chunk_size.width:
            self.chunk_x += 1
            self.x = 1