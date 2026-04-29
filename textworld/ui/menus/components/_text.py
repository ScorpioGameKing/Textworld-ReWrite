import pyray as pr
from textworld.models import Coords

class UIText():

    _position: Coords
    _offset: Coords = Coords(0,0)
    _text_size: int
    _text: str
    _font_data: dict

    def __init__(self, window, position, text_size, text):
        self._window = window
        self._position = position
        self._text_size = text_size
        self._text = text

    def update_position(self, x, y):
        self._offset = Coords(self._position.x + x, self._position.y + y)
    
    def update(self):
        pass

    def render(self):
        pr.draw_text_ex(self._window.fonts['monocraft']['font'], self._text, [self._offset.x, self._offset.y], self._text_size, 2, self._window.colors['bg'])
