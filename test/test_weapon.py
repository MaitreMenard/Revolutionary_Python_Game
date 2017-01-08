from src.Character import Character
from src.Weapon import Weapon

import unittest

# TODO: remplacer par des vrais unit tests
def test():
    weapon = Weapon("thief's blade")
    char1 = Character("mage")
    char2 = Character("thief")
    
    char1.pick_up(weapon)
    char1.equip(weapon)
    print("Dmg: {}, Hit: {}, Crit: {}, Magic: {}, Hit effects: {}".format(weapon.dmg, weapon.hit,
                                             weapon.crit, weapon.magic, weapon.on_hit_actions))
    char1.unequip(weapon)
    char1.drop(weapon)
    
    char2.pick_up(weapon)
    char2.equip(weapon)
    print("Dmg: {}, Hit: {}, Crit: {}, Magic: {}, Hit effects: {}".format(weapon.dmg, weapon.hit,
                                             weapon.crit, weapon.magic, weapon.on_hit_actions))

if __name__ == '__main__':
    test()