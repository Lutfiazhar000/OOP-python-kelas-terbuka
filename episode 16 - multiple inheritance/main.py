# multiple inheritance

class A:
    def methodA(self):
        print("ini adalah method A")

class B:
    def methodB(self):
        print("ini adalah method B")

class C(A,B):
    pass

object = C()

object.methodA()
object.methodB()