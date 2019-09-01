#ispred lika pravi stepenice prema dolje za postepeni silazak BLOCK-SLATE umjesto stepenica do badrock i stavlja baklje


from mc import * #import api-ja
mc = Minecraft() #inicijalizacija sustava za rad sa Minecraftom

def postepeniSilazak ():
   """
   ispred lika pravi stepenice prema dolje za postepeni silazak BLOCK-SLATE umjesto stepenica do badrock i stavlja baklje
   okolo uklanja opasne blokove
   """
   #priprema
   zaMaknutiOpasno = [ WATER_FLOWING.id , WATER_STATIONARY.id , LAVA_FLOWING.id , LAVA_STATIONARY.id , SAND.id , GRAVEL.id ] # Dodani shljunak i pjesak jer padanje sve poremete
   smjer = [
   [ [0,0] ,[4,3] ,[0,0] ],
   [ [2,1] ,[0,0] ,[1,2] ],
   [ [0,0] ,[3,4] ,[0,0] ],
   ]
   #gdje sam
   radnaPozicija = mc.player.getPos()		
   #kamo gledam
   smjerRada = mc.player.getDirection ()			#uzmem kamo gledam
   #smjer gledanja radi preglednosti spremimo u "vektor""
   Vx=0												#pocetne vrijednosti su nule
   Vz=0
   if abs (smjerRada.x) > abs (smjerRada.z): 		#nadje se dominanti smjer i spremi u vektor
      Vx=int(round(smjerRada.x))
   else:
      Vz=int(round(smjerRada.z))
   if Vx == 1 :										#Korektor za smjer stepenica
      korektor = 0x1
   if Vx == -1 :
      korektor = 0x0
   if Vz == 1 :
      korektor = 0x3
   if Vz == -1 :
      korektor = 0x2

   #crtanje
                 
   
   if  abs ( Vx )  != abs ( Vz ) :		# ne pod 45
      while  1 :			# dok je iznad baznog
         radnaPozicija.y -= 1					# pomak dolje
         radnaPozicija.x += ( 2*Vx*1  + 2*Vz*0 ) 	    # pomak relativni "naprijed"
         radnaPozicija.z += ( 2*Vx*0  + 2*Vz*1 ) 	    # pomak relativni "naprijed"		 
         mc.postToChat("X: %f Y: %f Z: %f " % ( radnaPozicija.x , radnaPozicija.y , radnaPozicija.z  ) )
         
         for dZ in  range( -3 , 5 ) :    		# shirina
            for dY  in  range( -1 , 8 ) :		#visinat
               for dX in range ( 0 , 4 ) :   
                  gdjeX=radnaPozicija.x + Vx*dX + Vz*dZ    		# pomak po x
                  gdjeY=radnaPozicija.y + dY
                  gdjeZ=radnaPozicija.z + Vx*dZ + Vz*dX			# pomak po Z
                  if mc.getBlock ( gdjeX , gdjeY , gdjeZ ) in zaMaknutiOpasno :
                     mc.setBlock(gdjeX , gdjeY , gdjeZ , STONE.id , 2 )			#postavi blok   
         
         for dZ in  range( -1 , 2 ) :    		# shirina
            for dY  in  range( 0 , 6 ) :		#visinat
               for dX in range ( 1 , 3 ) :   
                  gdjeX=radnaPozicija.x + Vx*dX + Vz*dZ    		# pomak po x
                  gdjeY=radnaPozicija.y + dY
                  gdjeZ=radnaPozicija.z + Vx*dZ + Vz*dX			# pomak po Z
                  if dY == 0 :	#dolje stepenicu staviti
                     if mc.getBlock( gdjeX , gdjeY , gdjeZ ) != BEDROCK.id	:				#ako nije kraj
                        if dX == 1 :
                           mc.setBlock( gdjeX , gdjeY , gdjeZ , 155  )							#postavi blok						
                        else :                        
                           mc.setBlock( gdjeX , gdjeY , gdjeZ , 44 ,7  )						#postavi slab												
                     else :																	# ako naleti na dno onda kraj
                        return 1
                  else :
                     mc.setBlock(gdjeX , gdjeY , gdjeZ , AIR)
                  if ( dY == 4 ) and (  dZ == 1 ):
                     mc.setBlock( gdjeX , gdjeY , gdjeZ ,   50 ,( smjer [Vx+1][Vz+1] ) [1] )        # baklje na desnoj strani
                  if ( dY == 4 ) and ( dZ == -1  ):
                     mc.setBlock( gdjeX , gdjeY , gdjeZ ,  50  , ( smjer [Vx+1][Vz+1] ) [0]  )        # baklje na lijevoj strani
                  #mc.postToChat("gdjeX: %f gdjeY: %f gdjeZ: %f " % ( gdjeX , gdjeY , gdjeZ  ) )
   #mc.postToChat("X: %f Y: %f Z: %f " % ( radnaPozicija.x , radnaPozicija.y , radnaPozicija.z  ) )
   return 1
   
postepeniSilazak ()

