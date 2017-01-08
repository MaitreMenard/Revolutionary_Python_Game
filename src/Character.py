from resources.classes import CLASSES
from src.Weapon import Weapon

class Character():
    
    def __init__(self, char_class):
        assert isinstance(char_class, str)
        self.char_class = char_class
        self.inventory = []
        
    def pick_up(self, item):
        #TODO: add assert on type of item
        assert item not in self.inventory
        assert item.owner is None
        item.owner = self
        self.inventory.append(item)
        
    def drop(self, item):
        #TODO: add assert on type of item
        assert item in self.inventory
        item.owner = None
        self.inventory.remove(item)
        
    def equip(self, weapon):
        assert isinstance(weapon, Weapon)
        assert weapon in self.inventory
        assert not weapon.is_equipped
        weapon.toggle_equip()
        #other things
        
    def unequip(self, weapon):
        assert isinstance(weapon, Weapon)
        assert weapon in self.inventory
        assert weapon.is_equipped
        weapon.toggle_equip()
        #other things