import pyray as pr
from textworld.models import Coords

class GameView():
    
    _window: TextworldWindow

    def __init__(self, window):
        self._window = window

    def update(self):
        pass

    def _build_display_string(self):
        #print(self._window.dimensions.width, f"{self._window.game.active_world[0,0][0,0].get_tile()}")
        string = ""
        _vertical = (self._window.dimensions.height - self._window.fonts['blocked'].baseSize) / self._window.fonts['blocked'].baseSize
        _horizontal = (self._window.dimensions.width - self._window.fonts['blocked'].baseSize) / 15.75
        x_coord = 0
        while pr.measure_text_ex(self._window.fonts['blocked'], string, self._window.fonts['blocked'].baseSize, 2).x < self._window.dimensions.width - self._window.fonts['blocked'].baseSize:
            string = f"{string}{self._window.game.active_world[0,0][0,x_coord].get_tile()}"
            #print(pr.measure_text_ex(self._window.fonts['monocraft'], string, self._window.fonts['monocraft'].baseSize, 2).x)
            x_coord += 1
        print(len(string), _vertical, _horizontal, self._window.fonts['blocked'].glyphs.advanceX)
        return string

    def render(self):
        # TODO Pass string data from loaded chunks
        self._build_display_string()
        pr.draw_text_ex(
            self._window.fonts['blocked'],
            self._build_display_string(),
            [2, 2],
            self._window.fonts['blocked'].baseSize,
            2, 
            self._window.colors['fg'])
