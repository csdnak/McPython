#ispred lika polukruzni tunel  i to samo blokove iz liste 

from crtanje import *		#tu je funkcija koju zovem
from mc import * #import api-ja
mc = Minecraft() #inicijalizacija sustava za rad sa Minecraftom

def ench_table ( orMjL ,  orSm  ,  iX=0 , iZ=0 , iY=0  ):
   #gradi se "iz centra"
   orMjL = premjesti_origin ( orMjL , iX  , iZ , iY ,  orSm ) #centar , stup u sredini 
   crtaj_kvadar ( orMjL , ( -2 , -2 , 0 )  , ( 2 , 2 , 1 ) , orSm , 47 , 0 )  #police sa knjigama
   crtaj_kvadar ( orMjL , ( -1 , -1 , 0 )  , ( 1 , 1 , 1 ) , orSm , 0 , 0 )  #rupa u sredini
   crtaj_kvadar ( orMjL , ( -2 , 0 , 0 )  , ( -2 , 0 , 1 ) , orSm , 0 , 0 )  #ulaz do stola
   crtaj_kvadar ( orMjL , (0 , 0 , 0)  , (0 , 0 , 0) , orSm , 116 , 0 ) #enchanting table
   crtaj_kutiju ( orMjL , (-3,-2,0) , (-3,-1,1) , orSm , rel_smjer  = "meni" , blok_id = 54     ) #prazne kutije
   crtaj_kutiju ( orMjL , (-3,1,0) , (-3,2,1) , orSm , rel_smjer  = "meni" , blok_id = 54     )


 
if __name__ == "__main__":    #direktan poziv
   orMj = gdjeSam ()
   orSm = gdjeGledam ()
   ench_table (  orMj ,  orSm  ,  iX=3 , iZ=0 , iY=0  )