import pyray as pr
from textworld.ui.menus.components import BasePanel

class GameMenu():
    
    _window: TextworldWindow
    components: dict = {}

    def __init__(self, window):
        self._window = window
        self.components.update({'left_panel':BasePanel(20, 40, 200, 590, self._window.colors["fg"], self._window.colors["bg"])})
        self.components.update({'right_panel':BasePanel(1060, 40, 200, 590, self._window.colors["fg"], self._window.colors["bg"], 'right')})
        self.components.update({'top_panel':BasePanel(240, 40, 800, 370, self._window.colors["fg"], self._window.colors["bg"], 'up')})
        self.components.update({'bottom_panel':BasePanel(240, 430, 800, 200, self._window.colors["fg"], self._window.colors["bg"], 'down')})

    def render(self):
        for component in self.components:
            self.components[component].render()

    def update(self): 
        self.components['left_panel'].update_colors(self._window.colors)
        self.components['right_panel'].update_colors(self._window.colors)
        self.components['top_panel'].update_colors(self._window.colors)
        self.components['bottom_panel'].update_colors(self._window.colors)
        for component in self.components:
            self.components[component].update()