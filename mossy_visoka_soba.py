#ispred lika soba 11 x 11

from crtanje import *		#tu je funkcija koju zovem
from mc import * #import api-ja
mc = Minecraft() #inicijalizacija sustava za rad sa Minecraftom

def visoka_soba (   iX=0 , iZ=0 , iY=0 ,  materijal = 98, dv = 1 , stepenice_mat = 109):
   """
   ispred lika soba 10 x 10
   iX, - relativni pomak po X
   iZ, - relativni pomak po Z
   iY , - relativni pomak po Y
   materijal - materijal zidova okolo - default stonebrick block
   dv - modifikator
   """
   #gdje sam
   orMj = gdjeSam ()
   orSm = gdjeGledam ()
   iX += 1  #pomak zbog debljine zida 
   orMj = premjesti_origin ( orMj , iX , iZ , iY ,  orSm ) #mice ishodiste na centar kupole

   crtaj_kvadar ( orMj , (-1,-16,-1)  , (21,16,12) , orSm , materijal , dv )   #zidovi
   crtaj_kvadar ( orMj , (0,-15,0)  , (20,15,11) , orSm , 0 , blok_dv = 0 )   #rupa
   crtaj_kvadar ( orMj , (-1,0,0)  , (-1,0,1) , orSm , 0 , blok_dv = 0 )   #vrata
   # ornamenti
   crtaj_kvadar ( orMj , (0,-15,11)  , (20,15,11) , orSm , materijal , dv ) #strop pasice
   crtaj_kvadar ( orMj , (1,-14,11)  , (19,14,11) , orSm , 0 , 0 )
   
   crtaj_kvadar ( orMj , (0,-15,0)  , (20,-15,11) , orSm , materijal , dv ) #lijevi stupovi
   crtaj_kvadar ( orMj , (1,-15,0)  , (19,-15,10) , orSm , 0 , 0 )

   crtaj_kvadar ( orMj , (0,15,0)  , (20,15,11) , orSm , materijal , dv ) #desni stupovi
   crtaj_kvadar ( orMj , (1,15,0)  , (19,15,10) , orSm , 0 , 0 )
   
   # vijenci 
   crtaj_stepenice ( orMj , (19,15,10) , (19,15,10) , orSm , blok_id = stepenice_mat , rel_smjer  = "meni" , gore_dolje = "da"  )   # na kraju sobe
   crtaj_stepenice ( orMj , (19,-15,10) , (19,-15,10) , orSm , blok_id = stepenice_mat , rel_smjer  = "meni" , gore_dolje = "da"  )

   crtaj_stepenice ( orMj , (1,15,10) , (1,15,10) , orSm , blok_id = stepenice_mat , rel_smjer  = "odmene" , gore_dolje = "da"  ) # ne pocetku sobe
   crtaj_stepenice ( orMj , (1,-15,10) , (1,-15,10) , orSm , blok_id = stepenice_mat , rel_smjer  = "odmene" , gore_dolje = "da"  )

   crtaj_stepenice ( orMj , (20,-14,10) , (20,-14,10) , orSm , blok_id = stepenice_mat , rel_smjer  = "desno" , gore_dolje = "da"  ) # lijevi zid
   crtaj_stepenice ( orMj , (0,-14,10) , (0,-14,10) , orSm , blok_id = stepenice_mat , rel_smjer  = "desno" , gore_dolje = "da"  )    
   
   crtaj_stepenice ( orMj , (20,14,10) , (20,14,10) , orSm , blok_id = stepenice_mat , rel_smjer  = "lijevo" , gore_dolje = "da"  ) # desni zid
   crtaj_stepenice ( orMj , (0,14,10) , (0,14,10) , orSm , blok_id = stepenice_mat , rel_smjer  = "lijevo" , gore_dolje = "da"  )    
   
  
   
   #lampe u podu
   dY = -1
   for dX in ( 2 , 5 , 8 , 11 , 14 , 17 ):
      for dZ in ( -12,-9,-6,-3 , 0 , 3 ,6 , 9 , 12):
         gdje = rel2abs ( orMj ,  ( dX , dZ  , dY  )  , orSm  )  #relativne koordinate u apsolutne worlda
         mc.setBlock( gdje , 89 )
   #lampe u stropu
   dY = 12
   for dX in ( 2 , 5 , 8 , 11 , 14 , 17 ):
      for dZ in ( -12,-9,-6,-3 , 0 , 3 ,6 , 9 , 12):
         gdje = rel2abs ( orMj ,  ( dX , dZ  , dY  )  , orSm  )  #relativne koordinate u apsolutne worlda
         mc.setBlock( gdje , 89 )

         
   #ulazna vrata 
   crtaj_kvadar ( orMj , (-2,0,0)  , (-2,0,0) , orSm , 70 , blok_dv = 0 )   #pressure plate ispred vrata
   crtaj_vrata ( orMj , (-1,0,0) , orSm , "meni"  , blok_id = 71  , kvaka = "desno"  ) #iron door
   crtaj_kvadar ( orMj , (0,0,0)  , (0,0,0) , orSm , 70 , blok_dv = 0 )   #pressure plate iza vrata
         
   return 1
 
if __name__ == "__main__":    #direktan poziv
   #polukrugTunel (   iX=2 , iZ=0 , iY=0 , radius = 8 , duzina = 70 , korekcija = 0 , uspon = 0  )
   visoka_soba (   iX=1 , iZ=0 , iY=0 ) 