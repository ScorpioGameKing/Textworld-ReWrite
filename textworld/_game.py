from textworld.data import DataManager
from textworld.generation import TextworldWorld
from textworld.models import Size, Coords
from textworld.ui import TextworldWindow, GameView

class TextworldGame():

    data_manager: DataManager
    window: TextworldWindow
    active_world: TextworldWorld

    def __init__(self):
        self.data_manager = DataManager()
        self.window = TextworldWindow(self, Size(640,1280), "Textworld")

        self.active_world = TextworldWorld(Size(1, 1), Size(150, 150), 1)
        self.active_world.generate_world(self.data_manager["textworld"])
        for y in range(0, self.active_world.chunk_count.height):
                for x in range(0, self.active_world.chunk_count.width):
                    self.active_world.dump_chunk(Coords(x, y))

        self.window.create_window()
        self.window.add_to_render_pool("game_view", GameView(self.window))
        self.window.run()