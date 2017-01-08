import abc

class GameObject():
    __metaclass__ = abc.ABCMeta
    
    def __init__(self, x=0, y=0):
        self._x=x
        self._y=y
        
    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self, value):
        assert(isinstance(value, int))
        assert(value >= 0), "Coordinates should be strictly positive"
        self._x = value
        
    @property
    def y(self):
        return self._y
    
    @y.setter
    def y(self, value):
        assert(isinstance(value, int))
        assert(value >= 0), "Coordinates should be strictly positive"
        self._y = value

    def get_position(self):
        return self._x, self._y
    
    def set_position(self, x, y):
        self.x = x
        self.y = y