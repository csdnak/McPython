#ispred lika cisti pravokutnik  3x4 i dugacak 9 i to samo blokove iz liste LOSHE !!!! BUGS

from mc import * #import api-ja
mc = Minecraft() #inicijalizacija sustava za rad sa Minecraftom

def Kopanje ():
   """
   ispod lika cisti pravokutnik  50 x 100  i dubok 3 i to samo blokove iz liste zaMaknuti
   """
   zaMaknuti = [ SAND.id , STONE.id , DIRT.id , GRAVEL.id , GRASS.id , GRASS_TALL.id , COBBLESTONE.id , WATER_FLOWING.id , WATER_STATIONARY.id , LAVA_FLOWING.id , LAVA_STATIONARY.id]
   zaMaknutiOpasno = [ WATER_FLOWING.id , WATER_STATIONARY.id , LAVA_FLOWING.id , LAVA_STATIONARY.id]
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
   mc.postToChat("vX: %f vZ: %f " % ( Vx , Vz  ) )

   # makni lavu i vodu
   if  abs ( Vx )  != abs ( Vz ) :		# ne pod 45
      for dZ in  range( -105 , 105 ) :    		# prodji cijeli pravokutnik
         mc.postToChat(" ---- dZ: %f " % ( dZ  ) )
         for dY  in  range (  -1 , -6 , -1 ) : 
            #mc.postToChat("dY: %f " % ( dY  ) )
            for dX in  range ( -105 , 105  ) :
               #mc.postToChat("dX: %f " % ( dX  ) )
               if ( dZ != 0 ) or ( dX != 0 ) : 
                  gdjeX=radnaPozicija.x + Vx*dX + Vz*dZ    		# pomak po x
                  gdjeY=radnaPozicija.y + dY						# pomak po y
                  gdjeZ=radnaPozicija.z + Vx*dZ + Vz*dX			# pomak po Z
                  if mc.getBlock ( gdjeX , gdjeY , gdjeZ ) in zaMaknutiOpasno :
                     mc.setBlock(gdjeX , gdjeY , gdjeZ , STONE.id)			#postavi blok   
   #crtanje
   
   if  abs ( Vx )  != abs ( Vz ) :		# ne pod 45
      for dZ in  range( -100 , 100 ) :    		# prodji cijeli pravokutnik
         mc.postToChat("dZ: %f " % ( dZ  ) )
         for dY  in  range (  1 , -5 , -1 ) : 
            #mc.postToChat("dY: %f " % ( dY  ) )
            for dX in  range ( -100 , 100  ) :
               #mc.postToChat("dX: %f " % ( dX  ) )
               if ( dZ != 0 ) or ( dX != 0 ) : 
                  gdjeX=radnaPozicija.x + Vx*dX + Vz*dZ    		# pomak po x
                  gdjeY=radnaPozicija.y + dY						# pomak po y
                  gdjeZ=radnaPozicija.z + Vx*dZ + Vz*dX			# pomak po Z
                  mc.setBlock(gdjeX , gdjeY , gdjeZ , AIR.id)			#postavi blok
                  
                  """
                  if mc.getBlock ( gdjeX , gdjeY , gdjeZ ) in zaMaknuti :
                     mc.setBlock(gdjeX , gdjeY , gdjeZ , AIR.id)			#postavi blok
                  """
   
   return 1

   
   

   

Kopanje ()