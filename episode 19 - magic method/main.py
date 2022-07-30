# magic method

class Mangga:
    def __init__(self,nama,jumlah):
        self.nama = nama
        self.jumlah = jumlah

    def __repr__(self): # __repr__ biasa dipake u/ debug
        return "debug = Mangga: {} sejumlah {} buah".format(self.nama,self.jumlah)

    def __str__(self): # __str__ sama dengan __repr__, __str__ biasa dipake u/ program yg sudah jadi
        return "Mangga: {} sejumlah {} buah".format(self.nama,self.jumlah)

    def __add__(self,object):
        return self.jumlah + object.jumlah

    @property # harus pakai property
    def __dict__(self):
        return "object ini memiliki nama dan jumlah"
keranjang1 = Mangga("mana lagi",20)
keranjang2 = Mangga("arumanis",25)
print(repr(keranjang1))
print(keranjang2)
print(keranjang1 + keranjang2)
print(keranjang2.__dict__) 
# hasil jika tidak pakai property 
# <bound method Mangga.__dict__ of debug = Mangga: arumanis sejumlah 25 buah>
