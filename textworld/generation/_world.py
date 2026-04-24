from time import gmtime, strftime
from textworld.models import Coords, Size, Tile
from textworld.generation._generator import Generator
import pickle, gzip, threading, os
import numpy as np

class TextworldWorld():
    __chunks: dict[Coords, np.array] = {}
    chunk_count: Size[int]
    chunk_size: Size[int]
    __seed: int
    __entity_positions: dict[Coords, str] = {}

    def __init__(self, chunk_count: Size[int], chunk_size: Size[int], seed:int = int(strftime("%Y%m%d%H%M%S", gmtime()))):
        self.chunk_count = chunk_count
        self.chunk_size = chunk_size
        self.__seed = seed
        self.lock = threading.Lock()

    def generate_chunk(self, database: Database, coords: Coords, generator: Generator):
        chunk = generator.generate_chunk(database, self.chunk_size, coords)
        with self.lock:
            self.__chunks[coords] = chunk

    def generate_live_chunk(self, database: Database, coords: Coords):
        print(f"Live Chunk at: {coords}")
        with Generator(self.__seed) as generator:
            chunk = generator.generate_chunk(database, self.chunk_size, coords)
            self.__chunks[coords] = chunk
    
    def __generate_multiple_chunks(self, database: Database):
        with Generator(self.__seed) as generator:
            for y in range(0, self.chunk_count.height):
                for x in range(0, self.chunk_count.width):
                    self.generate_chunk(database, Coords(x, y), generator)

    def generate_world(self, database: Database):
        thread = threading.Thread(target=self.__generate_multiple_chunks(database))
        thread.start()

    def dump_chunk(self, coords: tuple[int, int]):
        try:
            path = f'dumps/chunk_{coords.x}_{coords.y}.txt'
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "w") as _d:
                chunk = self[coords.x, coords.y]
                for y in range(chunk.rows):
                    for x in range(chunk.columns):
                        _d.write(f"{chunk[x,y].tile_char}")
                    _d.write("\n")
        except Exception as e:
            print(f"Failed to dump chunk {coords} with error {e}")

    def save_world(self):
        data = pickle.dumps(self, protocol=pickle.HIGHEST_PROTOCOL)
        return gzip.compress(data)
    
    def __getitem__(self, coords: tuple[int,int]) -> np.typing.NDArray | None:
        try:
            return self.__chunks[Coords(*coords)]
        except:
            return None
    
    def __setitem__(self, _: Coords, __:np.array):
        raise NotImplementedError('TextworldWorld object does not support setting indecies')
    
    def __getstate__(self):
        self.lock = None
        return (self.chunk_count, self.chunk_size, self.__chunks)
    
    def __setstate__(self, state):
        (self.chunk_count, self.chunk_size, self.__chunks) = state
        self.lock = threading.Lock()
            
    def __repr__(self) -> str:
        return f'Chunks: {len(self.__chunks.keys())}'