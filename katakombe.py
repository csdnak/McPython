#ispred lika katakombe 21 x 21

from crtanje import *		#tu je funkcija koju zovem
from mc import * #import api-ja
mc = Minecraft() #inicijalizacija sustava za rad sa Minecraftom

def katakombe ( orMjL ,  orSm ,iX=0 , iZ=0 , iY=0 ,  materijal = 98, dv = 0 , stepenice_mat = 109):
   #ishodiste je u sredini sobe
   orMjL = premjesti_origin ( orMjL , iX  , iZ , iY ,  orSm ) #centar , stup u sredini 
   filter ( orMjL , ( -11 , 0 , 0 ) , orSm ,  visina = 7 ,   sirina = 10 , dubina = 21, baklje="ne") 
   #strop
   crtaj_kvadar ( orMjL , (-10,-10,6)  , (10,10,6) , orSm , materijal , dv ) 
   #podesti
   crtaj_kvadar ( orMjL , (-1,-1,0)  , (1,1,0) , orSm , 44 , 0 ) 
   #stup
   crtaj_kvadar ( orMjL , (0,0,1)  , (0,0,3) , orSm , materijal , dv ) 
   #doljnja lampa
   crtaj_kvadar ( orMjL , (0,0,0)  , (0,0,0) , orSm , 89 , 0 ) 
   #gornja lampa
   crtaj_kvadar ( orMjL , (0,0,4)  , (0,0,4) , orSm , 89 , 0 ) 
   #vijenci
   crtaj_stepenice ( orMjL , (1,-1,5) , (1,1,5) , orSm , blok_id = stepenice_mat , rel_smjer  = "odmene" , gore_dolje = "da"  )
   crtaj_stepenice ( orMjL , (-1,-1,5) , (-1,1,5) , orSm , blok_id = stepenice_mat , rel_smjer  = "meni" , gore_dolje = "da"  )
   crtaj_stepenice ( orMjL , (0,-1,5) , (0,-1,5) , orSm , blok_id = stepenice_mat , rel_smjer  = "lijevo" , gore_dolje = "da"  )       
   crtaj_stepenice ( orMjL , (0,1,5) , (0,1,5) , orSm , blok_id = stepenice_mat , rel_smjer  = "desno" , gore_dolje = "da"  ) 
   
   #stropne lampe
   crtaj_kvadar ( orMjL , (-6,0,6)  , (-6,0,6) , orSm , 89 , 0 )
   crtaj_kvadar ( orMjL , (-6,-6,6)  , (-6,-6,6) , orSm , 89 , 0 )
   crtaj_kvadar ( orMjL , (6,0,6)  , (6,0,6) , orSm , 89 , 0 )
   crtaj_kvadar ( orMjL , (6,6,6)  , (5,6,6) , orSm , 89 , 0 )
   crtaj_kvadar ( orMjL , (0,-6,6)  , (0,-6,6) , orSm , 89 , 0 )
   crtaj_kvadar ( orMjL , (6,-6,6)  , (6,-6,6) , orSm , 89 , 0 )
   crtaj_kvadar ( orMjL , (0,6,6)  , (0,6,6) , orSm , 89 , 0 )
   crtaj_kvadar ( orMjL , (-6,5,6)  , (0,6,6) , orSm , 89 , 0 )
   
   #baklje na podu - maknuto
   """
   for dX in ( -9, -6, -3 , 0 ,3 , 6 ,9  ):
      for dZ in ( -9, -6, -3 , 0 ,3 , 6 ,9  ):
         gdje = rel2abs ( orMjL ,  ( dX , dZ , 0 )  , orSm  )
         kojiBlok = mc.getBlock ( gdje ) 
         if kojiBlok == AIR.id :
            mc.setBlock(gdje , TORCH.id , 5 )
   """
 
if __name__ == "__main__":    #direktan poziv
   
   orMj = gdjeSam ()
   orSm = gdjeGledam ()
   """ shiroko
   for dX in range (-126,127,21):
      for dZ in range ( -126 , 127 , 21 ):
         katakombe ( orMj ,  orSm ,  iX=11 + dX, iZ=dZ , iY=0 ) 
   """
   for dX in range (-84,85,21):
      mc.postToChat("dX %f" % dX )
      for dZ in range ( -84 , 85 , 21 ):
         katakombe ( orMj ,  orSm ,  iX=11 + dX, iZ=dZ , iY=0 ) 
      
   mc.postToChat("Kraj !!!" )
   