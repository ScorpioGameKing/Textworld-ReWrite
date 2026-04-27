import pyray as pr
from textworld.models import Size, Coords

class LayoutContainer():

    _children: dict = {}
    _margin: int = 0
    _position: Coords = Coords(0, 0)
    _size: Size = Size(0, 0)
    _rows: int = 1
    _cols: int = 1

    def __init__(self, margin:int = 0, position: Coords = Coords(0,0), size: Size = Size(0,0), rows: int = 1, cols: int = 1):
        self.update_layout(margin, position, size, rows, cols)
    
    def update_layout(self, margin, position, size, rows, cols):
        self._margin = margin
        self._position = position
        self._size = size
        self._rows = rows
        self._cols = cols
    
    def add_to_layout(self, name, obj):
        self._children.update({name:{
            'object':obj,
            'row': len(self._children) + 1},
            'col': self._cols})
    
    def reposition(self):
        for _child in self._children:
            self._children[_child]['object'].update_position(
                self._position.x + (self._children[_child]['col'] * self._margin), 
                self._position.y + (self._children[_child]['row'] * self._margin))
    
    def update(self):
        for _child in self._children:
            self._children[_child]['object'].update()

    def render(self):
        for _child in self._children:
            self._children[_child]['object'].render()
