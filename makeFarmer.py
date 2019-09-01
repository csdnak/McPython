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
def makeFarmer ( ):
# origin ispred na sredini 
   orMj = gdjeSam ()
   orSm = gdjeGledam ()
   playerPos = mc.player.getPos()
   # +++++++++++++++++++++++++++++++++++++++++++++ GENERIRA 
   # full farmer
   #id = mc.spawnEntity('Villager',  int( playerPos.x + 4 ) , int( playerPos.y ),  int( playerPos.z ), "{Profession:0,Career:1,Inventory:[0:{id:1,Count:52b,Damage:4s,},1:{id:1,Count:55b,Damage:0s,},2:{id:2,Count:55b,Damage:0s,},3:{id:2,Count:55b,Damage:0s,},4:{id:2,Count:55b,Damage:0s,},5:{id:1,Count:52b,Damage:4s,},6:{id:1,Count:55b,Damage:0s,},]}")
   #id = mc.spawnEntity('Villager',  int( playerPos.x + 4 ) , int( playerPos.y ),  int( playerPos.z -1 ), "{Profession:2,Career:1}")
   #id = mc.spawnEntity('Villager',  int( playerPos.x  ) , int( playerPos.y ),  int( playerPos.z -7), "{Profession:0,Career:1}")
   id = mc.spawnEntity('Villager',  int( playerPos.x  ) , int( playerPos.y ),  int( playerPos.z -2), "{Profession:0,Career:1}")
   #id = mc.spawnEntity('Villager',  int( playerPos.x + 4 ) , int( playerPos.y ),  int( playerPos.z +3), "{Profession:2,Career:1}")



makeFarmer ( )