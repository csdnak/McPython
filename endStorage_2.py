
import time 
from crtanje import *		#tu je funkcija koju zovem
from mc import *		

def modul_kraj2 (  orMj ,  orSm , iX=0 , iZ=0 , iY=0  ,  materijal = 98, dv = 0  , kutija = "kutija"  ):

   dX = 0
   orMj = premjesti_origin ( orMj , iX , iZ , iY ,  orSm ) #mice gdje treba, crta ispred toon-a 

   
   if ( kutija == "kutija" ) :
      kmat = 54
   else :
      kmat = 146
   crtaj_hopper    ( orMj , [ 3 , 0, 4 ]  , [ 3 ,  0 , 4  ] , orSm , "desno" ) # hopper razvodnik
   
   
   
   crtaj_kutiju ( orMj , [ 1 , 0, 0 ]  , [ 2 ,  0 , 3  ] , orSm , rel_smjer  = "meni" , blok_id = kmat     )
   crtaj_hopper    ( orMj , [ 3 , 0, 3 ]  , [ 3 ,  0 , 0  ] , orSm , "meni" ) # hopperi iza kutije
   crtaj_comparator ( orMj , [ 0   , 0, 0 ]  , [ 0   ,  0 , 0 ]  , orSm , rel_smjer  = "meni" ) #ima li stvari u kutiji
   

def modul_sorter2 (  orMj ,  orSm , iX=0 , iZ=0 , iY=0  ,  materijal = 98, dv = 0  , kutija = "kutija" , crtaj_kutije = "da" ):

   orMj = premjesti_origin ( orMj , iX , iZ , iY ,  orSm ) #mice gdje treba, crta ispred kutija
   if crtaj_kutije == "da" :
      if ( kutija == "kutija" ) :
         kmat = 54
      else :
         kmat = 146
      crtaj_kutiju ( orMj , [ 3   , 0, 2 ]  , [ 4   ,  0 , 2  ] , orSm , rel_smjer  = "desno" , blok_id = kmat     )
      crtaj_hopper    ( orMj , [ 3   , 0, 1 ]  , [ 3   ,  0 , 0  ] , orSm , "meni" ) # hopper ispod kutije
      crtaj_kutiju ( orMj , [ 1   , 0, 0 ]  , [ 2   ,  0 , 1  ] , orSm , rel_smjer  = "desno" , blok_id = kmat     )
      crtaj_stepenice ( orMj , ( 1   , 0 ,  2  ) , ( 1   , 0 ,  2  ) , orSm , blok_id = 53 , rel_smjer  = "odmene" , gore_dolje = "ne"  )
      crtaj_comparator ( orMj , [ 0   , 0, 0 ]  , [ 0   ,  0 , 0 ]  , orSm , rel_smjer  = "meni" ) #ima li stvari u kutiji
   crtaj_kvadar ( orMj , [ 8   , 0, 0 ]  , [ 8   , 0 , 0  ] , orSm , materijal , 2 ) # doljnji blok
   crtaj_kvadar ( orMj , [ 7   , 0, 1 ]  , [ 9   , 0 , 1  ] , orSm , materijal , 2 ) # srednji blokovi
   crtaj_kvadar ( orMj , [ 6   , 0, 2 ]  , [ 8   , 0 , 2  ] , orSm , materijal , 2 ) # gornji blokovi
   
   crtaj_repeater ( orMj , [ 8   , 0, 1 ]  , [ 8   ,  0 , 1  ]  , orSm , rel_smjer  = "meni" )
   crtaj_redstonetorch ( orMj , [ 6   , 0, 1 ]  ,  orSm  , "meni" )
   
   crtaj_redstonedust ( orMj , [ 9   , 0, 2 ]  , [ 9   ,  0 , 2  ] , orSm )
   
   crtaj_redstonedust ( orMj , [ 8   , 0, 3 ]  , [ 7   ,  0 , 3  ] , orSm )
   crtaj_comparator ( orMj , [ 6   , 0, 3 ]  , [ 6   ,  0 , 3 ]  , orSm , rel_smjer  = "odmene" )
   
   crtaj_hopper    ( orMj , [ 5   , 0, 4 ]  , [ 5   ,  0 , 4  ] , orSm , "desno" ) # gornji
   
   sto =  '{TransferCooldown:0,Items:[0:{Slot:0b,id:"item_frame",Count:1b,Damage:0s,},1:{Slot:1b,id:"flower_pot",Count:1b,Damage:0s,tag:{display:{Name:"Bla Filler"}}},2:{Slot:2b,id:"flower_pot",Count:1b,Damage:0s,tag:{display:{Name:"Bla Filler"}}},3:{Slot:3b,id:"flower_pot",Count:1b,Damage:0s,tag:{display:{Name:"Bla Filler"}}},4:{Slot:4b,id:"flower_pot",Count:1b,Damage:0s,tag:{display:{Name:"Bla Filler"}}},],id:"Hopper",Lock:"",}' 
   bla = rel2abs ( orMj , ( 5 , 0 , 3  ) , orSm )
   time.sleep ( 0.1 )
   mc.setBlockWithNBT(bla,154,smjer_hoppera ( orSm , "meni")  , sto )   #hopper gleda meni
   
   crtaj_hopper    ( orMj , [ 5   , 0, 2 ]  , [ 5   ,  0 , 2  ] , orSm , "meni" ) # doljnji
   
   
   

