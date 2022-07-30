# method resolution order / multiple inheritance

class A:
    def show(self):
        print("ini adalah show A")

class B:
    def show(self):
        print("ini adalah show B")

# urutan inheritance di mulai dari C,A,B
class C(A,B): # jika dirubah (B,A) maka urutan inheritance adalah C,B,A
    pass # jika def show() di class C tidak aktif maka dilakukan inheritance pada class A & B
    # def show(self): # jika def show() di class C aktif maka tidak dilakukan inheritance
    #     print("ini adalah show C")

object = C()
object.show()
help(object) 


