from dataclasses import dataclass

@dataclass
class Tile:
    """
    The dataclass model used to represent Tiles within Textworld
    """

    tile_char:str
    name:str
    color:str

    def get_tile(self):
        return self.tile_char
    
    def __getstate__(self):
        return (self.tile_char, self.color, self.name)
    
    def __setstate__(self, state):
        (self.tile_char, self.color, self.name) = state