# surival house  from https://www.youtube.com/watch?v=VCgZ4Y6pP0g
#definicija objekta i poziv rutine za crtanje
from crtanje import *		#
from mc import *			
mc = Minecraft() #inicijalizacija sustava za rad sa Minecraftom

def mali (  orMj ,  orSm , iX=0 , iZ=0 , iY=0 ) :
   orMj = premjesti_origin ( orMj , iX , iZ , iY ,  orSm ) #mice ishodiste na centar
   crtaj_kvadar ( orMj , ( 0 , -1 , 1 )  , ( 0 , -1 , 3  ) , orSm , 5 , 0 ) #lijevi stup
   crtaj_kvadar ( orMj , ( 0 , 1 , 1 )  , ( 0 , 1 , 3  ) , orSm , 5 , 0 ) #desni stup
   crtaj_kvadar ( orMj , [ 0,0,2 ]  , [ 0,0,2  ], orSm , 102 , blok_dv = 0 ) # prozor 
   crtaj_stepenice ( orMj , [ 0 , 0 , 3 ]  , [ 0 , 0 , 3  ], orSm , blok_id = 53 , rel_smjer  = "meni" , gore_dolje = "da"  ) #gore stepenica    
   crtaj_stepenice ( orMj , [ 0 , 0 , 1 ]  , [ 0 , 0 , 1  ], orSm , blok_id = 53 , rel_smjer  = "meni" , gore_dolje = "ne"  ) #dolje stepenica    
   
def naopake_stepenice ( orMj ,  orSm , iX=0 , iZ=0 , iY=0 , duzina_udesno = 1 ):
   orMj = premjesti_origin ( orMj , iX , iZ , iY ,  orSm )     #mice ishodiste na prvu , krajnju lijevu stepenicu
   crtaj_stepenice ( orMj , ( 0 , 0 , 0 )  , ( 0 , 0 + duzina_udesno , 0  ), orSm , blok_id = 53 , rel_smjer  = "meni" , gore_dolje = "da"  )
   
def uspravne_stepenice ( orMj ,  orSm , iX=0 , iZ=0 , iY=0 , duzina_udesno = 1 ):
   orMj = premjesti_origin ( orMj , iX , iZ , iY ,  orSm )     #mice ishodiste na prvu , krajnju lijevu stepenicu
   crtaj_stepenice ( orMj , ( 0 , 0 , 0 )  , ( 0 , 0 + duzina_udesno , 0  ), orSm , blok_id = 53 , rel_smjer  = "meni" , gore_dolje = "ne"  )


