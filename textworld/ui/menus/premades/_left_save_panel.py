from textworld.ui.menus.components import BasePanel, UIText
from textworld.models import Size, Coords

class LeftSavePanel(BasePanel):

    _window: TextworldWindow
    _header: UIText
    _name: UIText
    _hp: UIText
    _mp: UIText
    _stamina: UIText

    def __init__(self, window, position, size, bg_color, fg_color, slide_dir=None, slide_speed=None):
        super().__init__(position, size, bg_color, fg_color, slide_dir, slide_speed)
        self._window = window
        self._header = UIText(self._window, Coords(20, 5), 24, "~CHARACTER~")
        self._name = UIText(self._window, Coords(6, 30), 18, "Name: *REPLACE*")
        self._hp = UIText(self._window, Coords(6, 43), 18, "HP: *REPLACE*")
        self._mp = UIText(self._window, Coords(6, 56), 18, "HP: *REPLACE*")
        self._stamina = UIText(self._window, Coords(6, 69), 18, "SP: *REPLACE*")
        
    def update_items(self):
        self._header.update_position(self._current_position.x, self._current_position.y)
        self._name.update_position(self._current_position.x, self._current_position.y)
        self._hp.update_position(self._current_position.x, self._current_position.y)
        self._mp.update_position(self._current_position.x, self._current_position.y)
        self._stamina.update_position(self._current_position.x, self._current_position.y)

    def update(self):
        super().update()
        self.update_items()
        self._header.update()
        self._name.update()
        self._hp.update()
        self._mp.update()
        self._stamina.update()
    
    def render(self):
        super().render()
        self._header.render()
        self._name.render()
        self._hp.render()
        self._mp.render()
        self._stamina.render()
