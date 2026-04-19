from textworld.data import DataManager
from textworld.generation import Generator, TextworldWorld
from textworld.models import Size, Coords

class TextworldGame():

    data_manager: DataManager

    def __init__(self):
        self.data_manager = DataManager()

        world = TextworldWorld(Size(5, 5), Size(50, 50), 1)
        world.generate_world(self.data_manager["textworld"])
        world.dump_chunk(Coords(0, 0))