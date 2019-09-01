#ispred lika soba 11 x 11

from crtanje import *		#tu je funkcija koju zovem
from mc import * #import api-ja
mc = Minecraft() #inicijalizacija sustava za rad sa Minecraftom

def mobspawner_soba (   iX=0 , iZ=0 , iY=0 ,  materijal = 98, dv = 1 , stepenice_mat = 109):
   """
   ispred lika soba SA SPAWNEROM
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

   crtaj_kvadar ( orMj , (-1,-9,-1)  , (31,9,43) , orSm , materijal , dv )   #zidovi
   crtaj_kvadar ( orMj , (0,-7,0)  , (30,7,40) , orSm , 0 , blok_dv = 0 )   #rupa
   crtaj_kvadar ( orMj , (-1,0,0)  , (-1,0,1) , orSm , 0 , blok_dv = 0 )   #rupa za vrata
  
  
   
   #lampe u podu
   dY = -1
   for dX in ( 2 , 5 , 8 , 11 , 14 , 17 , 20 , 24 , 27):
      for dZ in ( -6,-3 , 0 , 3 ,6  ):
         gdje = rel2abs ( orMj ,  ( dX , dZ  , dY  )  , orSm  )  #relativne koordinate u apsolutne worlda
         mc.setBlock( gdje , 89 )
   dY = 42
   for dX in ( 2 , 5 , 8 , 11 , 14 , 17 , 20 , 24 , 27):
      for dZ in ( -9,-6,-3 , 0 , 3 ,6 , 9 ):
         gdje = rel2abs ( orMj ,  ( dX , dZ  , dY  )  , orSm  )  #relativne koordinate u apsolutne worlda
         mc.setBlock( gdje , 89 )
 
    
   #spawneri
   
   crtaj_kvadar ( orMj , (0,-1,35)  , (30,-1,35) , orSm , materijal , dv )   
   crtaj_kvadar ( orMj , (0,1,35)  , (30,1,35) , orSm , materijal , dv )   
   
   #pistoni - lijevi
   crtaj_kvadar ( orMj , (0,-2,36)  , (30,-4,36) , orSm , materijal , dv )  #kamenje ispred i iza pistona
   crtaj_redstonedust (  orMj , (0,-4,37)  , (30,-4,37) , orSm ) #redstone vodic
   crtaj_sticky_piston    ( orMj , (0,-3,36)  , (30,-3,36) , orSm,  "desno"  ) #piston
   crtaj_kvadar ( orMj , (0,-2,37)  , (30,-3,40) , orSm , materijal , dv )  #kamenje iznad
   crtaj_kvadar ( orMj , (0,-6,36)  , (16,-5,36) , orSm , materijal , dv )  #kamenje na sredini
   crtaj_repeater ( orMj , (14,-5,37)  , (16,-5,37) , orSm , rel_smjer  = "desno" ) #repeaters
   #12 kamen za torch12
   crtaj_kvadar ( orMj , (12,-6,37)  , (12,-6,37) , orSm , materijal , dv )  #kamen za baklju
   crtaj_baklju ( orMj , (12,-6,38)   ,  orSm ,  "gore"   )
   crtaj_redstonetorch (  orMj , (13,-6,37)   ,  orSm ,  "odmene"  )
   crtaj_repeater ( orMj , (11,-6,37)  , (1,-6,37) , orSm , rel_smjer  = "odmene" ) #repeaters uzduz
   crtaj_repeater ( orMj , (0,-5,37)  , (0,-5,37) , orSm , rel_smjer  = "lijevo" ) #repeater
   crtaj_kvadar ( orMj , (1,-5,36)  , (13,-5,36) , orSm , 0 , 0 ) # rupa
   crtaj_redstonedust (  orMj , (0,-6,37)  , (0,-6,37) , orSm ) #redstone vodic
   crtaj_redstonedust (  orMj , (14,-6,37)  , (17,-6,37) , orSm ) #redstone vodic kratki
   for br in range ( 36 , 1 , -1 ) : #servisne stepenice
      crtaj_stepenice ( orMj , (36-br,-7,br )  , (36-br,-7,br ) , orSm ,   blok_id = 109 ,rel_smjer  = "odmene"   )
   
   
   

   #pistoni - desni
   crtaj_kvadar ( orMj , (0,2,36)  , (30,4,36) , orSm , materijal , dv )  #kamenje ispred i iza pistona
   crtaj_redstonedust (  orMj , (0,4,37)  , (30,4,37) , orSm ) #redstone vodic
   crtaj_sticky_piston    ( orMj , (0,3,36)  , (30,3,36) , orSm,  "lijevo"  ) #piston
   crtaj_kvadar ( orMj , (0,2,37)  , (30,3,40) , orSm , materijal , dv )  #kamenje iznad
   crtaj_kvadar ( orMj , (0,6,36)  , (16,5,36) , orSm , materijal , dv )  #kamenje na sredini
   crtaj_repeater ( orMj , (14,5,37)  , (16,5,37) , orSm , rel_smjer  = "lijevo" ) #repeaters
   #12 kamen za torch12
   crtaj_kvadar ( orMj , (12,6,37)  , (12,6,37) , orSm , materijal , dv )  #kamen za baklju
   crtaj_baklju ( orMj , (12,6,38)    ,  orSm ,  "gore" )
   crtaj_redstonetorch (  orMj , (13,6,37)   ,  orSm ,  "odmene"  )
   crtaj_repeater ( orMj , (11,6,37)  , (1,6,37) , orSm , rel_smjer  = "odmene" ) #repeaters uzduz
   crtaj_repeater ( orMj , (0,5,37)  , (0,5,37) , orSm , rel_smjer  = "desno" ) #repeater
   crtaj_kvadar ( orMj , (1,5,36)  , (13,5,36) , orSm , 0 , 0 ) # rupa
   crtaj_redstonedust (  orMj , (0,6,37)  , (0,6,37) , orSm ) #redstone vodic
   crtaj_redstonedust (  orMj , (14,6,37)  , (17,6,37) , orSm ) #redstone vodic kratki
   for br in range ( 36 , 1 , -1 ) : #servisne stepenice
      crtaj_stepenice ( orMj , (36-br,7,br )  , (36-br,7,br ) , orSm ,  blok_id = 109 , rel_smjer  = "odmene"   )
      
   #ulazna vrata 
   crtaj_kvadar ( orMj , (-2,4,0)  , (-2,4,0) , orSm , 70 , blok_dv = 0 )   #pressure plate ispred vrata
   crtaj_vrata ( orMj , (-1,4,0) , orSm , "meni"  , blok_id = 71  , kvaka = "desno"  ) #iron door
   crtaj_kvadar ( orMj , (0,4,0)  , (0,4,0) , orSm , 70 , blok_dv = 0 )   #pressure plate iza vrata
   
   
   #HOPPERI PO SREDINI
   crtaj_hopper    ( orMj , (0,0,-1)  , (30,-0,-1) , orSm , "meni")
         
   return 1
 
if __name__ == "__main__":    #direktan poziv
   #polukrugTunel (   iX=2 , iZ=0 , iY=0 , radius = 8 , duzina = 70 , korekcija = 0 , uspon = 0  )
   mobspawner_soba (   iX=1 , iZ=0 , iY=0 ) 