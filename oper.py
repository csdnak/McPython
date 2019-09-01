# Test novih funkcija iz modula CRTANJE.PY
#definicija objekta i poziv rutine za crtanje
from crtanje import *		#tu je funkcija koju zovem
from mc import *			
mc = Minecraft() #inicijalizacija sustava za rad sa Minecraftom

# test vrata ++++++

orMj = gdjeSam ()
orSm = gdjeGledam ()

#sandstone glatki
materijal = 1
dv = 1

filter ( orMj , ( 0 , 0 , 0 ) , orSm ,  visina = 7 ,   sirina = 26 , dubina = 36, baklje="da") 
#crtaj_terase ( gdjeSam () ,  [ 0 , 0 , 0  ] , gdjeGledam () ,  visina = 9 ,  korak = 2 , sirina = 26 , baklje="da")
