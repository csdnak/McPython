#Testiranje NBT atributa

import time 
import sys
from crtanje import *		#tu je funkcija koju zovem

from mc import *			
mc = Minecraft() #inicijalizacija sustava za rad sa Minecraftom


"""
Pazi
http://minecraft.gamepedia.com/Chunk_format#Villager
http://minecraft.gamepedia.com/Villager#Professions_and_careers
"""

# origin ispred na sredini 
orMj = gdjeSam ()
orSm = gdjeGledam ()




playerPos = mc.player.getPos()



# +++++++++++++++++++++++++++++++++++++++++++++ GENERIRA MULU

id = mc.spawnEntity('Villager', int ( playerPos.x + 2 ) ,int ( playerPos.y ), int ( playerPos.z ), "{ Profession:0,Career:1}")


