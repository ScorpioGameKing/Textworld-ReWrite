from textworld.data import DataManager
from textworld.generation import TextworldWorld
from textworld.models import Size, Coords

class TextworldGame():

    data_manager: DataManager

    def __init__(self):
        self.data_manager = DataManager()

        world = TextworldWorld(Size(1, 1), Size(500, 500), 1)
        world.generate_world(self.data_manager["textworld"])
        for y in range(0, world.chunk_count.height):
                for x in range(0, world.chunk_count.width):
                    world.dump_chunk(Coords(x, y))