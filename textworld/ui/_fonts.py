import pyray as pr
from os import listdir
import fnmatch

class Fonts():

    _fonts: dict = {}
    _font: pr.Font
    font_name: str = ""
    _default_font: str = "monocraft"
    _font_location: str = "textworld/ui/resources/fonts/"
    
    def set_font(self, font_name):
        self._font = self._fonts[font_name]
        self.font_name = font_name
    
    def get_font(self):
        return self._font

    def load_fonts(self):
        print(listdir(self._font_location))
        for font_dir in listdir(self._font_location):
            for font in listdir(f"{self._font_location}{font_dir}"):
                _font_split = font.split('.')
                match _font_split[1]:
                    case 'ttf':
                        match _font_split[0]:
                            case 'monocraft':
                                self._fonts.update({
                                    _font_split[0]:
                                    {'font':pr.load_font_ex(f"{self._font_location}{font_dir}//{font}", 24, None, 0),
                                    'x_in': 0,
                                    'y_in': 0,
                                    'min_size': 18,
                                    'max_size': 50
                                    }
                                    })
                            case 'blocks':
                                self._fonts.update({
                                    _font_split[0]:
                                    {'font':pr.load_font_ex(f"{self._font_location}{font_dir}//{font}", 20, None, 0),
                                    'x_in': 1,
                                    'y_in': 1,
                                    'min_size': 8,
                                    'max_size': 30
                                    }
                                    })
                            case 'stencilie':
                                self._fonts.update({
                                    _font_split[0]:
                                    {'font':pr.load_font_ex(f"{self._font_location}{font_dir}//{font}", 20, None, 0),
                                    'x_in': 1,
                                    'y_in': 1,
                                    'min_size': 10,
                                    'max_size': 30
                                    }
                                    })
                            case 'happykiller':
                                self._fonts.update({
                                    _font_split[0]:
                                    {'font':pr.load_font_ex(f"{self._font_location}{font_dir}//{font}", 20, None, 0),
                                    'x_in': 1,
                                    'y_in': 1,
                                    'min_size': 16,
                                    'max_size': 36
                                    }
                                    })
                            case 'blockface':
                                self._fonts.update({
                                    _font_split[0]:
                                    {'font':pr.load_font_ex(f"{self._font_location}{font_dir}//{font}", 20, None, 0),
                                    'x_in': 1,
                                    'y_in': 1,
                                    'min_size': 16,
                                    'max_size': 40
                                    }
                                    })
                            case 'blockface-bold':
                                self._fonts.update({
                                    _font_split[0]:
                                    {'font':pr.load_font_ex(f"{self._font_location}{font_dir}//{font}", 20, None, 0),
                                    'x_in': 1,
                                    'y_in': 1,
                                    'min_size': 16,
                                    'max_size': 40
                                    }
                                    })
                            case 'origa':
                                self._fonts.update({
                                    _font_split[0]:
                                    {'font':pr.load_font_ex(f"{self._font_location}{font_dir}//{font}", 20, None, 0),
                                    'x_in': 1,
                                    'y_in': 1,
                                    'min_size': 12,
                                    'max_size': 40
                                    }
                                    })
                            case 'origap':
                                self._fonts.update({
                                    _font_split[0]:
                                    {'font':pr.load_font_ex(f"{self._font_location}{font_dir}//{font}", 20, None, 0),
                                    'x_in': 1,
                                    'y_in': 1,
                                    'min_size': 12,
                                    'max_size': 40
                                    }
                                    })
                            case 'uglyhandwriting':
                                self._fonts.update({
                                    _font_split[0]:
                                    {'font':pr.load_font_ex(f"{self._font_location}{font_dir}//{font}", 20, None, 0),
                                    'x_in': 1,
                                    'y_in': 1,
                                    'min_size': 16,
                                    'max_size': 40
                                    }
                                    })
                    case 'otf':
                        match _font_split[0]:
                            case 'pecita':
                                self._fonts.update({
                                    _font_split[0]:
                                    {'font':pr.load_font_ex(f"{self._font_location}{font_dir}//{font}", 20, None, 0),
                                    'x_in': 1,
                                    'y_in': 1,
                                    'min_size': 18,
                                    'max_size': 40
                                    }
                                    })
        self.set_font(self._default_font)

    def __getitem__(self, font_name):
        return self._fonts[font_name]
