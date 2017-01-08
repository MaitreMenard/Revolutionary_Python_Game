from src.GameObject import GameObject
from src.Item import Item

class Chest(GameObject):
    """ A container for up to 3 items"""
    
    def __init__(self, x=0, y=0, content=[]):
        super().__init__(x, y)
        assert(isinstance(content, list))
        assert(len(content) <= 3)
        assert(all(isinstance(item, Item) for item in content))
        self._content = content
        
    def retrieve(self, index):
        assert(isinstance(index, int))
        assert(0 <= index < 3)
        #TODO: catch IndexError: index out of range
        return self._content.pop(index)
    
    def store(self, item):
        assert(isinstance(item, Item))
        if len(self._content >= 3):
            #TODO: catch IndexError: index out of range
            raise IndexError("Chest cannot contain more than 3 items!")
        self._content.append(item)
        
    
    def switch(self, index, item):
        assert(isinstance(index, int))
        assert(0 <= index < 3)
        assert(isinstance(item, Item))
        #TODO: catch IndexError: index out of range
        tmp = self._content[index]
        self._content[index] = item
        return tmp
        
        
        