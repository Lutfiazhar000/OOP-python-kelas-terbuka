# diamond problem

class A:
    pass
    def show(self):
        print("ini adalah show A")

class B(A):
    pass
    def show(self):
        print("ini adalah show B")

class C(A):
    pass
    def show(self):
        print("ini adalah show C")

class D(B,C):
    pass

object = D()
object.show()
help(object) # urutan deamond inheritance di mulai dari kiri D,B,C,A