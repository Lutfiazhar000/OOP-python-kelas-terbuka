class Hero:
    # class variables
    jumlah = 0

    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        # instance variables
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        Hero.jumlah +=1

    # void finction, methods tanpa return
    def whoAmI(self):
        print("i'm..." + self.name)

    # method dengan argument
    def healthUP(self,up):
        self.health += up

    # method dengan return
    def getHealth(self):
        return self.health

hero1 = Hero("azir",150,20,2)
hero2 = Hero("nasus",150,40,5)

hero1.whoAmI()
hero1.healthUP(20)

print(hero1.getHealth())