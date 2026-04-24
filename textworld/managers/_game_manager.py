class GameManager():

    game: TextworldGame

    def __init__(self, game):
        self._game = game
    
    def update(self):
        self._game.game_view.get_zoom_dir(self._game.mouse_manager.scroll_dir)

        _hold_left_shift = self._game.keyboard_manager.get_held_key("LSH")
        
        _pressed_w = self._game.keyboard_manager.get_pressed_key("W")
        _pressed_a = self._game.keyboard_manager.get_pressed_key("A")
        _pressed_s = self._game.keyboard_manager.get_pressed_key("S")
        _pressed_d = self._game.keyboard_manager.get_pressed_key("D")

        _hold_w = self._game.keyboard_manager.get_held_key("W")
        _hold_a = self._game.keyboard_manager.get_held_key("A")
        _hold_s = self._game.keyboard_manager.get_held_key("S")
        _hold_d = self._game.keyboard_manager.get_held_key("D")

        _pressed_f = self._game.keyboard_manager.get_pressed_key("F")
        _pressed_t = self._game.keyboard_manager.get_pressed_key("T")
        
        if _pressed_f:
            self._game.window.toggle_font()
            self._game.game_view.update_font()

        if _pressed_t:
            self._game.window.toggle_theme()
        
        if not _hold_left_shift and _hold_w:
            print("W")
            self._game.player_manager.active_player.up()
        
        if not _hold_left_shift and _hold_s:
            print("S")
            self._game.player_manager.active_player.down()
        
        if not _hold_left_shift and _hold_a:
            print("A")
            self._game.player_manager.active_player.left()
        
        if not _hold_left_shift and _hold_d:
            print("D")
            self._game.player_manager.active_player.right()
        
        if _hold_left_shift and _pressed_w:
            print("Left Shift + W")
            self._game.player_manager.active_player.chunk_up()
        
        if _hold_left_shift and _pressed_s:
            print("Left Shift + S")
            self._game.player_manager.active_player.chunk_down()

        if _hold_left_shift and _pressed_a:
            print("Left Shift + A")
            self._game.player_manager.active_player.chunk_left()
        
        if _hold_left_shift and _pressed_d:
            print("Left Shift + D")
            self._game.player_manager.active_player.chunk_right()

        #print(self._game.player_manager.active_player.get_position())

        #print(self._game.player_manager.active_player.get_position())
        self._game.game_view.get_player_position(self._game.player_manager.active_player.get_position())