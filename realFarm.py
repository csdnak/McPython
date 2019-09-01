#ispred lika vrt
#ispred lika vrt

from mc import * #import api-ja
from crtanje import *	
import time
mc = Minecraft() #inicijalizacija sustava za rad sa Minecraftom


def realFarm (  orMj ,  orSm , iX=8 , iZ=0 , iY=0 , urod = 59):

   orMj = premjesti_origin ( orMj , iX , iZ , iY ,  orSm ) #mice ishodiste na centar
   
   crtaj_kvadar ( orMj , ( -5 , -5 , 0 )  , ( 5 , 5 , 1  ) , orSm , 98 , 0 ) #temelji i okvir od stomebricks
   crtaj_hopper    ( orMj , ( -4 , -4 , 0 )  , ( 4 , 4 , 0  ) , orSm  ,  rel_smjer = "meni" ) #Hopperi u sredini
   crtaj_hopper    ( orMj , ( -4 , -3 , 0 )  , ( -4 , 4 , 0  ) , orSm  ,  rel_smjer = "lijevo" ) #Hopperi u sredini
   crtaj_hopper    ( orMj , ( -5 , -4 , 0 )  , ( -5 , -4 , 0  ) , orSm  ,  rel_smjer = "meni" ) #Hopperi u sredini
   
   crtaj_kvadar ( orMj , ( -4 , -4 , 1 )  , ( 4 , 4 , 1  ) , orSm , 66 , 0 ) #rails
   
   for br in  ( -4 , -3 , -2 , -1 , 1 , 2, 3 ,4 ) :
      crtaj_kvadar ( orMj , ( br , br , 1 )  , ( br , br , 1  ) , orSm , 27 , 8 ) 
   
   
   
   crtaj_kvadar ( orMj , ( -5 , -5 , 3 )  , ( 5 , 5 , 3  ) , orSm , 85 , 2 ) #fence
   crtaj_kvadar ( orMj , ( -4 , -4 , 3 )  , ( 4 , 4 , 3  ) , orSm , 0 , 0 ) #air   
   crtaj_kvadar ( orMj , ( 0 , 0 , 1 )  , ( 0 , 0 , 1  ) , orSm , 89 , 0 ) #glowstone lampa ispod vode
   crtaj_kvadar ( orMj , ( -5 , -5 , 2 )  , ( 5 , 5 , 2  ) , orSm , 89 , 0 ) #glowstone ispof fence
   crtaj_kvadar ( orMj , ( -4 , -4 , 2 )  , ( 4 , 4 , 2  ) , orSm , 60 , 0 ) #farmland
   crtaj_kvadar ( orMj , ( -4 , -4 , 3 )  , ( 4 , 4 , 3  ) , orSm , urod , 7 ) #wheat   
   crtaj_kvadar ( orMj , ( 0 , 0 , 2 )  , ( 0 , 0 , 2  ) , orSm , 9 , 0 ) #voda
   
   crtaj_kvadar ( orMj , ( 0 , 0 , 3 )  , ( 0 , 0 , 3  ) , orSm , 89 , 0 ) #glowstone lampa iznad vode

   time.sleep ( 10 )
   for dX in range( -4 , 5  ):
      for dZ in range ( -4 , 5 ):
         if dX != 0 and dZ != 0 :
            gdje = rel2abs ( orMj , (  dX,dZ,1 )   , orSm  )
            id = mc.spawnEntity('MinecartHopper',  int (gdje [0])  ,int (gdje [1]) ,int (gdje [2]) , "{Type:0}" )
            time.sleep ( 0.1 )
   gdje = rel2abs ( orMj , (  1,1,3 )   , orSm  )
   time.sleep ( 0.6 )
   if urod == 59 :
      id = mc.spawnEntity('Villager',  int (gdje [0])  ,int (gdje [1]) ,int (gdje [2]), "{Profession:0,Career:1,Inventory:[0:{id:59,Count:62b,Damage:4s,},1:{id:1,Count:55b,Damage:0s,},2:{id:1,Count:62b,Damage:0s,},3:{id:2,Count:62b,Damage:0s,},4:{id:2,Count:62b,Damage:0s,},5:{id:1,Count:62b,Damage:4s,},6:{id:7,Count:2b,Damage:0s,},7:{id:7,Count:2b,Damage:0s,},]}")
   if urod == 141 :
      id = mc.spawnEntity('Villager',  int (gdje [0])  ,int (gdje [1]) ,int (gdje [2]), "{Profession:0,Career:1,Inventory:[0:{id:141,Count:62b,Damage:4s,},1:{id:1,Count:55b,Damage:0s,},2:{id:1,Count:62b,Damage:0s,},3:{id:1,Count:62b,Damage:0s,},4:{id:2,Count:62b,Damage:0s,},5:{id:1,Count:62b,Damage:4s,},6:{id:1,Count:62b,Damage:0s,},7:{id:1,Count:62b,Damage:0s,},]}")
   if urod == 142 :
      id = mc.spawnEntity('Villager',  int (gdje [0])  ,int (gdje [1]) ,int (gdje [2]), "{Profession:0,Career:1,Inventory:[0:{id:142,Count:62b,Damage:4s,},1:{id:1,Count:55b,Damage:0s,},2:{id:1,Count:62b,Damage:0s,},3:{id:1,Count:62b,Damage:0s,},4:{id:2,Count:62b,Damage:0s,},5:{id:1,Count:62b,Damage:4s,},6:{id:1,Count:62b,Damage:0s,},7:{id:1,Count:62b,Damage:0s,},]}")
   
def vrt (  orMj ,  orSm , iX=0 , iZ=0 , iY=0 ):
   """
   funkcija za crtanje vrta oko lika
   """
   
   orMj = premjesti_origin ( orMj , iX , iZ , iY ,  orSm ) #mice ishodiste na centar
   crtaj_kvadar ( orMj , ( -5 , -5 , 0 )  , ( 5 , 5 , 0  ) , orSm , 98 , 0 ) #temelji od stomebricks
   crtaj_kvadar ( orMj , ( -4 , -4 , 0 )  , ( 4 , 4 , 0  ) , orSm , 60 , 0 ) #farmland

   crtaj_kvadar ( orMj , ( -4 , -4 , 1 )  , ( 4 , -2 , 1  ) , orSm , 59 , 0 ) #wheat   
   crtaj_kvadar ( orMj , ( -4 , -1 , 1 )  , ( 4 , 1 , 1  ) , orSm , 141 , 0 ) #carrot   
   crtaj_kvadar ( orMj , ( -4 , 2 , 1 )  , ( 4 , 4 , 1  ) , orSm , 142 , 0 ) #potato     
   
   crtaj_kvadar ( orMj , ( 0 , 0 , 0 )  , ( 0 , 0 , 0  ) , orSm , 9 , 0 ) #voda
   crtaj_kvadar ( orMj , ( 0 , 0 , 1 )  , ( 0 , 0 , 1  ) , orSm , 89 , 0 ) #glowstone lampa iznad vode


   return 1
   
   
   
if __name__ == "__main__":    #direktan poziv
   
   orMj = gdjeSam ()
   orSm = gdjeGledam ()
   realFarm (  orMj ,  orSm , iX=8 , iZ=-15 , iY=0 )
   #time.sleep (10)
   realFarm (  orMj ,  orSm , iX=8 , iZ=0 , iY=0 , urod = 141 )
   #time.sleep (10)
   realFarm (  orMj ,  orSm , iX=8 , iZ=15 , iY=0 , urod = 142)
   #time.sleep (10)