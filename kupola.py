#kreira kupolu debljine stjenke 1

from crtanje import *		#tu je funkcija koju zovem
from mc import * #import api-ja
mc = Minecraft() #inicijalizacija sustava za rad sa Minecraftom

def kupola ( orMj , orSm , iX=0 , iZ=0 , iY=0 , radius = 6 , korekcija = 2 , materijal = 1 , dv = 0) :
   """
   kreira kupolu debljine stjenke 1: NAPOMENA :nije bas debljina stjenke 1 !!!!
   iX, - relativni pomak po X
   iZ, - relativni pomak po Z
   iY , - relativni pomak po Y
   radius radius kupole, default  6
   korekcija - koliko se spusta kupola da ljepse izgleda
   materijal - default zrak stone 
   dv  podtip materijala ili orijentacija bloka default 0
   """
   #gdje sam

    
   #orMj = premjesti_origin ( orMj , iX , iZ , iY ,  orSm ) #mice ishodiste na centar kupole
   
   for dX in  range( - radius , radius + 1 ) :    		# prodji cijeli pravokutnik
      for dZ  in  range ( - radius , radius + 1 ) : 
         for dY in  range ( 0 , radius + 1  ) :    
            if ( dX**2 + (dY+korekcija)**2 + dZ**2 < radius**2 ) and ( dX**2 + (dY+korekcija)**2 + dZ**2 > (radius-1)**2 ) :
               gdje = rel2abs ( orMj ,  ( dX , dZ , dY )  , orSm  )  #relativne koordinate u apsolutne worlda
               mc.setBlock(gdje , materijal , dv )                   #postavi blok
   crtaj_kvadar ( orMj , ( -radius  , -radius , -1 )  , (  radius , radius , -1 ) , orSm ,  89 , 0 ) # glowstone podloga
            
   return 1

 
if __name__ == "__main__":    #direktan poziv
   orMj = gdjeSam ()
   orSm = gdjeGledam ()
   kupola ( orMj , orSm ,  0, 0 , 0 , 11 , 2 , 1 , 4 )

