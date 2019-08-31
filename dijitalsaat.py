import datetime
import time

import fonts
import text
from mine import *

foreground = block.SEA_LANTERN
background = block.AIR

mc = Minecraft()
pos = mc.player.getTilePos()
forward = text.angleToTextDirection(mc.player.getRotation())

prevTime = ""

while True:
    curTime = datetime.datetime.now().strftime("%I:%M:%S %p")
    if curTime[0] == '0':
        curTime = ' ' + curTime[1:]
    if prevTime != curTime:
        for i in range(len(curTime)):
            if i >= len(prevTime) or prevTime[i] != curTime[i]:
                text.drawText(mc, fonts.FONTS['8x8'], pos + forward * (8 * i), forward, Vec3(0, 1, 0), curTime[i:],
                              foreground, background)
                break
        prevTime = curTime
    time.sleep(0.1)
