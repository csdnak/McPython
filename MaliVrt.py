# NE RADI - ERROR  pravi stazu od zlatnih blokova dugacku 2000 siroku 3

from mc import * # ajmo probati ovaj import

mc = Minecraft() #inicijalizacija sustava za rad sa Minecraftom

radnaPozicija = mc.player.getPos()		#gdje sam

smjerRada = mc.player.getDirection ()	#uzmem kamo gledam
smjerRada.y = radnaPozicija.y - 1		#radimo na levelu ispod
smjerRada.x = round (smjerRada.x) 		# nabacimo cjelobrojni inkrement/dekrement
smjerRada.z = round (smjerRada.z)

korektor=0							#korektor za postavljanje baklj i pravom smijeru
if smjerRada.x:
   korektor=2			

if  abs ( smjerRada.x )  != abs ( smjerRada.z ) :	#da ne ode pod 45
   for brojalica in  range (2000) :			#duzina 2000
      radnaPozicija.x += smjerRada.x
      radnaPozicija.z += smjerRada.z
      mc.setBlock(radnaPozicija.x , smjerRada.y , radnaPozicija.z , GOLD_BLOCK) #sredisnji blok
      mc.setBlock(radnaPozicija.x + abs ( smjerRada.z ), smjerRada.y , radnaPozicija.z + abs ( smjerRada.x ) , GOLD_BLOCK)                  #diferencijalno prosirenje staze
      mc.setBlock(radnaPozicija.x - abs ( smjerRada.z ), smjerRada.y , radnaPozicija.z - abs ( smjerRada.x ) , GOLD_BLOCK)                  #diferencijalno prosirenje staze
      for dizalica in range ( 1,4 ):			# napravi tunel
         mc.setBlock(radnaPozicija.x , smjerRada.y + dizalica , radnaPozicija.z , AIR) #sredisnji blok
         mc.setBlock(radnaPozicija.x + abs ( smjerRada.z ), smjerRada.y + dizalica , radnaPozicija.z + abs ( smjerRada.x ) , AIR)                  #diferencijalno prosirenje staze
         mc.setBlock(radnaPozicija.x - abs ( smjerRada.z ), smjerRada.y + dizalica , radnaPozicija.z - abs ( smjerRada.x ) , AIR)                  #diferencijalno prosirenje staze
         if ( dizalica == 3 ) and ( not ( brojalica % 4 ) )  :                                                                      # smjer nort southw
            mc.setBlock(radnaPozicija.x - abs ( smjerRada.z   ), smjerRada.y + dizalica , radnaPozicija.z - abs ( smjerRada.x  ) , 50  , 1 + korektor )        # baklje na desnoj strani
            mc.setBlock(radnaPozicija.x + abs ( smjerRada.z   ), smjerRada.y + dizalica , radnaPozicija.z + abs ( smjerRada.x  ) , 50 ,  2 + korektor )        # baklje na lijevoj strani
			
            
	  
