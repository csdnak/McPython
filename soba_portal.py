#ispred lika soba 11 x 11

from crtanje import *		#tu je funkcija koju zovem
from mc import * #import api-ja
mc = Minecraft() #inicijalizacija sustava za rad sa Minecraftom

def soba_portal ( orMj , orSm ,  iX=0 , iZ=0 , iY=0 ,  materijal = 98, dv = 1 , stepenice_mat = 109):
   """
   ispred lika soba 10 x 10
   iX, - relativni pomak po X
   iZ, - relativni pomak po Z
   iY , - relativni pomak po Y
   materijal - materijal zidova okolo - default stonebrick block
   dv - modifikator
   """

   

   iX += 1  #pomak zbog debljine zida 
   orMj = premjesti_origin ( orMj , iX , iZ , iY ,  orSm ) #mice ishodiste na centar 
   crtaj_kvadar ( orMj , (-1,-6,-1)  , (11,6,7) , orSm , materijal , dv )   #zidovi
   crtaj_kvadar ( orMj , (0,-5,0)  , (10,5,6) , orSm , 0 , blok_dv = 0 )   #rupa
   crtaj_kvadar ( orMj , (-1,0,0)  , (-1,0,1) , orSm , 0 , blok_dv = 0 )   #vrata
   # ornamenti
   crtaj_kvadar ( orMj , (0,-5,6)  , (10,5,6) , orSm , materijal , dv ) #strop pasice
   crtaj_kvadar ( orMj , (1,-4,6)  , (9,4,6) , orSm , 0 , 0 )
   
   crtaj_kvadar ( orMj , (0,-5,0)  , (10,-5,6) , orSm , materijal , dv ) #lijevi stupovi
   crtaj_kvadar ( orMj , (1,-5,0)  , (9,-5,5) , orSm , 0 , 0 )

   crtaj_kvadar ( orMj , (0,5,0)  , (10,5,6) , orSm , materijal , dv ) #desni stupovi
   crtaj_kvadar ( orMj , (1,5,0)  , (9,5,5) , orSm , 0 , 0 )
   
   # vijenci 
   crtaj_stepenice ( orMj , (9,5,5) , (9,5,5) , orSm , blok_id = stepenice_mat , rel_smjer  = "meni" , gore_dolje = "da"  )   # na kraju sobe
   crtaj_stepenice ( orMj , (9,-5,5) , (9,-5,5) , orSm , blok_id = stepenice_mat , rel_smjer  = "meni" , gore_dolje = "da"  )

   crtaj_stepenice ( orMj , (1,5,5) , (1,5,5) , orSm , blok_id = stepenice_mat , rel_smjer  = "odmene" , gore_dolje = "da"  ) # ne pocetku sobe
   crtaj_stepenice ( orMj , (1,-5,5) , (1,-5,5) , orSm , blok_id = stepenice_mat , rel_smjer  = "odmene" , gore_dolje = "da"  )

   crtaj_stepenice ( orMj , (10,-4,5) , (10,-4,5) , orSm , blok_id = stepenice_mat , rel_smjer  = "desno" , gore_dolje = "da"  ) # lijevi zid
   crtaj_stepenice ( orMj , (0,-4,5) , (0,-4,5) , orSm , blok_id = stepenice_mat , rel_smjer  = "desno" , gore_dolje = "da"  )    
   
   crtaj_stepenice ( orMj , (10,4,5) , (10,4,5) , orSm , blok_id = stepenice_mat , rel_smjer  = "lijevo" , gore_dolje = "da"  ) # desni zid
   crtaj_stepenice ( orMj , (0,4,5) , (0,4,5) , orSm , blok_id = stepenice_mat , rel_smjer  = "lijevo" , gore_dolje = "da"  )    
   
  
   
   #lampe u podu
   dY = -1
   for dX in ( 2 , 5 , 8 ):
      for dZ in ( -3 , 0 , 3 ):
         gdje = rel2abs ( orMj ,  ( dX , dZ  , dY  )  , orSm  )  #relativne koordinate u apsolutne worlda
         mc.setBlock( gdje , 89 )

   #lampe u stropu
   dY = 7
   for dX in ( 2 , 5 , 8 ):
      for dZ in ( -3 , 0 , 3 ):
         gdje = rel2abs ( orMj ,  ( dX , dZ  , dY  )  , orSm  )  #relativne koordinate u apsolutne worlda
         mc.setBlock( gdje , 89 )

         
   #ulazna vrata 
   crtaj_kvadar ( orMj , (-2,0,0)  , (-2,0,0) , orSm , 70 , blok_dv = 0 )   #pressure plate ispred vrata
   crtaj_vrata ( orMj , (-1,0,0) , orSm , "meni"  , blok_id = 71  , kvaka = "desno"  ) #iron door
   crtaj_kvadar ( orMj , (0,0,0)  , (0,0,0) , orSm , 70 , blok_dv = 0 )   #pressure plate iza vrata
   
   #portal
   crtaj_kvadar ( orMj , [  7 , -2, 0 ]  , [ 7 , 2 , 5  ] , orSm , 49 , 0 ) # obsidian
   crtaj_kvadar ( orMj , [  7 , -1 , 1 ]  , [ 7 , 1 , 4  ] , orSm , AIR.id , 0 ) # rupa portala
   crtaj_stepenice ( orMj , (6,-2,0) , (6,2,0) , orSm , blok_id = stepenice_mat , rel_smjer  = "meni" , gore_dolje = "ne"  ) 
         
   return 1
 
if __name__ == "__main__":    #direktan poziv
   #polukrugTunel (   iX=2 , iZ=0 , iY=0 , radius = 8 , duzina = 70 , korekcija = 0 , uspon = 0  )
   #gdje sam
   orMj = gdjeSam ()
   orSm = gdjeGledam ()
   soba_portal (  orMj , orSm , iX=1 , iZ=0 , iY=0 ) 