class GameManager():

    _game: TextworldGame
    _in_game: bool = True
    _paused: bool = False

    def __init__(self, game):
        self._game = game
    
    def update(self):
        
        '''
        -----------------------------------------
        | Catch Keys
        -----------------------------------------
        '''

        # Modifier Keys
        _hold_left_shift = self._game.keyboard_manager.get_held_key("LSH")
        
        # Key Presses
        _pressed_equal = self._game.keyboard_manager.get_pressed_key("EQL")
        _pressed_minus = self._game.keyboard_manager.get_pressed_key("-")
        _pressed_p = self._game.keyboard_manager.get_pressed_key("P")
        _press_e = self._game.keyboard_manager.get_pressed_key("E")
        _press_enter = self._game.keyboard_manager.get_pressed_key("ENT")
        _left_click = self._game.keyboard_manager.get_mouse_pressed("LEFT")

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
        # Font Cycle Up
        if not _hold_left_shift and _pressed_equal:
            self._game.window.cycle_font_up()
            self._game.game_view.update_font()

        # Font Cycle Down
        if not _hold_left_shift and _pressed_minus:
            self._game.window.cycle_font_down()
            self._game.game_view.update_font()

        # Theme Cycle Up
        if _hold_left_shift and _pressed_equal:
            self._game.window.cycle_theme_up()

        # Theme Cycle Down
        if _hold_left_shift and _pressed_minus:
            self._game.window.cycle_theme_down()
        
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
                
                # Mouse Checks
                self._game.game_view.get_zoom_dir(self._game.mouse_manager.scroll_dir)
                
                # Pause Menu UI Toggle
                if _pressed_p:
                    self._game.menu_manager.get_active().components['pause-screen'].toggle_visible()
                    self._paused = True

                # Move Player Up
                if _hold_left_shift and _hold_w:
                    self._game.player_manager.active_player.up()
                elif _press_w:
                    self._game.player_manager.active_player.up()

                # Move Player Down
                if _hold_left_shift and _hold_s:
                    self._game.player_manager.active_player.down()
                elif _press_s:
                    self._game.player_manager.active_player.down()
                
                # Move Player Left
                if _hold_left_shift and _hold_a:
                    self._game.player_manager.active_player.left()
                elif _press_a:
                    self._game.player_manager.active_player.left()
                
                # Move Player Right
                if _hold_left_shift and _hold_d:
                    self._game.player_manager.active_player.right()
                elif _press_d:
                    self._game.player_manager.active_player.right()
                
                # Update the Game View's target position
                self._game.game_view.get_player_position(self._game.player_manager.active_player.get_position())
            
            elif self._paused:

                '''
                -----------------------------------------
                | Paused Keybinds
                -----------------------------------------
                '''

                # Pause Menu UI Toggle
                if _pressed_p:
                    self._game.menu_manager.get_active().components['pause-screen'].toggle_visible()
                    self._paused = False
                
                if _press_w or _press_a:
                    self._game.menu_manager.get_active().components['pause-screen'].top_panel.hover_up()
                
                if _press_s or _press_d:
                    self._game.menu_manager.get_active().components['pause-screen'].top_panel.hover_down()

                if _press_e or _press_enter or _left_click:
                    self._game.menu_manager.get_active().components['pause-screen'].top_panel.press_selected()
                