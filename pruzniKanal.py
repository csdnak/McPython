#ispred lika cisti trapezoidni lik i to samo blokove iz liste - samo za prugu

from mc import * #import api-ja
mc = Minecraft() #inicijalizacija sustava za rad sa Minecraftom

def Kanal ():
   """
   ispred lika cisti trapezoidni lik i to samo blokove iz liste
   """
   zaMaknuti = [ SANDSTONE.id , SAND.id , STONE.id , DIRT.id , GRAVEL.id , GRASS.id , GRASS_TALL.id , COBBLESTONE.id , WATER_FLOWING.id , WATER_STATIONARY.id , LAVA_FLOWING.id , LAVA_STATIONARY.id , 17 , 162 ] # 17 , 162 wood
   zaMaknutiOpasno = [ WATER_FLOWING.id , WATER_STATIONARY.id , LAVA_FLOWING.id , LAVA_STATIONARY.id , SAND.id , GRAVEL.id ] # Dodani shljunak i pjesak jer padanja sve poremete
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

   udaljenost = 0 # ovdje pise koliko je daleko
   prosirenje = 5 # counter , pravo prosirenje je za 2 manje
   
   
   duzina_kanala = 260
   granica = 12
   
   if  abs ( Vx )  != abs ( Vz ) :		# ne pod 45
      for dY in range ( 0  ,40 ) :
         mc.postToChat("Level %f" % dY )
         for dZ in range (  - dY - prosirenje  , dY + prosirenje + 1  ) : 
            for dX in range ( 1 + duzina_kanala + 2 ) :
               gdjeX=radnaPozicija.x + Vx* ( dX  ) +  Vz*dZ # pomak po x
               gdjeY=radnaPozicija.y + dY						   # pomak po y
               gdjeZ=radnaPozicija.z + Vx*dZ + Vz*( dX )		# pomak po Z
               if abs ( ( dZ )  ) < granica + prosirenje : # ????
                  kojiBlok = mc.getBlock ( gdjeX , gdjeY , gdjeZ )
                  if kojiBlok in zaMaknutiOpasno :
                     mc.setBlock(gdjeX , gdjeY , gdjeZ , STONE.id , 2 )			#postavi blok 
                  # Nebitno za vlak ??
                  gornjiBlok = mc.getBlock ( gdjeX , gdjeY + 1 , gdjeZ )      # provjeri i sredi i blok "iznad" da stalno nepadaju
                  if gornjiBlok in zaMaknutiOpasno :
                     mc.setBlock(gdjeX , gdjeY + 1 , gdjeZ , STONE.id , 2 )			#postavi blok 
                  # """
                     
                  if  abs ( dZ ) <  ( dY - 2 + prosirenje  ) : 
                     if ( abs  ( dZ )  < 11 + prosirenje ) :
                        if dX in range ( 1 , duzina_kanala - 2 ) :
                        ###(abs ( ( dZ )  ) < granica ) and ( ( dY - abs ( dZ )   ) > 3  )  and  ( dX in range ( 1 , duzina_kanala - 2 )): # u uzem dijelu chisti
                           if kojiBlok in zaMaknuti :
                              mc.setBlock(gdjeX , gdjeY , gdjeZ , AIR.id)			#postavi blok
                  
         
         
   
   
   mc.postToChat("K R A J  !!!!!!!!!!!!!!!!!!!!!!!!!!!!" )
   return 1
      
      
     
    
   
Kanal ()