import pyray as pr
import math
from textworld.models import Coords

class GameView():
    
    _window: TextworldWindow
    _font_data: dict = {}
    _zoom: int = 0
    _zoom_min: int = 0
    _zoom_max: int = 0 

    def __init__(self, window):
        self._window = window

    def get_zoom_dir(self, _zoom_dir):
        self._zoom_dir = _zoom_dir

    def update(self):
        self._font_data = self._window.fonts.get_font()
        if self._zoom == 0:
            self._zoom = self._font_data['font'].baseSize
            self._zoom_min = self._font_data['min_size']
            self._zoom_max = self._font_data['max_size']
        else:
            if self._zoom + self._zoom_dir <= self._zoom_max and self._zoom + self._zoom_dir >= self._zoom_min:
                self._zoom += self._zoom_dir
        print(f"Game View: {self._zoom_dir} Zoom: {self._zoom}")

    def render(self):
        _font_data = self._window.fonts.get_font()
        for y in range(0, math.trunc(self._window.dimensions.height / self._zoom)):
            for x in range(0, math.trunc(self._window.dimensions.width / pr.measure_text_ex(_font_data['font'], "x", self._zoom, 0).x)):
                _tile = self._window.game.active_world[0,0][x,y]
                _x = _font_data['x_in'] + x * pr.measure_text_ex(_font_data['font'], "x", self._zoom, 0).x
                _y = _font_data['y_in'] + y * self._zoom
                pr.draw_text_ex(
                    _font_data['font'],
                    _tile.get_tile(),
                    [_x, _y],
                    self._zoom,
                    1, 
                    self._window.colors[_tile.get_color()])