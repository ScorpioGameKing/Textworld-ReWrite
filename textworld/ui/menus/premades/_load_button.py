from textworld.ui.menus.components import UIButton

class UILoadButton(UIButton):

    def button_press(self):
        super().button_press()
        print("Do a Screen Swap Here")