# Test novih funkcija iz modula CRTANJE.PY
#definicija objekta i poziv rutine za crtanje
from crtanje import *		#tu je funkcija koju zovem
from mc import *			
mc = Minecraft() #inicijalizacija sustava za rad sa Minecraftom


crtaj_deblo ( gdjeSam () , ( 3 , 0 , 0 ) , (3 ,0 , 5 ) , gdjeGledam () , "gore" , 17, 0  )

crtaj_redstonetorch ( gdjeSam () , ( 2 , 0 , 1 ) ,  gdjeGledam () ,  "meni"   )
crtaj_redstonetorch ( gdjeSam () , ( 3 , 1 , 2 ) ,  gdjeGledam () ,  "desno"   )
crtaj_redstonetorch ( gdjeSam () , ( 4 , 0 , 3 ) ,  gdjeGledam () ,  "odmene"   )
crtaj_redstonetorch ( gdjeSam () , ( 3 , -1 , 4 ) ,  gdjeGledam () , "lijevo"   )
crtaj_redstonetorch ( gdjeSam () , ( 3 , 0 , 5 ) ,  gdjeGledam () ,  "gore"   )
