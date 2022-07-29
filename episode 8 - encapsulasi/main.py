#  encapsulasi

class Hero:
    def __init__(self,name,health,attackPower):
        self.__name = name
        self.__health = health
        self.__attPower = attackPower

    # getter
    def getName(self):
        return self.__name
    
    def getHealth(self):
        return self.__health

    # setter
    def attacked(self,damagePower):
        self.__health -= damagePower

    def setAttPowe(self,nilaiBaru):
        self.__attPower = nilaiBaru

# awal game
swain = Hero("swain",100,20)

# game berjalan
print(swain.getName())
print(swain.getHealth())
swain.attacked(3)
print(swain.getHealth())
