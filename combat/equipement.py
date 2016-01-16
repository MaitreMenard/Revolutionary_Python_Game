"""
class Sword:
    def __init__(self):
        self.name
        self.rank
        self.atk
        self.hit
        self.crit
        self.durability
        self.price
    
    def summary(self):
        print("weapon : {}, rank : {}, atk : {}, hit : {}, crit : {}, durability : {}".format(self.name, self.rank, str(self.atk), str(self.hit), str(self.crit), str(self.durability)))        
        
    def use(self):
        self.durability -= 1
        if self.durability == 0:
            self.destroy()
            print("An {} broke!".format(self.name))
"""

class IronSword():
    number = 0
    def __init__(self, durability = 40):
        self.id = IronSword.number
        IronSword.number += 1
        self.name = "iron sword"
        self.rank = "e"
        self.atk = 3
        self.hit = 100
        self.crit = 0
        self.durability = durability
        self.price = 400
    
    def summary(self):
        print("weapon : {}, rank : {}, atk : {}, hit : {}, crit : {}, durability : {}".format(self.name, self.rank, str(self.atk), str(self.hit), str(self.crit), str(self.durability)))        
        
    def use(self):
        self.durability -= 1
        if self.durability == 0:
            self.destroy()
            print("An iron sword broke!")

class SteelSword():
    number = 0
    def __init__(self):
        self.id = SteelSword.number
        SteelSword.number += 1
        self.rank = "d"
        self.atk = 5
        self.hit = 90
        self.crit = 0
        self.durability = 35
        self.price = 875
        
class SilverSword():
    number = 0
    def __init__(self):
        self.id = SilverSword.number
        SilverSword.number += 1
        self.rank = "b"
        self.atk = 8
        self.hit = 100
        self.crit = 0
        self.durability = 20
        self.price = 2000   