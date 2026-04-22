import pyray as pr

class GameView():
    
    _window: TextworldWindow

    def __init__(self, window):
        self._window = window

    def update(self):
        pass

    def render(self):
        # TODO Pass string data from loaded chunks
        pr.draw_text_ex(
            self._window.fonts['blocked'],
             """gggggdddfffffffffffffdddgggggggggggssssssssssssssssssssssgggggggggggggggggggggggggsss
ggggggddffffffffffffffddggggggggggggssssssssssssssssssssssgggggggggggggggggggggggssss
ggggggdddfffffffffffffdddggggggggggggssssssssssssssssssssssggggggggggggggggggggggssss
gggggggdddffffffffffffdddgggggggggggggsssssssssssssssssssssgggggggggggggggggggggsssss
gggggggdddfffffffffffffdddgggggggggggggsssssssssssssssssssssgggggggggggggggggggssssss
ggggggggdddffffffffffffdddgggggggggggggggsssssssssssssssssssgggggggggggggggggggssssss
gggggggggdddfffffffffffddddggggggggggggggggsssssssssssssssssggggggggggggggggggsssssss
ggggggggggdddffffffffffddddggggggggggggggggggsssssssssssssssggggggggggggggggggsssssss
gggggggggggddddffffffffdddddgggggggggggggggggggsssssssssssssggggggggggggggggggsssssss
ggggggggggggddddddffffddddddgggggggggggggggggggggggsssssssgggggggggggggggggggssssssss
ggggggggggggggdddddddddddddddgggggggggggggggggggggggggggggggggggggggggggggggggsssssss
gggggggggggggggdddddddddddddddggggggggggggggggggggggggggggggggggggggggggggggggsssssss
sgggggggggggggggggdddddddddddddgggggggggggggggggggggggggggggggggggggggggggggggsssssss
ssggggggggggggggggggdddddddddddddggggggggggggggggggggggggggggggggggggggggggggggssssss
ssgggggggggggggggggggggdddddddddddddggggggggggggggggggggggggggggggggggggggggggggsssss
sssggggggggggggggggggggggdddddddddddddddggggggggggggggggggggggggggggggggggggggggggsss
ssssggggggggggggggggggggggdddddddddddddddddggggggggggggggggggggggggggggggggggggggggss
ssssssgggggggggggggggggggggddddddddddddddddddgggggggggggggggggggggggggggggggggggggggg
sssssssgggggggggggggggggggggddddddffffffffddddddggggggggggggggggggggggggggggggggggggg
sssssssssggggggggggggggggggggddddffffffffffffdddddggggggggggggggggggggggggggggggggggg
ssssssssssssgggggggggggggggggddddffffffffffffffddddddgggggggggggggggggggggggggggggggg
ssssssssssssssggggggggggggggggdddfffffffffffffffffddddddggggggggggggggggggggggggggggg
ssssssssssssssssggggggggggggggdddfffffffffffffffffffdddddddgggggggggggggggggggggggggg
sssssssssssssssssggggggggggggggdddffffffmmmmmmfffffffffdddddddddggggggggggggggggggggg
sssssssssssssssssssggggggggggggdddfffffmmmmmmmmmmfffffffffdddddddddddddddgggggggggggg
                """,
              [2, 2],
              self._window.fonts['blocked'].baseSize,
              2, 
              self._window.colors['fg'])
