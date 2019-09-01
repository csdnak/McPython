#ispred lika vrt

from mc import * #import api-ja
from crtanje import *
import time
mc = Minecraft() #inicijalizacija sustava za rad sa Minecraftom



def razorFarm ( orMj , orSm , iX=0 , iZ=0 , iY=0 ):

   orMj   = premjesti_origin ( orMj ,   iX , iZ , iY    , orSm  )
   crtaj_kvadar ( orMj , [ 0 , -6 , 0 ]  , [ 24 , 6 , 22  ] , orSm , 0 , 0 ) # clear the deck
   crtaj_kvadar ( orMj , [ 0 , -6 , -5 ]  , [ 24 , 6 , -1  ] , orSm , 3 , 0 ) # clear the deck
   
def wheatFarm ( orMj , orSm , iX=0 , iZ=0 , iY=0 , urod = 59):

   orMj   = premjesti_origin ( orMj ,   iX , iZ , iY    , orSm  )
   crtaj_kvadar ( orMj , [ -5 , -7 , 0 ]  , [ 21 , 7 , 29  ] , orSm , 0 , 0 ) # clear the deck
   mc.postToChat("Poc"  )
   #glowstone kocka
   crtaj_kvadar ( orMj , (  -5 , -5 , 0)  , (  15 , 5 , 1 ) , orSm ,  89 , 0 )
   #ograda okolo
   crtaj_kvadar ( orMj , (  -5 , -5 , 2)  , (  15 , 5 , 2 ) , orSm ,  85 , 0 )
   #glowstone kvrga iza
   crtaj_kvadar ( orMj , (  15 , -2 , 0)  , (  19 , 2 , 3 ) , orSm ,  89 , 0 )
   #cobblestone ispod mjesta za konzumera
   crtaj_kvadar ( orMj , (  18 , 0 , 0)  , (  18 , 0 , 0 ) , orSm ,  4 , 0 )
   #siroko mjesto za konzumera
   crtaj_kvadar ( orMj , (  18 , -1 , 1)  , (  18 , 1 , 2 ) , orSm ,  0 , 0 )
   crtaj_hopper    ( orMj , (  18 , -2 , 0)  , (  18 , 3 , 0 ) , orSm ,  "desno" , blok_id = 154 , blok_dv = 0 )

   #kiosk ispred konzumera
   crtaj_kvadar ( orMj , (  17 , -1 , 2)  , (  18 , 1 , 2 ) , orSm ,  0 , 0 )

   #gore zrak
   crtaj_kvadar ( orMj , (  -4 , -4 , 1)  , (  14 , 4 , 2 ) , orSm ,  0 , 0 )
   #dolje farmland
   crtaj_kvadar ( orMj , (  -4 , -4 , 0)  , (  14 , 4 , 0 ) , orSm ,  60 , 0 )
   #posadi wheat

   crtaj_kvadar ( orMj , (  -4 , -4 , 1)  , (  14 , -2 , 1 ) , orSm ,  urod , 7 )
   crtaj_kvadar ( orMj , (  -4 , -1 , 1)  , (  14 , 1 , 1 ) , orSm ,  urod , 7 )
   crtaj_kvadar ( orMj , (  -4 , 2 , 1)  , (  14 , 4 , 1 ) , orSm ,  urod , 7 )

   #voda u sredini
   crtaj_kvadar ( orMj , (  -1 , 0 , 0)  , (  -1 , 0 , 0 ) , orSm ,  9 , 0 )
   crtaj_kvadar ( orMj , (  5 , 0 , 0)  , (  5 , 0 , 0 ) , orSm ,  9 , 0 )
   crtaj_kvadar ( orMj , (  11 , 0 , 0)  , (  11 , 0 , 0 ) , orSm ,  9 , 0 )
   #hopperi iza
   crtaj_hopper    ( orMj , (  17 , -2 , 1)  , (  17 , 3 , 1 ) , orSm ,  "desno" , blok_id = 154 , blok_dv = 0 )
   #kutije iza hoppera
   crtaj_kutiju ( orMj , (  17  , 4 , 1)  , (  17 , 5 , 1 ) , orSm , rel_smjer  = "odmene" , blok_id = 54     )
   #zrak iznad kutije iza hoppera
   crtaj_kvadar ( orMj , (  17 , 4 , 2)  , (  17 , 5 , 2 ) , orSm , 0 , 0      )
   #cobblestone ispod vrata
   crtaj_kvadar ( orMj , (  15 , 0 , 0)  , (  16 , 0 , 0) , orSm ,  4 , 0 )
   # soba za vrtlara
   crtaj_kvadar ( orMj , (  15 , 0 , 1)  , (  16 , 0 , 2) , orSm ,  0 , 0 )
   #vrata
   crtaj_vrata ( orMj , (  15 , 0 , 1)   , orSm , "meni"   )
   #konzumer - stavi ga u minecart da se bolje pozicionira
   crtaj_kvadar ( orMj , ( 18,0,1)  , (  18,0,1 ) , orSm ,  66 , 0 )
   time.sleep  ( 2 )
   gdje = rel2abs ( orMj , (  18,0,1 )   , orSm  )
   id = mc.spawnEntity('Minecart',  int (gdje [0])  ,int (gdje [1]) ,int (gdje [2]) , "{Type:0}" )
   time.sleep  ( 2 ) # minecart
   id = mc.spawnEntity('Villager',  int (gdje [0])  ,int (gdje [1]) ,int (gdje [2]) , "{Profession:2,Career:2,Inventory:[0:{id:1,Count:62b,Damage:4s,},1:{id:1,Count:62b,Damage:0s,},2:{id:1,Count:62b,Damage:0s,},3:{id:1,Count:62b,Damage:0s,},4:{id:1,Count:62b,Damage:0s,},5:{id:1,Count:62b,Damage:4s,},6:{id:1,Count:62b,Damage:0s,},7:{id:1,Count:62b,Damage:0s,},]}") 
   #worker
   gdje2 = rel2abs ( orMj , (  2,0,1 )   , orSm  )
   #id = mc.spawnEntity('Villager',  int (gdje2 [0])  ,int (gdje2 [1]) ,int (gdje2 [2]) , "{Profession:0,Career:2,Inventory:[0:{id:142,Count:62b,Damage:4s,},1:{id:142,Count:55b,Damage:0s,},2:{id:142,Count:62b,Damage:0s,},3:{id:142,Count:62b,Damage:0s,},4:{id:142,Count:62b,Damage:0s,},5:{id:142,Count:62b,Damage:4s,},6:{id:142,Count:62b,Damage:0s,},7:{id:142,Count:62b,Damage:0s,},]}")
   #id = mc.spawnEntity('Villager', int (gdje2 [0])  ,int (gdje2 [1]) ,int (gdje2 [2]) , "{Profession:0,Career:2,Inventory:[0:{id:141,Count:62b,Damage:4s,},1:{id:141,Count:55b,Damage:0s,},2:{id:141,Count:62b,Damage:0s,},3:{id:141,Count:62b,Damage:0s,},4:{id:141,Count:62b,Damage:0s,},5:{id:141,Count:62b,Damage:4s,},6:{id:141,Count:62b,Damage:0s,},7:{id:142,Count:62b,Damage:0s,},]}")
   id = mc.spawnEntity('Villager', int (gdje2 [0])  ,int (gdje2 [1]) ,int (gdje2 [2]) , "{Profession:0,Career:2,Inventory:[0:{id:59,Count:62b,Damage:4s,},1:{id:59,Count:55b,Damage:0s,},2:{id:59,Count:62b,Damage:0s,},3:{id:59,Count:62b,Damage:0s,},4:{id:59,Count:62b,Damage:0s,},5:{id:59,Count:42b,Damage:4s,},6:{id:59,Count:2b,Damage:0s,},7:{id:59,Count:2b,Damage:0s,},]}")
   
   
   
   """
   
   if  abs ( Vx )  != abs ( Vz ) :		# ne pod 45
      for dZ in  range( -5 , 6 ) :    		# prodji chep
         for dY  in  range ( 0,1 ) : 
            for dX in  range ( 1 , 12  ) :
               gdjeX=radnaPozicija.x + Vx*dX + Vz*dZ    		# pomak po x
               gdjeY=radnaPozicija.y + dY
               gdjeZ=radnaPozicija.z + Vx*dZ + Vz*dX			# pomak po Z
               mc.setBlock(gdjeX , gdjeY , gdjeZ , 98 , 0 )			#postavi blok stone blocks
      for dZ in  range( -4 , 5 ) :    		# prodji chep
         for dY  in  range ( 0,1  ) : 
            for dX in  range ( 2 , 11  ) :
               gdjeX=radnaPozicija.x + Vx*dX + Vz*dZ    		# pomak po x
               gdjeY=radnaPozicija.y + dY
               gdjeZ=radnaPozicija.z + Vx*dZ + Vz*dX			# pomak po Z
               mc.setBlock(gdjeX , gdjeY , gdjeZ , 60)			#postavi blok farmlanda
               sto = 59                                     # zasadi ponesto
               if ( int ( gdjeX ) % 2 ) == 0 :
                  sto = 142
               if ( int ( gdjeX ) % 4 ) == 0 :
                  sto = 141
               mc.setBlock(gdjeX , gdjeY+1 , gdjeZ , sto , 2 )			#postavi blok wheata
               
      for dZ in  range ( 0 , 1 ) :    		# prodji chep
         for dY  in  range ( 0,1 ) : 
            for dX in range ( 6 , 7  ) :
               gdjeX=radnaPozicija.x + Vx*dX + Vz*dZ    		# pomak po x
               gdjeY=radnaPozicija.y + dY
               gdjeZ=radnaPozicija.z + Vx*dZ + Vz*dX			# pomak po Z
               mc.setBlock(gdjeX , gdjeY , gdjeZ , 9)			#postavi blok vode
               mc.setBlock(gdjeX , gdjeY+1 , gdjeZ , 0)			#postavi blok zraka
      
   """
   return 1

if __name__ == "__main__":    #direktan poziv
   orMj = gdjeSam ()
   orSm = gdjeGledam ()


   #wheatFarm (  orMj , orSm , iX=7 , iZ=0 , iY=-2  , urod = 141 ) #carrot
   #wheatFarm (  orMj , orSm , iX=7 , iZ=0 , iY=-2  , urod = 142 )#potato 
   razorFarm (  orMj , orSm , iX=1 , iZ=0 , iY=0  ) #wheat
   
   """
   orSm = ortUlijevo ( ortUlijevo ( orSm ))

   wheatFarm (  orMj , orSm , iX=7 , iZ=-16 , iY=-2  , urod = 142 ) #potato
   wheatFarm (  orMj , orSm , iX=7 , iZ=0 , iY=-2  , urod = 141 ) #carrot
   wheatFarm (  orMj , orSm , iX=7 , iZ=16 , iY=-2  ) #wheat
   """
   
   
   
   

