#ispred lika polukruzni tunel  i to samo blokove iz liste 

from crtanje import *		#tu je funkcija koju zovem
from mc import * #import api-ja
mc = Minecraft() #inicijalizacija sustava za rad sa Minecraftom

def polukrugTunel (   iX=0 , iZ=0 , iY=0 , radius = 5 , duzina = 10 , korekcija = 0.0 , uspon = -0.25 ):
   """
   ispred polukruzni tunel  
   iX, - relativni pomak po X
   iZ, - relativni pomak po Z
   iY , - relativni pomak po Y
   radius - radius tunela default 5.0 
   duzina - duzina tunela default 5, 
   korekcija - korekcija oblika, da bude ljepsi default 0.0 
   uspon - korekcija smjera koliko gore dolje  default  0
   """
   #gdje sam
   orMj = gdjeSam ()
   orSm = gdjeGledam ()
    
   orMj = premjesti_origin ( orMj , iX , iZ , iY ,  orSm ) #mice ishodiste na centar kupole

   dYmodifikator = 0.0     # pocetna vrijednost promjene visine
   for dX in  range( 0 , duzina  ) :    		# prodji cijeli pravokutnik
      for dZ  in  range ( - radius , radius + 1 ) : 
         for dY in  range ( - 1 , radius + 1  ) :     
            gdje = rel2abs ( orMj ,  ( dX , dZ  , dY + dYmodifikator )  , orSm  )  #relativne koordinate u apsolutne worlda
            if  ( abs ( dY  + korekcija )   <   (   ( math.cos  (  float (  dZ  )   / radius  ) ) *    radius        )      ) :
               mc.setBlock(gdje , AIR)			#postavi blok
            elif ( dZ == 0  ) :
               mc.setBlock( gdje , 89 )
            if  ( dY == -1 ) :
               if (abs (dX) % 3) == 0  and ( abs (dZ) % 3 ) == 0 :
                  mc.setBlock( gdje , 89 )		   #u podlogu obavezno u razmaku stavi glowstone
               else :
                  mc.setBlock(gdje , 98 , 1)			#postavi blok 
      dYmodifikator += uspon
   return 1
 
if __name__ == "__main__":    #direktan poziv
   #polukrugTunel (   iX=2 , iZ=0 , iY=0 , radius = 8 , duzina = 70 , korekcija = 0 , uspon = 0  )
   polukrugTunel (   iX=1 , iZ=0 , iY=0 , radius = 4 , duzina = 16 , korekcija = 1 , uspon = -0.3 )
   #polukrugTunel (   iX=1 , iZ=0 , iY=0 , radius = 3 , duzina = 8 , korekcija = 0 , uspon = -0.5 )