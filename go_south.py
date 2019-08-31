# teleport eksperiment
import time 
from mc import * #import api-ja
mc = Minecraft() #inicijalizacija sustava za rad sa Minecraftom


   
   
  

  
def ubij_ispod (pos) :
   mc.setBlock(pos.x  , pos.y - 1 , pos.z , AIR.id  )
   return
   
  
  
def go_south (pomak)  :
   pos = mc.player.getTilePos()
   mc.setBlock(pos.x - pomak , 109 , pos.z  , STONE.id)
   time.sleep ( 1 )
   ubij_ispod ( pos )
   mc.player.setPos(pos.x - pomak , 110 , pos.z)
   time.sleep ( 6 )
      
korak = 135
pocetak =  mc.player.getTilePos()
go_south ( korak )
