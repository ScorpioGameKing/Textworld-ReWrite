from textworld.ui.menus.components import UIButton

class UIExitButton(UIButton):

    def button_press(self):
        super().button_press()
        print("Do a Menu Swap Here")