def endStorage_2 (  orMj , orSm , iX=0 , iZ=0 , iY=0   ) :

   orMj = premjesti_origin ( orMj , iX , iZ , iY ,  orSm ) #mice gdje treba

   
   
   #priprema
   
   crtaj_hopper    ( orMj , ( 4   , -21, 4 )  , ( 4   ,  21 , 4  ) , orSm , "lijevo" ) # prvi razvod
   #crtaj_hopper    ( orMj , ( 50   , -21, 4 )  , ( 50   ,  21 , 4  ) , orSm , "lijevo" ) # drugi razvod

   crtaj_hopper    ( orMj , ( 4   , 21, 4 )  , ( 4   ,  21 , 4  ) , orSm , "odmene" ) # 
   crtaj_hopper    ( orMj , ( 75   , 21, 4 )  , ( 75   ,  21 , 4  ) , orSm , "lijevo" ) # drugi razvod
   crtaj_hopper    ( orMj , ( 75   , 20, 4 )  , ( 75   ,  20 , 4  ) , orSm , "meni" ) # 
   
   crtaj_hopper    ( orMj , ( 4   , 11, 4 )  , ( 4   ,  11 , 4  ) , orSm , "odmene" ) # 
   crtaj_hopper    ( orMj , ( 75   , 11, 4 )  , ( 75   ,  11 , 4  ) , orSm , "lijevo" ) # drugi razvod
   crtaj_hopper    ( orMj , ( 75   , 10, 4 )  , ( 75   ,  10 , 4  ) , orSm , "meni" ) # 

   crtaj_hopper    ( orMj , ( 4   , -10, 4 )  , ( 4   ,  -10 , 4  ) , orSm , "odmene" ) # 
   crtaj_hopper    ( orMj , ( 75   , -10, 4 )  , ( 75   ,  -10 , 4  ) , orSm , "lijevo" ) # drugi razvod
   crtaj_hopper    ( orMj , ( 75   , -11, 4 )  , ( 75   ,  -11 , 4  ) , orSm , "meni" ) #    
   
   crtaj_hopper    ( orMj , ( 4   , -20, 4 )  , ( 4   ,  -20 , 4  ) , orSm , "odmene" ) # 
   crtaj_hopper    ( orMj , ( 75   , -20, 4 )  , ( 75   ,  -20 , 4  ) , orSm , "lijevo" ) # drugi razvod
   crtaj_hopper    ( orMj , ( 75   , -21, 4 )  , ( 75   ,  -21 , 4  ) , orSm , "meni" ) #      
   
   
   #return 1
   
   #proba dead end
   orSm = ortUdesno( orSm )

   for br in range ( -5 , -75 ,-1 ) :
      if br % 2 == 1 :
         koja_kutija = "kutija"
      else:
         koja_kutija = "druga_kutija"

      modul_kraj2 (  orMj ,  orSm , iX=-24 , iZ=br , iY=0   , kutija = koja_kutija )
      modul_kraj2 (  orMj ,  orSm , iX=17 , iZ=br , iY=0   , kutija = koja_kutija )
      modul_kraj2 (  orMj ,  orSm , iX=-14 , iZ=br , iY=0   , kutija = koja_kutija )
      modul_kraj2 (  orMj ,  orSm , iX=7 , iZ=br , iY=0   , kutija = koja_kutija )
      
   orSm = ortUdesno( ortUdesno ( orSm ) )
    
   for br in range ( 5  , 75 ) :
      if br % 2 == 1 :
         koja_kutija = "kutija"
      else:
         koja_kutija = "druga_kutija"
      modul_kraj2 (  orMj ,  orSm , iX=-24 , iZ=br , iY=0   , kutija = koja_kutija )
      modul_kraj2 (  orMj ,  orSm , iX=17 , iZ=br , iY=0   , kutija = koja_kutija )
      modul_kraj2 (  orMj ,  orSm , iX=-14 , iZ=br , iY=0   , kutija = koja_kutija )
      modul_kraj2 (  orMj ,  orSm , iX=7 , iZ=br , iY=0   , kutija = koja_kutija )

if __name__ == "__main__":    #direktan poziv
   orMj = gdjeSam ()
   orSm = gdjeGledam ()
   endStorage_2 (  orMj , orSm  ,  iX=8 )