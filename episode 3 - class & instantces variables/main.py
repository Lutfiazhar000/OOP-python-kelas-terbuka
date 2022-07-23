class Hero :
    #  class variable atau static variable
    jumlah = 0

    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        # ini adalah instant variables
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        Hero.jumlah += 1
        print("membuat hero dengan nama " + inputName)

hero1 = Hero("sniper",100,73,4)
print(Hero.jumlah)
hero2 = Hero("evelynn",120,55,3)
print(Hero.jumlah)
hero3 = Hero("katarina",200,41,2)
print(Hero.jumlah)
