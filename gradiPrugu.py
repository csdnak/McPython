# crta prugu duzine cca 256 ( velicina minecraft chunka ???? )  - SIROVO I NEDORADJENO
import time 
#gradi prugu ali postepeno jump po jump

from mc import * # ajmo probati ovaj import
from crtanje import *	
mc = Minecraft() #inicijalizacija sustava za rad sa Minecraftom


def obradi_trans ( radnaPozicija , dX , dY , dZ , Vx , Vz ) :
   gdjeX=radnaPozicija.x + Vx*dX + Vz*dZ    		# pomak po x
   gdjeY=radnaPozicija.y + dY						# pomak po y
   gdjeZ=radnaPozicija.z + Vx*dZ + Vz*dX			# pomak po Z
   return ( gdjeX , gdjeY , gdjeZ )




def zachepi (  ) : # pripremi teren 15 polja naprijed
   zaMaknuti = [ SANDSTONE.id , SAND.id , STONE.id , DIRT.id , GRAVEL.id , GRASS.id , GRASS_TALL.id , COBBLESTONE.id , WATER_FLOWING.id , WATER_STATIONARY.id , LAVA_FLOWING.id , LAVA_STATIONARY.id , 17 , 162 ] # 17 , 162 wood
   zaMaknutiOpasno = [ WATER_FLOWING.id , WATER_STATIONARY.id , LAVA_FLOWING.id , LAVA_STATIONARY.id , SAND.id , GRAVEL.id ] # Dodani shljunak i pjesak jer padanja sve poremete
   udaljenost = 0 # ovdje pise koliko je daleko
   prosirenje = 5 # counter , pravo prosirenje je za 2 manje
   duzina_kanala = 14
   granica = 12
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


   
   if  abs ( Vx )  != abs ( Vz ) :		# ne pod 45
      for dY in range ( 0  ,10 ) :  # kanal
         #mc.postToChat("Level %f" % dY )
         for dZ in range (  - dY - prosirenje  , dY + prosirenje + 1  ) : 
            for dX in range ( 1 + duzina_kanala + 2 ) :
               """
               gdjeX=radnaPozicija.x + Vx* ( dX  ) +  Vz*dZ # pomak po x
               gdjeY=radnaPozicija.y + dY						   # pomak po y
               gdjeZ=radnaPozicija.z + Vx*dZ + Vz*( dX )		# pomak po Z
               """
               gdjeX , gdjeY , gdjeZ = obradi_trans ( radnaPozicija , dX , dY , dZ , Vx , Vz )
               if abs ( ( dZ )  ) < granica + prosirenje : # ????
                  kojiBlok = mc.getBlock ( gdjeX , gdjeY , gdjeZ )
                  if kojiBlok in zaMaknutiOpasno :
                     mc.setBlock(gdjeX , gdjeY , gdjeZ , STONE.id , 2 )			#postavi blok 
                  # Nebitno za vlak ??
                  gornjiBlok = mc.getBlock ( gdjeX , gdjeY + 1 , gdjeZ )      # provjeri i sredi i blok "iznad" da stalno nepadaju
                  if gornjiBlok in zaMaknutiOpasno :
                     mc.setBlock(gdjeX , gdjeY + 1 , gdjeZ , STONE.id , 2 )			#postavi blok 
                  # """
                     
                  #if  abs ( dZ ) <  ( dY - 2 + prosirenje  ) : 
                     #if ( abs  ( dZ )  < 11 + prosirenje ) :
                        #if dX in range ( 1 , duzina_kanala  ) :
                        ###(abs ( ( dZ )  ) < granica ) and ( ( dY - abs ( dZ )   ) > 3  )  and  ( dX in range ( 1 , duzina_kanala - 2 )): # u uzem dijelu chisti
                           #if kojiBlok in zaMaknuti : 
                              #mc.setBlock(gdjeX , gdjeY , gdjeZ , AIR.id)			#postavi blok
      #if  abs ( Vx )  != abs ( Vz ) :		# ne pod 45
      for dX in range ( 1 , duzina_kanala ) :   #tunel
         for dZ in range ( -1 , 2 )	:
            for dY in range ( 0, 3 )  :
               """
               gdjeX=radnaPozicija.x + Vx*dX + Vz*dZ    		# pomak po x
               gdjeY=radnaPozicija.y + dY						# pomak po y
               gdjeZ=radnaPozicija.z + Vx*dZ + Vz*dX			# pomak po Z
               """
               gdjeX , gdjeY , gdjeZ = obradi_trans ( radnaPozicija , dX , dY , dZ , Vx , Vz )
               mc.setBlock(gdjeX , gdjeY , gdjeZ , AIR)			#postavi blok
 
   mc.postToChat("K R A J  !!!!!!!!!!!!!!!!!!!!!!!!!!!!" )
   return 1

