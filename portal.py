# surival house 7 x 7 from http://www.minecraftforum.net/forums/minecraft-discussion/survival-mode/290440-minecraft-survival-starter-houses
#definicija objekta i poziv rutine za crtanje
from crtanje import *		#tu je funkcija koju zovem
from mc import *			
mc = Minecraft() #inicijalizacija sustava za rad sa Minecraftom

# origin ispred na sredini 
orMj = gdjeSam ()
orSm = gdjeGledam ()


# reset
crtaj_kvadar ( orMj , [  0 , -3, -1 ]  , [ 0 , 3 , 8  ] , orSm , 49 , 0 ) # obsidian
crtaj_kvadar ( orMj , [  0 , -2 , 0 ]  , [ 0 , 2 , 7  ] , orSm , AIR.id , 0 ) # air