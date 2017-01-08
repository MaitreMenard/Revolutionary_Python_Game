class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Equipement:
    def __init__(self, name, rank, hardness, durability, price):
        self.name = name
        self.rank = rank
        self.hardness = hardness
        self.durability = durability
        self.price = price
        
    def summary(self):
        pass


class Sword(Equipement):
    def __init__(self):
        super.__init__()
        self.atk
        self.hit
        self.crit
    
    def summary(self):
        print("weapons : {}, rank : {}, atk : {}, hit : {}, crit : {}, durability : {}".format(self.name, self.rank, str(self.atk), str(self.hit), str(self.crit), str(self.durability)))        
        
    def use(self):
        self.durability -= 1
        if self.durability == 0:
            self.destroy()
            print("An {} broke!".format(self.name))

    def modify(self, name=None, atk=None, hit=None, crit=None, durability=None):
        if name is not None:
            self.name = name
        if atk is not None:
            self.atk = atk
        if hit is not None:
            self.hit = hit
        if crit is not None:
            self.crit = crit
        if durability is not None:
            self.durability = durability

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
        print("weapons : {}, rank : {}, atk : {}, hit : {}, crit : {}, durability : {}".format(self.name, self.rank, str(self.atk), str(self.hit), str(self.crit), str(self.durability)))        
        
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