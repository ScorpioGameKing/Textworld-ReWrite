from textworld.models import Size
from textworld.ui._colors import Colors
from textworld.ui._fonts import Fonts
import ntpath
import os
import pyray as pr

class TextworldWindow():

    game: TextworldGame
    dimensions: Size
    title: str
    fonts: Fonts
    colors: Colors
    _window: pr.init_window
    _render_pool: dict
    _update_pool: dict

    def __init__(self, game, dimensions:Size, title:str):
        self.game = game
        self.dimensions = dimensions
        self.title = title
        self._update_pool = {}
        self._render_pool = {}
        self.fonts = Fonts()
        self.colors = Colors()

    def create_window(self):
        self._window = pr.init_window(self.dimensions.width, self.dimensions.height, self.title)
        pr.set_target_fps(60)
        pr.set_window_monitor(0)
        self.fonts.load_fonts()
    
    def toggle_font(self):
        print(self.fonts.font_name)
        if self.fonts.font_name == "monocraft":
            self.fonts.set_font("blocked")
        elif self.fonts.font_name == "blocked":
            self.fonts.set_font("monocraft")
    
    def toggle_theme(self):
        print(self.colors.theme_name)
        if self.colors.theme_name == "gruvbox-dark":
            self.colors.set_theme("gruvbox-light")
        elif self.colors.theme_name == "gruvbox-light":
            self.colors.set_theme("gruvbox-dark")
    
    def run(self):
        self._main_loop()
    
    def add_to_render_pool(self, key, value):
        self._render_pool.update({key: value})
    
    def add_to_update_pool(self, key, value):
        self._update_pool.update({key: value})
    
    def remove_from_render_pool(self, key):
        self._render_pool.pop(key)
    
    def remove_from_update_pool(self, key):
        self._update_pool.pop(key)
    
    def _update_loop(self):
        for obj in self._update_pool:
            try: 
                self._update_pool[obj].update()
            except:
                pass

    def _render_loop(self):
        pr.begin_drawing()
        pr.clear_background(self.colors['bg'])
        for obj in self._render_pool:
            try: 
                self._render_pool[obj].render()
            except:
                pass
        pr.end_drawing()

    def _main_loop(self):
        while not pr.window_should_close():
            self._update_loop()
            self._render_loop()
        pr.close_window()