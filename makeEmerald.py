# Testiranje NBT atributa

from crtanje import *  # tu je funkcija koju zovem

from mc import *

mc = Minecraft()  # inicijalizacija sustava za rad sa Minecraftom

# origin ispred na sredini 
orMj = gdjeSam()
orSm = gdjeGledam()

playerPos = mc.player.getPos()


mc.setBlocks ( int(playerPos.x + 2), int(playerPos.y + 2), int(playerPos.z), int(playerPos.x + 7), int(playerPos.y + 2), int(playerPos.z) , 129 , 0 )