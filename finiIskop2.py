
#import time

from crtanje import *  # tu je funkcija koju zovem
#from mc import *  # import api-ja

zaObradu = [STONE.id, DIRT.id, GRASS.id, SANDSTONE.id, 12, GRAVEL.id, COBBLESTONE.id, CLAY.id, GOLD_ORE.id,
            IRON_ORE.id, COAL_ORE.id, DIAMOND_ORE.id, OBSIDIAN.id, REDSTONE_ORE.id, LAPIS_LAZULI_ORE.id,
            129, 179, 172, 159, 87, 153,  88, 213, 5 , 85 , 188, 189, 190, 191, 192, 30, 66 ]  # 129 emerald




def iskop(orMj, orSm, dimenzije=30, visina=5):      #ovdje se definira oblik iskopa
    popis = dict()
    brojKutija = 0
    # Ovo kupi rude
    if orMj[1] < 0:
        orMj[1] -= 1
    if orMj[0] < 0:
        orMj[0] -= 1
        

    a = 1
    for dY in range(0,visina):
        mc.postToChat("Level: %s " % dY)
        odakle = -2
        dokle = 3
        if dY == visina - 1 :
            odakle = -1
            dokle = 2
        for dZ in range( odakle , dokle ):
            for dX in range(1, dimenzije  + 1):
                a += 1

                gdje = rel2abs((int(orMj[0]), int(orMj[1]), int(orMj[2])), (dX, dZ, dY), orSm)
                myBlock = mc.getBlockWithData(int(gdje[0]), int(gdje[1]), int(gdje[2]))
                if myBlock.id in (8, 9, 10, 11):  # makni lavu i vodu
                    mc.setBlock(int(gdje[0]), int(gdje[1]), int(gdje[2]), AIR.id, 0)
                if myBlock.id in zaObradu:
                    a = a + 1
                    mc.setBlock(int(gdje[0]), int(gdje[1]), int(gdje[2]), AIR.id, 0)  # stavlja rupu     
                    if ((myBlock.id, myBlock.data)) in popis:  # puni popis
                        popis[(myBlock.id, myBlock.data)] += 1
                    else:
                        popis[(myBlock.id, myBlock.data)] = 1
    slozi_NBT_za_kutije ( orMj, orSm , popis ) # poziva pravljenje i punjenje kutija sa materijalom koji je iskopao



 

    
# iskop fazoniranog tunela ispred i puni kutije iza    
    
if __name__ == "__main__":  # direktan poziv
    orMj = gdjeSam()
    orSm = gdjeGledam()
    iskop(orMj, orSm)
    mc.postToChat("The End")