import mcpi.minecraft as minecraft
import mcpi.block as block
 
mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()
 
x = pos.x
y = pos.y
z = pos.z
 
width = 100 #第一层边长
high = 0 
 
while True:
    for a in range(width):
        for b in range(width):
            mc.setBlock(x+a+high, pos.y+high, pos.z+b+high, block.GOLD_BLOCK.id)
 
    width-=2
    high+=1
 
    if width <= 0:
        break
