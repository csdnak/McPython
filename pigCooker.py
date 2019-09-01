#make cooker

from mc import * #import api-ja
from crtanje import *	
mc = Minecraft() #inicijalizacija sustava za rad sa Minecraftom

def cooker (  orMj ,  orSm , iX=0 , iZ=0 , iY=0 ):
   """
   make cooker
   """
   
   orMj = premjesti_origin ( orMj , iX , iZ , iY ,  orSm ) #mice ishodiste na centar
   crtaj_kvadar ( orMj , ( -1 , -1 , -1 )  , ( 1 , 1 , 2  ) , orSm , 98 , 0 ) #temelji od stomebricks
   crtaj_kutiju ( orMj , ( -1 , 0 , -1 )  , ( -2 , 0 , -1 ) , orSm , rel_smjer  = "meni" ) # storage
   crtaj_hopper    ( orMj , ( 0 , 0 , -1 )  , ( 1 , 0 , -1 ) , orSm ,  rel_smjer = "meni" )  #hoppers 
   crtaj_kvadar ( orMj , ( -1 , 0 , 0 )  , ( -1 , 0 , 1  ) , orSm , 20 , 0 ) # access
   crtaj_kvadar ( orMj , ( 0 , 0 , 0 )  , ( 1 , 0 , 0 ) , orSm , 44 , 5 )
   #crtaj_klopku   ( orMj , ( 0 , 0 , 0 )   , orSm , rel_smjer = "lijevo" , stanje="zatvoreno" , visina = "dolje" )   # first down trapdoor
   #crtaj_klopku   ( orMj , ( 1 , 0 , 0 )   , orSm , rel_smjer = "lijevo" , stanje="zatvoreno" , visina = "dolje" )   # second down trapdoor
   #crtaj_klopku   ( orMj , ( -1 , 0 , 1 )   , orSm , rel_smjer = "lijevo" , stanje="zatvoreno" , visina = "gore" )   # front up trapdoor
   crtaj_klopku   ( orMj , ( 1 , 0 , 1 )   , orSm , rel_smjer = "lijevo" , stanje="zatvoreno" , visina = "gore" )   # back up trapdoor
   
   crtaj_kvadar ( orMj , ( 0 , 0 , 1 )  , ( 0 , 0 , 1 ) , orSm , 11 , 0 ) #lava
   
   
   



   return 1
   
   
   
if __name__ == "__main__":    #direktan poziv
   
   orMj = gdjeSam ()
   orSm = gdjeGledam ()
   cooker (  orMj ,  orSm , iX=2 , iZ=0 , iY=0 )
