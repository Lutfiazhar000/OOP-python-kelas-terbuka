# property getter dan setter

class Hero:
    def __init__(self,name,health,armor):
        self.name = name
        self.__health = health
        self.__armor = armor
        # self.info = "name {} : \n\t health: {}".format(self.__name,self.__health)

    @property
    def info(self):
        return "name {} : \n\t health: {}".format(self.name,self.__health)

    @property
    def armor(self):
        pass

    @armor.getter
    def armor(self):
        return self.__armor

    @armor.setter
    def armor(self,input):
        self.__armor = input
    
    @armor.deleter
    def armor(self):
        print("armor di delete")
        self.__armor = None


darius = Hero('darius',100,30)

print("merubah info")
print(darius.info)
darius.name = 'katarina'
print(darius.info)

print("getter & setter untuk __armor:")
print(darius.armor)
darius.armor = 20
print(darius.armor)

print("armor di delete")
del darius.armor
print(darius.__dict__)