# super (inheritance)

class Hero:
    def __init__(self,name,health):
        self.name = name
        self.health = health

    def showInfo (self):
        print("{} dengan health {}".format(self.name,self.health))

class HeroIonia(Hero):
    def __init__(self, name):
        super().__init__(name, 100)
        super().showInfo()

class HeroShurima(Hero):
    def __init__(self, name):
        super().__init__(name, 120)
        super().showInfo()

akali = HeroIonia("akali")
azir = HeroShurima("azir")