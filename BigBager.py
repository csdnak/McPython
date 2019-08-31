#ispred lika cisti pravokutnik  3x4 i dugacak 9 i to samo blokove iz liste 

import time
from mc import * #import api-ja
from crtanje import *		#tu je funkcija koju zovem
mc = Minecraft() #inicijalizacija sustava za rad sa Minecraftom

def bigBager ( orMj , orSm ,   visina = 45) :

    for dY in  range(  0 + 50 , -visina , -1 ):
        sirina = visina + dY
        gdje = rel2abs ( orMj ,  ( sirina + 5, sirina + 20 ,   dY )  , orSm  )
        gdje2 = rel2abs ( orMj ,  ( -sirina - 5 , -sirina - 20,   dY ) , orSm  ) 
        mc.setBlocks ( gdje , gdje2 , AIR.id , 0 )
 
    mc.postToChat("dy: %f " % dY )
 
    mc.postToChat("Kraj !!!" )
    return 1

   
 
if __name__ == "__main__":    #direktan poziv
   orMj = gdjeSam ()
   orSm = gdjeGledam ()
   bigBager ( orMj , orSm ,  visina = 50)   
