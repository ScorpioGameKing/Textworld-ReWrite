class GameManager():

    game: TextworldGame
    _move_table:list = [False, False, False, False]

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
            self._move_table[0] = True
        
        if self._game.keyboard_manager.get_key("S"):
            self._move_table[1] = True
        
        if self._game.keyboard_manager.get_key("A"):
            self._move_table[2] = True
        
        if self._game.keyboard_manager.get_key("D"):
            self._move_table[3] = True

        print(self._move_table)
        self._game.player_manager.active_player.update_positon(self._move_table[0], self._move_table[1], self._move_table[2], self._move_table[3])
        self._move_table = [False, False, False, False]
        print(self._game.player_manager.active_player.get_position())

        #print(self._game.player_manager.active_player.get_position())
        self._game.game_view.get_player_position(self._game.player_manager.active_player.get_position())