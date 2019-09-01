# surival house 7 x 7 from http://www.minecraftforum.net/forums/minecraft-discussion/survival-mode/290440-minecraft-survival-starter-houses
#definicija objekta i poziv rutine za crtanje
from crtanje import *		#tu je funkcija koju zovem
from crtanje2 import *		#tu je funkcija koju zovem
from mc import *			
mc = Minecraft() #inicijalizacija sustava za rad sa Minecraftom

def kuca_07 (  orMj ,  orSm , iX=0 , iZ=0 , iY=0 ) :
   orMj = premjesti_origin ( orMj , iX , iZ , iY ,  orSm ) #mice ishodiste na centar
   #clear the deck
   crtaj_kvadar ( orMj , [ -2 , -3 , -3 ]  , [ 2 , 3 , 9  ] , orSm , 0 , 0 ) # zrak
   #crta iz sredine 7 siroko 5 duboko

   crtaj_kvadar ( orMj , ( -2 , -3 , 0 )  , ( 2 , 3 , 0  ) , orSm , 4 , 0 ) #temelji od cobblestone
   crtaj_kvadar ( orMj , ( -1 , -2 , 0 )  , ( 1 , 2 , 0  ), orSm , 5 , 0 ) # blok oak wood za pod
   crtaj_kvadar ( orMj , ( -2 , 1 , 0 )  , ( -2 , 1 , 0  ), orSm , 5 , 0 ) # blok oak wood za ulaz
   
   #stupovi na coskovima 4 visoko
   for dX in ( -2 , 2 ):
      for dZ in ( -3 , 3 ):
         crtaj_deblo ( orMj , ( dX , dZ , 0 ) , ( dX , dZ , 2 ) , orSm , "gore" , blok_id = 17 , podtip = 0   )   
   #prvi i drugi i treci red naprijed nazad
   for dX in ( -2 , 2 ):
      for dZ in ( -2 , 0 , 2 ):
         crtaj_kvadar ( orMj , ( dX , dZ , 1 )  , ( dX , dZ , 3  ), orSm , 5 , 0 ) # blok oak wood za ulaz
   #prvi i drugi i treci red lijevo desno
   for dX in ( -1 , 1 ):
      for dZ in ( -3  , 3 ):
         crtaj_kvadar ( orMj , ( dX , dZ , 1 )  , ( dX , dZ , 3  ), orSm , 5 , 0 ) # blok oak wood za ulaz
   #drugi red stepenice u zidu
   crtaj_stepenice ( orMj , [ -2 , -1 , 1 ]  , [ -2 , -1 , 1  ], orSm , blok_id = 53 , rel_smjer  = "meni" , gore_dolje = "ne"  ) #zid prema meni
   crtaj_kvadar ( orMj , [ -2 , -1 , 2 ]  , [ -2 , -1 , 2  ], orSm , 102 , blok_dv = 0 ) # prozor
   crtaj_stepenice ( orMj , [ 2 , 1 , 1 ]  , [ 2 , 1 , 1  ], orSm , blok_id = 53 , rel_smjer  = "odmene" , gore_dolje = "ne"  ) #zadnji zid  desno
   crtaj_kvadar ( orMj , [ 2 , 1 , 2 ]  , [ 2 , 1 , 2  ], orSm , 102 , blok_dv = 0 ) # prozor
   crtaj_stepenice ( orMj , [ 2 , -1 , 1 ]  , [ 2 , -1 , 1  ], orSm , blok_id = 53 , rel_smjer  = "odmene" , gore_dolje = "ne"  ) #zadnji zid lijevo
   crtaj_kvadar ( orMj , [ 2 , -1 , 2 ]  , [ 2 , -1 , 2  ], orSm , 102 , blok_dv = 0 ) # prozor
   crtaj_stepenice ( orMj , [ 0 , 3 , 1 ]  , [ 0 , 3 , 1  ], orSm , blok_id = 53 , rel_smjer  = "desno" , gore_dolje = "ne"  ) # zid  desno
   crtaj_kvadar ( orMj , [ 0 , 3 , 2 ]  , [ 0 , 3 , 2  ], orSm , 102 , blok_dv = 0 ) # prozor
   crtaj_stepenice ( orMj , [ 0 , -3 , 1 ]  , [ 0 , -3 , 1  ], orSm , blok_id = 53 , rel_smjer  = "lijevo" , gore_dolje = "ne"  ) # zid lijevo  
   crtaj_kvadar ( orMj , [ 0 , -3 , 2 ]  , [ 0 , -3 , 2  ], orSm , 102 , blok_dv = 0 ) # prozor   
   

   
   #cetvrti  red stepenice u zidu
   crtaj_stepenice ( orMj , [ -2 , -1 , 3 ]  , [ -2 , -1 , 3  ], orSm , blok_id = 53 , rel_smjer  = "meni" , gore_dolje = "da"  ) #zid prema meni
   crtaj_stepenice ( orMj , [ 2 , 1 , 3 ]  , [ 2 , 1 , 3  ], orSm , blok_id = 53 , rel_smjer  = "odmene" , gore_dolje = "da"  ) #zadnji zid  desno
   crtaj_stepenice ( orMj , [ 2 , -1 , 3 ]  , [ 2 , -1 , 3  ], orSm , blok_id = 53 , rel_smjer  = "odmene" , gore_dolje = "da"  ) #zadnji zid lijevo
   crtaj_stepenice ( orMj , [ 0 , 3 , 3 ]  , [ 0 , 3 , 3  ], orSm , blok_id = 53 , rel_smjer  = "desno" , gore_dolje = "da"  ) # zid  desno
   crtaj_stepenice ( orMj , [ 0 , -3 , 3 ]  , [ 0 , -3 , 3  ], orSm , blok_id = 53 , rel_smjer  = "lijevo" , gore_dolje = "da"  ) # zid lijevo   
      

   
   #vrata
   
   crtaj_vrata ( orMj , [ -2 , 1 , 1 ]   , orSm, "meni"  , blok_id = 64  , kvaka = "desno"  )#vrata 
   
   #krov
   crtaj_stepenice ( orMj , [ -2 , -4 , 3 ]  , [ -2 , 4 , 3  ], orSm , blok_id = 53 , rel_smjer  = "meni" , gore_dolje = "ne"  ) #krov prema meni
   crtaj_stepenice ( orMj , [ 2 , -4 , 3 ]  , [ 2 , 4 , 3  ], orSm , blok_id = 53 , rel_smjer  = "odmene" , gore_dolje = "ne"  ) #krov prema meni
   crtaj_stepenice ( orMj , [ -1 , -4 , 4 ]  , [ -1 , 4 , 4  ], orSm , blok_id = 53 , rel_smjer  = "meni" , gore_dolje = "ne"  ) #krov prema meni
   crtaj_stepenice ( orMj , [ 1 , -4 , 4 ]  , [ 1 , 4 , 4  ], orSm , blok_id = 53 , rel_smjer  = "odmene" , gore_dolje = "ne"  ) #krov prema meni
   
   #rogovi
   for dZ in ( -3 , 3  ):
      crtaj_kvadar ( orMj , [ 0 , dZ , 4 ]  , [ 0 , dZ , 4  ], orSm , 5 , 0 ) # blok oak wood
   crtaj_kvadar ( orMj , (0 , -4 , 5 )  , (0 , 4 , 5  ), orSm , 126 , blok_dv = 0 ) #wooden slab u sredini
   
   crtaj_deblo ( orMj , (0 , -2 , 4 )  , (0 , 2 , 4  ) , orSm , "lijevo_desno" , blok_id = 17 , podtip = 0   ) #deblo u sredini
   
   #baklje
   crtaj_baklju (  orMj , [ 0 , -2 , 3 ]   , orSm, "desno"    )#iznad lijevog prozora
   crtaj_baklju (  orMj , [ 0 , 2 , 3 ]   , orSm, "lijevo"    )#iznad desnog prozora
   
   #podest
   crtaj_kvadar ( orMj , (-3 , -3 , 0 )  , (-4 , 3 , 0  ), orSm , 126 , blok_dv = 8 ) #wooden slab podest ulaz - gore
   crtaj_kvadar ( orMj , (-4 , 0 , 0 )  , (-4 , 4 , 0  ), orSm , 5 , 0 )  #okvir oko stepenica za ulazak na podest
   crtaj_stepenice ( orMj , (-4 , 1 , 0 )  , (-4 , 1 , 0  ), orSm , blok_id = 53 , rel_smjer  = "meni" , gore_dolje = "ne"  ) #stepenica za ulazak na podest
   
   
   
   crtaj_kvadar ( orMj , (-4 , -4 , 0 )  , (-4 , -4 , 0  ), orSm , 5 , 0 )  #lijevo kocka
   crtaj_stepenice ( orMj , (-3 , -4 , 0 )  , (-2 , -4 , 0  ), orSm , blok_id = 53 , rel_smjer  = "lijevo" , gore_dolje = "da"  ) #stepenica za ulazak na podest
   crtaj_stepenice ( orMj , (-3 , 3 , 0 )  , (-3 , 4 , 0  ), orSm , blok_id = 53 , rel_smjer  = "odmene" , gore_dolje = "ne"  ) #stepenica silazak sa podesta
   crtaj_stepenice ( orMj , (-4 , 3 , 0 )  , (-4 , 3 , 0  ), orSm , blok_id = 53 , rel_smjer  = "meni" , gore_dolje = "da"  ) #stepenica naopako pored ulaza HACK - zadnje
   crtaj_kvadar ( orMj , (-3 , -4 , 3 )  , (-4 , 4 , 3  ), orSm , 126  ) #wooden slab podest ulaz - gore

   #podest ograde
   crtaj_kvadar ( orMj , (-2 , -4 , 1 )  , (-4 , -4 , 1  ), orSm , 85 , blok_dv = 0 ) #stupci
   crtaj_kvadar ( orMj , (-4 , -4 , 1 )  , (-4 , 0 , 1  ), orSm , 85 , blok_dv = 0 ) #stupci
   crtaj_kvadar ( orMj , (-4 , 2 , 1 )  , (-4 , 4 , 1  ), orSm , 85 , blok_dv = 0 ) #stupci
   for dZ in ( -4 , 0, 2 , 4 ):
      crtaj_kvadar ( orMj , (-4 , dZ , 2 )  , (-4 , dZ , 2  ), orSm , 85 , blok_dv = 0 ) #stupci gore
   crtaj_vrataograde ( orMj ,  [ -4 , 1 , 1  ] , orSm ,  "lijevo_desno"  ) #vrata u ogradi
   
   #desni podest
   crtaj_kvadar ( orMj , (-2 , 4 , -1 )  , ( 2 , 4 , -1  ), orSm , 126 , blok_dv = 8 ) #wooden slab 
   crtaj_deblo ( orMj , (-4 , 5 , -1 )  , ( 2 , 5 , -1  ) , orSm , "gore" , blok_id = 17 , podtip = 0   ) #u zemlji
   crtaj_deblo ( orMj , (2 , 5 , 0 )  , ( 2 , 5 , 1  ) , orSm , "gore" , blok_id = 17 , podtip = 0   ) #gore
   crtaj_kvadar ( orMj , (2 , 5 , 2 )  , ( 2 , 5 , 2  ), orSm , 126 , blok_dv = 0 )#slab
   crtaj_vrataograde ( orMj ,  [ 2 , 4 , 1  ] , orSm ,  "lijevo_desno"  ) #vrata u ogradi#zadnja vrata
   crtaj_kvadar ( orMj , (-4 , 5 , 0 )  , ( 1 , 5 , 1  ), orSm , 18 , blok_dv = 0 )#grmlje
      
   #pec 
   crtaj_pec  ( orMj , [ -1 , 2 , 3 ] , [ 1 , 2 , 3 ] , orSm , "lijevo" )
   crtaj_baklju (  orMj , [ 0 , 2 , 3 ]   , orSm, "lijevo"    )#iznad desnog prozora
   #workbench
   crtaj_banak ( orMj ,( -1 , -2 , 1 ) , ( -1 , -2 , 1 ) , orSm , rel_smjer  = "meni" )
   #kutija
   crtaj_kutiju ( orMj , ( 1 , -2 , 1 ) , ( 0 , -2 , 1 ) , orSm , "desno" )
   
   #krevet
   crtaj_krevet  ( orMj , ( 1 , 0 , 1 ) , ( 1 , -1 , 1 )  , orSm , "lijevo" )
   #kutija
   crtaj_kutiju ( orMj , ( 1 , 1 , 1 ) , ( 1 , 2 , 1 ) , orSm , "meni" )   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
if __name__ == "__main__":    #direktan poziv
   
   orMj = gdjeSam ()
   orSm = gdjeGledam ()
   kuca_07 (  orMj ,  orSm , iX=8 , iZ=0 , iY=0 )
   

