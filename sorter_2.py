import time

from crtanje import *  # tu je funkcija koju zovem
from mc import *


def modul_kraj2(orMj, orSm, iX=0, iZ=0, iY=0, materijal=98, dv=0, kutija="kutija"):
    dX = 0
    orMj = premjesti_origin(orMj, iX, iZ, iY, orSm)  # mice gdje treba, crta ispred toon-a

    if (kutija == "kutija"):
        kmat = 54
    else:
        kmat = 146
    crtaj_hopper(orMj, [3, 0, 4], [3, 0, 4], orSm, "lijevo")  # hopper razvodnik
    crtaj_kutiju(orMj, [1, 0, 0], [2, 0, 3], orSm, rel_smjer="meni", blok_id=kmat)
    crtaj_hopper(orMj, [3, 0, 3], [3, 0, 0], orSm, "meni")  # hopper iza kutije
    crtaj_comparator(orMj, [0, 0, 0], [0, 0, 0], orSm, rel_smjer="meni")  # ima li stvari u kutiji


def modul_sorter2(orMj, orSm, iX=0, iZ=0, iY=0, materijal=98, dv=0, kutija="kutija", crtaj_kutije="da"):
    orMj = premjesti_origin(orMj, iX, iZ, iY, orSm)  # mice gdje treba, crta ispred kutija
    if crtaj_kutije == "da":
        if (kutija == "kutija"):
            kmat = 54
        else:
            kmat = 146
        crtaj_kutiju(orMj, [3, 0, 2], [4, 0, 2], orSm, rel_smjer="desno", blok_id=kmat)
        crtaj_hopper(orMj, [3, 0, 1], [3, 0, 0], orSm, "meni")  # hopper ispod kutije
        crtaj_kutiju(orMj, [1, 0, 0], [2, 0, 1], orSm, rel_smjer="desno", blok_id=kmat)
        crtaj_stepenice(orMj, (1, 0, 2), (1, 0, 2), orSm, blok_id=109, rel_smjer="odmene", gore_dolje="da")
        crtaj_kvadar(orMj, (1, 0 , 3), (1, 0 , 3), orSm, 44, 0) #slabstone iznad stepenice
        crtaj_comparator(orMj, [0, 0, 0], [0, 0, 0], orSm, rel_smjer="meni")  # ima li stvari u kutiji
    crtaj_kvadar(orMj, [8, 0, 0], [8, 0, 0], orSm, materijal, 2)  # doljnji blok
    crtaj_kvadar(orMj, [7, 0, 1], [9, 0, 1], orSm, materijal, 2)  # srednji blokovi
    crtaj_kvadar(orMj, [6, 0, 2], [8, 0, 2], orSm, materijal, 2)  # gornji blokovi

    crtaj_repeater(orMj, [8, 0, 1], [8, 0, 1], orSm, rel_smjer="meni")
    crtaj_redstonetorch(orMj, [6, 0, 1], orSm, "meni")

    crtaj_redstonedust(orMj, [9, 0, 2], [9, 0, 2], orSm)

    crtaj_redstonedust(orMj, [8, 0, 3], [7, 0, 3], orSm)
    crtaj_comparator(orMj, [6, 0, 3], [6, 0, 3], orSm, rel_smjer="odmene")

    crtaj_hopper(orMj, [5, 0, 4], [5, 0, 4], orSm, "desno")  # gornji
    crtaj_kvadar(orMj, (5, 0, 5), (5, 0, 5), orSm, 44, 0)

    sto = '{Items:[{Slot:0b,id:"minecraft:item_frame",Count:4b,Damage:0s,},{Slot:1b,id:"minecraft:flower_pot",Count:1b,Damage:0s,tag:{display:{Name:"Bla Filler"}}},{Slot:2b,id:"minecraft:flower_pot",Count:1b,Damage:0s,tag:{display:{Name:"Bla Filler"}}},{Slot:3b,id:"minecraft:flower_pot",Count:1b,Damage:0s,tag:{display:{Name:"Bla Filler"}}},{Slot:4b,id:"minecraft:flower_pot",Count:1b,Damage:0s,tag:{display:{Name:"Bla Filler"}}},],id:"minecraft:hopper",Lock:"",}'
    bla = rel2abs(orMj, (5, 0, 3), orSm)
    time.sleep(0.1)
    mc.setBlockWithNBT(bla, 154, smjer_hoppera(orSm, "meni"), sto)  # hopper gleda meni puko NBT proba novi forge
    # crtaj_hopper(orMj, [5, 0, 3], [5, 0, 3], orSm, "meni")  # smrdani selektor
    crtaj_hopper(orMj, [5, 0, 2], [5, 0, 2], orSm, "meni")  # doljnji


