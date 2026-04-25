from textworld.ui.menus import GameMenu

class MenuManager():

    _window: TextworldWindow
    menus: dict = {}
    active: str = "game-menu"

    def __init__(self, window):
        self._window = window
        self.add_menu(self.active, GameMenu(self._window))

    def add_menu(self, key, menu):
        self.menus.update({key:menu})
    
    def get_active(self):
        return self.menus[self.active]

    def update(self):
        for menu in self.menus:
            self.menus[menu].update()

    def render(self):
        for menu in self.menus:
            self.menus[menu].render()