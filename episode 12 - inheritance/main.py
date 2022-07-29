# inheritance -> sesuatu yg diturunkan atau diwariskan

class Hero:
    def __init__(self,name,health):
        self.name = name
        self.health = health

class HeroIonia(Hero):
    pass

class HeroShurima(Hero):
    pass

akali = Hero("akali",100)
irellia = HeroIonia("irellia",100)
azir = HeroShurima("azir",120)

print(akali.name)
print(irellia.name)
print(azir.name)
# print(help(azir))
