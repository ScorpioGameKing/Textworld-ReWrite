from textworld.entities.player import Player

class PlayerManager():

    active_player: Player

    def __init__(self):
        pass

    def create_player(self, x, y, chunk_x, chunk_y):
        self.active_player = Player(x, y, chunk_x, chunk_y)
    
    def update(self):
        active_player.update()