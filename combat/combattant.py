import random
import math
import equipement
import Erreur

class combattant():
    
    def __init__(self, level, hp, atk, defense, Matk, exp, weapon): 
        self.vivant = True
        self.heal_counts = 1
        self.cooldown = 0
        self.enemy_poisonned = False
        self.compteur_poison = 0
        self.level = level
        self.maxhp = hp
        self.hp = hp
        self.atk = atk
        self.defense = defense
        self.Matk = Matk
        self.exp = exp
        self.weapon = weapon
        self.summary()
    
    def summary(self):
        print("level : {}, HP : {}/{}, atk : {}, def : {}, Matk : {}, exp : {}".format(str(self.level), str(self.hp), str(self.maxhp), str(self.atk), str(self.defense), str(self.Matk), str(self.exp)))
        self.weapon.summary()
        
    def attack_1(self):
        succès = random.randrange(100)
        if succès > 9:
            dmg = (10 + self.atk + self.weapon.atk)
        else:
            print("Attack missed !")
            dmg = 0
        self.weapon.use()
        return dmg
        
    def attack_2(self):
        succès = random.randrange(100)
        if succès > 24:
            dmg = (20 + self.atk + self.weapon.atk)
        else:
            print("Attack missed !")
            dmg = 0
        self.weapon.use()
        return dmg
    
    def poison(self):
        succès = random.randrange(100)
        if succès > 24:
            self.enemy_poisonned = True
            self.compteur_poison = 4
            print("The enemy is now poisonned for 4 turns.")
        else:
            print("Attack missed !")
    
    def poison_dmg(self):
        poison_dmg = 0
        if self.enemy_poisonned == True:
            if self.compteur_poison > 0:
                self.compteur_poison -= 1
                poison_dmg = (3 + math.floor(self.Matk/2))
            else:
                self.enemy_poisonned = False
                self.compteur_poison = 0
                print("Poison faded")
        return poison_dmg
            
    def ult(self):
        succès = random.randrange(100)
        if succès > 49:
            dmg = (50 + self.atk + self.weapon.atk)
        else:
            print("Attack missed !")
            dmg = 0
        self.cooldown = 2
        self.weapon.use()
        return dmg
            
    def heal(self):
        if self.maxhp - self.hp >= 25 + self.Matk:
            healed = 25 + self.Matk
        else:
            healed = self.maxhp - self.hp
        self.hp += healed
        print("Your HP + " + str(healed))
        self.heal_counts -= 1
        return healed
    
    def info(self):
        move = input("Press the key of the move on which you want infos : ")
        if move == "q":
            print("Your basic attack.\nDamage : 10 + {}\nAccuracy : 90 %\n\n".format(self.atk + self.weapon.atk))
        elif move == "w":
            print("Your special attack. \nDamage : 20 + {}\nAccuracy : 75 %\n\n".format(self.atk + self.weapon.atk))
        elif move == "e":
            print("Poison your ennemy for 4 turns. \nDamage each turn : 3 + {}\nAccuracy : 75 %\n\n".format(str(math.floor(self.Matk/2))))
        elif move == "r":
            print("Your ultimate. \nDamage : 50 + {}\nAccuracy : 50 % \nCooldown : 2 turns\n\n".format(self.atk + self.weapon.atk))
        elif move == "h":
            print("This move allows you to regain up to 25 + {} health. \nCannot heal you over your max HP. \nCan only be used once in a fight.\n\n".format(self.Matk))
        else:
            print ("There is no move assigned to this key.\n\n")
    
    def levelup(self):
        if self.exp >= 100:
            self.level += 1
            self.exp -= 100
            print("Level Up ! \n{} --> {} \nExp = {}".format((self.level - 1), self.level, self.exp))
            
            self.maxhp += 2
            print("Max HP + 2 = {}".format(self.maxhp))
            
            succès_atk = random.randrange(100)
            if succès_atk > 49:
                self.atk += 3
                print("Atk + 3 = {}".format(self.atk))
            else:
                self.atk += 2
                print("Atk + 2 = {}".format(self.atk))
                
            succès_def = random.randrange(100)
            if succès_def > 74:
                self.defense += 2
                print("Def + 2 = {}".format(self.defense))
            else:
                self.defense += 1
                print("Def + 1 = {}".format(self.defense))
                
            succès_Matk = random.randrange(100)
            if succès_Matk > 49:
                self.Matk += 1
                print("Matk + 1 = {}".format(self.Matk))
            else:
                print("Matk + 0 = {}".format(self.Matk))    
                
    def damage(self, dmg):
        damageReceived = dmg - self.defense
        if damageReceived > 0:
            self.hp -= damageReceived
            print("Your HP -" + str(damageReceived))
            return damageReceived
        else:
            print("The enemy's attack was blocked!")
            return 0