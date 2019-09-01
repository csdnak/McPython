#ispred lika vrt
#ispred lika vrt

from mc import * #import api-ja
from sorter_2 import *	
mc = Minecraft() #inicijalizacija sustava za rad sa Minecraftom

def samoModulSorter2 (  orMj ,  orSm , iX=0 , iZ=0 , iY=0 ):
   """
   funkcija za crtanje vrta oko lika
   """
   
   orMj = premjesti_origin ( orMj , iX , iZ , iY ,  orSm ) #mice ishodiste na centar
   modul_sorter2 (  orMj ,  orSm , iX=-4 , iZ=0 , iY=0  ,  materijal = 98, dv = 0  , kutija = "kutija" , crtaj_kutije = "ne" )


   return 1
   
   
   
if __name__ == "__main__":    #direktan poziv
   
   orMj = gdjeSam ()
   orSm = gdjeGledam ()
   for dZ in range ( 0 , 6 ):   
      samoModulSorter2 (  orMj ,  orSm , iX=4 , iZ=dZ , iY=0 )
      samoModulSorter2 (  orMj ,  orSm , iX=4 , iZ=dZ , iY=0 )