def kuca_09 (  orMj ,  orSm , iX=0 , iZ=0 , iY=0 ) :
   orMj = premjesti_origin ( orMj , iX , iZ , iY ,  orSm ) #mice ishodiste na centar

   #clear the deck
   crtaj_kvadar ( orMj , ( 1 , -4 , -1 )  , ( 9 , 4 , 11  ) , orSm , 0 , 0 ) # zrak
   
   #temelj
   crtaj_kvadar ( orMj , ( 1 , -4 , -1 )  , ( 9 , 4 , -1  ) , orSm , 13 , 0 ) # gravel
   
   for dX in ( 1 , 4 , 9  ):
      for dZ in ( -4 , 0 , 4 ):
         crtaj_deblo ( orMj , ( dX , dZ , 0 ) , ( dX , dZ , 1 ) , orSm , "gore" , blok_id = 17 , podtip = 0   ) # stupovi
   
   #okviri dolje
   naopake_stepenice ( orMj ,  orSm , iX=4 , iZ=1 , iY=1 , duzina_udesno = 2 ) 
   naopake_stepenice ( orMj ,  orSm , iX=1 , iZ=-3 , iY=1 , duzina_udesno = 2 )  
   ortPom = ortUdesno ( orSm )
   naopake_stepenice ( orMj ,  ortPom , iX=-4 , iZ=-3 , iY=1 , duzina_udesno = 1 )  
   naopake_stepenice ( orMj ,  ortPom , iX=-4 , iZ=-8 , iY=1 , duzina_udesno = 3 )  
   ortPom = ortUdesno ( ortPom )
   naopake_stepenice ( orMj ,  ortPom , iX=-9 , iZ=1 , iY=1 , duzina_udesno = 2 )  
   naopake_stepenice ( orMj ,  ortPom , iX=-9 , iZ=-3 , iY=1 , duzina_udesno = 2 )  
   ortPom = ortUdesno ( ortPom )   
   naopake_stepenice ( orMj ,  ortPom , iX=-4 , iZ=5 , iY=1 , duzina_udesno = 3 ) 
   #blok podest iza ulaznih stepenica
   crtaj_kvadar ( orMj , ( 2 , -1 , 1 )  , ( 4 , -3 , 1  ), orSm , 5 , 0 ) # blok oak wood za pod
   #ulazne stepenice
   ortPom = ortUlijevo ( orSm )
   uspravne_stepenice ( orMj ,  ortPom , iX=0 , iZ=2 , iY=0 , duzina_udesno = 1 ) 
   uspravne_stepenice ( orMj ,  ortPom , iX=1 , iZ=2 , iY=1 , duzina_udesno = 1 ) 
   #baklje ispod
   crtaj_baklju (  orMj , [ 5 , 0 , 0 ]   , orSm, "gore"    )
   crtaj_baklju (  orMj , [ 8 , 0 , 0 ]   , orSm, "gore"    )
   #lisce ispod
   crtaj_kvadar ( orMj , ( 4 , 1 , 0 )  , ( 4 , 3 , 0  ) , orSm , 18 , 0 )
   crtaj_kvadar ( orMj , ( 5 , 4 , 0 )  , ( 8 , 4 , 0  ) , orSm , 18 , 0 )
   crtaj_kvadar ( orMj , ( 9 , -3 , 0 )  , ( 9 , -1 , 0  ) , orSm , 18 , 0 )
   crtaj_kvadar ( orMj , ( 9 , 3 , 0 )  , ( 9 , 1 , 0  ) , orSm , 18 , 0 )
   crtaj_kvadar ( orMj , ( 5 , -4 , 0 )  , ( 8 , -4 , 0  ) , orSm , 18 , 0 )
   crtaj_kvadar ( orMj , ( 2 , -4 , 0 )  , ( 3 , -4 , 0  ) , orSm , 18 , 0 )
   crtaj_kvadar ( orMj , ( 1 , -3 , 0 )  , ( 1 , -1 , 0  ) , orSm , 18 , 0 )
   crtaj_kvadar ( orMj , ( 2 , 4 , 0 )  , ( 3 , 4 , 0  ) , orSm , 18 , 0 )
   #blok ispod sobe
   crtaj_kvadar ( orMj , ( 5 , -3 , 1 )  , ( 8 , 3 , 1  ), orSm , 5 , 0 ) # blok oak wood za pod
   #zatvaranje tavana 
   for dX in ( 4 , 9  ):
         crtaj_kvadar ( orMj , ( dX , -2 , 5 )  , ( dX , 2 , 6  ), orSm , 5 , 0 ) # blok oak wood
   #stupci
   for dZ in ( -4 , 0 ):   #najbliza 2 idu jedan gore
         crtaj_deblo ( orMj , ( 1 , dZ , 2 ) , ( 1 , dZ , 2 ) , orSm , "gore" , blok_id = 17 , podtip = 0   ) # stupovi
   for dZ in ( -4 , 4 ): #vanjski idu 2 gore
      for dX in ( 4 , 9 ):
         crtaj_deblo ( orMj , ( dX , dZ , 2 ) , ( dX , dZ , 3 ) , orSm , "gore" , blok_id = 17 , podtip = 0   ) # stupovi
   
   for dX in ( 4 , 9 ):   #srednji 6 gore
      crtaj_deblo ( orMj , ( dX , 0 , 2 ) , ( dX , 0 , 7 ) , orSm , "gore" , blok_id = 17 , podtip = 0   ) # stupovi
   #krajnji desni zid
   crtaj_kvadar ( orMj , ( 5 , 4 , 2 )  , ( 8 , 4 , 3  ), orSm , 5 , 0 ) # blok oak wood za zid
   #krajnji lijevi zid
   crtaj_kvadar ( orMj , ( 5 , -4 , 2 )  , ( 8 , -4 , 3  ), orSm , 5 , 0 ) # blok oak wood za zid
   #desno od predulaza
   mali (  orMj ,  orSm , iX=4 , iZ=2 , iY=1 )
   # iza zidovi
   ortPom = ortUdesno ( ortUdesno ( orSm ) )
   mali (  orMj ,  ortPom , iX=-9 , iZ=-2 , iY=1 )
   mali (  orMj ,  ortPom , iX=-9 , iZ=2 , iY=1 )
   #ulaz iza podesta
   crtaj_kvadar ( orMj , ( 4 , -1 , 2 )  , ( 4 , -3 , 4  ), orSm , 5 , 0 ) # blok oak wood za zid
   crtaj_vrata ( orMj , ( 4 , -2 , 2 )   , orSm, "odmene"  , blok_id = 64  , kvaka = "desno"  )#vrata
   #ograda oko podesta
   crtaj_kvadar ( orMj , ( 1 , -1 , 2 )  , ( 1 , -3 , 2  ), orSm , 85 , blok_dv = 0 ) #stupci ograda 
   crtaj_kvadar ( orMj , ( 2 , -4 , 2 )  , ( 3 , -4 , 2  ), orSm , 85 , blok_dv = 0 ) #stupci ograda 
   #lijevi i desni krov
   ortPomL = ortUdesno ( orSm )
   ortPomD = ortUlijevo ( orSm )
   for br in range ( 0 , 5 ):
      uspravne_stepenice ( orMj ,  ortPomL , iX=-5 + br , iZ=-10 , iY=3 + br , duzina_udesno = 7 )
      uspravne_stepenice ( orMj ,  ortPomD , iX=-5 + br , iZ=3 , iY=3 +br, duzina_udesno = 7 )
   crtaj_kvadar ( orMj ,[ 4 , 0 , 8 ]  , [ 9 , 0 , 8  ], orSm , 126 , blok_dv = 0 )#slab iznad na spoju krovova
   crtaj_stepenice ( orMj , ( 3 , 0 , 8  )  , ( 3 , 0 , 8  ), orSm , blok_id = 53 , rel_smjer  = "odmene" , gore_dolje = "ne"  ) # ukras na krovu
   crtaj_stepenice ( orMj , ( 10 , 0 , 8  )  , ( 10 , 0 , 8  ), orSm , blok_id = 53 , rel_smjer  = "odmene" , gore_dolje = "ne"  ) # ukras na krovu
   #police unutra
   for dX in ( 5 , 8  ):
      crtaj_kvadar ( orMj ,( dX , -3 , 4 )  , ( dX , 3 , 4  ), orSm , 126 , blok_dv = 8 )#slab
   for corr in ( -1 , 1 ):   #kutije na policama
      crtaj_kutiju ( orMj , ( 5 , -2 * corr , 5 ) , ( 5 , -1 * corr , 5 ) , orSm , "odmene" )
      crtaj_kutiju ( orMj , ( 5 , -1 * corr , 6 ) , ( 5 , -1 * corr , 6 ) , orSm , "odmene" )
      crtaj_kutiju ( orMj , ( 8 , -2 * corr , 5 ) , ( 8 , -1 * corr , 5 ) , orSm , "meni" )
      crtaj_kutiju ( orMj , ( 8 , -1 * corr , 6 ) , ( 8 , -1 * corr , 6 ) , orSm , "meni" )
   crtaj_kvadar ( orMj , ( 5 , 0 , 5 )  , ( 5 , 0 , 5  ), orSm , 145 , blok_dv = 0 ) #anvil
   
   
   #kamin
   crtaj_kvadar ( orMj , ( 8 , -1 , 2 )  , ( 8 , 1 , 2  ), orSm , 4 , blok_dv = 0 ) #cobblestone
   crtaj_pec  ( orMj , ( 8 , 0 , 2 ) , ( 8 , 0 , 2 ) , orSm , "meni" )
   crtaj_stepenice ( orMj , [ 8 , -1 , 3 ]  , [ 8 , -1 , 3  ], orSm , blok_id = 67 , rel_smjer  = "lijevo" , gore_dolje = "ne"  )#lijeva kocka
   crtaj_stepenice ( orMj , [ 8 , 0 , 3 ]  , [ 8 , 0 , 3  ], orSm , blok_id = 67 , rel_smjer  = "meni" , gore_dolje = "da"  )#srednja kocka
   crtaj_stepenice ( orMj , [ 8 , 1 , 3 ]  , [ 8 , 1 , 3  ], orSm , blok_id = 67 , rel_smjer  = "desno" , gore_dolje = "ne"  )#desna kocka
   crtaj_kvadar ( orMj , ( 8 , 0 , 4 )  , ( 8 , 0 , 8  ), orSm , 4 , blok_dv = 0 ) #cobblestone dimnjak
   crtaj_kvadar ( orMj , ( 8 , 0 , 9 )  , ( 8 , 0 , 9  ), orSm , 139 , blok_dv = 0 ) # 139 vrh dimnjaka
   crtaj_kvadar ( orMj , ( 8 , 0 , 4 )  , ( 8 , 0 , 4  ), orSm , 89 , blok_dv = 0 ) #moja lampa
   crtaj_kvadar ( orMj , ( 8 , 2 , 2 )  , ( 8 , 2 , 2  ), orSm , 47 , blok_dv = 0 ) # bookshelf
   crtaj_krevet  ( orMj , [ 7 , 3 , 2 ]  , [ 8 , 3 , 2  ], orSm , rel_smjer = "odmene"  )
   
   
   
   #svod iznad podesta
   crtaj_baklju (  orMj , ( 3 , -3 , 2 )   , orSm, "gore"    ) #baklja ispod svoda
   crtaj_kvadar ( orMj ,( 3 , -4 , 3 )  , ( 1 , -4 , 3  ), orSm , 126 , blok_dv = 0 )#slab
   crtaj_kvadar ( orMj ,( 3 , -4 , 3 )  , ( 3 , -4 , 3  ), orSm , 126 , blok_dv = 8 )#slab popuna
   crtaj_kvadar ( orMj ,( 3 , -3 , 3 )  , ( 1 , -3 , 3  ), orSm , 126 , blok_dv = 8 )#slab
   crtaj_kvadar ( orMj , ( 3 , -3 , 4 )  , ( 3 , -3 , 4  ), orSm , 5 , 0 ) # popuna
   crtaj_kvadar ( orMj ,( 3 , -2 , 4 )  , ( 1 , -2 , 4  ), orSm , 126 , blok_dv = 0 )#slab
   crtaj_kvadar ( orMj ,( 3 , -2 , 4 )  , ( 3 , -2 , 4  ), orSm , 126 , blok_dv = 8 )#slab popuna
   crtaj_kvadar ( orMj , ( 3 , -2 , 5 )  , ( 3 , -2 , 5  ), orSm , 5 , 0 ) # popuna
   crtaj_kvadar ( orMj ,( 3 , -1 , 4 )  , ( 1 , -1 , 4  ), orSm , 126 , blok_dv = 8 )#slab
   crtaj_kvadar ( orMj ,( 3 , -1 , 5 )  , ( 3 , -1 , 5  ), orSm , 126 , blok_dv = 0 )#slab
   crtaj_kvadar ( orMj ,( 3 , 0 , 5 )  , ( 1 , 0 , 5  ), orSm , 126 , blok_dv = 0 )#slab
   crtaj_kvadar ( orMj , ( 1 , 0 , 3  )  , ( 1 , 0 , 4  ), orSm , 85 , blok_dv = 0 ) #stupci ograda
   
   #ulazni stupac
   crtaj_kvadar ( orMj ,( 1 , 4 , 1 )  , ( 1 , 4 , 1  ), orSm , 126 , blok_dv = 0 )#slab
   
   #radna polica lijevo od vrata
   crtaj_kvadar ( orMj ,( 5 , -3 , 2 )  , ( 8 , -3 , 2  ), orSm , 126 , blok_dv = 8 )#slab polica
   crtaj_banak ( orMj ,( 6 , -3 , 2 ) , ( 6 , -3 , 2 ) , orSm , rel_smjer  = "odmene" )
   crtaj_kutiju ( orMj , ( 7 , -3 , 1 ) , ( 8 , -3 , 1 ) , orSm , "desno" )
   
   
   
   
   
   

