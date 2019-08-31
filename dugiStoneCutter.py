# ispred lika crta more baklji po tlu

import time
from mc import *  # import api-ja
from crtanje import *  # tu je funkcija koju zovem

mc = Minecraft()  # inicijalizacija sustava za rad sa Minecraftom
import time

zaObradu = [GRASS.id, SANDSTONE.id, SAND.id, STONE.id, DIRT.id, GRAVEL.id, COBBLESTONE.id, CLAY.id, GOLD_ORE.id,
            IRON_ORE.id, COAL_ORE.id, DIAMOND_ORE.id, OBSIDIAN.id, REDSTONE_ORE.id, LAPIS_LAZULI_ORE.id,
            129]  # 129 emerald

popis = dict()


def stoneCutter(orMj, orSm, dimenzije=5, visina=5):
    a = 1
    for dY in range(visina, -1, -1):
        mc.postToChat("Level: %s " % dY)
        for dZ in range(-3 - dY, 3 + dY):
            for dX in range(1, dimenzije + 1 + dY):
                a += 1

                gdje = rel2abs((int(orMj[0]), int(orMj[1]), int(orMj[2])), (dX, dZ, dY), orSm)
                # id = mc.spawnEntity('Minecart',  int (gdje [0])  ,int (gdje [1]) ,int (gdje [2]) , "{Type:0}" )
                # block = getBlockWithData( int (gdje [0])  ,int (gdje [1]) ,int (gdje [2]))
                myBlock = mc.getBlockWithData(int(gdje[0]), int(gdje[1]), int(gdje[2]))
                myBlock = mc.getBlockWithData(int(gdje[0]), int(gdje[1]), int(gdje[2]))

                if myBlock.id in (10, 11):  # makni lavu
                    mc.setBlock(int(gdje[0]), int(gdje[1]), int(gdje[2]), AIR.id, 0)
                if myBlock.id in zaObradu:
                    a = a + 1
                    # time.sleep ( 0.5 )
                    mc.setBlock(int(gdje[0]), int(gdje[1]), int(gdje[2]), AIR.id, 0)

                    if popis.has_key((myBlock.id, myBlock.data)):
                        popis[(myBlock.id, myBlock.data)] += 1
                    else:
                        popis[(myBlock.id, myBlock.data)] = 1





                        # time.sleep ( 0.5 )
                        # myId = mc.spawnEntity('Item', int (gdje [0])  ,int (gdje [1]) ,int (gdje [2] ) , sto )

    for bla in popis.keys():
        blok = bla[0]
        modifikacija = bla[1]
        # prijevodi:
        # diamond
        # 56 : 264,
        if bla[0] == 56:
            blok = 264
        # redstone
        # 73 : 331 ,
        if bla[0] == 73:
            blok = 331
        # lapis
        # 21 : 351 , 4
        if bla[0] == 21:
            blok = 351
            modifikacija = 4
        # emerald
        # 129 :  388
        if bla[0] == 129:
            blok = 388
            # coal COAL_ORE.id  263
        if bla[0] == COAL_ORE.id:
            blok = 263
            modifikacija = 0

        mc.postToChat("Key: %s %s " % (bla[0], bla[1]))
        mc.postToChat("Value: %s " % popis[bla])
        while popis[bla] > 0:
            if popis[bla] > 64:
                sto = ('{Item:{id:%s,Count:%s,Damage:%s}}' % (blok, 64, modifikacija))
            else:
                sto = ('{Item:{id:%s,Count:%s,Damage:%s}}' % (blok, popis[bla], modifikacija))

            mc.postToChat("XXX: %s  " % (sto))
            gdje = rel2abs(orMj, (0, 0, 3), orSm)
            time.sleep(6)
            myId = mc.spawnEntity('Item', int(gdje[0]), int(gdje[1]), int(gdje[2]), sto)
            popis[bla] -= 64

    mc.postToChat("Kraj :  XXXXXXXXXXXX")
    return 1


if __name__ == "__main__":  # direktan poziv
    orMj = gdjeSam()
    orSm = gdjeGledam()
    stoneCutter(orMj, orSm, dimenzije=35, visina=5)
    # bakljada (dimenzije = 200 , visina = 80)
