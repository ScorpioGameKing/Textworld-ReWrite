from textworld.ui.menus.components import BasePanel, LayoutContainer, UIText
from textworld.models import Size, Coords

class LeftSavePanel(BasePanel):

    _window: TextworldWindow
    _layout: LayoutContainer

    def __init__(self, window, position, size, bg_color, fg_color, slide_dir=None, slide_speed=None):
        super().__init__(position, size, bg_color, fg_color, slide_dir, slide_speed)
        self._window = window
        self._layout = LayoutContainer(5, self._current_position, self._size, 0, 0)
        self._layout.add_to_layout("player-name", UIText(self._window, Coords(2, 5), 18, "Player Name:"))
        self._layout.add_to_layout("player-hp", UIText(self._window, Coords(2, 15), 18, "Cur./Max HP:"))
        self._layout.add_to_layout("player-mp", UIText(self._window, Coords(2, 25), 18, "Cur./Max HP:"))
        self._layout.add_to_layout("player-stamina", UIText(self._window, Coords(2, 35), 18, "Cur./Max SP:"))

    def update(self):
        super().update()
        self._layout.reposition()
        self._layout.update()
    
    def render(self):
        super().render()
        self._layout.render()
