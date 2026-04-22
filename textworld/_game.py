from textworld.data import DataManager
from textworld.generation import TextworldWorld
from textworld.models import Size, Coords
from textworld.ui import TextworldWindow, GameView

class TextworldGame():

    data_manager: DataManager
    window: TextworldWindow

    def __init__(self):
        self.data_manager = DataManager()
        self.window = TextworldWindow(Size(640,1280), "Textworld")

        world = TextworldWorld(Size(1, 1), Size(150, 150), 1)
        world.generate_world(self.data_manager["textworld"])
        for y in range(0, world.chunk_count.height):
                for x in range(0, world.chunk_count.width):
                    world.dump_chunk(Coords(x, y))

        self.window.create_window()
        self.window.add_to_render_pool("game_view", GameView(self.window))
        self.window.run()