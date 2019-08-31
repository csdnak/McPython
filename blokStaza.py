#ispred lika hodnik

import random
import sys
import time
from crtanje import *		#tu je funkcija koju zovem
from mc import * #import api-ja
mc = Minecraft() #inicijalizacija sustava za rad sa Minecraftom



def blokStaza (  orMj  ,  orSm , iX=0 , iZ=0 , iY=0 , duzina= 10 ,  sirina = 1):
   """
   
   iX, - relativni pomak po X
   iZ, - relativni pomak po Z
   iY , - relativni pomak po Y
   duzina - koliko dugo
   
   """


   orMj = premjesti_origin ( orMj , iX , iZ , iY ,  orSm ) #mice ishodiste  
   
   for dZ in range ( - sirina , sirina + 1 ) :
      for dX in range ( 0 ,   duzina  ):
         gdje = rel2abs ( orMj ,  ( dX , dZ  , -1  )  , orSm  )  #relativne koordinate u apsolutne worlda
         mc.setBlock( gdje ,  98 ) 

         
      
   time.sleep ( 1 )      
   return 1
 
if __name__ == "__main__":    #direktan poziv
   
   orMj = gdjeSam ()
   orSm = gdjeGledam ()
   
   
   #rndStaza (  orMj ,  orSm , iX=1 , iZ=0 , iY=0 , duzina= 10  )
   blokStaza (  orMj ,  orSm , iX=1 , iZ=0 , iY=0   )
   