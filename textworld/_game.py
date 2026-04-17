from textworld.data import DataManager
from textworld.generation import Generator
from textworld.models import Size, Coords

class TextworldGame():

    data_manager: DataManager

    def __init__(self):
        self.data_manager = DataManager()

        chunk = None

        with Generator(1) as gen:
            chunk = gen.generate_chunk(self.data_manager["textworld"], Size(50, 50), Coords(0, 0))

        print(chunk[2,2])