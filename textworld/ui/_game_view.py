import pyray as pr
from pathlib import Path

class GameView():
    
    def __init__(self):
        pass

    def update(self):
        pass

    def render(self):
        font_location = "textworld/ui/resources/fonts/blocked.ttf"
        _font = pr.load_font_ex(font_location, 20, None, 0)
        pr.draw_text_ex(_font, "gggggdddfffffffffffffdddgggggggggggssssssssssssssssssssssgggggggggggggggggggggggggssssssssssssssssss", [2, 2], _font.baseSize, 2, pr.WHITE)
