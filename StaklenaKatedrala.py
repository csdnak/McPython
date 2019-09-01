#ispred lika na seljacki nacin iskopa kupolu

import time
from crtanje import *		#tu je funkcija koju zovem
from hodnik_portala import *
from mc import * #import api-ja

mc = Minecraft() #inicijalizacija sustava za rad sa Minecraftom

def iskopajKupolu (  orMj , orSm ,iX=0 , iZ=0 , iY=0 , radius = 6 , korekcija = 2 , materijal = 0 , dv = 0):
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

    
   orMj = premjesti_origin ( orMj , iX , iZ , iY ,  orSm ) #mice ishodiste na centar kupole
   
   for dX in  range( - radius , radius + 1 ) :    		# prodji cijeli pravokutnik
      for dZ  in  range ( - radius , radius + 1 ) : 
         for dY in  range ( 0 , radius + 1  ) :    
            if ( dX**2 + (dY+korekcija)**2 + dZ**2 < radius**2 )  : #malo splostiti kupolu, ljepsa je
               gdje = rel2abs ( orMj ,  ( dX , dZ , dY )  , orSm  )  #relativne koordinate u apsolutne worlda
               mc.setBlock(gdje , materijal , dv )                   #postavi blok
            
   return 1

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

    
   orMj = premjesti_origin ( orMj , iX , iZ , iY ,  orSm ) #mice ishodiste na centar kupole
   
   for dX in  range( - radius , radius + 1 ) :    		# prodji cijeli pravokutnik
      for dZ  in  range ( - radius , radius + 1 ) : 
         for dY in  range ( 0 , radius + 1  ) :    
            if ( dX**2 + (dY+korekcija)**2 + dZ**2 < (radius+1)**2 ) and ( dX**2 + (dY+korekcija)**2 + dZ**2 > (radius-1)**2 ) :
            
               gdje = rel2abs ( orMj ,  ( dX , dZ , dY )  , orSm  )  #relativne koordinate u apsolutne worlda
               if ( dX % 5 == 0 ) and ( dZ % 5 == 0 )  :
                  mc.setBlock(gdje , 89 , 0 )                   #postavi blok
               else:
                  mc.setBlock(gdje , materijal , dv )                   #postavi blok
            gdje = rel2abs ( orMj ,  ( dX , dZ , -1 - iY )  , orSm  )  #relativne koordinate u apsolutne worlda                 
            if ( dX % 5 == 0 ) and ( dZ % 5 == 0 ) and ( dY == 0 ) :
               
               mc.setBlock(gdje , 89 , 0 )                   # glowstone podloga
            
            elif (dY == 0) : 
               
               mc.setBlock(gdje , 95 , 4 )                   #postavi podni blok - zuti blok stakla da se Ghastovi ne spawnaju
                           
            
   return 1   

def kula ( orMj ,orSm, iX=0, iZ=0, iY=0  , radius = 6 ,  visina = 10 ,  materijal = 1, dv = 0 , rasvjeta = "ne" ):
   """
   kopa cilindricnu rupu do dna relativno pomaknutu u odnosu na lik
   iX, - relativni pomak po X
   iZ, - relativni pomak po Z
   iY , - relativni pomak po Y
   radius radius rupe, default  6
   """
   orMj = premjesti_origin ( orMj , iX , iZ , iY ,  orSm ) #mice ishodiste na centar cilindra
   
   for dY in range ( 0 ,  visina  ):           #ide  sloj po sloj dolje
      for dX in range( - radius, radius + 1):
         for dZ in range( - radius, radius + 1):
            if dX**2 + dZ**2  < radius**2:  #kopati ili ne kopati
               gdje = rel2abs ( orMj ,  ( dX , dZ , dY )  , orSm  )  #relativne koordinate u apsolutne worlda
               mc.setBlock(gdje , AIR.id , 2 )                       # sve ide van
   
   time.sleep ( 5 )
   
   for dX in range( - radius, radius + 1):
      pomZ = int (sqrt( radius ** 2 - dX ** 2)+.5)
      for dZ in ( - pomZ, pomZ ):
         if ( dX % 5 == 0 ) and ( dZ % 5 == 0 )  :
            crtaj_kvadar ( orMj , ( dX , dZ , 0 )  , ( dX , dZ , visina-1 )  , orSm , 89 , 0 )
            crtaj_kvadar ( orMj , ( dZ , dX , 0 )  , ( dZ , dX , visina-1 )  , orSm , 89 , 0 ) # programerski hack                
         else:
            crtaj_kvadar ( orMj , ( dX , dZ , 0 )  , ( dX , dZ , visina-1 )  , orSm , materijal , dv )
            crtaj_kvadar ( orMj , ( dZ , dX , 0 )  , ( dZ , dX , visina-1 )  , orSm , materijal , dv ) # programerski hack                 

         
 

 