if __name__ == "__main__":    #direktan poziv
   
   orMj = gdjeSam ()
   orSm = gdjeGledam ()
   kuca_09 (  orMj ,  orSm , iX=8 , iZ=0 , iY=0 )
   
"""
def dugonja (  orMj ,  orSm , iX=0 , iZ=0 , iY=0 ) :
   orMj = premjesti_origin ( orMj , iX , iZ , iY ,  orSm ) #mice ishodiste na centar
   crtaj_kvadar ( orMj , ( 0 , -1 , 1 )  , ( 0 , -1 , 4  ) , orSm , 5 , 0 ) #lijevi stup
   crtaj_kvadar ( orMj , ( 0 , 1 , 1 )  , ( 0 , 1 , 4  ) , orSm , 5 , 0 ) #desni stup
   crtaj_stepenice ( orMj , [ 0 , 0 , 1 ]  , [ 0 , 0 , 1  ], orSm , blok_id = 53 , rel_smjer  = "meni" , gore_dolje = "ne"  ) #dolje stepenica
   crtaj_stepenice ( orMj , [ 0 , 0 , 4 ]  , [ 0 , 0 , 4  ], orSm , blok_id = 53 , rel_smjer  = "meni" , gore_dolje = "da"  ) #gore stepenica  
   crtaj_kvadar ( orMj , [ 0,0,2 ]  , [ 0,0,3  ], orSm , 102 , blok_dv = 0 ) # prozor   
   
def mali (  orMj ,  orSm , iX=0 , iZ=0 , iY=0 ) :
   orMj = premjesti_origin ( orMj , iX , iZ , iY ,  orSm ) #mice ishodiste na centar
   crtaj_kvadar ( orMj , ( 0 , -1 , 1 )  , ( 0 , -1 , 3  ) , orSm , 5 , 0 ) #lijevi stup
   crtaj_kvadar ( orMj , ( 0 , 1 , 1 )  , ( 0 , 1 , 3  ) , orSm , 5 , 0 ) #desni stup
   crtaj_kvadar ( orMj , [ 0,0,2 ]  , [ 0,0,2  ], orSm , 102 , blok_dv = 0 ) # prozor 
   crtaj_stepenice ( orMj , [ 0 , 0 , 3 ]  , [ 0 , 0 , 3  ], orSm , blok_id = 53 , rel_smjer  = "meni" , gore_dolje = "da"  ) #gore stepenica      

def kuca_08 (  orMj ,  orSm , iX=0 , iZ=0 , iY=0 ) :
   orMj = premjesti_origin ( orMj , iX , iZ , iY ,  orSm ) #mice ishodiste na centar

   
   
   
   crtaj_kvadar ( orMj , ( -4 , 1 , 0 )  , ( 4 , 3 , 0  ) , orSm , 4 , 0 ) #temelji od cobblestone desni dio
   crtaj_kvadar ( orMj , ( 0 , -1 , 0 )  , ( 7 , -5 , 0  ) , orSm , 4 , 0 ) #temelji od cobblestone lijevi dio
   crtaj_kvadar ( orMj , ( 1 , 5 , 0 )  , ( 3 , 5 , 0  ) , orSm , 4 , 0 ) #frcoljak
   
   
   #stupci
   for dX in ( -4 , 0 , 4 ):
      for dZ in ( 0 , 4 ) :
         crtaj_deblo ( orMj , ( dX , dZ , 0 ) , ( dX , dZ , 3 ) , orSm , "gore" , blok_id = 17 , podtip = 0   ) # stupovi u sredini
   crtaj_deblo ( orMj , (  0 , -5 , 0 ) , (  0 , -5 , 3 ) , orSm , "gore" , blok_id = 17 , podtip = 0   )   #lijevi krajnji stup
   crtaj_deblo ( orMj , (  0 , 6 , 0 ) , (  0 , 6 , 3 ) , orSm , "gore" , blok_id = 17 , podtip = 0   ) #desni prednji stup
   crtaj_deblo ( orMj , (  4 , 6 , 0 ) , (  4 , 6 , 3 ) , orSm , "gore" , blok_id = 17 , podtip = 0   ) #lijevi prednji stup
   
   #pod
   crtaj_kvadar ( orMj , ( -2 , 1 , 0 )  , ( -2 , 3 , 0  ), orSm , 5 , 0 ) # blok oak wood za pod kriz dolje desno
   crtaj_kvadar ( orMj , ( -1 , 2 , 0 )  , ( -3 , 2 , 0  ), orSm , 5 , 0 ) # blok oak wood za pod
   
   crtaj_kvadar ( orMj , ( 0 , 1 , 0 )  , ( 0 , 3 , 0  ), orSm , 5 , 0 ) # blok oak wood za pod frcoljak iznad kriz dolje desno
   
   crtaj_kvadar ( orMj , ( 1 , -4 , 0 )  , ( 3 , 4 , 0  ), orSm , 5 , 0 ) # blok oak wood centralni
   crtaj_kvadar ( orMj , ( 4 , -2 , 0 )  , ( 6 , -4 , 0  ), orSm , 5 , 0 ) # blok oak wood gore lijevo
   crtaj_kvadar ( orMj , ( 4 , -1 , 0 )  , ( 4 , -1 , 0  ), orSm , 5 , 0 ) # blok oak kocka
   
   #desni podest
   crtaj_stepenice ( orMj , [ -1 , 6 , 0 ]  , [ -4 , 6 , 0  ], orSm , blok_id = 53 , rel_smjer  = "desno" , gore_dolje = "da"  ) #stepenice desno na kraju
   crtaj_kvadar ( orMj ,[ -1 , 6 , 3 ]  , [ -5 , 6 , 3  ], orSm , 126 , blok_dv = 0 )#slab iznad
   crtaj_kvadar ( orMj , ( -5 , 4 , 0 )  , ( -5 , 6 , 0  ), orSm , 5 , 0 )   #podest naprijed # blok oak wood
   crtaj_stepenice ( orMj , [ -5 , 5 , 0 ]  , [ -5 , 5 , 0  ], orSm , blok_id = 53 , rel_smjer  = "meni" , gore_dolje = "ne"  ) # prednja stepenica
   crtaj_kvadar ( orMj , ( -4 , 5 , 0 )  , ( 0 , 5 , 0  ), orSm , 5 , 0 )   #podest sredina # blok oak wood
   crtaj_kvadar ( orMj ,[ -5 , 5 , 3 ]  , [ 0 , 5 , 3  ], orSm , 126 , blok_dv = 0 )#slab iznad
   crtaj_kvadar ( orMj , ( -3 , 4 , 0 )  , ( -1 , 4 , 0  ), orSm , 5 , 0 )   #podest lijevi kraj # blok oak wood
   crtaj_kvadar ( orMj , (-1 , 6 , 1 )  , (-4 , 6 , 1  ), orSm , 85 , blok_dv = 0 ) #stupci ograda desno
   for dZ in ( 4 , 6 ) :
      crtaj_kvadar ( orMj , (-5 , dZ , 1 )  , (-5 , dZ , 2  ), orSm , 85 , blok_dv = 0 ) #stupci ograda napres podest
   
   ortPom = ortUlijevo ( orSm )
   dugonja (  orMj ,  ortPom , iX=-5 , iZ=2 , iY=0 )     
   crtaj_baklju (  orMj , [ 0 , 5 , 2 ]   , orSm, "meni"    )#

   #predvorje
   mali (  orMj ,  orSm , iX=-4 , iZ=2 , iY=0 )  #prednji
   crtaj_stepenice ( orMj , [ -4 , 2 , 1 ]  , [ -4 , 2 , 1  ], orSm , blok_id = 53 , rel_smjer  = "meni" , gore_dolje = "ne"  ) #dolje stepenica
   ortPom = ortUdesno ( orSm )
   mali (  orMj ,  ortPom , iX=3 , iZ=2 , iY=0 )  #desni
   ortPom = ortUlijevo ( orSm )   
   mali (  orMj ,  ortPom , iX=-1 , iZ=-2 , iY=0 )  #lijevi
   ortPom = ortUdesno ( ortUdesno ( orSm ) )
   mali (  orMj ,  ortPom , iX=-4 , iZ=-2 , iY=0 )  #zadnji
   crtaj_stepenice ( orMj , [ 4 , 2 , 1 ]  , [ 4 , 2 , 1  ], orSm , blok_id = 53 , rel_smjer  = "odmene" , gore_dolje = "ne"  ) #dolje stepenica
   crtaj_vrata ( orMj , [ -2 , 3 , 1 ]   , orSm, "desno"  , blok_id = 64  , kvaka = "desno"  )#vrata
   crtaj_vrata ( orMj , [ -2 , 1 , 1 ]   , orSm, "lijevo"  , blok_id = 64  , kvaka = "lijevo"  )#vrata
   crtaj_kvadar ( orMj , ( 0 , 2 , 4 )  , ( -3 , 2 , 4  ) , orSm , 5 , 0 ) #popuna stropa
   crtaj_baklju (  orMj , [ -3 , 2 , 3 ]   , orSm, "odmene"    )#
   
   #lijevi podest
   crtaj_stepenice ( orMj , [ -3 , 0 , 0 ]  , [ -3 , -7 , 0  ], orSm , blok_id = 53 , rel_smjer  = "meni" , gore_dolje = "da"  ) #stepenice lijevo napred
   crtaj_kvadar ( orMj , [ -3 , 0 , 1 ]  , [ -3 , -7 , 1  ], orSm , 85 , 0 )   #ograda
   crtaj_kvadar ( orMj , [ -3 , 0 , 2 ]  , [ -3 , 0 , 2 ]  , orSm , 85 , 0 )   #ograda
   crtaj_kvadar ( orMj , [ -2 , 0 , 0 ]  , [ -1 , -6 , 0  ], orSm , 5 , 0 )   #chep
   crtaj_stepenice ( orMj , [ -3 , -7 , 0 ]  , [ 4 , -7 , 0  ], orSm , blok_id = 53 , rel_smjer  = "lijevo" , gore_dolje = "da"  ) #stepenice lijevo lijevo
   crtaj_kvadar ( orMj , [ -3 , -7 , 1 ]  , [ 4 , -7 , 1  ], orSm , 85 , 0 )   #ograda
   crtaj_kvadar ( orMj ,  [ -2 , -6 , 0 ]  , [ 3 , -6 , 0  ], orSm , 5 , 0 )   #chep
   crtaj_stepenice ( orMj , [ 4 , -6 , 0 ]  , [ 4 , -6 , 0  ], orSm , blok_id = 53 , rel_smjer  = "odmene" , gore_dolje = "da"  )
   crtaj_kvadar ( orMj , [ 4 , -6 , 1 ]  , [ 4 , -6 , 3  ], orSm , 85 , 0 )   #ograda
   
   crtaj_kvadar ( orMj , [ -3 , -7 , 2  ]  , [ -3 , -7 , 2 ], orSm , 85 , 0 )   #ograda
   crtaj_kvadar ( orMj ,[ -2 , 0 , 3 ]  , [ -3 , -7 , 3 ], orSm , 126 , blok_dv = 0 )#slab iznad
   crtaj_stepenice ( orMj , [ -1 , -7 , 3 ]  , [ 0 , -7 , 3  ], orSm , blok_id = 53 , rel_smjer  = "lijevo" , gore_dolje = "ne"  )
   crtaj_kvadar ( orMj , [ 0 , -7 , 2  ]  , [ 0 , -7  , 2 ], orSm , 85 , 0 )   #ograda
   crtaj_baklju (  orMj , [ -1 , 0 , 2 ]   , orSm, "lijevo"    )#
   crtaj_baklju (  orMj , [ 0 , -6 , 2 ]   , orSm, "lijevo"    )#
   
   
   
   
   
   #predvorje krov
   crtaj_stepenice ( orMj , [ -1 , 4 , 3 ]  , [ -5 , 4 , 3  ], orSm , blok_id = 53 , rel_smjer  = "desno" , gore_dolje = "ne"  ) #
   crtaj_stepenice ( orMj , [ -1 , 3 , 4 ]  , [ -5 , 3 , 4  ], orSm , blok_id = 53 , rel_smjer  = "desno" , gore_dolje = "ne"  ) #
   crtaj_kvadar ( orMj , (0 , 2 , 5 )  , (-4 , 2 , 5  ), orSm , 126 , blok_dv = 0 ) #wooden slab u sredini
   crtaj_stepenice ( orMj , [ 0 , 1 , 4 ]  , [ -5 , 1 , 4  ], orSm , blok_id = 53 , rel_smjer  = "lijevo" , gore_dolje = "ne"  ) #
   crtaj_stepenice ( orMj , [ -1 , 0 , 3 ]  , [ -5 , 0 , 3  ], orSm , blok_id = 53 , rel_smjer  = "lijevo" , gore_dolje = "ne"  ) #
   crtaj_kvadar ( orMj , (-5 , 2 , 4  )  , (-5 , 2 , 4  ), orSm , 5 , 0 )   #chep
   crtaj_stepenice ( orMj , (-5 , 2 , 5  )  , (-5 , 2 , 5  ), orSm , blok_id = 53 , rel_smjer  = "odmene" , gore_dolje = "ne"  ) # ukras na chepu
   
   
   #desna soba
   
   #krov
   crtaj_stepenice ( orMj , [ 0 , 3 , 4 ]  , [ 0 , 7 , 4  ], orSm , blok_id = 53 , rel_smjer  = "meni" , gore_dolje = "ne"  ) #
   crtaj_baklju (  orMj , [ 3 , 3 , 3 ]   , orSm, "meni"    )#iznad
   
   #lijeva soba
   #lijevi prednji zid
   crtaj_kvadar ( orMj , ( 0 , -4 , 1 )  , ( 0 , -1 , 3  ), orSm , 5 , 0 ) # blok oak wood 
   crtaj_kvadar ( orMj , [ 0 , -3 , 2 ]  , [ 0 , -2 , 2  ], orSm , 102 , blok_dv = 0 ) # prozor
   crtaj_stepenice ( orMj , [ 0 , -3 , 1 ]  , [ 0 , -2 , 1  ], orSm , blok_id = 53 , rel_smjer  = "meni" , gore_dolje = "ne"  ) #dolje stepenice
   #prednji krov
   crtaj_stepenice ( orMj , [ -1 , -6 , 3 ]  , [ -1 , -1 , 3  ], orSm , blok_id = 53 , rel_smjer  = "meni" , gore_dolje = "ne"  ) #
   crtaj_stepenice ( orMj , [ 0 , -6 , 4 ]  , [ 0 , 0 , 4  ], orSm , blok_id = 53 , rel_smjer  = "meni" , gore_dolje = "ne"  ) #
   crtaj_stepenice ( orMj , [ 1 , -6 , 5 ]  , [ 1 , 7 , 5  ], orSm , blok_id = 53 , rel_smjer  = "meni" , gore_dolje = "ne"  ) #zajednicki krov lijeve i desne sobe
   crtaj_deblo ( orMj , [ 2 , -5 , 5 ]  , [ 2 , 6 , 5  ] , orSm , "lijevo_desno" , blok_id = 17 , podtip = 0   ) #deblo u sredini
   crtaj_kvadar ( orMj , [ 2 , -6 , 6 ]  , [ 2 , 7 , 6  ], orSm , 126 , blok_dv = 0 ) #wooden slab u sredini na deblu
   crtaj_stepenice ( orMj , [ 2 , -6 , 6 ]  , [ 2 , -6 , 6 ], orSm , blok_id = 53 , rel_smjer  = "desno" , gore_dolje = "ne"  ) # ukras na deblu lijevo
   crtaj_stepenice ( orMj , [  2 , 7 , 6 ]  , [ 2 , 7 , 6  ], orSm , blok_id = 53 , rel_smjer  = "lijevo" , gore_dolje = "ne"  ) # ukras na deblu desno
   crtaj_stepenice ( orMj , [ 3 , -6 , 5 ]  , [ 3 , 7 , 5  ], orSm , blok_id = 53 , rel_smjer  = "odmene" , gore_dolje = "ne"  ) #zajednicki krov lijeve i desne nazad
   crtaj_stepenice ( orMj , [ 4 , -6 , 4 ]  , [ 4 , 7 , 4  ], orSm , blok_id = 53 , rel_smjer  = "odmene" , gore_dolje = "ne"  ) #zajednicki krov lijeve i desne nazad
   
   #lijevi krajnji zid
   ortPom = ortUdesno ( orSm )
   dugonja (  orMj ,  ortPom , iX=-5 , iZ=-2 , iY=0 )   
   
   #zadnja soba
   for br in range (0,3):
      for dZ in (-1 , -5 ):
         crtaj_kvadar ( orMj , ( 4+br , dZ , 1 )  , ( 4+br , dZ , 3 - br  ), orSm , 5 , 0 ) # blok oak wood
   for br in range (0,4):
      crtaj_stepenice ( orMj , ( 5+br , 0 , 3 - br )  , ( 5+br , -6 , 3 - br  ), orSm , blok_id = 53 , rel_smjer  = "odmene" , gore_dolje = "ne"  )
         
   crtaj_krevet  ( orMj , [ 5 , -2 , 1 ]  , [ 6 , -2 , 1  ], orSm , rel_smjer = "odmene"  )
   crtaj_krevet  ( orMj , [ 5 , -4 , 1 ]  , [ 6 , -4 , 1  ], orSm , rel_smjer = "odmene"  )
   
   crtaj_kutiju ( orMj , ( 1 , -4 , 1 ) , ( 1 , -3 , 1 ) , orSm , "odmene" )
   crtaj_kutiju ( orMj , ( 1 , -1 , 1 ) , ( 1 , 0 , 1 ) , orSm , "odmene" )
   
   crtaj_pec  ( orMj , ( 1 , -2 , 1 ) , ( 1 , -2 , 1 ) , orSm , "odmene" )
   
   crtaj_banak ( orMj ,( 2 , -2 , 0 ) , ( 2 , -2 , 0 ) , orSm , rel_smjer  = "odmene" )
   
   crtaj_baklju (  orMj , [ 1 , -3 , 3]   , orSm, "odmene"    )#iznad lijevog prozora  
   crtaj_stepenice ( orMj , [ 1 , -4 , 4 ]  , [ 1 , 4 , 4  ], orSm , blok_id = 53 , rel_smjer  = "odmene" , gore_dolje = "da"  )
   crtaj_stepenice ( orMj , [ 3 , -4 , 4 ]  , [ 3 , 4 , 4  ], orSm , blok_id = 53 , rel_smjer  = "meni" , gore_dolje = "da"  )
   crtaj_deblo ( orMj , (  1 , 0 , 4 ) , (  3, 0 , 4 ) , orSm , "naprijed_nazad" , blok_id = 17 , podtip = 0   ) #

   
         
   
   

   
   
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
   
   """
   
   
   
   
   
   
   
   
   
   
   
   
   

   

