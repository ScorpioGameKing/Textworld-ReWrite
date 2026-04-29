from textworld.ui.menus.components import BasePanel, UIText
from textworld.models import Size, Coords

class RightSavePanel(BasePanel):

    _window: TextworldWindow
    _header: UIText
    _quest: UIText
    _quest_line: UIText
    _objective: UIText
    _objective_line: UIText

    def __init__(self, window, position, size, bg_color, fg_color, slide_dir=None, slide_speed=None):
        super().__init__(position, size, bg_color, fg_color, slide_dir, slide_speed)
        self._window = window
        self._header = UIText(self._window, Coords(32, 5), 24, "~JOURNAL~")
        self._quest = UIText(self._window, Coords(6, 30), 18, "Cur. Quest:")
        self._quest_line = UIText(self._window, Coords(6, 43), 18, "*REPLACE VALUE*")
        self._objective = UIText(self._window, Coords(6, 56), 18, "Cur. Goal:")
        self._objective_line = UIText(self._window, Coords(6, 69), 18, "*REPLACE VALUE*")

    def update_items(self):
        self._header.update_position(self._current_position.x, self._current_position.y)
        self._quest.update_position(self._current_position.x, self._current_position.y)
        self._quest_line.update_position(self._current_position.x, self._current_position.y)
        self._objective.update_position(self._current_position.x, self._current_position.y)
        self._objective_line.update_position(self._current_position.x, self._current_position.y)

    def update(self):
        super().update()
        self.update_items()
        self._header.update()
        self._quest.update()
        self._quest_line.update()
        self._objective.update()
        self._objective_line.update()
    
    def render(self):
        super().render()
        self._header.render()
        self._quest.render()
        self._quest_line.render()
        self._objective.render()
        self._objective_line.render()
       
