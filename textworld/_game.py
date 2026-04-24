from textworld.data import DataManager
from textworld.generation import TextworldWorld
from textworld.models import Size, Coords
from textworld.ui import TextworldWindow, GameView
from textworld.managers import MouseManager, KeyboardManager, GameManager, PlayerManager

class TextworldGame():

    data_manager: DataManager
    window: TextworldWindow
    active_world: TextworldWorld
    game_view: GameView
    mouse_manager: MouseManager
    keyboard_manager: KeyboardManager
    player_manager: PlayerManager
    game_manager: GameManager

    def __init__(self):
        self.data_manager = DataManager()
        self.active_world = TextworldWorld(Size(3, 3), Size(200, 200), 1)
        self.active_world.generate_world(self.data_manager["textworld"])
        """
        for y in range(0, self.active_world.chunk_count.height):
                for x in range(0, self.active_world.chunk_count.width):
                    self.active_world.dump_chunk(Coords(x, y))
        """
        self.window = TextworldWindow(self, Size(640,1280), "Textworld")
        self.window.create_window()
        
        self.mouse_manager = MouseManager()
        self.keyboard_manager = KeyboardManager()

        self.player_manager = PlayerManager()
        self.player_manager.create_player(120, 180, 1, 1)

        self.game_view = GameView(self.window)
        
        self.game_manager = GameManager(self)
                
        self.window.add_to_update_pool("game_manager", self.game_manager)
        self.window.add_to_update_pool("mouse_manager", self.mouse_manager)
        self.window.add_to_update_pool("keyboard_manager", self.keyboard_manager)
        self.window.add_to_update_pool("player_manager", self.player_manager)
        self.window.add_to_update_pool("game_view", self.game_view)
        
        self.window.add_to_render_pool("game_view", self.game_view)
        
        self.window.run()