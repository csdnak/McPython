# crtanje rupe, lifta i sortera
#definicija objekta i poziv rutine za crtanje
import time 
from crtanje import *		#tu je funkcija koju zovem
from lift import *		#tu je funkcija koju zovem
from sorter import *		#tu je funkcija koju zovem

from mc import *			
mc = Minecraft() #inicijalizacija sustava za rad sa Minecraftom

# origin ispred na sredini 
orMj = gdjeSam ()
orSm = gdjeGledam ()

#sandstone glatki
materijal = 1
dv = 1



dubina = nadji_dno ( orMj , ( 0 , 0 , 0 ) , orSm )
mc.postToChat("dubina %f " % dubina  )
rupa2 ( orMj , ( 0 , 0 , 9 ) , orSm ,  visina = dubina ,   sirina = 4 , dubina = 9, baklje="ne") 
rupa2 ( orMj , ( 0 , 0 , 9 ) , orSm ,  visina = dubina ,   sirina = 4 , dubina = 9, baklje="ne")


crtaj_kvadar ( orMj , [ 10 , -4, -1 ]  , [ 10 , -4 , dubina +1 ] , orSm , STONE.id , 2 )
crtaj_ljestve  ( orMj , [ 9 , -4, -1 ]  , [ 9 , -4 , dubina +1 ] , orSm , "odmene" )
crtaj_kvadar ( orMj , [ 8 , -4, -1 ]  , [ 8 , -4, 0  ] , orSm , STONE.id , 2 )

crtaj_kvadar ( orMj , [ 0 , -4, -1 ]  , [ 0 , -4 , dubina +1 ] , orSm , STONE.id , 2 )
crtaj_ljestve  ( orMj , [ 1 , -4, -1 ]  , [ 1 , -4 , dubina +1 ] , orSm , "meni" )
crtaj_kvadar ( orMj , [ 2, -4, -1 ]  , [ 2 , -4, 0  ] , orSm , STONE.id , 2 )



sorter  ( 7 , 2 , 0 , 40 , 10 )

crtaj_hopper    ( orMj , ( 7 , 3 , 6 ) , ( 7 , 3 , 6 ) , orSm ,  "dolje" ) 
crtaj_hopper    ( orMj , ( 7 , 3 , 5 ) , ( 7 , 3 , 5 ) , orSm ,  "odmene" ) 
crtaj_lift ( 5 , -1 ,   dubina ,   ( - dubina  + 5 )  )



