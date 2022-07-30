class Region:
    def setRegion(self,region):
        self.region = region

    def showRegion(self):
        print(self.region)

class Role:
    def setRole(self,role):
        self.role = role

    def showRole(self):
        print(self.role)

class Hero(Region,Role):
    def __init__(self,name,health):
        self.name = name
        self.health = health

shen = Hero("shen",100)
shen.setRegion("ionia")
shen.setRole("mid")

shen.showRegion()
shen.showRole()