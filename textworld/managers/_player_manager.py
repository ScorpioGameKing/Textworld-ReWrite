from textworld.entities.player import Player

class PlayerManager():

    active_player: Player
    _chunk_size: Size

    def __init__(self):
        pass
    
    def update_chunk_size(self, _chunk_size):
        self._chunk_size = _chunk_size

    def create_player(self, x, y, chunk_x, chunk_y, _chunk_size=None):
        if not _chunk_size == None: self._chunk_size = _chunk_size
        self.active_player = Player(x, y, chunk_x, chunk_y, self._chunk_size)
    
    def update(self):
        active_player.update()