from textworld.ui.menus.components import BasePanel, LayoutContainer, UIText
from textworld.models import Size, Coords

class LeftSavePanel(BasePanel):

    _window: TextworldWindow
    _name: UIText
    _hp: UIText
    _mp: UIText
    _stamina: UIText

    def __init__(self, window, position, size, bg_color, fg_color, slide_dir=None, slide_speed=None):
        super().__init__(position, size, bg_color, fg_color, slide_dir, slide_speed)
        self._window = window
        self._name = UIText(self._window, Coords(6, 5), 18, "Player Name:")
        self._hp = UIText(self._window, Coords(6, 18), 18, "Cur./Max HP:")
        self._mp = UIText(self._window, Coords(6, 31), 18, "Cur./Max HP:")
        self._stamina = UIText(self._window, Coords(6, 43), 18, "Cur./Max SP:")
        
    def update_items(self):
        self._name.update_font()
        self._hp.update_font()
        self._mp.update_font()
        self._stamina.update_font()
        self._name.update_position(self._current_position.x, self._current_position.y)
        self._hp.update_position(self._current_position.x, self._current_position.y)
        self._mp.update_position(self._current_position.x, self._current_position.y)
        self._stamina.update_position(self._current_position.x, self._current_position.y)

    def update(self):
        super().update()
        self.update_items()
        self._name.update()
        self._hp.update()
        self._mp.update()
        self._stamina.update()
    
    def render(self):
        super().render()
        self._name.render()
        self._hp.render()
        self._mp.render()
        self._stamina.render()
