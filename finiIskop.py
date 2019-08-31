
#import time

from crtanje import *  # tu je funkcija koju zovem
#from mc import *  # import api-ja

zaObradu = [STONE.id, DIRT.id, GRASS.id, SANDSTONE.id, 12, GRAVEL.id, COBBLESTONE.id, CLAY.id, GOLD_ORE.id,
            IRON_ORE.id, COAL_ORE.id, DIAMOND_ORE.id, OBSIDIAN.id, REDSTONE_ORE.id, LAPIS_LAZULI_ORE.id,
            129, 179, 172, 159, 87, 153,  88, 213, 5 , 85 , 188, 189, 190, 191, 192, 30, 66 ]  # 129 emerald

popis = dict()

sadrzaj = list ()

brojKutija = 0

def obradi_kutiju ( uJednaKutija, uBrojKutija, orMj, orSm):
    #mc.postToChat("%s . kutija: %s " % (uBrojKutija, uJednaKutija))
    
    sadrzaj=""
    sadrzaj += '{Items:[' 
    sadrzaj += uJednaKutija
    sadrzaj += '],id:"minecraft:chest",Lock:"",}'
    orMj = gdjeSam()
    orSm = gdjeGledam()
    polozaj = rel2abs ( orMj , ( -2 - 2 * uBrojKutija , 0 , 0  ) , orSm )
    mc.setBlockWithNBT(polozaj,54,1, sadrzaj )
    

def iskop(orMj, orSm, dimenzije=15, visina=7):
    # Ovo kupi rude
    if orMj[1] < 0:
        orMj[1] -= 1
    if orMj[0] < 0:
        orMj[0] -= 1
        
    jednaKutija = ''
    brojKutija = 0
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


    # slaze stringove
    brojalica = 0
    mali_string = "" #jedan element
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

        if bla[0] == 153:   #nether quartz
            blok = 406
            modifikacija = 0
        # cobweb
        if bla[0] == 30:
            blok = 287
            modifikacija = 0            
        # rail
        if bla[0] == 66:
            blok = 66
            modifikacija = 0   
            
        while popis[bla] > 0:
            if popis[bla] > 64:
                count = 64
            else:
                count = popis[bla]
            popis[bla] -= 64

            #ovo trebamo dobiti 2:{Slot:2b,id:"3",Count:64b,Damage:0s,},

            mali_string = '{Slot:%sb,id:"%s",Count:%sb,Damage:%ss,},' % ( brojalica, blok, count, modifikacija )

            nesto = jednaKutija
            jednaKutija= nesto + mali_string
            brojalica += 1
            if brojalica > 25:
                obradi_kutiju (  jednaKutija, brojKutija, orMj, orSm )
                brojalica = 0
                jednaKutija = ""
                brojKutija += 1

    obradi_kutiju( jednaKutija, brojKutija, orMj, orSm)


    # crta kutije

if __name__ == "__main__":  # direktan poziv
    orMj = gdjeSam()
    orSm = gdjeGledam()
    iskop(orMj, orSm)
    mc.postToChat("The End")