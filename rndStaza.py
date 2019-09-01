#ispred lika hodnik

import random
import sys
import time
from crtanje import *		#tu je funkcija koju zovem
from mc import * #import api-ja
mc = Minecraft() #inicijalizacija sustava za rad sa Minecraftom


def rndBlok ():
   distribution = ((.032,Block(91, 0))  ,
                  (.005,Block(OBSIDIAN.id, 0))  ,
                  (.005,Block(WOOD.id, 0))  ,   
                  (.01,Block(BRICK_BLOCK.id, 0))  ,                        
                  (.01,Block(WOOD_PLANKS.id, 0))  ,                     
                  #(.01,Block(DIRT.id, 0))  ,                     
                  (.015,MOSS_STONE), 
                  (.03,Block(STONE_BRICK.id, 1)), 
                  (.03,Block(STONE_BRICK.id, 2)), 
                  (.07,Block(STONE_BRICK.id, 0)) , 
                  (.07,Block(SAND.id, 0))  , 
                  (.07,Block(STONE.id, 0))  ,                   
                  (.3,Block(GRAVEL.id, 0)) , 
                  (.3,Block(COBBLESTONE.id, 0)) , 
                  (.96,Block(168, 1)) 
                  )
   while 1 == 1 :
      r = random.random()
      for p,b in distribution:
         r -= p
         if r<0:
            yield b
            break


def rndStaza (  orMj  ,  orSm , iX=0 , iZ=0 , iY=0 , duzina= 3 ,  sirina = 1):
   """
   
   iX, - relativni pomak po X
   iZ, - relativni pomak po Z
   iY , - relativni pomak po Y
   duzina - koliko dugo
   
   """


   orMj = premjesti_origin ( orMj , iX , iZ , iY ,  orSm ) #mice ishodiste  
   kojiBlok = rndBlok ()
   
   
   for dZ in range ( - sirina , sirina + 1 ) :
      for dX in range ( 0 ,   duzina  ):
         gdje = rel2abs ( orMj ,  ( dX , dZ  , -1  )  , orSm  )  #relativne koordinate u apsolutne worlda
         mc.setBlock( gdje ,  kojiBlok.next  () ) 
         gdje = rel2abs ( orMj ,  ( dX , dZ  , 0 )  , orSm  )  #relativne koordinate u apsolutne worlda
         mc.setBlock( gdje ,  AIR.id , 0 ) 
         
      
   time.sleep ( 1 )      
   return 1
 
if __name__ == "__main__":    #direktan poziv
   
   orMj = gdjeSam ()
   orSm = gdjeGledam ()
   
   
   #rndStaza (  orMj ,  orSm , iX=1 , iZ=0 , iY=0 , duzina= 10  )
   rndStaza (  orMj ,  orSm , iX=1 , iZ=0 , iY=0   )
   