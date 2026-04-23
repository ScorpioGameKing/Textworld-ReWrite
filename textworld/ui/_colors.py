class Colors():
    _themes: dict = {}
    _theme: dict = {}
    _default_theme: str = 'gruvbox-light'

    def __init__(self):
        self._build_themes()
        self.set_theme(self._default_theme)

    def set_theme(self, theme_name):
        self._theme = self._themes[theme_name]
    
    def _build_themes(self):
        # Gruvbox Dark
        self._themes.update({
            'gruvbox-dark':{
                'bg'    :(40,  40,  40,  255),
                'fg'    :(235, 219, 178, 255),
                'red'   :(204, 36,  29,  255),
                'green' :(152, 151, 26,  255),
                'yellow':(215, 153, 33,  255),
                'blue'  :(69,  133, 136, 255),
                'purple':(177, 98,  134, 255),
                'aqua'  :(104, 157, 106, 255),
                'gray'  :(168, 153, 132, 255),
                'orange':(214, 93,  14,  255),
                'white' :(253, 248, 227, 255),
                'brown' :(131, 115, 93,  255)
            },
            'gruvbox-light':{
                'bg'    :(213, 196, 161,  255),
                'fg'    :(60,  56,  54, 255),
                'red'   :(204, 36,  29,  255),
                'green' :(152, 151, 26,  255),
                'yellow':(215, 153, 33,  255),
                'blue'  :(69,  133, 136, 255),
                'purple':(177, 98,  134, 255),
                'aqua'  :(104, 157, 106, 255),
                'gray'  :(124, 111, 100, 255),
                'orange':(214, 93,  14,  255),
                'white' :(253, 248, 227, 255),
                'brown' :(131, 115, 93,  255)
            }
        })
    
    def __getitem__(self, color):
        return self._theme[color]
