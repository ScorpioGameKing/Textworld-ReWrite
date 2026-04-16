import numpy as np
from opensimplex import OpenSimplex
from time import gmtime, strftime
from textworld.data import TileQuery
from textworld.models import Size, Coords, Tile

class Generator():

    _noise_seed:int
    _noise_generator: OpenSimplex

    def __init__(self, noise_seed:int = int(strftime("%Y%m%d%H%M%S", gmtime()))):
        self._noise_seed = noise_seed
        self._noise_generator = OpenSimplex(self._noise_seed)

    def generate_chunk(self, database:Database, size:Size, coords:Coords):
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
                    tile_data = db.fetch_tile(TileQuery.SELECT_WITH_COLORS_BY_NOISE, (noise_value, noise_value))
                    row.append(Tile(tile_data[0], tile_data[1], tile_data[2]))
                chunk.append(row)
    
    def __enter__(self):
        return self

    def __exit__(self, *args):
        pass