# teleportira na pocetak

from mc import * # ajmo probati ovaj import
import time

mc = Minecraft() #inicijalizacija sustava za rad sa Minecraftom

radnaPozicija = mc.player.getPos()		#gdje sam
mc.postToChat("Gdje sam X: %f Y: %f Z: %f " % ( radnaPozicija.x , radnaPozicija.y , radnaPozicija.z  ) )

mc.player.setPos( 0 , 0  , 8 ) 
time.sleep(3.0)

mc.postToChat("GOTOVO !!! "  )