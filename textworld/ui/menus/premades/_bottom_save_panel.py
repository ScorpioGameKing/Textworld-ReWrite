from textworld.ui.menus.components import BasePanel, UIText
from textworld.models import Size, Coords

class BottomSavePanel(BasePanel):

    _window: TextworldWindow
    _header: UIText
    _category: UIText
    _grid: UIText

    def __init__(self, window, position, size, bg_color, fg_color, slide_dir=None, slide_speed=None):
        super().__init__(position, size, bg_color, fg_color, slide_dir, slide_speed)
        self._window = window
        self._header = UIText(self._window, Coords(300, 5), 32, "~INVENTORY~")
        self._category = UIText(self._window, Coords(6, 30), 18, "Category: *REPLACE VALUE*")
        self._grid = UIText(self._window, Coords(6, 43), 18, "WIP Item Grid")
    
    def update_items(self):
        self._header.update_position(self._current_position.x, self._current_position.y)
        self._category.update_position(self._current_position.x, self._current_position.y)
        self._grid.update_position(self._current_position.x, self._current_position.y)
    
    def update(self):
        super().update()
        self.update_items()
        self._header.update()
        self._category.update()
        self._grid.update()
    
    def render(self):
        super().render()
        self._header.render()
        self._category.render()
        self._grid.render()