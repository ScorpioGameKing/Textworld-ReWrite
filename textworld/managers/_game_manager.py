class GameManager():

    game: TextworldGame

    def __init__(self, game):
        self._game = game
    
    def update(self):
        self._game.game_view.get_zoom_dir(self._game.mouse_manager.scroll_dir)