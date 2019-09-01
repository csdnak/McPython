#Testiranje NBT atributa

import time 
import sys
from crtanje import *		#tu je funkcija koju zovem

from mc import *			
mc = Minecraft() #inicijalizacija sustava za rad sa Minecraftom


"""
print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)
print '/give spavle axe'
"""

# origin ispred na sredini 
orMj = gdjeSam ()
orSm = gdjeGledam ()




playerPos = mc.player.getPos()



# +++++++++++++++++++++++++++++++++++++++++++++ GENERIRA Svinju

id = mc.spawnEntity('Pig', int ( playerPos.x + 1 ) ,int ( playerPos.y ), int ( playerPos.z ), "{NoAI:0,Type:2,Variant:3,Tame:1}")


