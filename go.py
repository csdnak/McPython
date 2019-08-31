# teleportira 100 blokova "negdje"

from mc import * # ajmo probati ovaj import
import time

mc = Minecraft() #inicijalizacija sustava za rad sa Minecraftom

radnaPozicija = mc.player.getPos()		#gdje sam
mc.postToChat("Gdje sam X: %f Y: %f Z: %f " % ( radnaPozicija.x , radnaPozicija.y , radnaPozicija.z  ) )

smjerRada = mc.player.getDirection ()	#uzmem kamo gledam
radnaPozicija.y = radnaPozicija.y + 1		#radimo na levelu iznad
smjerRada.x = round (smjerRada.x) 		# nabacimo cjelobrojni inkrement/dekrement
smjerRada.z = round (smjerRada.z)


if  abs ( smjerRada.x )  != abs ( smjerRada.z ) :	#da ne ode pod 45
   radnaPozicija.x = smjerRada.x * 100
   radnaPozicija.z = smjerRada.z * 100
   #mc.postToChat("Kamo Idem X: %f Y: %f Z: %f " % ( radnaPozicija.x , radnaPozicija.y , radnaPozicija.z  ) )
   mc.player.setPos( int (radnaPozicija.x ), int ( radnaPozicija.y )  , int ( radnaPozicija.z ) ) 
   time.sleep(.3)
   mc.postToChat("Doshao X: %f Y: %f Z: %f " % ( radnaPozicija.x , radnaPozicija.y , radnaPozicija.z  ) )
            
	  
