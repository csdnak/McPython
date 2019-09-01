# surival house 7 x 7 from http://www.minecraftforum.net/forums/minecraft-discussion/survival-mode/290440-minecraft-survival-starter-houses
#definicija objekta i poziv rutine za crtanje
from crtanje import *		#tu je funkcija koju zovem
from crtanje2 import *		#tu je funkcija koju zovem
from mc import *			
mc = Minecraft() #inicijalizacija sustava za rad sa Minecraftom

def kuca_06 (  orMj ,  orSm , iX=0 , iZ=0 , iY=0 ) :
   orMj = premjesti_origin ( orMj , iX , iZ , iY ,  orSm ) #mice ishodiste na centar

   #crta iz sredine 7 siroko 5 duboko

   #clear the deck
   crtaj_kvadar ( orMj , [ -2 , -3 , -3 ]  , [ 2 , 3 , 9  ] , orSm , 0 , 0 ) # zrak
   crtaj_kvadar ( orMj , [ -1 , -2 , -3 ]  , [ 1 , 2 , -3  ] , orSm , 5 , 0 ) # blok oak wood
   crtaj_kvadar ( orMj , [ -2 , -3 , -3 ]  , [ 2 , 3 , 1  ] , orSm , 4 , 0 ) # blok coblestonea
   crtaj_kvadar ( orMj , [ -1 , -2 , 0 ]  , [ 1 , 2, 0  ] , orSm , 5 , 0 ) # blok oak wood
   #crtaj_kvadar ( orMj , [ -2 , -3 , 1 ]  , [ 2 , 3 , 1  ] , orSm , 4 , 0 ) # blok coblestonea
   crtaj_kvadar ( orMj , [ -2 , -3 , 2 ]  , [ 2 , 3, 3  ] , orSm , 5 , 0 ) # blok oak wood
   
   crtaj_kvadar ( orMj , [ -1 , -2 , -2 ]  , [ 1 , 2 , -1  ] , orSm , 0 , 0 ) # praznina u coblestoneu
   crtaj_kvadar ( orMj , [ -1 , -2 , 1 ]  , [ 1 , 2 , 3  ] , orSm , 0 , 0 ) # praznina u sobi
   #krovic na iznad kuce
   crtaj_kvadar ( orMj , (-4 , -3 , 4 )  , (2 , 3 , 4  ), orSm , 126 , blok_dv = 0 ) #
   #stupovi na coskovima 5 visoko
   for dX in ( -2 , 2 ):
      for dZ in ( -3 , 3 ):
         crtaj_deblo ( orMj , ( dX , dZ , 0 ) , ( dX , dZ , 4 ) , orSm , "gore" , blok_id = 17 , podtip = 0   )
   """
   #zadnji i prenji zid cobblestone
   for dX in ( -2 , 2 ):
      crtaj_kvadar ( orMj , [ dX , -2 , 0 ]  , [ dX , 2 , 1  ] , orSm , 4 , 0 ) # blok coblestonea
   #sastrane zidovi coblestonea
   for dZ in (-3 , 3):
      crtaj_kvadar ( orMj , [ -1 , dZ , 0 ]  , [ 1 , dZ , 1  ] , orSm , 4 , 0 ) # blok coblestonea
   #pod na visini 1
   crtaj_kvadar ( orMj , [ -1 , -2 , 0 ]  , [ 1 , 2 , 0  ] , orSm , 5 , 0 ) # blok oak wood
   """
   #procelje temelja
   crtaj_kvadar ( orMj , [ -2 , 0 , 0 ]  , [ -2 , 0 , 0  ] , orSm , 5 , 0 ) # blok oak wood ?????????
   crtaj_kvadar ( orMj , [ -2 , 0 , 2 ]  , [ -2 , 0 , 1  ] , orSm , 5 , 0 ) # blok zraka
   #prvi red podesta
   crtaj_kvadar ( orMj , [ -3 , -2 , 0 ]  , [ -3 , 2 , 0  ] , orSm , 5 , 0 ) # blok oak wood
   crtaj_stepenice ( orMj , [ -3 , -3 , 0 ]  , [ -3 , -3 , 0  ], orSm , blok_id = 53 , rel_smjer  = "lijevo" , gore_dolje = "da"  ) 
   crtaj_stepenice ( orMj , [ -3 , 3 , 0 ]  , [ -3 , 3 , 0  ] , orSm , blok_id = 53 , rel_smjer  = "desno" , gore_dolje = "da"  ) 
   #drugi, srednji,  red podesta
   crtaj_stepenice ( orMj , [ -4 , -3 , 0 ]  , [ -4 , 3 , 0  ] , orSm , blok_id = 53 , rel_smjer  = "meni" , gore_dolje = "da"  ) 
   #treci,  red podesta
   crtaj_stepenice ( orMj , [ -5 , 0 , 0 ]  , [ -5 , 0 , 0  ] , orSm , blok_id = 53 , rel_smjer  = "meni" , gore_dolje = "ne"  ) 
   crtaj_stepenice ( orMj , [ -5 , -1 , 0 ]  , [ -5 , -1 , 0  ] , orSm , blok_id = 53 , rel_smjer  = "lijevo" , gore_dolje = "ne"  ) 
   crtaj_stepenice ( orMj , [ -5 , 1 , 0 ]  , [ -5 , 1 , 0  ] , orSm , blok_id = 53 , rel_smjer  = "desno" , gore_dolje = "ne"  ) 
   #ograde na podestu
   for dZ in ( -3 , 3 ):
      crtaj_kvadar ( orMj , (-4 , dZ , 1 )  , (-3 , dZ , 1 ) , orSm , 85 , blok_dv = 0 ) #Krajnji
   for dZ in ( -2 , 1 ):
      crtaj_kvadar ( orMj , (-4 , dZ , 1 )  , (-4 , dZ + 1, 1  ), orSm , 85 , blok_dv = 0 ) #unutrasnji
   for dZ in ( -3 , -1 , 1 , 3):
      crtaj_kvadar ( orMj , (-4 , dZ , 2 )  , (-4 , dZ , 3  ), orSm , 85 , blok_dv = 0 ) #stupci
   #fence prozori
   for aa in (-1,1):
      crtaj_kvadar ( orMj , (-2 , 2 * aa, 2 )  , (-2 , 2 * aa, 2  ), orSm , 85 , blok_dv = 0 ) #prednji prozori
      crtaj_kvadar ( orMj , (0 , 3 * aa, 2 )  , (0 , 3 * aa, 2  ), orSm , 85 , blok_dv = 0 ) #prozori sastrane
   crtaj_kvadar ( orMj , (2 , -1, 2 )  , (2 , 1, 2  ), orSm , 85 , blok_dv = 0 ) #prozori pozadi
  
   #lojtrice pozadi desno
   crtaj_ljestve  ( orMj , (1,2,-2) , (1,2,3) , orSm , rel_smjer  = "odmene" )
   #klapna izbad lojtrica
   crtaj_klopku   (  orMj , (1,2,4)  , orSm ,  "lijevo"  , stanje="zatvoreno" , visina = "dolje" )
   
   #dimnjak
   crtaj_kvadar ( orMj , (-1 , -2,1 )  , (-1 , -2, 5  ), orSm , 139 , blok_dv = 0 ) #prvo uski dio cijelom visinom
   crtaj_kvadar ( orMj , (-1 , -2,4 )  , (-1 , -2, 4  ), orSm , 4 , blok_dv = 0 ) #siroki dio kroz slab
   #pec ispod dimnjaka
   crtaj_pec  ( orMj , (-1 ,-2 ,  1 ) , ( - 1 ,-2 , 1 ) , orSm , "desno" )
   #workbench
   crtaj_banak ( orMj ,( 0 , -2 , 1 ) , ( 0 , -2 , 1 ) , orSm , rel_smjer  = "meni" )
   #kutija
   crtaj_kutiju ( orMj , ( 1 , -2 , 1 ) , ( 1 , -2 , 1 ) , orSm , "desno" )
   #krevet
   crtaj_krevet  ( orMj , ( 1 , 0 , 1 ) , ( 1 , -1 , 1 )  , orSm , "lijevo" )
   # kutije u podrumu
   crtaj_kutiju ( orMj , ( -1 , -2 , -2 ) , ( -1 , -1 , -2 ) , orSm , "odmene" ) #lijeva kutija
   crtaj_kutiju ( orMj , ( -1 , 2 , -2 ) , ( -1 , 1 , -2 ) , orSm , "odmene" )   #desna kutija
   # izlaz pozadi
   # kvrga
   crtaj_kvadar ( orMj , [ 3 , -2 , -3 ]  , [ 4 , 2 , -1  ] , orSm , 4 , 0 ) #kvrga iza za stepenice
   crtaj_kvadar ( orMj , [ 3 , -2 , 0 ]  , [ 4 , 2 , 0  ] , orSm , 85 , 0 ) #ograda iza
   #crtaj_kvadar ( orMj , [ 2 , 0 , -2 ]  , [ 2 , 0 , -1  ] , orSm , 0 , 0 ) #rupa u temelju cobblestoneu
   crtaj_vrata ( orMj , [ 2 , 0 , -2 ]   , orSm, "odmene"  , blok_id = 64  , kvaka = "desno"  )#vrata iza
   crtaj_kvadar ( orMj , [ 3 , 0 , -2 ]  , [ 3 , 2 , 0  ] , orSm , 0 , 0 ) #rupa iza za stepenice
   crtaj_stepenice ( orMj , [ 3 , 1 , -2 ]  , [ 3 , 1 , -2  ] , orSm , blok_id = 67 , rel_smjer  = "lijevo" , gore_dolje = "ne"  ) #prva stepenica
   crtaj_stepenice ( orMj , [ 3 , 2 , -1 ]  , [ 3 , 2 , -1  ] , orSm , blok_id = 67 , rel_smjer  = "lijevo" , gore_dolje = "ne"  )    #druga stepenica
   #ulazna vrata 
   crtaj_vrata ( orMj , [ -2 , 0 , 1 ]   , orSm, "meni"  , blok_id = 64  , kvaka = "desno"  )#vrata 
   #vrt sastrane
   crtaj_kvadar ( orMj , [ -2 , -4 , -1 ]  , [ 2 , -8 , -1  ] , orSm , 4 , 0 )  #okvir od cobblestonea
   crtaj_kvadar ( orMj , [ -2 , -4 , 0 ]  , [ 2 , -8 , 0  ] , orSm , 85 )  #ograda oko vrta
   crtaj_kvadar ( orMj , [ -1 , -4 , 0]  , [ 1 , -7 , 0  ] , orSm , 0 , 0 )  #rupa u ogradi
   
   crtaj_kvadar ( orMj , [ -1 , -4 , -1 ]  , [ 1 , -7 , -1  ] , orSm , 60 , 0 )  #farmland
   crtaj_kvadar ( orMj , [ -1 , -4 , 0]  , [ 1 , -7 , 0  ] , orSm , 59 , 0 )  #wheat
   crtaj_kvadar ( orMj , [ 1 , -5 , -1 ]  , [ 1 , -5 , -1  ] , orSm , 8 , 0 )  #voda
   crtaj_vrataograde ( orMj ,  [ -2 , -5 , 0  ] , orSm ,  "lijevo_desno"  ) #vrata u ogradi
   #baklje
   crtaj_baklju (  orMj , [ -3 , -1 , 2 ]   , orSm, "meni"    )#oko ulaza
   crtaj_baklju (  orMj , [ -3 , 1 , 2 ]   , orSm, "meni"    )#oko ulaza
   crtaj_baklju (  orMj , [ -1 , 0 , 3 ]   , orSm, "odmene"    )#unutra
   crtaj_baklju (  orMj , [ -1 , 0 , -1 ]   , orSm, "odmene"    )#podrum meni
   
   
   
   
   
   

      
   
   

   
   
   
if __name__ == "__main__":    #direktan poziv
   #polukrugTunel (   iX=2 , iZ=0 , iY=0 , radius = 8 , duzina = 70 , korekcija = 0 , uspon = 0  )
   orMj = gdjeSam ()
   orSm = gdjeGledam ()
   kuca_06 (  orMj ,  orSm , iX=6 , iZ=0 , iY=0 )
   

