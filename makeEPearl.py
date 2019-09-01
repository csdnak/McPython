# Testiranje NBT atributa

from crtanje import *  # tu je funkcija koju zovem

from mc import *

mc = Minecraft()  # inicijalizacija sustava za rad sa Minecraftom

# origin ispred na sredini 
orMj = gdjeSam()
orSm = gdjeGledam()

playerPos = mc.player.getPos()
# +++++++++++++++++++++++++++++++++++++++++++++ GENERIRA XP orb
id = mc.spawnEntity('ThrownEnderpearl', int(playerPos.x + 2), int(playerPos.y + 2), int(playerPos.z),"{NoGravity:1,Type:2,Variant:3,Tame:1}")
