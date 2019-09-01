import random

from mine import *

mc = Minecraft()

x, y, z = mc.player.getPos()

ne = random.choice([block.DIAMOND_BLOCK, block.CACTUS, block.COAL_BLOCK, block.COMMAND_BLOCK, block.ACACIA_WOOD, block.BEDROCK])

mc.setBlock(x, y - 1, z, ne)
mc.setBlock(x, y, z, ne)
mc.setBlock(x, y + 1, z, ne)
