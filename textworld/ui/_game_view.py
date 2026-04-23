import pyray as pr
from textworld.models import Coords

class GameView():
    
    _window: TextworldWindow

    def __init__(self, window):
        self._window = window

    def update(self):
        pass

    def render(self):
        _vertical = 32 #(self._window.dimensions.height - self._window.fonts['blocked'].baseSize) / self._window.fonts['blocked'].baseSize
        _horizontal = 91
        for y in range(0, int(_vertical)):
            for x in range(0, int(_horizontal)):
                pr.draw_text_ex(
                    self._window.fonts['blocked'],
                    self._window.game.active_world[0,0][x,y].get_tile(),
                    [   
                        x * pr.measure_text_ex(self._window.fonts['blocked'], "g", self._window.fonts['blocked'].baseSize, 2).x, 
                        y * pr.measure_text_ex(self._window.fonts['blocked'], "g", self._window.fonts['blocked'].baseSize, 2).y
                    ],
                    self._window.fonts['blocked'].baseSize,
                    2, 
                    self._window.colors[self._window.game.active_world[0,0][x,y].get_color()])

