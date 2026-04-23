import pyray as pr
from os import listdir

class Fonts():

    _fonts: dict = {}
    _font: pr.Font
    _default_font: str = "blocked"
    _font_location: str = "textworld/ui/resources/fonts/"
    
    def set_font(self, font_name):
        self._font = self._fonts[font_name]
    
    def get_font(self):
        return self._font

    def load_fonts(self):
        for font in listdir(self._font_location):
            _font_split = font.split('.')
            match _font_split[1]:
                case 'ttf':
                    match _font_split[0]:
                        case 'monocraft':
                            self._fonts.update({
                                _font_split[0]:
                                {'font':pr.load_font_ex(f"{self._font_location}{font}", 24, None, 0),
                                'x_in': 0,
                                'y_in': 0,
                                'min_size': 18,
                                'max_size': 36
                                }
                                })
                        case 'blocked':
                            self._fonts.update({
                                _font_split[0]:
                                {'font':pr.load_font_ex(f"{self._font_location}{font}", 20, None, 0),
                                'x_in': 1,
                                'y_in': 1,
                                'min_size': 13,
                                'max_size': 34
                                }
                                })
                case 'otf':
                    self._fonts.update({_font_split[0]:pr.load_font_ex(f"{self._font_location}{font}", 20, None, 0)})
        self.set_font(self._default_font)

    def __getitem__(self, font_name):
        return self._fonts[font_name]
