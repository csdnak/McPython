#ispod lika radi piramidu

from mc import * #import api-ja
mc = Minecraft() #inicijalizacija sustava za rad sa Minecraftom

def piramida ():
   """
   funkcija za crtanje piramide neposredno ispod lika do BEDROCK-a
   """
   #gdje sam
   radnaPozicija = mc.player.getPos()	
   radnaPozicija.y -= 1
   #mc.postToChat("vX: %f vZ: %f " % ( Vx , Vz  ) )
   sirina = 0		#pocetna sirina je 0
   #crtanje
   mc.setBlock(radnaPozicija.x  , radnaPozicija.y  , radnaPozicija.z , GOLD_BLOCK)
   while 1 :		# ne pod 45
      sirina += 1
      Blok = SANDSTONE
      #QUARTZ_BLOCK
      if (sirina % 12345) == 0 :     #placeholder
         Blok = STONE
      elif (sirina % 5 ) == 0  :     # svaki peti red
         Blok = SANDSTONE
         #DIAMOND_BLOCK
      for dZ in  range( -sirina , sirina +1) :    		# prodji chep
         mc.setBlock(radnaPozicija.x + sirina , radnaPozicija.y - sirina , radnaPozicija.z + dZ , Blok)			#postavi blok   
         mc.setBlock(radnaPozicija.x - sirina , radnaPozicija.y - sirina , radnaPozicija.z + dZ , Blok)			#postavi blok   
         mc.setBlock(radnaPozicija.x + dZ , radnaPozicija.y - sirina , radnaPozicija.z + sirina , Blok)			#postavi blok   
         mc.setBlock(radnaPozicija.x - dZ , radnaPozicija.y - sirina , radnaPozicija.z - sirina , Blok)			#postavi blok   
         if mc.getBlock ( radnaPozicija.x , radnaPozicija.y - sirina , radnaPozicija.z ) == BEDROCK.id :                # kad dodje do podloge zavrsi
            return 1
   return 1
   
piramida ()


         