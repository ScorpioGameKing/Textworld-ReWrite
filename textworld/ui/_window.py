from textworld.models import Size
import pyray as pr

class TextworldWindow():

    dimensions: Size
    title: str
    _window: pr.init_window
    _render_pool: dict
    _update_pool: dict
    _fonts: dict

    def __init__(self, dimensions:Size, title:str):
        self.dimensions = dimensions
        self.title = title
        self._update_pool = {}
        self._render_pool = {}
        self._fonts = {}
    
    def _load_fonts(self):
        print("loaded fonts")
        font_location = "textworld/ui/resources/fonts/blocked.ttf"
        self._fonts.update({"blocked":pr.load_font_ex(font_location, 20, None, 0)})

    def create_window(self):
        self._window = pr.init_window(self.dimensions.width, self.dimensions.height, self.title)
        self._load_fonts()
    
    def run(self):
        self._main_loop()
    
    def add_to_render_pool(self, key, value):
        self._render_pool.update({key: value})
    
    def add_to_update_pool(self, key, value):
        self._update_pool.update({key, value})
    
    def remove_from_render_pool(self, key):
        self._render_pool.pop(key)
    
    def remove_from_update_pool(self, key):
        self._update_pool.pop(key)
    
    def _update_loop(self):
        for obj in self._update_pool:
            try: 
                self._update_pool[obj].update()
            except:
                pass

    def _render_loop(self):
        pr.begin_drawing()
        pr.clear_background(pr.BLACK)
        for obj in self._render_pool:
            try: 
                self._render_pool[obj].render()
            except:
                pass
        pr.end_drawing()

    def _main_loop(self):
        while not pr.window_should_close():
            self._update_loop()
            self._render_loop()
        pr.close_window()