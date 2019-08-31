import fonts
import text
from mine import *

mc = Minecraft()
pos = mc.player.getTilePos()
forward = text.angleToTextDirection(mc.player.getRotation())

foreground = block.BEDROCK
background = block.AIR

text.drawText(mc, fonts.FONTS['bigfoot'], pos + forward, forward, Vec3(0, 1, 0), "EMIR", foreground, background)
# text.drawText(mc, fonts.FONTS['8x8'], pos + forward, forward, Vec3(0, 1, 0), "CEM", foreground, background)
