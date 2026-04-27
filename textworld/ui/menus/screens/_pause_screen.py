from textworld.ui.menus.components import BasePanel

class PauseScreen():

    _window: TextworldWindow

    left_panel: BasePanel
    right_panel: BasePanel
    top_panel: BasePanel
    bottom_panel: BasePanel

    _colors: Colors

    def __init__(self, window):
        self._window = window
        self.left_panel = BasePanel(20, 40, 200, 590, self._window.colors["fg"], self._window.colors["bg"])
        self.right_panel = BasePanel(1060, 40, 200, 590, self._window.colors["fg"], self._window.colors["bg"], 'right')
        self.top_panel = BasePanel(240, 40, 800, 370, self._window.colors["fg"], self._window.colors["bg"], 'up', 6)
        self.bottom_panel = BasePanel(240, 430, 800, 200, self._window.colors["fg"], self._window.colors["bg"], 'down')

    def update_theme(self):
        self.left_panel.update_colors(self._window.colors)
        self.right_panel.update_colors(self._window.colors)
        self.top_panel.update_colors(self._window.colors)
        self.bottom_panel.update_colors(self._window.colors)
    
    def render(self):
        self.left_panel.render()
        self.right_panel.render()
        self.top_panel.render()
        self.bottom_panel.render()

    def update(self):
        self.left_panel.update()
        self.right_panel.update()
        self.top_panel.update()
        self.bottom_panel.update()
    
