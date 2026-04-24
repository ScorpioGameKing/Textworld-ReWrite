class GameManager():

    game: TextworldGame

    def __init__(self, game):
        self._game = game
    
    def update(self):
        self._game.game_view.get_zoom_dir(self._game.mouse_manager.scroll_dir)
        
        if self._game.keyboard_manager.get_key("F"):
            self._game.window.toggle_font()
            self._game.game_view.update_font()

        if self._game.keyboard_manager.get_key("T"):
            self._game.window.toggle_theme()
        
        if self._game.keyboard_manager.get_key("W"):
            self._game.player_manager.active_player.up()
        
        if self._game.keyboard_manager.get_key("S"):
            self._game.player_manager.active_player.down()
        
        if self._game.keyboard_manager.get_key("A"):
            self._game.player_manager.active_player.left()
        
        if self._game.keyboard_manager.get_key("D"):
            self._game.player_manager.active_player.right()

        print(self._game.player_manager.active_player.get_position())

        #print(self._game.player_manager.active_player.get_position())
        self._game.game_view.get_player_position(self._game.player_manager.active_player.get_position())