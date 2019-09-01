# rupa prema gore
#definicija objekta i poziv rutine za crtanje
import time 
from crtanje import *		#tu je funkcija koju zovem

from mc import *			
mc = Minecraft() #inicijalizacija sustava za rad sa Minecraftom

# origin ispred na sredini 
orMj = gdjeSam ()
orSm = gdjeGledam ()

#sandstone glatki
materijal = 1
dv = 1

filter ( orMj , ( 0 , 0 , 0 ) , orSm ,  visina = 70 ,   sirina = 4 , dubina = 9, baklje="ne") 

STONE.id , 2
crtaj_kvadar ( orMj , [ 10 , -4, 0 ]  , [ 10 , -4 , 70  ] , orSm , STONE.id , 2 )
crtaj_ljestve  ( orMj , [ 9 , -4, 0 ]  , [ 9 , -4 , 70  ] , orSm , "odmene" )