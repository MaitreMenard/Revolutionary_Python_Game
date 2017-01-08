import abc

class Item():
    __metaclass__ = abc.ABCMeta
    
    def __init__(self):
        self.name = None
        self.price = None
