import pyray as pr
from textworld.ui.menus.components import BasePanel
from textworld.ui.menus.screens import PauseScreen

class GameMenu():
    
    _window: TextworldWindow
    components: dict = {}

    def __init__(self, window):
        self._window = window
        self.components.update({'pause-screen':PauseScreen(self._window)})
        
    def render(self):
        for component in self.components:
            self.components[component].render()

    def update(self): 
        self.components['pause-screen'].update_theme()
        for component in self.components:
            self.components[component].update()