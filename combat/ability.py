import random

class ability:
    def __init__(self):
        self.accuracy = 0
        self.baseDamage = 0
        self.ratio = 0
        self.recoil = 0
        self.recoilChance = 0
        self.statusCondition = None
        self.statusChance = 0
        self.manaCost = 0
        
    def use(self, stat):
        success = random.randrange(100)
        damageDealt = 0
        condition = None
        recoil = 0
        if self.accuracy > success:
            damageDealt = self.baseDamage + self.ratio * stat
            statusSuccess = random.randrange(100)
            if self.statusChance > statusSuccess:
                condition = self.statusCondition
        else:
            recoilSuccess = random.randrange(100)
            if self.recoilChance > recoilSuccess:
                recoil = self.recoil
        return damageDealt, condition, recoil
            