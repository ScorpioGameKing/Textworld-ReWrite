import pyray as pr
from textworld.models import Coords, Size 

class BasePanel():
    _size: Size
    _screen_position: Coords
    _current_position: Coords
    visible: bool = False
    slide_dir: str = "left"
    slide_speed: int = 4
    panel: pr.draw_rectangle
    border: pr.draw_rectangle_lines
    bg_color: pr.Color
    border_color: pr.Color

    def __init__(self, position, size, bg_color, border_color, slide_dir=None, slide_speed=None):
        self._screen_position = position
        self._current_position = Coords(position.x, position.y)
        self._size = size
        self.bg_color = bg_color
        self.border_color = border_color
        if not slide_dir == None: self.slide_dir = slide_dir
        if not slide_speed == None: self.slide_speed = slide_speed
    
    def toggle_slide(self):
        self.visible = not self.visible

    def render(self):
        self.panel = pr.draw_rectangle(self._current_position.x, self._current_position.y, self._size.width, self._size.height, self.bg_color)
        self.border = pr.draw_rectangle_lines_ex(pr.Rectangle(self._current_position.x-1, self._current_position.y-1, self._size.width+1, self._size.height+1), 4.0, self.border_color)
    
    def update_colors(self, colors):
        self.bg_color = colors["fg"]
        self.border_color = colors["bg"]

    def update(self):
        if not self.visible:
            match self.slide_dir:
                case 'left':
                    if self._current_position.x > 0 - self._size.width:
                        self._current_position.x -= self.slide_speed
                case 'right':
                    if self._current_position.x < self._screen_position.x + self._size.width + (self._size.width * 0.5):
                        self._current_position.x += self.slide_speed
                case 'up':
                    if self._current_position.y > 0 - self._size.height:
                        self._current_position.y -= self.slide_speed
                case 'down':
                    if self._current_position.y < self._screen_position.y + self._size.height + (self._size.height * 0.5):
                        self._current_position.y += self.slide_speed
        else:
            match self.slide_dir:
                case 'left':
                    if self._current_position.x < self._screen_position.x:
                        self._current_position.x += self.slide_speed
                case 'right':
                    if self._current_position.x > self._screen_position.x:
                        self._current_position.x -= self.slide_speed
                case 'up':
                    if self._current_position.y < self._screen_position.y:
                        self._current_position.y += self.slide_speed
                case 'down':
                    if self._current_position.y > self._screen_position.y:
                        self._current_position.y -= self.slide_speed