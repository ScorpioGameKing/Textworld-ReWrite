from textworld.ui.menus.components import BasePanel, LayoutContainer
from textworld.models import Coords, Size

class PauseScreen():

    _window: TextworldWindow

    left_panel: BasePanel
    left_layout: LayoutContainer

    right_panel: BasePanel

    top_panel: BasePanel

    bottom_panel: BasePanel

    _colors: Colors

    def __init__(self, window):
        self._window = window
        self.left_panel = BasePanel(Coords(20, 40), Size(590, 200), self._window.colors["fg"], self._window.colors["bg"])
        self.left_layout = LayoutContainer(5, Coords(20, 40), Size(590, 200))

        self.right_panel = BasePanel(Coords(1060, 40), Size(590, 200), self._window.colors["fg"], self._window.colors["bg"], slide_dir='right')
        
        self.top_panel = BasePanel(Coords(240, 40), Size(370, 800), self._window.colors["fg"], self._window.colors["bg"], slide_dir='up', slide_speed=6)
        
        self.bottom_panel = BasePanel(Coords(240, 430), Size(200, 800), self._window.colors["fg"], self._window.colors["bg"], slide_dir='down')

    def update_theme(self):
        self.left_panel.update_colors(self._window.colors)
        self.right_panel.update_colors(self._window.colors)
        self.top_panel.update_colors(self._window.colors)
        self.bottom_panel.update_colors(self._window.colors)

    def toggle_visible(self):
        self.left_panel.visible = not self.left_panel.visible
        self.right_panel.visible = not self.right_panel.visible
        self.top_panel.visible = not self.top_panel.visible
        self.bottom_panel.visible = not self.bottom_panel.visible
    
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
    
