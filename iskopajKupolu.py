#ispred lika na seljacki nacin iskopa kupolu

from crtanje import *		#tu je funkcija koju zovem
from mc import * #import api-ja
mc = Minecraft() #inicijalizacija sustava za rad sa Minecraftom

def iskopajKupolu ( iX=0 , iZ=0 , iY=0 , radius = 6 , korekcija = 2 , materijal = 0 , dv = 0):
   """
   ispred lika na seljacki nacin iskopa kupolu
   iX, - relativni pomak po X
   iZ, - relativni pomak po Z
   iY , - relativni pomak po Y
   radius radius kupole, default  6
   korekcija - koliko se spusta kupola da ljepse izgleda
   materijal - default zrak 0 
   dv  podtip materijala ili orijentacija bloka default 0
   """
   orMj = gdjeSam ()
   orSm = gdjeGledam ()
    
   orMj = premjesti_origin ( orMj , iX , iZ , iY ,  orSm ) #mice ishodiste na centar kupole
   
   for dX in  range( - radius , radius + 1 ) :    		# prodji cijeli pravokutnik
      for dZ  in  range ( - radius , radius + 1 ) : 
         for dY in  range ( 0 , radius + 1  ) :    
            if ( dX**2 + (dY+korekcija)**2 + dZ**2 < radius**2 )  : #malo splostiti kupolu, ljepsa je
               gdje = rel2abs ( orMj ,  ( dX , dZ , dY )  , orSm  )  #relativne koordinate u apsolutne worlda
               mc.setBlock(gdje , materijal , dv )                   #postavi blok
            
   return 1

   
   
 
if __name__ == "__main__":    #direktan poziv
   iskopajKupolu ( 21, 0, 0 ,22 ,0 )

