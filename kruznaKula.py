#kruzna kula

import time
from crtanje import *		#tu je funkcija koju zovem
from mc import * #import api-ja
mc = Minecraft() #inicijalizacija sustava za rad sa Minecraftom

def kula ( orMj , iX, iZ, iY ,orSm , radius = 6 ,  visina = 10 ,  materijal = 1, dv = 0 , rasvjeta = "ne" ):
   """
   kopa cilindricnu rupu do dna relativno pomaknutu u odnosu na lik
   iX, - relativni pomak po X
   iZ, - relativni pomak po Z
   iY , - relativni pomak po Y
   radius radius rupe, default  6
   """
   #gdje sam i gdje gledam
   #mc.postToChat("prvi origin: %s" % ( orMj ) )
    
   orMj = premjesti_origin ( orMj , iX , iZ , iY ,  orSm ) #mice ishodiste na centar cilindra
   #mc.postToChat("prvi origin: %s" % ( orMj ) )
   #dubina = nadji_dno ( orMj , orMj , orSm )                #odredi dubinu do bedrocka
   #mc.postToChat("dubina: %f" % ( dubina ) )
   
   
   for dX in range( - radius, radius + 1):
      pomZ = int (sqrt( radius ** 2 - dX ** 2)+.5)
      for dZ in ( - pomZ, pomZ ):
         #if ( dX**2 + dZ**2   == radius**2 ) and ( dX**2 + dZ**2   >= (radius - 1 )**2 ):  #kopati ili ne kopati
         crtaj_kvadar ( orMj , ( dX , dZ , 0 )  , ( dX , dZ , visina-1 )  , orSm , materijal , dv )
         crtaj_kvadar ( orMj , ( dZ , dX , 0 )  , ( dZ , dX , visina-1 )  , orSm , materijal , dv ) # programerski hack
         if ( rasvjeta == "da" ) and ( int ( dX ) % 8 == 0 ) and ( int ( dY ) % 8 == 0 ) and ( int ( dZ ) % 8 == 0 ) : # ako je rasvijeta
            mc.setBlock(gdje , 89 , 0 )           
   """
   for dZ in range( - radius, radius + 1):
      pomX = int (sqrt( radius ** 2 - dZ ** 2))
      for dX in ( - pomX, pomX ):
         #if ( dX**2 + dZ**2   == radius**2 ) and ( dX**2 + dZ**2   >= (radius - 1 )**2 ):  #kopati ili ne kopati
         crtaj_kvadar ( orMj , ( dX , dZ , 0 )  , ( dX , dZ , visina-1 )  , orSm , materijal , dv )
   """         
   return 1         
            
            
 
if __name__ == "__main__":    #direktan poziv
   orMj = gdjeSam ()
   orSm = gdjeGledam ()

   kula ( orMj ,0 , 0 , 0 , orSm ,radius = 5 , visina = 14 ,  materijal = 98, dv = 1 ,rasvjeta = "ne" )
   kula ( orMj ,0 , 0 , 12 , orSm ,radius = 6 , visina = 4 ,  materijal = 98, dv = 1 , rasvjeta = "ne" )
   #kula ( orMj ,12 , 0 , 14 , orSm ,radius = 10 , visina = 2 , rasvjeta = "ne" )


