#ispred lika hodnik

import random
import sys
import time
from crtanje import *		#tu je funkcija koju zovem
from mc import * #import api-ja
mc = Minecraft() #inicijalizacija sustava za rad sa Minecraftom


def rndBlok ():
   distribution = (
                  (.15,108)  ,
                  (.20,109)  ,   
                  (.15,114)  ,                        
                  (.15,128)  ,                     
                  (.15,156), 
                  (.77,67), 
                  )
   while 1 == 1 :
      r = random.random()
      for p,b in distribution:
         r -= p
         if r<0:
            yield b
            break


def stepenica (  orMj  ,  orSm , iX=0 , iZ=0 , iY=0 , sirina  = 1 , duzina= 1 ):
   """
   
   iX, - relativni pomak po X
   iZ, - relativni pomak po Z
   iY , - relativni pomak po Y
   duzina - koliko dugo
   
   """


   orMj = premjesti_origin ( orMj , iX , iZ , iY ,  orSm ) #mice ishodiste  
   kojiBlok = rndBlok ()
   
   
   
   for dZ in range ( - sirina , sirina + 1 ) :
      for br in range ( 1 , duzina + 1 ) :
         crtaj_stepenice ( orMj , ( br , dZ , br - 1  ) , ( br , dZ , br - 1 ) , orSm , blok_id = kojiBlok.next  () , rel_smjer  = "meni" , gore_dolje = "ne"  ) 
         crtaj_kvadar ( orMj , ( br , dZ , br   ) , ( br , dZ , br + 2 ) , orSm , AIR.id , blok_dv = 0 )
         
      
   time.sleep ( 1 )      
   return 1
 
if __name__ == "__main__":    #direktan poziv
   
   orMj = gdjeSam ()
   orSm = gdjeGledam ()
   
   
   
   stepenica (  orMj ,  orSm , iX=0 , iZ=0 , iY=0 , sirina  = 1 , duzina= 1  )
   