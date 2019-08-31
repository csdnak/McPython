#ispred lika chisti pjesak 3x3x20

from mc import * #import api-ja
mc = Minecraft() #inicijalizacija sustava za rad sa Minecraftom

def gasi ():
   """
   ispred lika chisti pjesak 3x3x10
   """
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
   #mc.postToChat("vX: %f vZ: %f " % ( Vx , Vz  ) )

   #crtanje
   if  abs ( Vx )  != abs ( Vz ) :		# ne pod 45
      for dZ in  range( -60 , 60 ) :    		# prodji chep
         for dY  in  range( -3 , 3 ) : 
            for dX in range ( -60 , 61 ) :
               gdjeX=radnaPozicija.x + Vx*dX + Vz*dZ    		# pomak po x
               gdjeY=radnaPozicija.y + dY
               gdjeZ=radnaPozicija.z + Vx*dZ + Vz*dX			# pomak po Z
               koji = mc.getBlock ( gdjeX , gdjeY , gdjeZ )
               if  koji == 50 :	#ako je torch
                  mc.setBlock(gdjeX , gdjeY , gdjeZ , AIR)					#postavi blok zraka

         mc.postToChat("dZ: %f " % dZ )            
   return 1
   
gasi ()