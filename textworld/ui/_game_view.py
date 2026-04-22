import pyray as pr

class GameView():
    
    _window: TextworldWindow

    def __init__(self, window):
        self._window = window

    def update(self):
        pass

    def render(self):
        pr.draw_text_ex(self._window._fonts['blocked'], "gggggdddfffffffffffffdddgggggggggggssssssssssssssssssssssgggggggggggggggggggggggggssssssssssssssssss", [2, 2], 12, 2, pr.WHITE)
