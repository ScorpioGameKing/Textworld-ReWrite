import pyray as pr
from textworld.models import Coords, Size

class UIButton():

    _window: TextworldWindow
    _position: Coords
    _offset: Coords
    _size: Size
    _text: str
    _pressed: bool = False
    _mouse_hover: bool = False

    def __init__(self, window, position, size, text):
        self._window = window
        self._position = position
        self._size = size
        self._text = text
    
    def update_position(self, x, y):
        self._offset = Coords(self._position.x + x, self._position.y + y)
    
    def button_press(self):
        self._pressed = True
        print(f"{self._text} Button Is Pressed!")
    
    def update(self):
        if self._pressed: self._pressed = False
        if pr.check_collision_point_rec(pr.get_mouse_position(), pr.Rectangle(self._offset.x, self._offset.y, self._size.width, self._size.height)):
            self._mouse_hover = True
        else: self._mouse_hover = False

    def render(self):
        pr.draw_rectangle(self._offset.x-1, self._offset.y, self._size.width, self._size.height, self._window.colors['fg'])
        pr.draw_rectangle_lines_ex(pr.Rectangle(self._offset.x-1, self._offset.y-1, self._size.width+1, self._size.height+1), 2.0, self._window.colors['bg'])
        pr.draw_text_ex(self._window.fonts['monocraft']['font'], 
        self._text, 
        [self._offset.x + (self._size.width * 0.5 - (pr.measure_text_ex(self._window.fonts['monocraft']['font'], self._text, 20, 2).x * .5)), 
        self._offset.y + (self._size.height * 0.5 - (pr.measure_text_ex(self._window.fonts['monocraft']['font'], self._text, 20, 2).y * .5))], 
        20, 
        2, 
        self._window.colors['bg'])