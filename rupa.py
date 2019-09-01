#ispod lika cisti pravokutnik  

from mc import * #import api-ja
mc = Minecraft() #inicijalizacija sustava za rad sa Minecraftom

def rupa ():
   """
   ispod lika cisti pravokutnik  i to samo blokove iz liste pod i strop QUARTZ & QUARTZ
   """
   zaMaknuti = [ SAND.id , STONE.id , DIRT.id , GRAVEL.id , GRASS.id , GRASS_TALL.id , COBBLESTONE.id , WATER_FLOWING.id , WATER.id , LAVA_FLOWING.id , LAVA.id ]
   zaMaknutiOpasno = [ WATER_FLOWING.id , WATER_STATIONARY.id , LAVA_FLOWING.id , LAVA_STATIONARY.id , SAND.id , GRAVEL.id , AIR.id ] # Dodani shljunak i pjesak jer padanje sve poremete

   #gdje sam
   radnaPozicija = mc.player.getPos()		
   #kamo gledam
   smjerRada = mc.player.getDirection ()			#uzmem kamo gledam
   #smjer gledanja radi preglednosti spremimo u "vektor""
   Vx=0												#pocetne vrijednosti su nule
   Vz=0
   if abs (smjerRada.x) > abs (smjerRada.z): 		#nadje se dominanti smjer i spremi u vektor
      Vx=round(smjerRada.x)
   else:
      Vz=round(smjerRada.z)
   
   for dY in range ( -7 , 0 , 1 ) :
      for dZ in range ( -5 , 6 ) :
         for  dX in range ( -5 , 6 ) :
            gdjeX=radnaPozicija.x + Vx*dX + Vz*dZ    		# pomak po x
            gdjeY=radnaPozicija.y + dY
            gdjeZ=radnaPozicija.z + Vx*dZ + Vz*dX			# pomak po Z
            if mc.getBlock ( gdjeX , gdjeY , gdjeZ ) in zaMaknutiOpasno :
               mc.setBlock(gdjeX , gdjeY , gdjeZ , STONE.id , 2 )			#postavi blok 
            if ( dY ==  -5 ) and ( abs ( dZ ) < 2  ) and ( abs ( dZ ) < 2  ) :
               mc.setBlock(gdjeX , gdjeY , gdjeZ , STONE.id , 0 )			#platforma za padanje
                  
   for dY in range ( -5 , 0 , 1 ) :
      for dZ in range ( -3 , 4 ) :
         for  dX in range ( -3 , 4 ) :
            gdjeX=radnaPozicija.x + Vx*dX + Vz*dZ    		# pomak po x
            gdjeY=radnaPozicija.y + dY
            gdjeZ=radnaPozicija.z + Vx*dZ + Vz*dX			# pomak po Z
            if  ( mc.getBlock ( gdjeX , gdjeY , gdjeZ ) in zaMaknuti ) :
               mc.setBlock(gdjeX , gdjeY , gdjeZ , AIR)			#postavi blok

      

rupa ()