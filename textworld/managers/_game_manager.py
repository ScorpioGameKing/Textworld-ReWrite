class GameManager():

    game: TextworldGame

    def __init__(self, game):
        self._game = game
    
    def update(self):
        self._game.game_view.get_zoom_dir(self._game.mouse_manager.scroll_dir)
        
        if self._game.keyboard_manager.get_key("F"):
            print(self._game.game_view)
            self._game.window.toggle_font()
            self._game.game_view.update_font()

        if self._game.keyboard_manager.get_key("T"):
            print(self._game.game_view)
            self._game.window.toggle_theme()