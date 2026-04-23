import pyray as pr

class MouseManager():

    scroll_dir: int = 0

    def __init__(self):
        pass

    def update(self):
        self.scroll_dir = int(pr.get_mouse_wheel_move())