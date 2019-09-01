# crta malu kucu sa puno vrata, u for petlju se stavi koliko kuca da crta

from mc import * #import api-ja
from crtanje import *	
from vratarnica import *	
from vrt import *	
mc = Minecraft() #inicijalizacija sustava za rad sa Minecraftom

def selo (  orMj ,  orSm , iX=0 , iZ=0 , iY=0 ):
   
   orMj = premjesti_origin ( orMj , iX , iZ , iY ,  orSm ) #mice ishodiste na centar
   
   for dX in range ( -40 , 41 , 10 ):
      for dZ in range ( -10 , 11 , 10 ):
         vratarnica (  orMj ,  orSm , iX=dX , iZ=dZ , iY=0 )
      
   for dZ in range ( -40 , 41 , 10 ):
      for dX in range ( -10 , 11 , 10 ):
         vratarnica (  orMj ,  orSm , iX=dX , iZ=dZ , iY=0 )
   
   
   for dX in ( - 40 , -25 , 25 , 40 ):
      for dZ in (  - 40 , -25 , 25 , 40  ):
         vrt (  orMj ,  orSm , iX=dX , iZ=dZ , iY=0 )
   
   makeFarmer (orMj , 5 , -2 , 0 ,  orSm ,  Profession = 0 , Career = 1)
   makeFarmer (orMj , 6 , -2 , 0 ,  orSm ,  Profession = 0 , Career = 1)
   makeLibrarian (orMj , 5 , -1 , 0 ,  orSm ,  Profession = 1 , Career = 1)
   makePriest (orMj , 5 , 0 , 0 ,  orSm ,  Profession = 2 , Career = 1)
   makeBlacksmith (orMj , 5 , 1 , 0 ,  orSm ,  Profession = 3 , Career = 1)
   makeButcher (orMj , 5 , 2 , 0 ,  orSm ,  Profession = 4 , Career = 1)
   
   return 1

  
if __name__ == "__main__":    #direktan poziv
   
   orMj = gdjeSam ()
   orSm = gdjeGledam ()
   selo (  orMj ,  orSm , iX=0 , iZ=0 , iY=0 )
