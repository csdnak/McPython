#definicija objekta i poziv rutine za crtanje
from crtanje import *		#tu je funkcija koju zovem
from mc import *			
mc = Minecraft() #inicijalizacija sustava za rad sa Minecraftom


def gumica ():
   """
   cisti podrucje 100 x 100 x 10
   """
   
   crtaj_kvadar ( gdjeSam () , ( -250 , -250 , -2 )  , ( 250 , 250 , -1 ) , gdjeGledam () , 2 ) # zemlja
   crtaj_kvadar ( gdjeSam () , ( -250 , -250 , 0 )  , ( 250 , 250 , 110 ) , gdjeGledam () , 0 ) # zrak
   mc.postToChat("GOTOVO !!!!!!!!! " )

gumica ()