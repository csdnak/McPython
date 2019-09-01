#kat gore sa lampe

from crtanje import *		#tu je funkcija koju zovem
from hodnik_00 import *
from stepeniste import *
from mc import * #import api-ja
mc = Minecraft() #inicijalizacija sustava za rad sa Minecraftom

 
if __name__ == "__main__":    #direktan poziv
   #polukrugTunel (   iX=2 , iZ=0 , iY=0 , radius = 8 , duzina = 70 , korekcija = 0 , uspon = 0  )
   #visoka_soba (   iX=1 , iZ=0 , iY=0 ) 
   orMj = gdjeSam ()
   orSm = gdjeGledam ()
   orMjA = premjesti_origin ( orMj , -16 , 0 , 7 ,  orSm ) #mice ishodiste za slijedeci korak
   hodnik_00 (  orMjA ,  orSm , iX=0 , iZ=0 , iY=0 , duzina= 2 ,  materijal = 98, dv = 0 , stepenice_mat = 109 )
   orSmA=ortUdesno ( orSm )
   orMjA = premjesti_origin ( orMj , 4 , 0 , 0 ,  orSmA ) #mice ishodiste za slijedeci korak
   stepeniste ( orMjA , orSmA )


 