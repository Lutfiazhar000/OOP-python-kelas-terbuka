# latihan
# game league of legend abal-abal

class Hero:
    def __init__(self, name, health, attackPower, armorNumber):
        self.name = name
        self.health = health
        self.attackPower = attackPower
        self.armorNumber = armorNumber

    def attack(self, enemy):
        print(self.name + "attack " + enemy.name)
        enemy.attacked(self, self.attackPower)

    def attacked(self, enemy, attackPower_enemy):
        print(self.name + "attacked by " + enemy.name)
        attack_diterima = attackPower_enemy/self.armorNumber
        print("serangan yang diterima sebesar: " + str(attack_diterima))
        self.health -= attack_diterima
        print("darah " + self.name + "tersisa " + str(self.health))

sivir = Hero("sivir ",130,21,4)
jinx = Hero("jinx ",110,18,3)

sivir.attack(jinx)
print("\n")
jinx.attack(sivir)



