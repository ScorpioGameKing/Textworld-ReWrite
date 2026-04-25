class GameManager():

    game: TextworldGame

    def __init__(self, game):
        self._game = game
    
    def update(self):
        # Mouse Checks
        self._game.game_view.get_zoom_dir(self._game.mouse_manager.scroll_dir)

        # Modifier Keys
        _hold_left_shift = self._game.keyboard_manager.get_held_key("LSH")
        
        # Key Presses
        _pressed_w = self._game.keyboard_manager.get_pressed_key("W")
        _pressed_a = self._game.keyboard_manager.get_pressed_key("A")
        _pressed_s = self._game.keyboard_manager.get_pressed_key("S")
        _pressed_d = self._game.keyboard_manager.get_pressed_key("D")

        _pressed_f = self._game.keyboard_manager.get_pressed_key("F")
        _pressed_t = self._game.keyboard_manager.get_pressed_key("T")

        _pressed_u = self._game.keyboard_manager.get_pressed_key("U")
        _pressed_h = self._game.keyboard_manager.get_pressed_key("H")
        _pressed_j = self._game.keyboard_manager.get_pressed_key("J")
        _pressed_k = self._game.keyboard_manager.get_pressed_key("K")
        
        # Holding Key
        _hold_w = self._game.keyboard_manager.get_held_key("W")
        _hold_a = self._game.keyboard_manager.get_held_key("A")
        _hold_s = self._game.keyboard_manager.get_held_key("S")
        _hold_d = self._game.keyboard_manager.get_held_key("D")
        
        # Font Cycle
        if _pressed_f:
            self._game.window.toggle_font()
            self._game.game_view.update_font()

        # Theme Cycle
        if _pressed_t:
            self._game.window.toggle_theme()
        
        # Debug UI Toggle
        if not _hold_left_shift and _pressed_u:
            self._game.menu_manager.get_active().components['top_panel'].toggle_slide()
        
        if _pressed_h:
            self._game.menu_manager.get_active().components['left_panel'].toggle_slide()
        
        if _pressed_j:
            self._game.menu_manager.get_active().components['bottom_panel'].toggle_slide()
        
        if _pressed_k:
            self._game.menu_manager.get_active().components['right_panel'].toggle_slide()
        
        if _hold_left_shift and _pressed_u:
            self._game.menu_manager.get_active().components['top_panel'].toggle_slide()
            self._game.menu_manager.get_active().components['left_panel'].toggle_slide()
            self._game.menu_manager.get_active().components['bottom_panel'].toggle_slide()
            self._game.menu_manager.get_active().components['right_panel'].toggle_slide()
        
        # Move Player Up
        if not _hold_left_shift and _hold_w:
            self._game.player_manager.active_player.up()
        
        # Move Player Down
        if not _hold_left_shift and _hold_s:
            self._game.player_manager.active_player.down()
        
        # Move Player Left
        if not _hold_left_shift and _hold_a:
            self._game.player_manager.active_player.left()
        
        # Move Player Right
        if not _hold_left_shift and _hold_d:
            self._game.player_manager.active_player.right()
        
        # Move Chunk Up
        if _hold_left_shift and _pressed_w:
            self._game.player_manager.active_player.chunk_up()
        
        # Move Chunk Down
        if _hold_left_shift and _pressed_s:
            self._game.player_manager.active_player.chunk_down()

        # Move Chunk Left
        if _hold_left_shift and _pressed_a:
            self._game.player_manager.active_player.chunk_left()
        
        # Move Chunk Right
        if _hold_left_shift and _pressed_d:
            self._game.player_manager.active_player.chunk_right()

        # Update UI Colors
        #self._game.menu_manager.get_active().components['left_panel'].up
        
        # Update the Game View's target position
        self._game.game_view.get_player_position(self._game.player_manager.active_player.get_position())