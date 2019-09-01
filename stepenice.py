

from mc import *



def stepenice( duzina=3 , vrsta=156 ):
   mc = Minecraft()
   pos = mc.player.getTilePos()
   for brojalica in range ( duzina ):
      mc.setBlock(pos.x+brojalica+1,pos.y+brojalica,pos.z, vrsta , brojalica , brojalica)
	  
	  
	  
stepenice ( 22 , 128 )