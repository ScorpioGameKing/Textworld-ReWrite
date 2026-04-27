import pyray as pr
import math
from textworld.models import Coords

class GameView():
    
    _window: TextworldWindow
    _font_data: dict = {}
    _zoom: int = 0
    _zoom_dir: int = 0
    
    _player_x: int = 71#71
    _player_y: int = 17#17
    _chunk_x: int = 1
    _chunk_y: int = 1

    def __init__(self, window):
        self._window = window
        self.update_font()

    def get_zoom_dir(self, zoom_dir):
        self._zoom_dir = zoom_dir
    
    def get_player_position(self, position):
        self._player_x = position[0]
        self._player_y = position[1]
        self._chunk_x = position[2]
        self._chunk_y = position[3]
        print(self._player_x, self._player_y, self._chunk_x, self._chunk_y)
    
    def update_font(self):
        self._font_data = self._window.fonts.get_font()
        if self._zoom > self._font_data['max_size']: self._zoom = self._font_data['max_size']
        if self._zoom < self._font_data['min_size']: self._zoom = self._font_data['min_size']

    def update(self):
        if self._zoom + self._zoom_dir <= self._font_data['max_size'] and self._zoom + self._zoom_dir >= self._font_data['min_size']:
            self._zoom += self._zoom_dir

    def render(self):
        _height = math.trunc(self._window.dimensions.height / self._zoom)
        _width = math.trunc(self._window.dimensions.width / pr.measure_text_ex(self._font_data['font'], "x", self._zoom, 0).x)
        _draw_y = 1
        for y in range(math.trunc(self._player_y - (_height * 0.5)), math.trunc(self._player_y + (_height * 0.5))):
            _draw_x = 1
            for x in range(math.trunc(self._player_x - (_width * 0.5)), math.trunc(self._player_x + (_width * 0.5))):
                _x = self._font_data['x_in'] + (_draw_x * pr.measure_text_ex(self._font_data['font'], "x", self._zoom, 0).x)
                _y = self._font_data['y_in'] + (_draw_y * self._zoom)
                print(x, y, _x, _y)
                if x == self._player_x and y == self._player_y:
                    pr.draw_text_ex(
                        self._font_data['font'],
                        "P",
                        [_x, _y],
                        self._zoom,
                        1, 
                        self._window.colors["red"])
                else:
                    if x < 0: 
                        print(f"Left Stitch: {self._window.game.active_world[self._chunk_x - 1,self._chunk_y][x + self._window.game.active_world.chunk_size.width, y]}")
                        _tile = self._window.game.active_world[self._chunk_x - 1,self._chunk_y][self._window.game.active_world.chunk_size.width + x,y]
                        pr.draw_text_ex(
                            self._font_data['font'],
                            _tile.get_tile(),
                            [_x, _y],
                            self._zoom,
                            1, 
                            self._window.colors[_tile.get_color()])
                    if y < 0: y = 0
                    if x >= self._window.game.active_world.chunk_size.width: 
                        print(f"Right Stitch: {self._window.game.active_world[self._chunk_x + 1,self._chunk_y][x - self._window.game.active_world.chunk_size.width, y]}")
                        _tile = self._window.game.active_world[self._chunk_x + 1,self._chunk_y][x - self._window.game.active_world.chunk_size.width, y]
                        pr.draw_text_ex(
                            self._font_data['font'],
                            _tile.get_tile(),
                            [_x, _y],
                            self._zoom,
                            1, 
                            self._window.colors[_tile.get_color()])
                    if y >= self._window.game.active_world.chunk_size.height: y = 0
                    if x == 0  or y == 0:
                        pr.draw_text_ex(
                        self._font_data['font'],
                        "X",
                        [_x, _y],
                        self._zoom,
                        1, 
                        self._window.colors['purple'])
                    else:
                        _tile = self._window.game.active_world[self._chunk_x,self._chunk_y][x,y]
                        pr.draw_text_ex(
                            self._font_data['font'],
                            _tile.get_tile(),
                            [_x, _y],
                            self._zoom,
                            1, 
                            self._window.colors[_tile.get_color()])
                _draw_x += 1
            _draw_y += 1