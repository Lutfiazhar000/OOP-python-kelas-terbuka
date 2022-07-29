# override method

class Hero:
    def __init__(self,name,health):
        self.name = name
        self.health = health

    def showInfo (self):
        print("show info class hero")
        print("{} \n\thealth: {}".format(
            self.name,
            self.health
            )
        )

class HeroIonia(Hero):
    def __init__(self, name):
        super().__init__(name,100)

    # override
    def showInfo(self):
        print("show info subclass heroIonia")
        print("{} \n\tregion: ionia,\n\thealth: {}".format(
            self.name,
            self.health
            )
        )
        
class HeroShurima(Hero):
    def __init__(self, name):
        super().__init__(name,120)
        
ahri = HeroIonia("ahri")
renekton = HeroShurima("renekton")

renekton.showInfo() # akan mengambil info yang di class hero
ahri.showInfo() # akan mengambil info yang di subclass heroIonia