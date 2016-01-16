import time
import turtle

class bar:
    def __init__(self, hp, name = "Enemy", x = 0, y = 0, parent = turtle.Screen()):
        assert(isinstance(hp, int))
        assert(isinstance(name, str))
        assert(isinstance(x, (int,float)))
        assert(isinstance(y, (int,float)))
        self.max_hp = hp
        self.hp = hp
        self.reduction = 0
        self.rectangle = ((-30, -250), (30, -250), (30, 250 - self.reduction), (-30, 250 - self.reduction), (-30, -250))
        #turtle.addshape("barre", self.rectangle)
        
        self.parent = parent
        self.parent.addshape("barre", self.rectangle)
        self.parent.title("hp bar display")
        self.parent.setup(width=600, height=450)
        self.parent.tracer(n=0)
        
        self.fond = turtle.Turtle()
        self.fond.shape("square")
        self.fond.color("white")
        self.fond.pencolor("black")
        self.fond.shapesize(3.2, 25.2, 2.5)
        self.fond.penup()
        self.fond.goto(x,y)
        
        self.barre = turtle.Turtle()
        self.barre.shape("barre")
        self.barre.color("green")
        self.barre.penup()
        self.barre.goto(x,y)
        
        self.ecrivain = turtle.Turtle()
        self.ecrivain.ht()
        self.ecrivain.penup()
        self.ecrivain.goto(-240 + x, 32 + y)
        self.ecrivain.write("{}'s HP".format(name), font = ("Arial", 12, "normal"))
        self.ecrivain.setx(160 + x)
        self.ecrivain.sety(-54 + y)
        self.ecrivain.write("{} / {}".format(str(self.hp), str(self.max_hp)), align = "center", font =("Arial", 12, "normal"))
        
        self.parent.tracer(n=1)
        
    def racourcir(self, damage):
        for i in range(2*damage):
            if self.hp > 0:
                self.hp -= 0.5
                self.reduction = (500 - 500*self.hp/self.max_hp)
                self.ecrivain.undo()
                self.ecrivain.write("{0} / {1}".format(str(int(self.hp)),str(self.max_hp)), font = ("Arial", 12, "normal"))
                self.rectangle = ((-30, -250), (30, -250), (30, 250 - self.reduction), (-30, 250 - self.reduction), (-30, -250))
                self.parent.addshape("barre", self.rectangle)
                self.barre.shape("barre")
                if self.hp == 0:
                    self.barre.ht()
                elif self.hp <= 0.2*self.max_hp:
                    self.barre.color("red")
                elif self.hp <= 0.5*self.max_hp:
                    self.barre.color("yellow")
    
    def allonger(self, hp):
        for i in range(2*hp):
            if self.hp < self.max_hp:
                self.hp += 0.5
                self.reduction = (500 - 500*self.hp/self.max_hp)
                self.ecrivain.undo()
                self.ecrivain.write("{0} / {1}".format(str(int(self.hp)),str(self.max_hp)), font = ("Arial", 12, "normal"))
                self.rectangle = ((-30, -250), (30, -250), (30, 250 - self.reduction), (-30, 250 - self.reduction), (-30, -250))
                self.parent.addshape("barre", self.rectangle)
                self.barre.shape("barre")
                if self.hp > 0.5*self.max_hp:
                    self.barre.color("green")
                elif self.hp > 0.2*self.max_hp:
                    self.barre.color("yellow")
                
if __name__ == "__main__":
    fen = turtle.Screen()
    barre1 = bar(100, name = "Max", y = -120, parent = fen)
    barre2 = bar(100, y = 120, parent = fen)
    """
    time.sleep(3)
    barre.racourcir(10)
    time.sleep(2)
    barre.racourcir(50)
    time.sleep(2)
    barre.racourcir(30)
    time.sleep(2)
    barre.racourcir(10)
    """
    fen.listen()
    fen.mainloop()
    
