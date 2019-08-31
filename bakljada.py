#ispred lika crta more baklji po tlu

import time
from mc import * #import api-ja
from crtanje import *		#tu je funkcija koju zovem
mc = Minecraft() #inicijalizacija sustava za rad sa Minecraftom

zaStaviti = [ GRASS.id , SANDSTONE.id , SAND.id , STONE.id , DIRT.id , GRAVEL.id , COBBLESTONE.id , CLAY.id , FENCE.id , STONE_BRICK.id ,  17 , 162 , 5  , 78 ] # 17 , 162 wood 5 wood planks 78 snow_layer

def bakljada (  orMj , orSm ,  dimenzije = 30 , visina = 10 ):
   """
   stupac baklji
   """
   #dimenzije = 230     #za jake PC-e
   #dimenzije = 100   # za slabe PC-e
   #gdje sam


   
   for dX in  range( -dimenzije , dimenzije + 1, 5 ):
      mc.postToChat("dX: %f " % dX )
      for dZ in  range( -dimenzije , dimenzije + 1, 5 ):
         increment = -1
         while increment < visina :
            gdje = rel2abs ( orMj ,  ( dX , dZ ,  increment )  , orSm  )
            kojiBlok = mc.getBlock ( gdje ) 
            if increment > -1 :
               if kojiBlok == AIR.id or kojiBlok == GRASS_TALL.id or kojiBlok == SNOW.id :
                  if kojiBlokIspod in zaStaviti :
                     mc.setBlock(gdje , TORCH.id , 5 )
            increment += 1
            kojiBlokIspod = kojiBlok
      
 
   mc.postToChat("Kraj !!!" )
   return 1
   
if __name__ == "__main__":    #direktan poziv
   orMj = gdjeSam ()
   orSm = gdjeGledam ()
   bakljada ( orMj , orSm ,  dimenzije = 200 , visina = 110)   
   #bakljada ( orMj , orSm , dimenzije = 150 , visina = 110)   