def sorter2(orMj, orSm, iX=0, iZ=0, iY=0):
    orMj = premjesti_origin(orMj, iX, iZ, iY, orSm)  # mice gdje treba

    # crtaj_kvadar ( orMj , ( -5 , -32 , 0 ),( 50 , 32 , 8) , orSm , 0 , 0 ) #clear the deck
    # lijevi zid
    orSm = ortUlijevo(orSm)
    for br in range(0, 65):
        if br % 2 == 1:
            koja_kutija = "kutija"
        else:
            koja_kutija = "druga_kutija"

        modul_sorter2(orMj, orSm, iX=15, iZ=br, iY=0, materijal=98, dv=0, kutija=koja_kutija, crtaj_kutije="da")
    crtaj_hopper(orMj, (20, 65, 4), (20, 70, 4), orSm, "desno")
    crtaj_kvadar(orMj, (20, 65, 5), (20, 70, 5), orSm, 44, 0)

    # zadnji zid
    orSm = ortUdesno(orSm)
    for br in range(-13, 14):
        if br % 2 == 1:
            koja_kutija = "kutija"
        else:
            koja_kutija = "druga_kutija"

        modul_sorter2(orMj, orSm, iX=66, iZ=br, iY=0, materijal=98, dv=0, kutija=koja_kutija, crtaj_kutije="da")

    # lijevo krilo samo selektori bez kutija
    for br in range(-20, -13):
        if br % 2 == 1:
            koja_kutija = "kutija"
        else:
            koja_kutija = "druga_kutija"

        modul_sorter2(orMj, orSm, iX=66, iZ=br, iY=0, materijal=98, dv=0, kutija=koja_kutija, crtaj_kutije="ne")

    # desno krilo samo selektori bez kutija
    for br in range(14, 21):
        if br % 2 == 1:
            koja_kutija = "kutija"
        else:
            koja_kutija = "druga_kutija"

        modul_sorter2(orMj, orSm, iX=66, iZ=br, iY=0, materijal=98, dv=0, kutija=koja_kutija, crtaj_kutije="ne")

    crtaj_hopper(orMj, (71, -20, 4), (71, -12, 4), orSm, "desno")  # lijevi spoj
    crtaj_kvadar(orMj, (71, -20, 5), (71, -12, 5), orSm, 44, 0)

    crtaj_hopper(orMj, (71, 12, 4), (71, 19, 4), orSm, "desno")  # desni spoj
    crtaj_kvadar(orMj, (71, 12, 5), (71, 19, 5), orSm, 44, 0)
    # desni zid
    orSm = ortUdesno(orSm)
    for br in range(-64, 1):
        if br % 2 == 1:
            koja_kutija = "kutija"
        else:
            koja_kutija = "druga_kutija"

        modul_sorter2(orMj, orSm, iX=15, iZ=br, iY=0, materijal=98, dv=0, kutija=koja_kutija, crtaj_kutije="da")
    crtaj_hopper(orMj, (20, -71, 4), (20, -65, 4), orSm, "desno")
    crtaj_kvadar(orMj, (20, -71, 5), (20, -65, 5), orSm, 44, 0)


if __name__ == "__main__":  # direktan poziv
    orMj = gdjeSam()
    orSm = gdjeGledam()
    mc.postToChat("Pocetak !!!" )
    sorter2(orMj, orSm, iX=10)
    mc.postToChat("Kraj !!!" )
