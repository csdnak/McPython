#import time

from crtanje import *  # tu je funkcija koju zovem
#from mc import *  # import api-ja

zaObradu = [17, 162, 83, 81]  # 129 emerald

popis = dict()

sadrzaj = list ()

brojKutija = 0

def obradi_kutiju ( uJednaKutija, uBrojKutija, orMj, orSm):
    #mc.postToChat("%s . kutija: %s " % (uBrojKutija, uJednaKutija))
    
    sadrzaj=""
    sadrzaj += '{TransferCooldown:0,Items:[' 
    sadrzaj += uJednaKutija
    sadrzaj += '],id:"Chest",Lock:"",}'
    orMj = gdjeSam()
    orSm = gdjeGledam()
    polozaj = rel2abs ( orMj , ( -2 - 2 * uBrojKutija , 0 , 0  ) , orSm )
    mc.setBlockWithNBT(polozaj,54,1, sadrzaj )
    

def puniKutije(orMj, orSm, dimenzije=5, visina=25):
    # Ovo kupi rude
    jednaKutija = ''
    brojKutija = 0
    a = 1
    for dY in range( visina, -4, -1):
        mc.postToChat("Level: %s " % dY)
        for dZ in range(-dimenzije, dimenzije  + 1):
            for dX in range(-dimenzije, dimenzije  + 1):
                a += 1
                gdje = rel2abs((int(orMj[0]), int(orMj[1]), int(orMj[2])), (dX, dZ, dY), orSm)
                myBlock = mc.getBlockWithData(int(gdje[0]), int(gdje[1]), int(gdje[2]))
                if myBlock.id in zaObradu:
                    a = a + 1
                    mc.setBlock(int(gdje[0]), int(gdje[1]), int(gdje[2]), AIR.id, 0)  # stavlja rupu    
                    myBlock.data = myBlock.data & 3
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
        # trska
        # 83, 338,
        if bla[0] == 83:
            blok = 338


        while popis[bla] > 0:
            if popis[bla] > 64:
                count = 64
            else:
                count = popis[bla]
            popis[bla] -= 64

            #ovo trebamo dobiti 2:{Slot:2b,id:"3",Count:64b,Damage:0s,},
            mali_string = '{Slot:%sb,id:"%s",Count:%sb,Damage:%ss,},' % (  brojalica, blok, count, modifikacija )
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
    puniKutije(orMj, orSm, dimenzije=6, visina=25)
    mc.postToChat("The End")
