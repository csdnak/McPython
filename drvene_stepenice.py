#pet stepenica prema dolje
#definicija objekta i poziv rutine za crtanje
from crtanje import *		#tu je funkcija koju zovem

from mc import *			
mc = Minecraft() #inicijalizacija sustava za rad sa Minecraftom

# origin ispred na sredini 
orMj = gdjeSam ()
orSm = gdjeGledam ()

#oakwood stairs
materijal = 53



for br in range ( 5 ) :
   crtaj_stepenice ( orMj , ( 1 + br , -1 , -1 - br ) , ( 1 + br , 1 , -1 - br ) , orSm , blok_id = materijal , rel_smjer  = "odmene" )
   crtaj_kvadar ( orMj , ( 1 + br , -1 , 0 - br ) , ( 1 + br , 1 , 3 - br ) , orSm , 0 ) # zrak iznad stepenica
