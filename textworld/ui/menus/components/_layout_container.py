import pyray as pr
from textworld.models import Size, Coords

class LayoutContainer():

    _children: dict = {}
    _margin: int
    _position: Coords
    _size: Size
    _rows: int
    _cols: int

    def __init__(self, margin: int, position: Coords, size: Size, rows: int, cols: int):
        self.update_layout(margin, position, size, rows, cols)
    
    def update_layout(self, margin, position, size, rows, cols):
        self._margin = margin
        self._position = position
        self._size = size
        self._rows = rows
        self._cols = cols
    
    def add_to_layout(self, name, obj):
        print(len(self._children))
        self._children.update({name:{
            'object':obj,
            'row': len(self._children) + 1,
            'col': self._cols}})
        self._children[name]['object'].update_font()
    
    def reposition(self):
        for _child in self._children:
            print(f"Repositioning: {self._children[_child]['object']._position}")
            self._children[_child]['object'].update_position(
                self._position.x + (self._children[_child]['col'] * self._margin), 
                self._position.y + (self._children[_child]['row'] * self._margin))
    
    def update(self):
        self.reposition()
        for _child in self._children:
            self._children[_child]['object'].update()

    def render(self):
        for _child in self._children:
            self._children[_child]['object'].render()
