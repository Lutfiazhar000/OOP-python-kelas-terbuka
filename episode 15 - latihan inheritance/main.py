# latihan inhetance
from hero import HeroIonia,HeroShurima

ahri = HeroIonia('ahri')
renekton = HeroShurima('renekton')

ahri.Show_info()
renekton.Show_info()

ahri.gainExp = 200
renekton.gainExp = 250

ahri.Show_info()
renekton.Show_info()
