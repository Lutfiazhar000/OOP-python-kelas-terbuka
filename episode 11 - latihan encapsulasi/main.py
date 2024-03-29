# latihan encapsulasi

class Hero:
    __jumlah = 0

    def __init__(self,name,health,attPower,armor):
        self.__name = name
        self.__healthStandar = health
        self.__attPowerStandar = attPower
        self.__armorStandar = armor
        self.__level = 1
        self.__exp = 0

        self.__healthMax = self.__healthStandar * self.__level
        self.__attPower = self.__attPowerStandar * self.__level
        self.__armor = self.__armorStandar * self.__level

        self.__health = self.__healthMax

        Hero.__jumlah += 1
    
    @property
    def info(self):
        return "{}: \n\tlevel = {} \n\thealth = {}/{} \n\tattack = {} \n\tarmor = {}".format(self.__name,self.__level,self.__health,self.__healthMax,self.__attPower,self.__armor)

    @property
    def gainExp(self):
        pass

    @gainExp.setter
    def gainExp(self,addExp):
        self.__exp += addExp
        if (self.__exp >= 100):
            print(self.__name, "level up")
            self.__level += 1
            self.__exp -= 100

            self.__healthMax = self.__healthStandar * self.__level
            self.__attPower = self.__attPowerStandar * self.__level
            self.__armor = self.__armorStandar * self.__level

    def attack(self,enemy):
        self.gainExp = 50

aurelionSol = Hero("aurelionSol",120,10,7)
rumble = Hero("rumble",100,20,4)
print(aurelionSol.info)

# aurelionSol.gainExp = 60
# aurelionSol.gainExp = 90
# print(aurelionSol.__dict__)
# print(aurelionSol.info)

aurelionSol.attack(rumble)
aurelionSol.attack(rumble)
aurelionSol.attack(rumble)
print(aurelionSol.info)

print(aurelionSol.gainExp) # kosong