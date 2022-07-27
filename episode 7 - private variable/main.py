# private variable
class Hero:
    # class variable
    jumlah = 0
    __privateJumlah = 0

    def __init__(self,name,health):
        self.name = name
        self.health = health

        # variable private
        self.__private = "private"

        # variable protected
        self._protected = "protected"

anya = Hero("anya",2000)

# print(anya.__dict__)
# print(anya.health)
# print(anya.private)

# print(anya.__dict__) # ini testing variable private
# anya.__private = "testing"
# print(anya.__dict__)
# print(anya.private)

# print(anya.__dict__) # ini testing variable protected
# print(anya._protected)
# anya._protected = "protected"
# print(anya.__dict__)
# print(anya._protected)

# print(anya.__dict__) # ini testing pada class
# print(Hero.__dict__)
# print(Hero.__privateJumlah)


