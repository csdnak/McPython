# crta objekt zadan u dostavljenoj listi PROBA LOSHE
from mc import *  # ajmo probati ovaj import

mc = Minecraft()  # inicijalizacija sustava za rad sa Minecraftom


def crtanje2(ulaz):
    """
    funkcija za crtanje prima listu listi sa po 4 parametra
    1. parametar x koordinata
    2. parametar z koordinata
    3. parametar y koordinata
    4. parametar id bloka koji se postavlja
    """
    # gdje sam detaljno
    radnaPozicija = mc.player.getPos()
    # kamo gledam
    smjerRada = mc.player.getDirection()  # uzmem kamo gledam
    # smjer gledanja radi preglednosti spremimo u "vektor""
    Vx = 0  # pocetne vrijednosti su nule
    Vz = 0
    if abs(smjerRada.x) > abs(smjerRada.z):  # nadje se dominanti smjer i spremi u vektor
        Vx = round(smjerRada.x)
    else:
        Vz = round(smjerRada.z)

    v = 1
    # crtanje
    if abs(Vx) != abs(Vz):  # ne pod 45
        while v < 19:
            for brojalica in ulaz:
                gdjex = radnaPozicija.x + Vx * brojalica[0] + Vz * brojalica[1]  # pomak po x
                gdjez = radnaPozicija.z + Vx * brojalica[1] + Vz * brojalica[0]  # pomak po y
                # mc.postToChat("gdjex: %f gdjez: %f z-os: %f " % ( gdjex , gdjez , brojalica [1] ) )
                mc.setBlock(gdjex, brojalica[2], gdjez, brojalica[3], brojalica[4])  # postavi blok
            v = v + 1
            radnaPozicija.x = radnaPozicija.x + 5
    return 1
