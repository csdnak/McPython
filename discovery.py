# BUGOVITO NERADI

import time 
from mc import * #import api-ja
mc = Minecraft() #inicijalizacija sustava za rad sa Minecraftom

  
def ubij_ispod (pos) :
   mc.setBlock(pos.x  , pos.y - 1 , pos.z , AIR.id  )
   return
  
def go_south ( koliko , pomak ) :
   for brojalica in range ( 0 , koliko + 1 ):
      mc.postToChat("go_south : %f " % ( brojalica  ) )
      pos = mc.player.getTilePos()
      mc.setBlock(pos.x  , 89 , pos.z + pomak , STONE.id)
      time.sleep ( 3 )
      ubij_ispod ( pos )
      mc.player.setPos(pos.x  , 90 , pos.z - pomak)
      time.sleep ( 3 )
      
      
def go_west ( koliko , pomak ) :
   for brojalica in range ( 0 , koliko + 1 ):
      mc.postToChat("go_west : %f " % ( brojalica  ) )
      pos = mc.player.getTilePos()
      mc.setBlock(pos.x  - pomak , 89 , pos.z , STONE.id )
      time.sleep ( 3 )
      ubij_ispod ( pos )
      mc.player.setPos(pos.x - pomak , 90 , pos.z )
      time.sleep ( 3 )
      
      
def go_north ( koliko , pomak ) :
   for brojalica in range ( 0 , koliko + 1 ):
      mc.postToChat("go_north : %f " % ( brojalica  ) )
      pos = mc.player.getTilePos()
      mc.setBlock(pos.x  , 89 , pos.z - pomak , STONE.id )
      time.sleep ( 3 )
      ubij_ispod ( pos )
      mc.player.setPos(pos.x  , 90 , pos.z + pomak)
      time.sleep ( 3 )
      
def go_east ( koliko , pomak ) :
   for brojalica in range (  0 , koliko + 1  ):
      mc.postToChat("go_east : %f " % ( brojalica  ) )
      pos = mc.player.getTilePos()
      mc.setBlock(pos.x + pomak , 89 , pos.z  , STONE.id )
      time.sleep ( 3 )
      ubij_ispod ( pos )
      mc.player.setPos(pos.x + pomak , 90 , pos.z )
      time.sleep ( 3 )
      

korak = 70

pocetak =  mc.player.getTilePos()
for krug in range ( 2 , 225 , 2) :
   mc.postToChat("krug : %f " % ( krug  ) )
   go_south ( 0 , korak )
   go_west ((int ( krug / 2 ) + 1 ) , korak )
   go_north ( krug + 1 , korak )
   go_east ( (int ( krug / 2 ) + 1 ) , korak )
   go_east ( (int ( krug / 2 ) + 1 ) , korak )
   go_south ( krug +1 , korak )
   go_west (( int ( krug / 2 + 1 ) ) , korak )
   
mc.player.setPos( pocetak.x ,  pocetak.y ,  pocetak.z )

