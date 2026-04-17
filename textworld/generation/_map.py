from textworld.models import Size, Coords, Tile
import numpy as np

class TextworldMap():
    __columns: int
    __rows: int
    __tiles: dict[Coords, Tile]
    __noise: np.typing.NDArray

    def __init__(self, chunk_size: Size[int]):
        self.__columns = chunk_size.width
        self.__rows = chunk_size.height
        self.__tiles = {}
        self.__noise = np.zeros(shape=(self.__rows, self.__columns))

    def __getitem__(self, __slice: tuple[int, int] | slice):
        if getattr(__slice, 'start', None):
            start = __slice.start
            stop = __slice.stop
            rows = []
            for y in range(start[1], stop[1]):
                row = []
                for x in range(start[0], stop[0]):
                    row.append(self.__tiles[Coords(x, y)])
                rows.append(row)
            return rows
        else:
            return self.__tiles.get(Coords.from_tuple(__slice), None)
    
    def __setitem__(self, coords: tuple[int,int] | Coords, tile: Tile):
        try:
            match coords:
                case tuple():
                    self.__tiles[Coords.from_tuple(coords)] = tile
                case Coords():
                    self.__tiles[coords] = tile
        except TypeError as e:
            print(f"The supplied Coordinates are an incorrect type {e}")

    def __getstate__(self):
        return (self.columns, self.rows, self.__tiles)
    
    def __setstate__(self, state):
        (self.columns, self.rows, self.__tiles) = state