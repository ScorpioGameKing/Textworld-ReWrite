import numpy as np
from opensimplex import OpenSimplex
from time import gmtime, strftime
from textworld.data import TileQuery
from textworld.models import Size, Coords, Tile

class Generator():
    """
    Used to generate noise and transform it into tile objects for later use
    
    noise_seed:int(strftime("%Y%m%d%H%M%S", gmtime()))
    -> The integer used to seed the noise generation. By default it creates a
    random seed based on the system time and date.
    """

    _noise_generator: OpenSimplex

    def __init__(self, noise_seed:int = int(strftime("%Y%m%d%H%M%S", gmtime()))):

        self._noise_generator = OpenSimplex(noise_seed)

    def generate_chunk(self, database:Database, size:Size, coords:Coords):
        """
        Used to generate a chunk of the world. 

        database:Database
        -> The database of tiles used to generate the chunk

        size:Size
        -> The width and height of the chunk to generate 

        coords:Coords
        -> The X and Y position of the chunk in the worldspace
        """

        scale = (0.5 * 0.0625)
        chunk = []

        _w = np.array([((x + (coords.x * size.width)) * scale) for x in range(size.width)])
        _h = np.array([((y + (coords.y * size.height)) * scale) for y in range(size.height)])
        
        noise_field = self._noise_generator.noise2array(_w, _h)

        with database as db:
            for y in range(size.height):
                row = []
                for x in range(size.width):
                    noise_value = noise_field[x][y]
                    # TODO Look at porting the tile fetching and creation into the 
                    # database and return the tile dataclass instead
                    tile_data = db.fetch_tile(TileQuery.SELECT_WITH_COLORS_BY_NOISE, (noise_value, noise_value))
                    row.append(Tile(tile_data[0], tile_data[1], tile_data[2]))
                chunk.append(row)
    
    def __enter__(self):
        return self

    def __exit__(self, *args):
        pass