#ispred lika cisti trapezoidni lik i to samo blokove iz liste - NEDORADJENO HARDCODED LOSHE

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
   # nadji stepenice 
   stepenice_marker = 1
   udaljenost = 1 # ovdje pise koliko je daleko
   dZ = 0   # ne provjeravamo po lijevo desno
   while ( stepenice_marker == 1 ) :      #trazi se 156 QUARTZ
      
      gdjeX=radnaPozicija.x + Vx*( + udaljenost ) + Vz*dZ    		# pomak po x
      gdjeY=radnaPozicija.y + ( - udaljenost )						# pomak po y
      gdjeZ=radnaPozicija.z + Vx*dZ + Vz*( + udaljenost )			# pomak po Z
      if ( mc.getBlock ( gdjeX , gdjeY , gdjeZ ) != 156 ) :
         stepenice_marker = 0
         udaljenost -= 1
      udaljenost += 1
      
      mc.postToChat("udaljenost:  %f " % ( udaljenost  ) )
   
   #for dubina in range ( 2 ) : # ili ici jedan po jedan
   # postavi 3 nove stepenice
   
   for dZ in range ( -1 , 2 ) :
      if Vx == 1 :										#Korektor za smjer stepenica
         korektor = 0x1
      if Vx == -1 :
         korektor = 0x0
      if Vz == 1 :
         korektor = 0x3
      if Vz == -1 :
         korektor = 0x2
      gdjeX=radnaPozicija.x + Vx*(  udaljenost ) + Vz*dZ    		# pomak po x
      gdjeY=radnaPozicija.y + ( - udaljenost )						# pomak po y
      gdjeZ=radnaPozicija.z + Vx*dZ + Vz*( + udaljenost )			# pomak po Z
      mc.postToChat("Crtam stepenice"  )
      if mc.getBlock ( gdjeX , gdjeY , gdjeZ ) == 7 : # naletio na podlogu, bedrock
         mc.postToChat("!!!!!!!!!!!!!!!! B O T T O M  !!!!!!!!!!!!!!!!!!!!!!!!!!!!" )
         #return 1
      else :
         mc.setBlock ( gdjeX , gdjeY , gdjeZ , 156 , korektor)
      
     


   prosirenje = 0
   
   while udaljenost > -30 :
      # ochisti ispod i u nivou
      
      if  abs ( Vx )  != abs ( Vz ) :		# ne pod 45
         for dZ in  range( -4 - prosirenje, 5 + prosirenje ) :    		# prodji cijeli pravokutnik
            #mc.postToChat("Chischenje dZ: %f " % ( dZ  ) )
            for dY  in  range (  -0 , -2 , -1 ) : 
               #mc.postToChat("dY: %f " % ( dY  ) )
               for dX in  range ( -2 , 122 + prosirenje * 2 ) :
                  #mc.postToChat("dX: %f " % ( dX  ) )
                  if ( dZ != 0 ) or ( dX != 0 ) : 
                     if  1 == 1 : #( dX < 10 ) or ( dX > (  102 + prosirenje * 2 - 12 )  ) or ( dZ < ( -4 - prosirenje + 12  ) ) or ( dZ > ( 5 + prosirenje - 12 ) ) : # ne kontroliraj "praznu sredinu" obrnute piramide
                        gdjeX=radnaPozicija.x + Vx* ( dX + udaljenost ) +  + Vz*dZ    		# pomak po x
                        gdjeY=radnaPozicija.y + dY	- udaljenost					# pomak po y
                        gdjeZ=radnaPozicija.z + Vx*dZ + Vz*( dX + udaljenost )			# pomak po Z
                        if mc.getBlock ( gdjeX , gdjeY , gdjeZ ) in zaMaknutiOpasno :
                           mc.setBlock(gdjeX , gdjeY , gdjeZ , STONE.id , 2 )			#postavi blok   
      # napravi kanal
      
      mc.postToChat("Chischenje dZ: %f dY : %f" % ( dZ , dY ) )
      
      
      
      if  abs ( Vx )  != abs ( Vz ) :		# ne pod 45
         for dZ in  range( -3 - prosirenje ,4 + prosirenje ) :    		# prodji cijeli pravokutnik
            #mc.postToChat("dZ: %f " % ( dZ  ) )
            for dY  in  range (  0 , 1 ) : 
               #mc.postToChat("dY: %f " % ( dY  ) )
               for dX in  range ( 0 , 120 + prosirenje * 2 ) :
                  #mc.postToChat("dX: %f " % ( dX  ) )
                  if ( dZ != 0 ) or ( dX != 0 ) : 
                     gdjeX=radnaPozicija.x + Vx* ( dX + udaljenost ) +  + Vz*dZ    		# pomak po x
                     gdjeY=radnaPozicija.y + dY	- udaljenost					# pomak po y
                     gdjeZ=radnaPozicija.z + Vx*dZ + Vz*( dX + udaljenost )			# pomak po Z
                     """
                     ako ostavljamo rude
                     """
                     if mc.getBlock ( gdjeX , gdjeY , gdjeZ ) in zaMaknuti :
                        mc.setBlock(gdjeX , gdjeY , gdjeZ , AIR.id)			#postavi blok
                     
                     """
                     ako ne ostavljamo rude
                     
                     mc.setBlock(gdjeX , gdjeY , gdjeZ , AIR.id)			#postavi blok
                     """
                     
      mc.postToChat("Kopanje dZ: %f udaljenost : %f" % ( dZ , udaljenost ) )
      prosirenje += 1
      udaljenost -= 1
      
   mc.postToChat("K R A J  !!!!!!!!!!!!!!!!!!!!!!!!!!!!" )
   return 1
      
      
     
        

   
   
   
   
   
   
Kanal ()