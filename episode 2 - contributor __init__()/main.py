class Hero :
    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor

hero1 = Hero("sniper",100,73,4)
hero2 = Hero("evelynn",120,55,3)
hero3 = Hero("katarina",200,41,2)

print(hero1.__dict__)
print(hero2.__dict__)
print(hero3.__dict__)