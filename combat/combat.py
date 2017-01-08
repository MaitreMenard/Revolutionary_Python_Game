#import damage
import turtle
import combattant
import adversaire
import equipement
from hp_bar import bar
import Erreur
import random

class Combat:
    def __init__(self, combattant1 = None, combattant2 = None):
        with open("stats.txt", 'r') as fich:
            stats = fich.readlines()
        for i in range(len(stats)):
            stats[i] = stats[i].replace("\n", "")
        #self.combattant1 = combattant1
        #self.combattant2 = combattant2
        self.combattant1 = combattant.combattant(level = int(stats[0]), hp = int(stats[1]), atk = int(stats[2]), defense = int(stats[3]), Matk = int(stats[4]), exp = int(stats[5]), weapon = equipement.IronSword(int(stats[7])))
        self.combattant2 = adversaire.adversaire(hp = 120, atk = 20, defense = 15)
        self.lastInput = None
        self.c1DmgReceived = 0
        self.c1Healing = 0
        self.c2DmgReceived = 0
        self.c2Recoil = 0
        self.c2PsnDmg = 0
        
        self.fen = turtle.Screen()
        self.fen.title("Epic battle")
        self.fen.setup(width=600, height=450)
        self.barre1 = bar(self.combattant1.maxhp, name = "Max", y = -120, parent = self.fen)
        self.barre2 = bar(self.combattant2.maxhp, y = 120, parent = self.fen)
        
        self.fen.listen()
        #self.fen.mainloop()

    def userInputs(self):
        print("Your HP : " + str(self.combattant1.hp) +  "/" + str(self.combattant1.maxhp)) 
        print("The enemy's HP : " + str(self.combattant2.hp) +  "/" + str(self.combattant2.maxhp))
        self.lastInput = input("Select your next move (q, w, e, r or h) or press i for infos or s for character stats: ")
    
    def process(self):
        damageDealt = 0
        statusGiven = [False, 0, 0]
        if self.lastInput.lower() == "q":
            damageDealt = self.combattant1.attack_1()
        elif self.lastInput.lower() == "w":
            damageDealt = self.combattant1.attack_2()
        elif self.lastInput.lower() == "e":
            statusGiven = self.combattant1.poison()
        elif self.lastInput.lower() == "r":
            if self.combattant1.cooldown == 0:
                damageDealt = self.combattant1.ult()   
            else:
                print("This skill is still on cooldown.\n\n")
                return True
        elif self.lastInput.lower() == "h":
            if self.combattant1.heal_counts == 1:
                self.c1Healing = self.combattant1.heal()
            else:
                print("You can only heal yourself once.\n\n")
                return True
        elif self.lastInput.lower() == "i":
            self.combattant1.info()
            return True
        elif self.lastInput.lower() == "s":
            self.combattant1.summary()
            print("\n")
            return True
        else:
            print("You failed to select a valid move. You don't ability this turn.")
        
        if damageDealt != 0:
            self.c2DmgReceived = self.combattant2.damage(damageDealt)
            
        if statusGiven[0] == True:
            self.combattant2.poisonned = statusGiven
            
        damageReceived = 0
        if self.combattant2.hp > 0:
            x = random.randrange(100)
            try:
                if x > 24:
                    damageReceived = self.combattant2.attack_1()
                else:
                    damageReceived = self.combattant2.attack_2()
            except Erreur.RecoilDamage as rd:
                self.c2Recoil = rd.damage
            
        if damageReceived != 0:
            self.c1DmgReceived = self.combattant1.damage(damageReceived)
    
        if self.combattant2.hp > 0:
            self.combattant2.status()
            self.c2PsnDmg = self.combattant2.poisonned[1]
        
        if self.combattant1.cooldown > 0:
            self.combattant1.cooldown -= 1
        print("\n")
        return False
    
    def render(self):
        #combattant1's ability animation
        
        #combattant1's damage dealt
        self.barre2.racourcir(self.c2DmgReceived)
        self.c2DmgReceived = 0
        
        #combattant1's recoil damage
        
        #combattant1's healing
        self.barre1.allonger(self.c1Healing)
        self.c1Healing = 0
        
        #combattant2's ability animation
        
        #combattant2's damage dealt
        self.barre1.racourcir(self.c1DmgReceived)
        self.c1DmgReceived = 0
        
        #combattant2's recoil damage
        self.barre2.racourcir(self.c2Recoil)
        self.c2Recoil = 0
        
        #combattant2's healing done
        
        #combattant1's status effect
        
        #combattant2's status effect
        self.barre2.racourcir(self.c2PsnDmg)
        
    
    def cleanUp(self):
        if self.combattant1.hp <= 0:
            print("You lost !")

        if self.combattant2.hp <= 0:
            if self.lastInput.lower() == "r":
                print("Fatality!!!")
            print("You won !")
            if self.combattant1.hp == self.combattant1.maxhp:
                print("Perfect game!")  
            self.combattant1.exp += 25  
            print("Exp + 25 \nExp = {} \n".format(self.combattant1.exp)) 
            
        self.combattant1.levelup()
        ecrire_stats = open("stats.txt", "w")
        ecrire_stats.write("{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}".format(self.combattant1.level, self.combattant1.maxhp, self.combattant1.atk, self.combattant1.defense, self.combattant1.Matk, self.combattant1.exp, self.combattant1.weapon.name, self.combattant1.weapon.durability))
        ecrire_stats.close()
    
    def loop(self):
        while(self.combattant1.hp > 0 and self.combattant2.hp > 0):
            self.userInputs()
            skipRender = self.process()
            if skipRender:
                continue
            self.render()
        self.cleanUp()
        
if __name__ == "__main__":  
    a = Combat()
    a.loop()