if __name__ == "__main__":    #direktan poziv
   orMj = gdjeSam ()
   orSm = gdjeGledam ()
   polumjer = 15
   
   kula_mat = 95
   kula_dv = 0
   kula_stepenice = 128
   
   for aX in (  -34 , 0 , 34 ):
      for aZ in (  -34 , 0 , 34 ):
         if abs ( aX ) != abs ( aZ  ) :
            kula ( orMj ,orSm , iX=aX , iZ=aZ , iY=0  , radius = polumjer +1 ,  visina = 6 ,  materijal = kula_mat , dv = kula_dv )
            kula ( orMj ,orSm , iX=aX , iZ=aZ , iY=0  , radius = polumjer  ,  visina = 6 ,  materijal = kula_mat , dv = kula_dv )
            #kupola ( orMj , orSm , iX=0 , iZ=0 , iY=6 , radius = polumjer , korekcija = 1 , materijal = 98 , dv = 0)
            iskopajKupolu (  orMj , orSm ,iX=aX , iZ=aZ , iY=6 , radius = polumjer, korekcija = 0 )
            kupola ( orMj , orSm , iX=aX , iZ=aZ , iY=6 , radius = polumjer  , korekcija = 0 , materijal = kula_mat , dv = kula_dv)
            time.sleep ( 4 )


            

   polumjer = 20
   kula ( orMj ,orSm , iX=0 , iZ=0 , iY=0  , radius = polumjer +1 ,  visina = 6 ,  materijal = kula_mat , dv = kula_dv )
   kula ( orMj ,orSm , iX=0 , iZ=0 , iY=0  , radius = polumjer  ,  visina = 6 ,  materijal = kula_mat , dv = kula_dv )
   #kupola ( orMj , orSm , iX=0 , iZ=0 , iY=6 , radius = polumjer , korekcija = 1 , materijal = 98 , dv = 0)
   iskopajKupolu (  orMj , orSm ,iX=0 , iZ=0 , iY=6 , radius = polumjer, korekcija = 0 )
   kupola ( orMj , orSm , iX=0 , iZ=0 , iY=6 , radius = polumjer  , korekcija = 0 , materijal = kula_mat , dv = kula_dv)
   time.sleep ( 10 )
   
   crtaj_kvadar ( orMj , (  -7 , -35 , 0)  , (  7 , 35 , 5 ) , orSm ,  0 , 0 )
   crtaj_kvadar ( orMj , (  -35 , -7 , 0)  , (  35 , 7 , 5 ) , orSm ,  0 , 0 )

   crtaj_kvadar ( orMj , (  -6 , -35 , 6)  , (  6 , 35 , 7 ) , orSm ,  0 , 0 )
   crtaj_kvadar ( orMj , (  -35 , -6 , 6)  , (  35 , 6 , 7 ) , orSm ,  0 , 0 )

   crtaj_kvadar ( orMj , (  -5 , -35 , 8)  , (  5 , 35 , 9 ) , orSm ,  0 , 0 )
   crtaj_kvadar ( orMj , (  -35 , -5 , 8)  , (  35 , 5 , 9 ) , orSm ,  0 , 0 )
   
   crtaj_kvadar ( orMj , (  -3 , -35 , 10)  , (  3 , 35 , 10 ) , orSm ,  0 , 0 )
   crtaj_kvadar ( orMj , (  -35 , -3 , 10)  , (  35 , 3 , 10 ) , orSm ,  0 , 0 )
   
   crtaj_kvadar ( orMj , (  -1 , -35 , 11)  , (  1 , 35 , 11 ) , orSm ,  0 , 0 )
   crtaj_kvadar ( orMj , (  -35 , -1 , 11)  , (  35 , 1 , 11 ) , orSm ,  0 , 0 )

   
   for dummy in ( 1 , 2 , 3 , 4 ): 
      orSm = ortUdesno ( orSm )
      #hodnik_portala (  orMj  ,  orSm , iX=49  , iZ=0 , iY=0 , duzina= 5 ,  materijal = kula_mat  ,  dv = kula_dv , stepenice_mat =  kula_stepenice  )
      crtaj_kvadar ( orMj , (49,-3,4)  , (50,-4,4) , orSm ,  kula_mat , blok_dv = kula_dv )   #krpanje
      crtaj_kvadar ( orMj , (49,3,4)  , (50,4,4) , orSm ,  kula_mat , blok_dv = kula_dv )   #krpanje
   
