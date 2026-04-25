import pyray as pr
from textworld.ui.menus.components import BasePanel

class GameMenu():
    
    _window: TextworldWindow
    components: dict = {}

    def __init__(self, window):
        self._window = window
        self.components.update({'left_panel':BasePanel(20, 40, 200, 590, self._window.colors["fg"], self._window.colors["bg"])})

    def render(self):
        for component in self.components:
            self.components[component].render()

    def update(self): 
        self.components['left_panel'].update_colors(self._window.colors)
        for component in self.components:
            self.components[component].update()