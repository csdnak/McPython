import random

from mine import *

mc = Minecraft()

x, y, z = mc.player.getPos()


kac_tane = 3
for t in range(0, kac_tane):
    ne = random.choice([block.DIAMOND_BLOCK, block.CACTUS, block.COAL_BLOCK, block.COMMAND_BLOCK, block.ACACIA_WOOD, block.BEDROCK])

    mc.setBlock(x, y + t, z, ne)
