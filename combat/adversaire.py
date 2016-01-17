import random
import math
import equipement
import Erreur

class adversaire():
    
    def __init__(self, hp = 100, atk = 0, defense = 0):
        self.maxhp = hp
        self.hp = hp
        self.atk = atk
        self.defense = defense
        self.poisonned = [False, 0, 0]
        
    def attack_1(self):
        print("The enemy used his basic attack.")
        succès = random.randrange(100)
        if succès > 19:
            dmg = (12 + self.atk)
        else:
            print("The enemy's attack missed !")
            dmg = 0
        return dmg
        
    def attack_2(self):
        print("The enemy used his special attack.")
        dmg = 0
        succès = random.randrange(100)
        if succès > 39:
            dmg = (20 + self.atk)
        else:
            print("But he failed because he is a bronze noob. The enemy's HP -5")
            self.hp -= 5
            dmg = 0
            raise Erreur.RecoilDamage(self,5)
        return dmg
    
    def damage(self, dmg):
        damageReceived = dmg - self.defense
        if damageReceived > 0:
            self.hp -= damageReceived
            print("The enemy's HP -" + str(damageReceived))
            return damageReceived
        else:
            print("Your attack was blocked!")
            return 0      
    
    def status(self):
        if self.poisonned[0] == True:
            if self.poisonned[2] > 0:
                self.poisonned[2] -= 1
                self.hp -= self.poisonned[1]
                print("The enemy was hurt by poison. The enemy's HP -" + str(self.poisonned[1]))
            else:
                self.poisonned[0] = False
                self.poisonned[1] = 0
                self.poisonned[2] = 0
                print("Poison faded")