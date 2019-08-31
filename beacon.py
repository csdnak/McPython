#ispred lika polukruzni tunel  i to samo blokove iz liste 

from crtanje import *		#tu je funkcija koju zovem
from mc import * #import api-ja
mc = Minecraft() #inicijalizacija sustava za rad sa Minecraftom

def beacon ( orMjL ,  orSm  ,  iX=0 , iZ=0 , iY=0  ):
   #gradi se "iz centra"
   orMjL = premjesti_origin ( orMjL , iX  , iZ , iY ,  orSm ) #centar , stup u sredini 
   levela = 4
   for br in range (levela) :
      crtaj_kvadar ( orMjL , (-levela + br,-levela + br,br)  , (levela-br,levela - br,br) , orSm , 133 , 0 )  #piramida
   crtaj_kvadar ( orMjL , (0 , 0 ,levela)  , (0 , 0 ,levela) , orSm , 138 , 0 ) #beacon on top


 
if __name__ == "__main__":    #direktan poziv
   orMj = gdjeSam ()
   orSm = gdjeGledam ()
   beacon (  orMj ,  orSm  ,  iX=5 , iZ=0 , iY=0  )