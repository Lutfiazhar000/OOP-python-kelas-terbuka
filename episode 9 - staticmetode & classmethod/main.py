# staticmethod & classmethod

class Hero:
    __jumlah = 0;

    def __init__(self,name):
        self.__name = name
        Hero.__jumlah += 1

    # method ini hanya berlaku u/ objek
    def getJumlah(self):
        return Hero.__jumlah
    
    # method ini tidak berlaku u/ objek tetapi berlaku u/ class
    def getJumlah1():
        return Hero.__jumlah

    # method static (decorator) nempel class dan objek
    @staticmethod
    def getJumlah2():
        return Hero.__jumlah

    @classmethod
    def getJumlah3(cls):
        return cls.__jumlah

vi = Hero('vi')
print(Hero.getJumlah2())
jinx = Hero('jinx')
print(vi.getJumlah2())
catlyne = Hero(('catlyne'))
print(vi.getJumlah3())
