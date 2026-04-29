from textworld.ui.menus.components import BasePanel, LayoutContainer, UIText
from textworld.models import Size, Coords

class RightSavePanel(BasePanel):

    _window: TextworldWindow
    _header: UIText
    _quest: UIText
    _objective: UIText

    def __init__(self, window, position, size, bg_color, fg_color, slide_dir=None, slide_speed=None):
        super().__init__(position, size, bg_color, fg_color, slide_dir, slide_speed)
        self._window = window
        self._header = UIText(self._window, Coords(6, 3), 20, "~QUEST JOURNAL~")
        self._quest = UIText(self._window, Coords(6, 18), 18, "Current Quest:")
        self._objective = UIText(self._window, Coords(6, 31), 18, "Current Objective:")
        
    def update_items(self):
        self._header.update_font()
        self._quest.update_font()
        self._objective.update_font()
        self._header.update_position(self._current_position.x, self._current_position.y)
        self._quest.update_position(self._current_position.x, self._current_position.y)
        self._objective.update_position(self._current_position.x, self._current_position.y)

    def update(self):
        super().update()
        self.update_items()
        self._header.update()
        self._quest.update()
        self._objective.update()
    
    def render(self):
        super().render()
        self._header.render()
        self._quest.render()
        self._objective.render()
       
