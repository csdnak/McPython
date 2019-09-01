# crta prugu duzine cca 256 ( velicina minecraft chunka ???? )  - SIROVO I NEDORADJENO
import time 
from mc import * # ajmo probati ovaj import

mc = Minecraft() #inicijalizacija sustava za rad sa Minecraftom

radnaPozicija = mc.player.getPos()		#gdje sam

smjerRada = mc.player.getDirection ()	#uzmem kamo gledam
smjerRada.y = round (radnaPozicija.y )		#radimo na levelu ispod
smjerRada.x = round (smjerRada.x) 		# nabacimo cjelobrojni inkrement/dekrement
smjerRada.z = round (smjerRada.z)


"""
ubij lavu i vodu
"""

zaMaknuti = [ WATER_FLOWING.id , WATER_STATIONARY.id , LAVA_STATIONARY.id , LAVA_FLOWING.id , GRAVEL.id , SAND.id]

duzinaPruge = 260

#smjer gledanja radi preglednosti spremimo u "vektor""
Vx=0												#pocetne vrijednosti su nule
Vz=0
if abs (smjerRada.x) > abs (smjerRada.z): 		#nadje se dominanti smjer i spremi u vektor
   Vx=round(smjerRada.x)
else:
   Vz=round(smjerRada.z)
   #mc.postToChat("vX: %f vZ: %f " % ( Vx , Vz  ) )
mc.postToChat("S T A R T !!!! !!!!! "  )
#crtanje
if  abs ( Vx )  != abs ( Vz ) :		# ne pod 45
   for dX in range ( 0 , duzinaPruge ) :
      for dY in range ( -2 , 5 )	:
         for dZ in range ( -3 , 4 )  :
            gdjeX=radnaPozicija.x + Vx*dX + Vz*dZ    		# pomak po x
            gdjeY=radnaPozicija.y + dY						# pomak po y
            gdjeZ=radnaPozicija.z + Vx*dZ + Vz*dX			# pomak po Z
            if mc.getBlock ( gdjeX , gdjeY , gdjeZ ) in zaMaknuti :
               mc.setBlock(gdjeX , gdjeY , gdjeZ , STONE.id , 2 )		# "Krpa se granitom"
               #postavi blok	
      mc.postToChat("dX: %f dZ: %f " % ( dX , dZ  ) )               

mc.postToChat("okolo KRAJJJJJ !!!!! "  )
time.sleep ( 10 )           

"""t
napravi tunel i podlogu
"""
if  abs ( Vx )  != abs ( Vz ) :		# ne pod 45
   for dX in range ( 1 , duzinaPruge ) :
      for dY in range ( -1 , 0 )	:
         for dZ in range ( -1 , 2 )  :
            gdjeX=radnaPozicija.x + Vx*dX + Vz*dZ    		# pomak po x
            gdjeY=radnaPozicija.y + dY						# pomak po y
            gdjeZ=radnaPozicija.z + Vx*dZ + Vz*dX			# pomak po Z
            mc.setBlock(gdjeX , gdjeY , gdjeZ , STONE.id , 4 )			#postavi blok podloge - polished diorite

mc.postToChat("Podloga KRAJJJJJ !!!!! "  )
time.sleep ( 10 )                      	

if  abs ( Vx )  != abs ( Vz ) :		# ne pod 45
   for dX in range ( 1 , duzinaPruge ) :
      for dZ in range ( -1 , 2 )	:
         for dY in range ( 0, 3 )  :
            gdjeX=radnaPozicija.x + Vx*dX + Vz*dZ    		# pomak po x
            gdjeY=radnaPozicija.y + dY						# pomak po y
            gdjeZ=radnaPozicija.z + Vx*dZ + Vz*dX			# pomak po Z
            mc.setBlock(gdjeX , gdjeY , gdjeZ , AIR)			#postavi blok

            
mc.postToChat("Rupa KRAJJJJJ !!!!! "  )
time.sleep ( 10 )             
            
if  abs ( Vx )  != abs ( Vz ) :		# ne pod 45
   for dX in range ( 1 , duzinaPruge , 5 ) :
      for dZ in  ( -1 , 1 )	:
         for dY in range ( -1 , 0 )  :
            gdjeX=radnaPozicija.x + Vx*dX + Vz*dZ    		# pomak po x
            gdjeY=radnaPozicija.y + dY						# pomak po y
            gdjeZ=radnaPozicija.z + Vx*dZ + Vz*dX			# pomak po Z
            mc.setBlock(gdjeX , gdjeY , gdjeZ , GLOWSTONE_BLOCK)			#postavi blok

			
