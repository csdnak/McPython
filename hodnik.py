#ispred lika polukruzni tunel  i to samo blokove iz liste 

from crtanje import *		#tu je funkcija koju zovem
from mc import * #import api-ja
mc = Minecraft() #inicijalizacija sustava za rad sa Minecraftom

def hodnik (   iX=0 , iZ=0 , iY=0  , duzina = 10 ):
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
   
   crtaj_kvadar ( orMj , ( 1  , -3 , -1 )  , (  duzina , 3 , 5 ) , orSm , 98 , 0 ) # stonebrick tijelo
   crtaj_kvadar ( orMj , ( 1  , -2 , 0 )  , (  duzina , 2 , 4 ) , orSm , AIR.id , 0 ) # stonebrick rupa
   crtaj_kvadar ( orMj , ( 1  , -2 , 0 )  , (  duzina , -2 , 0 ) , orSm , 44 , 5 ) # stonebrick slab lijevi dolje
   crtaj_kvadar ( orMj , ( 1  , 2 , 0 )  , (  duzina , 2 , 0 ) , orSm , 44 , 5 ) # stonebrick slab desni dolje
   crtaj_stepenice ( orMj ,( 1  , -2 , 4 )  , (  duzina , -2 , 4 ) , orSm , blok_id = 109 , rel_smjer  = "desno" , gore_dolje = "da"  ) 
   crtaj_stepenice ( orMj ,( 1  , 2 , 4 )  , (  duzina , 2 , 4 ) , orSm , blok_id = 109 , rel_smjer  = "lijevo" , gore_dolje = "da"  ) 
   
   
   
   for dX in  range( 3 , duzina , 5 ) :    		# prodji cijeli pravokutnik
      crtaj_kvadar ( orMj , (dX,0,5)  , (dX,0,5) , orSm , 89 )
           

   return 1
 
if __name__ == "__main__":    #direktan poziv
   hodnik (   iX=1 , iZ=0 , iY=0 , duzina = 65  )