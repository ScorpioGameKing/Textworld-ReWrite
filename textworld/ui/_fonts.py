import pyray as pr
from os import listdir

class Fonts():

    _fonts: dict = {}
    _default_font: str = "Monocraft"
    _font_location: str = "textworld/ui/resources/fonts/"
    
    def set_font(self, font_name):
        self._font = self._fonts[font_name]

    def load_fonts(self):
        for font in listdir(self._font_location):
            self._fonts.update({font.split('.ttf')[0]:pr.load_font_ex(f"{self._font_location}{font}", 20, None, 0)})
    
    def __getitem__(self, font_name):
        return self._fonts[font_name]