mc.postToChat("Lampe KRAJJJJJ !!!!! "  )
time.sleep ( 10 ) 			
				  
"""
nacrtaj pocetak
"""

if Vx == 0 :
	korektor = 0
else :
	korektor = 1

dX = 1
dY = 0
dZ = 0

gdjeX=radnaPozicija.x + Vx*dX + Vz*dZ    		# pomak po x
gdjeY=radnaPozicija.y + dY						# pomak po y
gdjeZ=radnaPozicija.z + Vx*dZ + Vz*dX			# pomak po Z
mc.setBlock(gdjeX , gdjeY , gdjeZ , STONE.id , 2 )			#postavi blok

dX += 1

gdjeX=radnaPozicija.x + Vx*dX + Vz*dZ    		# pomak po x
gdjeY=radnaPozicija.y + dY						# pomak po y
gdjeZ=radnaPozicija.z + Vx*dZ + Vz*dX			# pomak po Z
mc.setBlock(gdjeX , gdjeY , gdjeZ , 27 , korektor)			#postavi blok

"""
nacrtaj 36 elemenata
"""

for nesto in range ( int (round ( duzinaPruge / 11 ) - 2) ):
   for br in range ( 8 ) :
      dX += 1
      gdjeX=radnaPozicija.x + Vx*dX + Vz*dZ    		# pomak po x
      gdjeY=radnaPozicija.y + dY						# pomak po y
      gdjeZ=radnaPozicija.z + Vx*dZ + Vz*dX			# pomak po Z
      mc.setBlock(gdjeX , gdjeY , gdjeZ , 66 , korektor)			#postavi blok


   dX += 1

   gdjeX=radnaPozicija.x + Vx*dX + Vz*dZ    		# pomak po x
   gdjeY=radnaPozicija.y + dY						# pomak po y
   gdjeZ=radnaPozicija.z + Vx*dZ + Vz*dX			# pomak po Z
   mc.setBlock(gdjeX , gdjeY , gdjeZ , 28 , korektor)			#postavi blok
   dX += 1

   gdjeX=radnaPozicija.x + Vx*dX + Vz*dZ    		# pomak po x
   gdjeY=radnaPozicija.y + dY						# pomak po y
   gdjeZ=radnaPozicija.z + Vx*dZ + Vz*dX			# pomak po Z
   mc.setBlock(gdjeX , gdjeY , gdjeZ , 27 , korektor)			#postavi blok
   dX += 1

   gdjeX=radnaPozicija.x + Vx*dX + Vz*dZ    		# pomak po x
   gdjeY=radnaPozicija.y + dY						# pomak po y
   gdjeZ=radnaPozicija.z + Vx*dZ + Vz*dX			# pomak po Z
   mc.setBlock(gdjeX , gdjeY , gdjeZ , 28 , korektor)			#postavi blok
   time.sleep ( 0.3 )
   mc.postToChat("dX: %f dZ: %f " % ( dX , dZ  ) )
   
for br in range ( 8 ) :
   dX += 1
   gdjeX=radnaPozicija.x + Vx*dX + Vz*dZ    		# pomak po x
   gdjeY=radnaPozicija.y + dY						# pomak po y
   gdjeZ=radnaPozicija.z + Vx*dZ + Vz*dX			# pomak po Z
   mc.setBlock(gdjeX , gdjeY , gdjeZ , 66 , korektor)			#postavi blok

time.sleep ( 1 )   


"""
nacrtaj kraj
"""
dX += 1

gdjeX=radnaPozicija.x + Vx*dX + Vz*dZ    		# pomak po x
gdjeY=radnaPozicija.y + dY						# pomak po y
gdjeZ=radnaPozicija.z + Vx*dZ + Vz*dX			# pomak po Z
mc.setBlock(gdjeX , gdjeY , gdjeZ , 27 , korektor)			#postavi blok

dX += 1

gdjeX=radnaPozicija.x + Vx*dX + Vz*dZ    		# pomak po x
gdjeY=radnaPozicija.y + dY						# pomak po y
gdjeZ=radnaPozicija.z + Vx*dZ + Vz*dX			# pomak po Z
mc.setBlock(gdjeX , gdjeY , gdjeZ , STONE.id , 2)			#postavi blok

time.sleep ( 1 )
mc.postToChat("KRAJJJJJ !!!!! "  )