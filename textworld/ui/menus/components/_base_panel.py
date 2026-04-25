import pyray as pr

class BasePanel():
    width: int
    height: int
    _x: int
    _y: int
    x: int
    y: int
    visible: bool = True
    slide_dir: str = "left"
    slide_speed: int = 4
    panel: pr.draw_rectangle
    border: pr.draw_rectangle_lines
    bg_color: pr.Color
    border_color: pr.Color

    def __init__(self, x, y, width, height, bg_color, border_color, slide_dir=None, slide_speed=None):
        self.x = x
        self.y = y
        self._x = x
        self._y = y
        self.width = width
        self.height = height
        self.bg_color = bg_color
        self.border_color = border_color
        if not slide_dir == None: self.slide_dir = slide_dir
        if not slide_speed == None: self.slide_speed = slide_speed
    
    def toggle_slide(self):
        self.visible = not self.visible

    def render(self):
        self.panel = pr.draw_rectangle(self.x, self.y, self.width, self.height, self.bg_color)
        self.border = pr.draw_rectangle_lines_ex(pr.Rectangle(self.x-1, self.y-1, self.width+1, self.height+1), 4.0, self.border_color)
    
    def update_colors(self, colors):
        self.bg_color = colors["fg"]
        self.border_color = colors["bg"]

    def update(self):
        if not self.visible:
            match self.slide_dir:
                case 'left':
                    if self.x > 0 - self.width:
                        self.x -= self.slide_speed
                case 'right':
                    if self.x < self.width + (self.width * 0.5):
                        self.x += self.slide_speed
                case 'up':
                    if self.y > 0 - self.height:
                        self.y -= self.slide_speed
                case 'down':
                    if self.y < self.height + (self.height * 0,5):
                        self.y += self.slide_speed
        else:
            match self.slide_dir:
                case 'left':
                    if self.x < self._x:
                        self.x += self.slide_speed
                case 'right':
                    if self.x > self._x:
                        self.x -= self.slide_speed
                case 'up':
                    if self.y < self._y:
                        self.y += self.slide_speed
                case 'down':
                    if self.y > self._y:
                        self.y -= self.slide_speed