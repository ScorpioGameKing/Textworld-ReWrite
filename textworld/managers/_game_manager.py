class GameManager():

    _game: TextworldGame
    _in_game: bool = True
    _paused: bool = True

    def __init__(self, game):
        self._game = game
    
    def update(self):
        '''
        -----------------------------------------
        | Catch Keys
        -----------------------------------------
        '''
        # Mouse Checks
        self._game.game_view.get_zoom_dir(self._game.mouse_manager.scroll_dir)

        # Modifier Keys
        _hold_left_shift = self._game.keyboard_manager.get_held_key("LSH")
        
        # Key Presses
        _pressed_f = self._game.keyboard_manager.get_pressed_key("F")
        _pressed_t = self._game.keyboard_manager.get_pressed_key("T")
        _pressed_p = self._game.keyboard_manager.get_pressed_key("P")

        # Pressing Key
        _press_w = self._game.keyboard_manager.get_pressed_key("W")
        _press_a = self._game.keyboard_manager.get_pressed_key("A")
        _press_s = self._game.keyboard_manager.get_pressed_key("S")
        _press_d = self._game.keyboard_manager.get_pressed_key("D")
 
        # Holding Key
        _hold_w = self._game.keyboard_manager.get_held_key("W")
        _hold_a = self._game.keyboard_manager.get_held_key("A")
        _hold_s = self._game.keyboard_manager.get_held_key("S")
        _hold_d = self._game.keyboard_manager.get_held_key("D")

        '''
        -----------------------------------------
        | Anytime Debug Keybinds
        -----------------------------------------
        '''
        # Font Cycle
        if _pressed_f:
            self._game.window.toggle_font()
            self._game.game_view.update_font()

        # Theme Cycle
        if _pressed_t:
            self._game.window.toggle_theme()
        
        '''
        -----------------------------------------
        | In Game Keybinds
        -----------------------------------------
        '''
        if self._in_game:
            
            if not self._paused:

                '''
                -----------------------------------------
                | Un-Paused Keybinds
                -----------------------------------------
                '''
                
                # Pause Menu UI Toggle
                if _pressed_p:
                    self._game.menu_manager.get_active().components['pause-screen'].top_panel.toggle_slide()
                    self._game.menu_manager.get_active().components['pause-screen'].left_panel.toggle_slide()
                    self._game.menu_manager.get_active().components['pause-screen'].bottom_panel.toggle_slide()
                    self._game.menu_manager.get_active().components['pause-screen'].right_panel.toggle_slide()
                    self._paused = True

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
                
                # Update the Game View's target position
                self._game.game_view.get_player_position(self._game.player_manager.active_player.get_position())
            
            elif self._paused:

                '''
                -----------------------------------------
                | Un-Paused Keybinds
                -----------------------------------------
                '''

                # Pause Menu UI Toggle
                if _pressed_p:
                    self._game.menu_manager.get_active().components['pause-screen'].top_panel.toggle_slide()
                    self._game.menu_manager.get_active().components['pause-screen'].left_panel.toggle_slide()
                    self._game.menu_manager.get_active().components['pause-screen'].bottom_panel.toggle_slide()
                    self._game.menu_manager.get_active().components['pause-screen'].right_panel.toggle_slide()
                    self._paused = False
