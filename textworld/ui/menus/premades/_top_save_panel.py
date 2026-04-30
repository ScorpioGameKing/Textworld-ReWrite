from textworld.ui.menus.components import BasePanel, UIText, UIButton
from textworld.ui.menus.premades._exit_button import UIExitButton
from textworld.ui.menus.premades._save_button import UISaveButton
from textworld.ui.menus.premades._load_button import UILoadButton
from textworld.ui.menus.premades._options_button import UIOptionsButton
from textworld.models import Coords, Size

class TopSavePanel(BasePanel):

    _window: TextworldWindow
    _header: UIText
    _continue: UIButton
    _save: UISaveButton
    _load: UILoadButton
    _options: UIOptionsButton
    _exit: UIExitButton
    _cursor: UIText
    _hovered: str = 'continue'

    def __init__(self, window, position, size, bg_color, fg_color, slide_dir=None, slide_speed=None):
        super().__init__(position, size, bg_color, fg_color, slide_dir, slide_speed)
        self._window = window
        self._header = UIText(self._window, Coords(300, 5), 32, "~PAUSE MENU~")
        self._cursor = UIText(self._window, Coords(320, 60), 22, "->")
        self._continue = UIButton(self._window, Coords(350, 60), Size(32, 110), "Continue")
        self._save = UISaveButton(self._window, Coords(350, 100), Size(32, 110), "Save")
        self._load = UILoadButton(self._window, Coords(350, 140), Size(32, 110), "Load")
        self._options = UIOptionsButton(self._window, Coords(350, 180), Size(32, 110), "Options")
        self._exit = UIExitButton(self._window, Coords(350, 220), Size(32, 110), "Exit")
    
    def press_selected(self):
        match self._hovered:
            case 'continue':
                    self._continue.button_press()
            case 'save':
                    self._save.button_press()
            case 'load':
                    self._load.button_press()
            case 'options':
                    self._options.button_press()
            case 'exit':
                    self._exit.button_press()

    def hover_down(self):
        match self._hovered:
            case 'continue':
                    self._hovered = 'save'
            case 'save':
                    self._hovered = 'load'
            case 'load':
                    self._hovered = 'options'
            case 'options':
                    self._hovered = 'exit'
            case 'exit':
                    self._hovered = 'continue'
    
    def hover_up(self):
        match self._hovered:
            case 'continue':
                    self._hovered = 'exit'
            case 'save':
                    self._hovered = 'continue'
            case 'load':
                    self._hovered = 'save'
            case 'options':
                    self._hovered = 'load'
            case 'exit':
                    self._hovered = 'options'

    def update_items(self):
        match self._hovered:
            case 'continue':
                    self._cursor._position = Coords(320, 60)
            case 'save':
                    self._cursor._position = Coords(320, 100)
            case 'load':
                    self._cursor._position = Coords(320, 140)
            case 'options':
                    self._cursor._position = Coords(320, 180)
            case 'exit':
                    self._cursor._position = Coords(320, 220)
        
        self._header.update_position(self._current_position.x, self._current_position.y)
        self._continue.update_position(self._current_position.x, self._current_position.y)
        self._cursor.update_position(self._current_position.x, self._current_position.y)
        self._save.update_position(self._current_position.x, self._current_position.y)
        self._load.update_position(self._current_position.x, self._current_position.y)
        self._options.update_position(self._current_position.x, self._current_position.y)
        self._exit.update_position(self._current_position.x, self._current_position.y)

    def update(self):
        super().update()
        self.update_items()
        self._header.update()
        self._continue.update()
        self._cursor.update()
        self._save.update()
        self._load.update()
        self._options.update()
        self._exit.update()
        if self._continue._mouse_hover: self._hovered = 'continue'
        if self._save._mouse_hover: self._hovered = 'save'
        if self._load._mouse_hover: self._hovered = 'load'
        if self._options._mouse_hover: self._hovered = 'options'
        if self._exit._mouse_hover: self._hovered = 'exit'
    
    def render(self):
        super().render()
        self._header.render()
        self._continue.render()
        self._cursor.render()
        self._save.render()
        self._load.render()
        self._options.render()
        self._exit.render()
        