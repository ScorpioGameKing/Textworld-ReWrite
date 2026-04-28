from textworld.ui.menus.components import BasePanel, LayoutContainer, UIText
from textworld.models import Size, Coords

class RightSavePanel(BasePanel):

    _window: TextworldWindow
    _layout: LayoutContainer

    def __init__(self, window, position, size, bg_color, fg_color, slide_dir=None, slide_speed=None):
        super().__init__(position, size, bg_color, fg_color, slide_dir, slide_speed)
        self._window = window
        self._layout = LayoutContainer(5, self._current_position, self._size, 0, 0)
        self._layout.add_to_layout("journal-header", UIText(self._window, Coords(6, 5), 24, "~QUEST JOURNAL~:"))
        self._layout.add_to_layout("current-quest", UIText(self._window, Coords(2, 15), 18, "Current Quest:"))
        self._layout.add_to_layout("current-objective", UIText(self._window, Coords(2, 25), 18, "Current Objective:"))

    def update(self):
        super().update()
        self._layout.reposition()
        self._layout.update()
    
    def render(self):
        super().render()
        self._layout.render()