def pocetak () :
   radnaPozicija = mc.player.getPos()		#gdje sam

   smjerRada = mc.player.getDirection ()	#uzmem kamo gledam
   smjerRada.y = round (radnaPozicija.y )		#radimo na levelu ispod
   smjerRada.x = round (smjerRada.x) 		# nabacimo cjelobrojni inkrement/dekrement
   smjerRada.z = round (smjerRada.z)
   Vx=0												#pocetne vrijednosti su nule
   Vz=0
   if abs (smjerRada.x) > abs (smjerRada.z): 		#nadje se dominanti smjer i spremi u vektor
      Vx=round(smjerRada.x)
   else:
      Vz=round(smjerRada.z)   
      
   if Vx == 0 :
      korektor = 0
   else :
      korektor = 1
   
   if  abs ( Vx )  != abs ( Vz ) :		# ne pod 45
      for dX in range ( 1 , 11 ) :
         for dY in range ( -1 , 0 )	:
            for dZ in range ( -1 , 2 )  :
               """
               gdjeX=radnaPozicija.x + Vx* ( dX  ) +  Vz*dZ # pomak po x
               gdjeY=radnaPozicija.y + dY						   # pomak po y
               gdjeZ=radnaPozicija.z + Vx*dZ + Vz*( dX )		# pomak po Z
               """
               gdjeX , gdjeY , gdjeZ = obradi_trans ( radnaPozicija , dX , dY , dZ , Vx , Vz )
               if ( dX == 1 )  and  ( dZ != 0 ) :
                  mc.setBlock(gdjeX , gdjeY , gdjeZ , GLOWSTONE_BLOCK)
               else :
                  mc.setBlock(gdjeX , gdjeY , gdjeZ , STONE.id , 4 )			#postavi blok podloge - polished diorite

   dX = 1
   dY = 0   # NA PODLOZI
   dZ = 0

   """
   gdjeX=radnaPozicija.x + Vx* ( dX  ) +  Vz*dZ # pomak po x
   gdjeY=radnaPozicija.y + dY						   # pomak po y
   gdjeZ=radnaPozicija.z + Vx*dZ + Vz*( dX )		# pomak po Z
   """
   gdjeX , gdjeY , gdjeZ = obradi_trans ( radnaPozicija , dX , dY , dZ , Vx , Vz )   
   mc.setBlock(gdjeX , gdjeY , gdjeZ , STONE.id , 2 )			#postavi blok odbojnik

   dX += 1

   gdjeX , gdjeY , gdjeZ = obradi_trans ( radnaPozicija , dX , dY , dZ , Vx , Vz )   
   mc.setBlock(gdjeX , gdjeY , gdjeZ , 27 , korektor)			#postavi blok elektificirano
   #mc.setBlock(gdjeX , gdjeY - 1 , gdjeZ + 1, GLOWSTONE_BLOCK)			#postavi blok
   #mc.setBlock(gdjeX , gdjeY - 1 , gdjeZ - 1, GLOWSTONE_BLOCK)			#postavi blok
   
   for br in range ( 8 ) :
      dX += 1
      gdjeX , gdjeY , gdjeZ = obradi_trans ( radnaPozicija , dX , dY , dZ , Vx , Vz )              
      mc.setBlock(gdjeX , gdjeY , gdjeZ , 66 , korektor)			#postavi blok obicna pruga


def segment () :

   orMj = gdjeSam ()
   orSm = gdjeGledam ()
   radnaPozicija = mc.player.getPos()		#gdje sam

   smjerRada = mc.player.getDirection ()	#uzmem kamo gledam
   smjerRada.y = round (radnaPozicija.y )		#radimo na levelu ispod
   smjerRada.x = round (smjerRada.x) 		# nabacimo cjelobrojni inkrement/dekrement
   Vx=0												#pocetne vrijednosti su nule
   Vz=0
   if abs (smjerRada.x) > abs (smjerRada.z): 		#nadje se dominanti smjer i spremi u vektor
      Vx=round(smjerRada.x)
   else:
      Vz=round(smjerRada.z)   
     
   if Vx == 0 :
      korektor = 0
   else :
      korektor = 1
   
   if  abs ( Vx )  != abs ( Vz ) :		# ne pod 45
      for dX in range ( 1 , 12 ) :
         crtaj_hopper    ( orMj , ( dX , -2 , -1 ) , ( dX , -2 , -1 ) , orSm ,  "meni" , blok_id = 154 , blok_dv = 0 ) 
         for dY in range ( -1 , 0 )	:
            for dZ in range ( -1 , 2 )  :
               gdjeX , gdjeY , gdjeZ = obradi_trans ( radnaPozicija , dX , dY , dZ , Vx , Vz )                    
               if ( dX == 2 )  and  ( dZ != 0 )  :
                  mc.setBlock(gdjeX , gdjeY , gdjeZ , GLOWSTONE_BLOCK)
               else :
                  mc.setBlock(gdjeX , gdjeY , gdjeZ , STONE.id , 4 )			#postavi blok podloge - polished diorite
            
               
               
                  
               

   dX = 1
   dY = 0   # NA PODLOZI
   dZ = 0

   gdjeX , gdjeY , gdjeZ = obradi_trans ( radnaPozicija , dX , dY , dZ , Vx , Vz )   
   mc.setBlock(gdjeX , gdjeY , gdjeZ , 28 , korektor)			#postavi blok senzor
   dX += 1

   gdjeX , gdjeY , gdjeZ = obradi_trans ( radnaPozicija , dX , dY , dZ , Vx , Vz )   
   mc.setBlock(gdjeX , gdjeY , gdjeZ , 27 , korektor)			#postavi blok elektificirano
   
   dX += 1

   gdjeX , gdjeY , gdjeZ = obradi_trans ( radnaPozicija , dX , dY , dZ , Vx , Vz )   
   mc.setBlock(gdjeX , gdjeY , gdjeZ , 28 , korektor)			#postavi blok senzor
   
   for br in range ( 7 ) :
      dX += 1
      gdjeX , gdjeY , gdjeZ = obradi_trans ( radnaPozicija , dX , dY , dZ , Vx , Vz )   
      mc.setBlock(gdjeX , gdjeY , gdjeZ , 66 , korektor)			#postavi blok obicna pruga

   return 1


