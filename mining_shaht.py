#ispred lika polukruzni tunel  i to samo blokove iz liste 

from crtanje import *		#tu je funkcija koju zovem
from mc import * #import api-ja
mc = Minecraft() #inicijalizacija sustava za rad sa Minecraftom

def mining_shaht ( orMjL ,  orSm  ,  iX=0 , iZ=0 , iY=0 ,materijal = 98, dv = 1 , stepenice_mat = 109 ):
   #gradi se "iz centra"
   
   orMj = premjesti_origin ( orMjL , iX  , iZ , iY ,  orSm ) #centar , stup u sredini 
   bedrock = nadji_dno ( orMjL , ( 0 , 0 , 0 ) , orSm ) + 2 # maknuti crne tocke u pregledu
   
   
   #stairways hole
   crtaj_kvadar ( orMj , ( -4 , -9 , 0 )  , (  4 , 9 , 3 ) , orSm ,  0 , 0  )  #priprema
   crtaj_kvadar ( orMj , ( -4 , -9 , -1 )  , (  4 , 9 , bedrock ) , orSm ,  materijal , dv  )  #edge
   crtaj_kvadar ( orMj , ( -3 , -8 , -1 )  , (  3 , 8 , bedrock ) , orSm ,  0 , 0 )     #hole

   countdown =  bedrock   #how much down
   counter = bedrock    # down counter
   pomak = 3      # from podium
   smjer = -1      # where to go on relative Z axis
   r_smjer="desno"   # sirection for stairway function
   dX = -3         # move on relative X axis

   #stairways down
   while counter :
      crtaj_stepenice ( orMj , ( 1 + dX, pomak  , counter )  , (  2 + dX, pomak  , counter ) , orSm , blok_id = stepenice_mat , rel_smjer  = r_smjer  )
      pomak  += smjer   # zig - zag
      counter += 1
      if pomak == 4 :   # podium
         pomak = 3
         crtaj_kvadar ( orMj , ( 2  ,  pomak + 1 , counter - 1 )  , ( -2 ,  pomak + 5 , counter - 1) , orSm ,  materijal , dv )
         crtaj_kvadar ( orMj , ( 1  ,  pomak + 2 , counter -1 )  , ( -1 ,  pomak + 4 , counter - 1 ) , orSm ,  89 , 0 )
      if pomak == -4 :   # podium
         pomak = -3
         crtaj_kvadar ( orMj , ( 2  , pomak - 1  , counter  - 1 )  , ( -2 ,  pomak - 5 , counter - 1  ) , orSm ,   materijal , dv  )
         crtaj_kvadar ( orMj , ( 1  , pomak - 2 , counter - 1)  , ( -1 ,  pomak - 4 , counter - 1 ) , orSm ,  89 , 0 )
      if ( (bedrock - counter ) % 7  ) == 0 :
         smjer *= -1
         if smjer == 1 :
            r_smjer="lijevo"
            dX = 0
         else:
            r_smjer="desno"
            dX = -3

   
   
   
   
   
"""   
   crtaj_kvadar ( orMjL , ( -2 , -2 , 0 )  , ( 2 , 2 , 1 ) , orSm , 47 , 0 )  #police sa knjigama
   crtaj_kvadar ( orMjL , ( -1 , -1 , 0 )  , ( 1 , 1 , 1 ) , orSm , 0 , 0 )  #rupa u sredini
   crtaj_kvadar ( orMjL , ( -2 , 0 , 0 )  , ( -2 , 0 , 1 ) , orSm , 0 , 0 )  #ulaz do stola
   crtaj_kvadar ( orMjL , (0 , 0 , 0)  , (0 , 0 , 0) , orSm , 116 , 0 ) #enchanting table
   crtaj_kutiju ( orMjL , (-3,-2,0) , (-3,-1,1) , orSm , rel_smjer  = "meni" , blok_id = 54     ) #prazne kutije
   crtaj_kutiju ( orMjL , (-3,1,0) , (-3,2,1) , orSm , rel_smjer  = "meni" , blok_id = 54     )
"""


 
if __name__ == "__main__":    #direktan poziv
   orMj = gdjeSam ()
   orSm = gdjeGledam ()
   mining_shaht (  orMj ,  orSm  ,  iX=4 , iZ=0 , iY=0  )