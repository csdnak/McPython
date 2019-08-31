#ispred lika vrt

from mc import * #import api-ja
from crtanje import *	
mc = Minecraft() #inicijalizacija sustava za rad sa Minecraftom

def farm (  orMj ,  orSm , iX=0 , iZ=0 , iY=0 ):
   """
   funkcija za crtanje velike farme ispred lika
   """
   orMj = premjesti_origin ( orMj , iX , iZ , iY ,  orSm ) #mice ishodiste na centar
   
   for dZ in ( -10 , 0 , 10 ) :
      crtaj_stepenice ( orMj , ( -1 , dZ , 0 )  , ( -1 , dZ , 0 ) , orSm , blok_id = 109 , rel_smjer  = "meni" , gore_dolje = "ne"  ) #stairs
      crtaj_kvadar ( orMj , ( -2 , dZ , 0 )  , ( -2 , dZ , 0 ) , orSm , 89 , blok_dv = 0 )
   crtaj_kvadar ( orMj , ( 0 , -10 , 0 )  , ( 9 , 10 , 0 ) , orSm , 98 , blok_dv = 2 ) #fondation
   crtaj_kvadar ( orMj , ( 2 , -8 , 0 )  , ( 8 , 8 , 0 ) , orSm , 60 , blok_dv = 0 ) #farmland
   crtaj_kvadar ( orMj , ( 2 , -8 , 1 )  , ( 8 , 8 , 1 ) , orSm , 59 , 7 )
   
   for dZ in ( -9 , 0 , 9 ):
      crtaj_kvadar ( orMj , ( 3 , dZ , -1 )  , ( 7 , dZ , -1 ) , orSm , 89 , blok_dv = 0 ) #glowstone under water
      crtaj_kvadar ( orMj , ( 3 , dZ , 0 )  , ( 7 , dZ , 0 ) , orSm , 9 , blok_dv = 0 ) #water
      crtaj_kvadar ( orMj , ( 2 , dZ , 1 )  , ( 8 , dZ , 1 ) , orSm , 44 , blok_dv = 5 ) #slabstone over water
   
   
   
   crtaj_kutiju ( orMj , ( 1 , 0 , -1 ) , ( 1 , 0 , -1 ) , orSm , rel_smjer  = "meni" , blok_id = 54 )
   crtaj_hopper    ( orMj , ( 1 , 1 , -1 ) , ( 1 , 8 , -1 ) , orSm ,  "lijevo" , blok_id = 154 , blok_dv = 0 )
   crtaj_kvadar ( orMj , ( 1 , 1 , 0 ) , ( 1 , 8 , 0 ) , orSm , 44 , blok_dv = 5 ) #slabstone over hopper
   crtaj_hopper    ( orMj , ( 1 , -1 , -1 ) , ( 1 , -8 , -1 ) , orSm ,  "desno" , blok_id = 154 , blok_dv = 0 )
   crtaj_kvadar ( orMj , ( 1 , -1 , 0 ) , ( 1 , -8 , 0 ) , orSm , 44 , blok_dv = 5 ) #slabstone over hopper
   
   orMj2 = premjesti_origin ( orMj , 9 , 0 , 1 ,  orSm )

   for dZ in ( -10 , 0 , 10 ) :
      crtaj_stepenice ( orMj2 , ( -1 , dZ , 0 )  , ( -1 , dZ , 0 ) , orSm , blok_id = 109 , rel_smjer  = "meni" , gore_dolje = "ne"  ) #stairs
      crtaj_kvadar ( orMj2 , ( -2 , dZ , -1 )  , ( -2 , dZ , -1 ) , orSm , 89 , blok_dv = 0 )
   crtaj_kvadar ( orMj2 , ( 0 , -10 , -1 )  , ( 6 , 10 , 0 ) , orSm , 98 , blok_dv = 2 ) #fondation
   crtaj_kvadar ( orMj2 , ( 0 , -8 , 0 )  , ( 6 , 8 , 0 ) , orSm , 60 , blok_dv = 0 ) #farmland
   crtaj_kvadar ( orMj2 , ( 0 , -8 , 1 )  , ( 6 , 8 , 1 ) , orSm , 141 , 7 )
   for dZ in ( -9 , 0 , 9 ):
      crtaj_kvadar ( orMj2 , ( 2 , dZ , -1 )  , ( 4 , dZ , -1 ) , orSm , 89 , blok_dv = 0 ) #glowstone under water
      crtaj_kvadar ( orMj2 , ( 2 , dZ , 0 )  , ( 4 , dZ , 0 ) , orSm , 9 , blok_dv = 0 ) #water    44:5
      crtaj_kvadar ( orMj2 , ( 0 , dZ , 1 )  , ( 6 , dZ , 1 ) , orSm , 44 , blok_dv = 5 ) #slabstone over water

   orMj2 = premjesti_origin ( orMj , 16 , 0 , 2 ,  orSm )

   for dZ in ( -10 , 0 , 10 ) :
      crtaj_stepenice ( orMj2 , ( -1 , dZ , 0 )  , ( -1 , dZ , 0 ) , orSm , blok_id = 109 , rel_smjer  = "meni" , gore_dolje = "ne"  ) #stairs
      crtaj_kvadar ( orMj2 , ( -2 , dZ , -1 )  , ( -2 , dZ , -1 ) , orSm , 89 , blok_dv = 0 )
   crtaj_kvadar ( orMj2 , ( 0 , -10 , -2 )  , ( 6 , 10 , 0 ) , orSm , 98 , blok_dv = 2 ) #fondation
   crtaj_kvadar ( orMj2 , ( 0 , -8 , 0 )  , ( 6 , 8 , 0 ) , orSm , 60 , blok_dv = 0 ) #farmland
   crtaj_kvadar ( orMj2 , ( 0 , -8 , 1 )  , ( 6 , 8 , 1 ) , orSm , 142 , 7 )
   
   for dZ in ( -9 , 0 , 9 ):
      crtaj_kvadar ( orMj2 , ( 2 , dZ , -1 )  , ( 4 , dZ , -1 ) , orSm , 89 , blok_dv = 0 ) #glowstone under water
      crtaj_kvadar ( orMj2 , ( 2 , dZ , 0 )  , ( 4 , dZ , 0 ) , orSm , 9 , blok_dv = 0 ) #water
      crtaj_kvadar ( orMj2 , ( 0 , dZ , 1 )  , ( 6 , dZ , 1 ) , orSm , 44 , blok_dv = 5 ) #slabstone over water
      
   orMj2 = premjesti_origin ( orMj , 23 , 0 , 3 ,  orSm )
   
   for dZ in ( -10 , 0 , 10 ) :
      crtaj_stepenice ( orMj2 , ( -1 , dZ , 0 )  , ( -1 , dZ , 0 ) , orSm , blok_id = 109 , rel_smjer  = "meni" , gore_dolje = "ne"  ) #stairs
      crtaj_kvadar ( orMj2 , ( -2 , dZ , -1 )  , ( -2 , dZ , -1 ) , orSm , 89 , blok_dv = 0 )
   crtaj_kvadar ( orMj2 , ( 0 , -10 , -3 )  , ( 10 , 10 , 0 ) , orSm , 98 , blok_dv = 2 ) #fondation
   crtaj_kvadar ( orMj2 , ( 0 , -8 , 0 )  , ( 6 , 8 , 0 ) , orSm , 60 , blok_dv = 0 ) #farmland
   crtaj_kvadar ( orMj2 , ( 0 , -8 , 1 )  , ( 6 , 8 , 1 ) , orSm , 207 , 3 )
   
   for dZ in ( -9 , 0 , 9 ):
      crtaj_kvadar ( orMj2 , ( 2 , dZ , -1 )  , ( 4 , dZ , -1 ) , orSm , 89 , blok_dv = 0 ) #glowstone under water
      crtaj_kvadar ( orMj2 , ( 2 , dZ , 0 )  , ( 4 , dZ , 0 ) , orSm , 9 , blok_dv = 0 ) #water
      crtaj_kvadar ( orMj2 , ( 0 , dZ , 1 )  , ( 6 , dZ , 1 ) , orSm , 44 , blok_dv = 5 ) #slabstone over water
   
   crtaj_kvadar ( orMj2 , ( 7 , 9 , 1 )  , ( 7 , 9 , 1 ) , orSm , 20 , blok_dv = 0 ) #make it simple
   crtaj_piston ( orMj2 , ( 7 , -8 , 1 )  , ( 7 , -1 , 1 ) , orSm ,  "meni" ) #left piston block
   crtaj_piston ( orMj2 , ( 7 , 1 , 1 )  , ( 7 , 8 , 1 ) , orSm ,  "meni" )   #right piston block
   crtaj_kvadar ( orMj2 , ( 8 , -10 , 1 )  , ( 10 , 10 , 1 ) , orSm , 98 , blok_dv = 2 ) #redstone foundation
   crtaj_kvadar ( orMj2 , ( 8 , -8 , 2 )  , ( 8 , 8 , 2 ) , orSm , 55 , blok_dv = 0 ) #redstone
   crtaj_kvadar ( orMj2 , ( 9 , 0 , 2 )  , ( 9 , 0 , 2 ) , orSm , 69 , blok_dv = 13 ) #lever - up - on
   crtaj_redstonetorch ( orMj2 , ( 10 , 0 , 2 )   , orSm , "gore"   ) # redstone torch
   crtaj_kvadar ( orMj2 , ( 10 , -2 , 1 ), ( 10 , -2 , 1 ) , orSm , 89 , blok_dv = 0 )
   crtaj_kvadar ( orMj2 , ( 10 , 2 , 1 )  , ( 10 , 2 , 1 ) , orSm , 89 , blok_dv = 0 )
   for dZ in ( -10 , 10 ) :
      crtaj_stepenice ( orMj2 , ( 7 , dZ , 1 )  , ( 7 , dZ , 1 ) , orSm , blok_id = 109 , rel_smjer  = "meni" , gore_dolje = "ne"  ) #stairs
      crtaj_kvadar ( orMj2 , ( 6 , dZ , 0 )  , ( 6 , dZ , 0 ) , orSm , 89 , blok_dv = 0 )
      crtaj_kvadar ( orMj2 , ( 9 , dZ , 1 )  , ( 9 , dZ , 1 ) , orSm , 89 , blok_dv = 0 )

   
   for dX in ( 5 , 7 ):
      crtaj_kvadar ( orMj2 , ( dX , 9 , 2 )  , ( dX , -9 , 2 ) , orSm , 20 , blok_dv = 0 ) #make it trasparent

   for dZ in ( -9 , 0 , 9  ):
      crtaj_kvadar ( orMj2 , ( 6 , dZ , 2 )  , ( 6 , dZ , 2 ) , orSm , 20 , blok_dv = 0 ) #make it trasparent

   crtaj_kvadar ( orMj2 , ( 6 , -8 , 2 )  , ( 6 , -1 , 2 ) , orSm ,  9 , 0) #left water block
   crtaj_kvadar ( orMj2 , ( 6 , 1 , 2 )  , ( 6 , 8 , 2 ) , orSm ,  9 , 0 )   #right water block
      
      
   return 1
   
   
   
if __name__ == "__main__":    #direktan poziv
   
   orMj = gdjeSam ()
   orSm = gdjeGledam ()
   farm (  orMj ,  orSm , iX=3 , iZ=0 , iY=0 )
