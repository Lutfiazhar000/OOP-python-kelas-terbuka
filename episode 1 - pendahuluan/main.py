class hero :
    pass

hero1 = hero() # object
hero2 = hero()
hero3 = hero();

hero1.name = "sniper"
hero1.health = 100

hero2.name = "sven"
hero2.health = 300

hero3.name = "yasuo"
hero3.health = 1000


print(hero1)
print(hero1.__dict__)
print(hero1.name)