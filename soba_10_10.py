#ispred lika soba 10 x 10

from crtanje import *		#tu je funkcija koju zovem
from mc import * #import api-ja
mc = Minecraft() #inicijalizacija sustava za rad sa Minecraftom

def soba_10_10 (   iX=0 , iZ=0 , iY=0 ):
   """
   ispred polukruzni tunel  
   iX, - relativni pomak po X
   iZ, - relativni pomak po Z
   iY , - relativni pomak po Y
   radius - radius tunela default 5.0 
   duzina - duzina tunela default 5, 
   korekcija - korekcija oblika, da bude ljepsi default 0.0 
   uspon - korekcija smjera koliko gore dolje  default  0
   """
   #gdje sam
   orMj = gdjeSam ()
   orSm = gdjeGledam ()
    
   orMj = premjesti_origin ( orMj , iX , iZ , iY ,  orSm ) #mice ishodiste na centar kupole

   crtaj_kvadar ( orMj , (,-5,0)  , (,,5) , orSm , 0 , blok_dv = 0 )
   return 1
 
if __name__ == "__main__":    #direktan poziv
   #polukrugTunel (   iX=2 , iZ=0 , iY=0 , radius = 8 , duzina = 70 , korekcija = 0 , uspon = 0  )
   soba_10_10 (   iX=1 , iZ=0 , iY=0 ) 