#ispred lika hodnik

import time
from crtanje import *		#tu je funkcija koju zovem
from mc import * #import api-ja
mc = Minecraft() #inicijalizacija sustava za rad sa Minecraftom

def hodnik_00 (  orMj  ,  orSm , iX=0 , iZ=0 , iY=0 , duzina= 3 ,  materijal = 98, dv = 0 , stepenice_mat = 109 ):
   """
   ispred lika soba 10 x 10
   iX, - relativni pomak po X
   iZ, - relativni pomak po Z
   iY , - relativni pomak po Y
   duzina - koliko dug u koracima po 10
   materijal - materijal zidova okolo - default stonebrick block
   dv - modifikator
   """
   #gdje sam

   orMj = premjesti_origin ( orMj , iX , iZ , iY ,  orSm ) #mice ishodiste na centar 
   
   for br in range ( duzina ):
      crtaj_kvadar ( orMj , (0,-4,-1)  , (17,4,4) , orSm , materijal , dv )   #zidovi - zatvoreno na daljem kraju otvoreno na pocetku
      crtaj_kvadar ( orMj , (0,-3,0)  , (16,3,3) , orSm , 0 , blok_dv = 0 )   #rupa
   
      #lampe u podu
      dY = -1
      dZ = 0 
      for dX in ( 0 , 8 , 16 ):
         gdje = rel2abs ( orMj ,  ( dX , dZ  , dY  )  , orSm  )  #relativne koordinate u apsolutne worlda
         mc.setBlock( gdje , 89 )
      
      #pasice u uglovima gore
      crtaj_kvadar ( orMj , (0,-3,3)  , (16,-3,3) , orSm , materijal , dv )   #lijeva pasica
      crtaj_kvadar ( orMj , (0,3,3)  , (16,3,3) , orSm , materijal , dv )   #desna pasica
      #poprecna pasica
      crtaj_kvadar ( orMj , (8,-3,3)  , (8,3,3) , orSm , materijal , dv )   #popreko
   
      #stupovi
      
      crtaj_kvadar ( orMj , (8,-3,0)  , (8,-3,3) , orSm , materijal , dv )   #lijevi stup
      crtaj_stepenice ( orMj , (7,-3,2) , (7,-3,2) , orSm , blok_id = stepenice_mat , rel_smjer  = "meni" , gore_dolje = "da"  ) #prema meni
      crtaj_stepenice ( orMj , (8,-2,2) , (8,-2,2) , orSm , blok_id = stepenice_mat , rel_smjer  = "desno" , gore_dolje = "da"  ) #u sredini
      crtaj_stepenice ( orMj , (9,-3,2) , (9,-3,2) , orSm , blok_id = stepenice_mat , rel_smjer  = "odmene" , gore_dolje = "da"  ) #u sredini
   
      crtaj_kvadar ( orMj , (8,3,0)  , (8,3,3) , orSm , materijal , dv )   #desni stup
      crtaj_stepenice ( orMj , (7,3,2) , (7,3,2) , orSm , blok_id = stepenice_mat , rel_smjer  = "meni" , gore_dolje = "da"  ) #prema meni
      crtaj_stepenice ( orMj , (8,2,2) , (8,2,2) , orSm , blok_id = stepenice_mat , rel_smjer  = "lijevo" , gore_dolje = "da"  ) #u sredini
      crtaj_stepenice ( orMj , (9,3,2) , (9,3,2) , orSm , blok_id = stepenice_mat , rel_smjer  = "odmene" , gore_dolje = "da"  ) #u sredini
      
      orMj = premjesti_origin ( orMj , 16 , 0 , 0 ,  orSm ) #mice ishodiste za slijedeci korak
      
      time.sleep ( 2 )
         
   return 1
 
if __name__ == "__main__":    #direktan poziv
   #polukrugTunel (   iX=2 , iZ=0 , iY=0 , radius = 8 , duzina = 70 , korekcija = 0 , uspon = 0  )
   orMj = gdjeSam ()
   orSm = gdjeGledam ()
   
   
   hodnik_00 (  orMj ,  orSm , iX=0 , iZ=0 , iY=0 , duzina= 5 ,  materijal = 98, dv = 0 , stepenice_mat = 109 )
   