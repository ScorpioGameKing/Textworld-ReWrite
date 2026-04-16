import numpy as np
from opensimplex import OpenSimplex
from time import gmtime, strftime
from textworld.data import Tile

class Generator():

    _noise_seed:int
    _noise_generator: OpenSimplex

    def __init__(self, noise_seed:int = int(strftime("%Y%m%d%H%M%S", gmtime()))):
        self._noise_seed = noise_seed
        self._noise_generator = OpenSimplex(self._noise_seed)

    def generate_chunk(self, database, size, coords):
        scale = (0.5 * 0.0625)
        chunk = []

        _w = np.array([((x + (coords[0] * size[0])) * scale) for x in range(size[0])])
        _h = np.array([((y + (coords[1] * size[1])) * scale) for y in range(size[1])])
        
        noise_field = self._noise_generator.noise2array(_w, _h)

        with database as db:
            for y in range(size[1]):
                row = []
                for x in range(size[0]):
                    noise_value = noise_field[x][y]
                    row.append(db.fetch_tile(Tile.SELECT_WITH_COLORS_BY_NOISE, (noise_value, noise_value))[0])
                chunk.append(row)
    
    def __enter__(self):
        return self

    def __exit__(self, *args):
        pass