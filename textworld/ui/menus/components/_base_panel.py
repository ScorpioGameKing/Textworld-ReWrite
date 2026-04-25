import pyray as pr

class BasePanel():
    width: int
    height: int
    x: int
    y: int
    panel: pr.draw_rectangle
    border: pr.draw_rectangle_lines

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def render(self):
        self.panel = pr.draw_rectangle(self.x, self.y, self.width, self.height, pr.WHITE)
        self.border = pr.draw_rectangle_lines(self.x, self.y, self.width, self.height, pr.BLACK)