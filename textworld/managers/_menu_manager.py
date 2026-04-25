from textworld.ui.menus import GameMenu

class MenuManager():
    menus: dict = {}
    active: str = "game-menu"

    def __init__(self):
        self.add_menu(self.active, GameMenu(20, 20, 200, 200))

    def add_menu(self, key, menu):
        self.menus.update({key:menu})

    def update(self):
        for menu in self.menus:
            self.menus[menu].update()

    def render(self):
        for menu in self.menus:
            self.menus[menu].render()