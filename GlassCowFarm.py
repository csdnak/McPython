#make cooker

from mc import * #import api-ja
from crtanje import *	
import time
mc = Minecraft() #inicijalizacija sustava za rad sa Minecraftom


def glassCowFarm (  orMj ,  orSm , iX=0 , iZ=0 , iY=0 ):

   orMj = premjesti_origin ( orMj , iX , iZ , iY ,  orSm ) #mice ishodiste na centar
   crtaj_kutiju ( orMj , ( 0 , -1 , -1 )  , ( 0 , 0 , -1 ) , orSm , rel_smjer  = "meni" ) # storage
   crtaj_kvadar ( orMj , ( 1 , -1 , -1 )  , ( 7 , 1 , -1  ) , orSm , 98 , 0 ) #temelji od stomebricks
   crtaj_kvadar ( orMj , ( 1 , -1 , 0 )  , ( 7 , 1 , 4  ) , orSm , 20 , 0 ) #gore staklo
   crtaj_hopper    ( orMj , ( 1 , 0 , -1 )  , ( 6 , 0 , -1 ) , orSm ,  rel_smjer = "meni" )  # u sredini hopperi prema meni
   crtaj_kvadar ( orMj , ( 2 , -1 , 0 )  , ( 6 , -1 , 0  ) , orSm , 98 , 0 )# po lijevoj strani podloga za droppere i nosaci za trapdoor
   #for br in range ( 3 , 7 ):
   #   crtaj_klopku   ( orMj , ( br , 0 , 0 )   , orSm , rel_smjer = "desno" , stanje="zatvoreno" , visina = "dolje" )
   sto =  '{TransferCooldown:0,Items:[0:{Slot:0b,id:"minecraft:lava_bucket",Count:1b,},],id:"dispenser",Lock:"",}'
   for br in range ( 3 , 6 ) :
      bla = rel2abs ( orMj , ( br , -1 ,  1  ) , orSm )
      #mc.postToChat("orginal: %s %s " %  ( dX , bla )    )
      time.sleep ( 0.1 )
      mc.setBlockWithNBT(bla,23,smjer_hoppera ( orSm , "desno")  , sto ) 
   """
   crtaj_dropper    ( orMj , ( 2 , -1 , 1 )  , ( 2 , -1 , 1  ) , orSm ,  rel_smjer = "desno" )
   crtaj_dropper    ( orMj , ( 3 , -1 , 1 )  , ( 3 , -1 , 1  ) , orSm ,  rel_smjer = "desno" )
   crtaj_dropper    ( orMj , ( 4 , -1 , 1 )  , ( 4 , -1 , 1  ) , orSm ,  rel_smjer = "desno" )
   """
   crtaj_kvadar ( orMj , ( 2 , 0 , 1 )  , ( 6 , 0 , 1  ) , orSm , 0 , 0 ) # doljnja rupa u ravnini droppera
   crtaj_kvadar ( orMj , ( 2 , 0 , 3 )  , ( 6 , 0 , 4  ) , orSm , 0 , 0 ) # gornja  rupa u ravnini droppera
   crtaj_kvadar ( orMj , ( 6 , 0 , 2 )  , ( 6 , 0 , 2  ) , orSm , 0 , 0 ) # spoj gore dolje
   crtaj_kvadar ( orMj , ( 6 , 0 , 4 )  , ( 6 , 0 , 4  ) , orSm , 44 , 5 ) # halfslabb
   crtaj_kvadar ( orMj , ( 2 , 0 , 2 )  , ( 2 , 0 , 2  ) , orSm , 0 , 0 ) # spoj gore dolje
   crtaj_kvadar ( orMj , ( 2 , 0 , 4 )  , ( 2 , 0 , 4  ) , orSm , 44 , 5 ) # halfslabb
   time.sleep ( 0.2 )

   for br in (  3 , 4 , 5 ):
      crtaj_button ( orMj , ( br , -2 , 0 )  , ( br , -2 , 0  ) , orSm ,  rel_smjer = "lijevo" )
   for br in range ( 2 , 7 ):
      crtaj_klopku   ( orMj , ( br , 0 , 0 )   , orSm , rel_smjer = "desno" , stanje="zatvoreno" , visina = "dolje" )     
   bla = rel2abs ( orMj , ( 4 , -1 , 3  ) , orSm )
   #time.sleep ( 10 )
   for jao in range ( 1, 6 ):
      #mc.spawnEntity('Cow', int ( bla [ 0 ] ) ,int ( bla [ 1 ] ), int ( bla [ 2 ] ), "{NoAI:0}")
      time.sleep ( 0.2 )
   
   
      

def cooker (  orMj ,  orSm , iX=0 , iZ=0 , iY=0 ):
   """
   make cooker
   """
   
   orMj = premjesti_origin ( orMj , iX , iZ , iY ,  orSm ) #mice ishodiste na centar
   crtaj_kvadar ( orMj , ( -1 , -2 , -1 )  , ( 1 , 1 , 2  ) , orSm , 98 , 0 ) #temelji od stomebricks
   time.sleep (10)
   crtaj_kutiju ( orMj , ( -2 , -1 , -1 )  , ( -2 , 0 , -1 ) , orSm , rel_smjer  = "meni" ) # storage
   crtaj_hopper    ( orMj , ( -1 , -1 , -1 )  , ( 1 , 0 , -1 ) , orSm ,  rel_smjer = "meni" )  #hoppers 
   crtaj_kvadar ( orMj , ( -1 , -1 , 0 )  , ( -1 , 0 , 1  ) , orSm , 20 , 0 ) # access
   #crtaj_kvadar ( orMj , ( 0 , 0 , 0 )  , ( 1 , 0 , 0 ) , orSm , 44 , 5 )
   crtaj_klopku   ( orMj , ( 0 , 0 , 0 )   , orSm , rel_smjer = "desno" , stanje="zatvoreno" , visina = "dolje" )   # first down trapdoor
   crtaj_klopku   ( orMj , ( 1 , 0 , 0 )   , orSm , rel_smjer = "desno" , stanje="zatvoreno" , visina = "dolje" )   # second down trapdoor
   crtaj_klopku   ( orMj , ( 0 , -1 , 0 )   , orSm , rel_smjer = "lijevo" , stanje="zatvoreno" , visina = "dolje" )   # first down trapdoor
   crtaj_klopku   ( orMj , ( 1 , -1 , 0 )   , orSm , rel_smjer = "lijevo" , stanje="zatvoreno" , visina = "dolje" )   # second down trapdoor
   #crtaj_klopku   ( orMj , ( -1 , 0 , 1 )   , orSm , rel_smjer = "lijevo" , stanje="zatvoreno" , visina = "gore" )   # front up trapdoor
   crtaj_klopku   ( orMj , ( 1 , 0 , 1 )   , orSm , rel_smjer = "desno" , stanje="zatvoreno" , visina = "gore" )   # back up trapdoor
   crtaj_klopku   ( orMj , ( 1 , -1 , 1 )   , orSm , rel_smjer = "lijevo" , stanje="zatvoreno" , visina = "gore" )   # back up trapdoor
   
   time.sleep (10)
   crtaj_kvadar ( orMj , ( 0 , -1 , 1 )  , ( 0 , 0 , 1 ) , orSm , 11 , 0 ) #lava
   
   
   



   return 1
   
   
   
if __name__ == "__main__":    #direktan poziv
   
   orMj = gdjeSam ()
   orSm = gdjeGledam ()
   glassCowFarm (  orMj ,  orSm , iX=3 , iZ=0 , iY=0 )
