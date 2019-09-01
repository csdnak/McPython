import time

from crtanje import *  # tu je funkcija koju zovem
from mc import *  # import api-ja

zaObradu = [DIAMOND_ORE.id,
            129]  # 129 emerald vreti SANDSTONE.id,

popis = dict()

sadrzaj = list ()

brojKutija = 0


def obradi_kutiju ( uJednaKutija,uBrojKutija):
    #mc.postToChat("%s . kutija: %s " % (uBrojKutija, uJednaKutija))
    
    sadrzaj=""
    sadrzaj += '{Items:[' 
    sadrzaj += uJednaKutija
    sadrzaj += '],id:"Hopper",Lock:"",}'
    orMj = gdjeSam()
    orSm = gdjeGledam()
    polozaj = rel2abs ( orMj , ( 2 + 2 * uBrojKutija , 0 , 0  ) , orSm )
    
    mc.setBlockWithNBT(polozaj,54,1, sadrzaj )
    

def puniKutije(orMj, orSm, dimenzije=5, visina=5):
    # Ovo kupi rude
    jednaKutija = ''
    brojKutija = 0
    a = 1
    for dY in range(visina, -1, -1):
        mc.postToChat("Level: %s " % dY)
        time.sleep(1)
        for dZ in range(-dimenzije - dY, dimenzije + dY):
            for dX in range(-dimenzije - 1, dimenzije + 1 + dY):
                a += 1
                gdje = rel2abs((int(orMj[0]), int(orMj[1]), int(orMj[2])), (dX, dZ, dY), orSm)
                myBlock = mc.getBlockWithData(int(gdje[0]), int(gdje[1]), int(gdje[2]))
                if myBlock.id in (             8, 9, 10, 11):  # makni lavu
                    mc.setBlock(int(gdje[0]), int(gdje[1]), int(gdje[2]), AIR.id, 0)
                if myBlock.id in zaObradu:
                    a = a + 1
                    mc.setBlock(int(gdje[0]), int(gdje[1]), int(gdje[2]), AIR.id, 0)  # stavlja rupu     
                    if popis.has_key((myBlock.id, myBlock.data)):  # puni popis
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

        #mc.postToChat("Key: %s %s " % (bla[0], bla[1]))
        #mc.postToChat("Value popis bla: %s " % popis[bla])

        while popis[bla] > 0:
            #mc.postToChat("Value popis bla: %s " % popis[bla])
            if popis[bla] > 64:
                count = 64
            else:
                count = popis[bla]
                
            popis[bla] -= 64
            #ovo trebamo dobiti '2:{Slot:2b,id:3,Count:64b,Damage:0s,},',
            mali_string = "'%s:{Slot:%sb,id:%s,Count:%sb,Damage:%ss,},'," % ( brojalica, brojalica,blok, count, modifikacija )
            #mc.postToChat("Mali string: %s " % mali_string )
            nesto = jednaKutija
            jednaKutija= nesto + mali_string
            brojalica += 1
            if brojalica > 25:
                obradi_kutiju (  jednaKutija ,brojKutija )
                brojalica = 0
                jednaKutija = ""
                brojKutija += 1

    obradi_kutiju(jednaKutija,brojKutija)


    # crta kutije


if __name__ == "__main__":  # direktan poziv
    orMj = gdjeSam()
    orSm = gdjeGledam()
    puniKutije(orMj, orSm, dimenzije=220, visina=6)
