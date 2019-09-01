#ispred lika hodnik

import time
from crtanje import *		#tu je funkcija koju zovem
from soba_portal import *
from mc import * #import api-ja
mc = Minecraft() #inicijalizacija sustava za rad sa Minecraftom

def hodnik_portala (  orMj  ,  orSm , iX=0 , iZ=0 , iY=0 , duzina= 3 ,  materijal = 98, dv = 0 , stepenice_mat = 109 ):
   """
   ispred lika hodnik dugacak 128 sa 2 portalne sobe

   """

   orMj = premjesti_origin ( orMj , iX , iZ , iY ,  orSm ) #mice ishodiste na centar 
   
   for br in range ( duzina ):
      crtaj_kvadar ( orMj , (0,-4,-1)  , (17,4,4) , orSm , materijal , dv )   #zidovi - zatvoreno na daljem kraju otvoreno na pocetku
      crtaj_kvadar ( orMj , (0,-3,0)  , (16,3,3) , orSm , 0 , blok_dv = 0 )   #rupa
      crtaj_kvadar ( orMj , (0,-3,4)  , (16,-4,4) , orSm , 0 , blok_dv = 0 )   #rupa
      crtaj_kvadar ( orMj , (0,3,4)  , (16,4,4) , orSm , 0 , blok_dv = 0 )   #rupa
      
   
      #lampe u podu
      dY = -1
      dZ = 0 
      for dX in ( 0 , 8 , 16 ):
         gdje = rel2abs ( orMj ,  ( dX , dZ  , dY  )  , orSm  )  #relativne koordinate u apsolutne worlda
         mc.setBlock( gdje , 89 )
         if dX == 8 :
            gdje = rel2abs ( orMj ,  ( dX+1 , dZ+1  , dY  )  , orSm  )  #relativne koordinate u apsolutne worlda
            mc.setBlock( gdje , 89 )
            gdje = rel2abs ( orMj ,  ( dX+1 , dZ-1  , dY  )  , orSm  )  #relativne koordinate u apsolutne worlda
            mc.setBlock( gdje , 89 )

      dY = 4
      dZ = 0 
      for dX in ( 0 , 8 , 16 ):
         gdje = rel2abs ( orMj ,  ( dX , dZ  , dY  )  , orSm  )  #relativne koordinate u apsolutne worlda
         mc.setBlock( gdje , 89 )
         
      #pasice u uglovima gore
      crtaj_kvadar ( orMj , (0,-3,3)  , (16,-3,3) , orSm , materijal , dv )   #lijeva pasica
      crtaj_kvadar ( orMj , (0,3,3)  , (16,3,3) , orSm , materijal , dv )   #desna pasica
      #poprecna pasica
      crtaj_kvadar ( orMj , (8,-3,3)  , (8,3,3) , orSm , materijal , dv )   #popreko
      #stakla
      crtaj_kvadar ( orMj , (0,-4,1)  , (16,-4,2) , orSm , 20 , 0 )   #lijeva 
      crtaj_kvadar ( orMj , (0,4,1)  , (16,4,2) , orSm , 20 , 0 )   #desna 
   
      #stupovi
      
      crtaj_kvadar ( orMj , (8,-3,0)  , (8,-3,2) , orSm , materijal , dv )   #lijevi stup
      crtaj_kvadar ( orMj , (8,-3,1)  , (8,-3,1) , orSm , 89 , 0 )   #lijevi stup lampa
      crtaj_stepenice ( orMj , (7,-3,2) , (7,-3,2) , orSm , blok_id = stepenice_mat , rel_smjer  = "meni" , gore_dolje = "da"  ) #prema meni
      crtaj_stepenice ( orMj , (8,-2,2) , (8,-2,2) , orSm , blok_id = stepenice_mat , rel_smjer  = "desno" , gore_dolje = "da"  ) #u sredini
      crtaj_stepenice ( orMj , (9,-3,2) , (9,-3,2) , orSm , blok_id = stepenice_mat , rel_smjer  = "odmene" , gore_dolje = "da"  ) #u sredini
   
      crtaj_kvadar ( orMj , (8,3,0)  , (8,3,2) , orSm , materijal , dv )   #desni stup
      crtaj_kvadar ( orMj , (8,3,1)  , (8,3,1) , orSm , 89 , 0 )   #desni stup lampa
      crtaj_stepenice ( orMj , (7,3,2) , (7,3,2) , orSm , blok_id = stepenice_mat , rel_smjer  = "meni" , gore_dolje = "da"  ) #prema meni
      crtaj_stepenice ( orMj , (8,2,2) , (8,2,2) , orSm , blok_id = stepenice_mat , rel_smjer  = "lijevo" , gore_dolje = "da"  ) #u sredini
      crtaj_stepenice ( orMj , (9,3,2) , (9,3,2) , orSm , blok_id = stepenice_mat , rel_smjer  = "odmene" , gore_dolje = "da"  ) #u sredini
      
      orMj = premjesti_origin ( orMj , 16 , 0 , 0 ,  orSm ) #mice ishodiste za slijedeci korak
      
      time.sleep ( 1 )
   
   orSm = ortUlijevo (orSm)
   soba_portal ( orMj , orSm ,  iX=4 , iZ=-16 , iY=0 ,  materijal = 24, dv = 2 , stepenice_mat = 128)
         
   return 1
 
if __name__ == "__main__":    #direktan poziv
   #polukrugTunel (   iX=2 , iZ=0 , iY=0 , radius = 8 , duzina = 70 , korekcija = 0 , uspon = 0  )
   orMj = gdjeSam ()
   orSm = gdjeGledam ()
   
   
   hodnik_portala (  orMj ,  orSm , iX=0 , iZ=0 , iY=0 , duzina= 4 ,  materijal = 24, dv = 2 , stepenice_mat = 128 )
   orMj = premjesti_origin ( orMj , 64 , 0 , 0 ,  orSm )
   hodnik_portala (  orMj ,  orSm , iX=0 , iZ=0 , iY=0 , duzina= 4 ,  materijal = 24, dv = 2 , stepenice_mat = 128 )
   