def jump () :

   pos = mc.player.getTilePos()
   smjerRada = mc.player.getDirection ()	#uzmem kamo gledam

   Vx=0												#pocetne vrijednosti su nule
   Vz=0
   if abs (smjerRada.x) > abs (smjerRada.z): 		#nadje se dominanti smjer i spremi u vektor
      Vx=int (round(smjerRada.x))
   else:
      Vz=int ( round(smjerRada.z)    )
   mc.player.setPos(pos.x + 10 * Vx , pos.y  , pos.z + 10 *  Vz)
   time.sleep ( 1 )
   return 1

def kraj () :
   radnaPozicija = mc.player.getPos()		#gdje sam

   smjerRada = mc.player.getDirection ()	#uzmem kamo gledam
   smjerRada.y = round (radnaPozicija.y )		#radimo na levelu ispod
   smjerRada.x = round (smjerRada.x) 		# nabacimo cjelobrojni inkrement/dekrement
   smjerRada.z = round (smjerRada.z)
   Vx=0												#pocetne vrijednosti su nule
   Vz=0
   if abs (smjerRada.x) > abs (smjerRada.z): 		#nadje se dominanti smjer i spremi u vektor
      Vx=round(smjerRada.x)
   else:
      Vz=round(smjerRada.z)   
      
   if Vx == 0 :
      korektor = 0
   else :
      korektor = 1
   
   if  abs ( Vx )  != abs ( Vz ) :		# ne pod 45
      for dX in range ( 1 , 11 ) :
         for dY in range ( -1 , 0 )	:
            for dZ in range ( -1 , 2 )  :
               gdjeX , gdjeY , gdjeZ = obradi_trans ( radnaPozicija , dX , dY , dZ , Vx , Vz )   
               if ( dX == 1 ) and  ( dZ  != 0 ) :
                  mc.setBlock(gdjeX , gdjeY , gdjeZ , GLOWSTONE_BLOCK)
               else :
                  mc.setBlock(gdjeX , gdjeY , gdjeZ , STONE.id , 4 )			#postavi blok podloge - polished diorite

   dX = 1
   dY = 0 
   dZ = 0
   for br in range ( 8 ) :
      gdjeX , gdjeY , gdjeZ = obradi_trans ( radnaPozicija , dX , dY , dZ , Vx , Vz )   
      mc.setBlock(gdjeX , gdjeY , gdjeZ , 66 , korektor)			#postavi blok obicna pruga

   dX += 1
   gdjeX , gdjeY , gdjeZ = obradi_trans ( radnaPozicija , dX , dY , dZ , Vx , Vz )   
   mc.setBlock(gdjeX , gdjeY , gdjeZ , 27 , korektor)			#postavi blok elektificirano
   #mc.setBlock(gdjeX , gdjeY - 1 , gdjeZ + 1, GLOWSTONE_BLOCK)			#postavi blok
   #mc.setBlock(gdjeX , gdjeY - 1 , gdjeZ - 1, GLOWSTONE_BLOCK)			#postavi blok
   
   dX += 1
   gdjeX , gdjeY , gdjeZ = obradi_trans ( radnaPozicija , dX , dY , dZ , Vx , Vz )   
   mc.setBlock(gdjeX , gdjeY , gdjeZ , STONE.id , 2 )			#postavi blok odbojnik

   return 1



zachepi ()
pocetak ()
jump ()
for br in range (27) :
   zachepi ()
   segment ()
   jump ()
   mc.postToChat("--------------------------- %f ------------------------------------" % br )
kraj ()


