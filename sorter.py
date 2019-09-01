# crtanje automatizirani sorter
#definicija objekta i poziv rutine za crtanje
import time 
#import sys
from crtanje import *		#tu je funkcija koju zovem
from modul_sorter import * 
from popis_blokova import *

from mc import *			
mc = Minecraft() #inicijalizacija sustava za rad sa Minecraftom


#sandstone glatki
materijal = 24
dv = 2

itemId = materialGenerator ()

"""
orMj = gdjeSam ()
orSm = gdjeGledam ()
   
#korekcija polozaja
orMjA = gdjeSam ()

mc.postToChat("orginal: %s " %  orMj    )

"""

def pocetak_sortera ( orMj , orSm ) :
   mc.postToChat("orginal: %s " %  orMj    )
   crtaj_hopper    ( orMj , [ 2  , 1, 4 ]  , [ 2 ,  1 , 4  ] , orSm , "odmene" ) # gornji
   crtaj_kutiju ( orMj , [ 1 , 1, 5 ]  , [ 2 ,  1 , 5  ] , orSm , rel_smjer  = "lijevo" )
   for br in range ( 0 , 4 ):
      crtaj_stepenice ( orMj , [ 2 , 5 - br , 0 + br ]  , [ 2 ,  5 - br , 0 + br  ] , orSm , blok_id = 128 , rel_smjer  = "desno" )
   crtaj_hopper    ( orMj , [ 0  , 1, 5 ]  , [ -23 ,  1 , 5  ] , orSm , "odmene" ) # izlaz iz sortera
   crtaj_hopper    ( orMj , [ -23  , 21, 5 ]  , [ -23 ,  2 , 5  ] , orSm , "lijevo" ) # od kutija to izlaza iz sorter
   crtaj_hopper    ( orMj , [ -23  , 21, 6 ]  , [ -23 ,  20 , 6  ] , orSm , "dolje" ) # spust iz kutija
   

def crtaj_modul ( orMj , orSm , dX  ):
   """
   dX - udaljenost modula
   koja_kutija - par - obicna , nepar - traped
   """
   """
   od = rel2abs ( origin , poc , smjer )
   do = rel2abs ( origin , kraj , smjer )
   mc.setBlocks ( od , do , blok_id , blok_dv  )
   """
   crtaj_kvadar ( orMj , [ 3 + dX , 0, 0 ]  , [ 3 + dX , -2 , 2  ] , orSm , materijal , 2 ) # blok
   crtaj_kvadar ( orMj , [ 3 + dX , -2, 2 ]  , [ 3 + dX ,  -2 , 2  ] , orSm , 0 , 0 ) # zrak
   crtaj_kvadar ( orMj , [ 3 + dX , -1, 1 ]  , [ 3 + dX ,  -1 , 1  ] , orSm , 0 , 0 ) # zrak
   crtaj_kvadar ( orMj , [ 3 + dX , 0, 0 ]  , [ 3 + dX ,  0 , 0  ] , orSm , 0 , 0 ) # zrak
   crtaj_kvadar ( orMj , [ 3 + dX , -2, 0 ]  , [ 3 + dX ,  -2 , 0  ] , orSm , 0 , 0 ) # zrak
   crtaj_redstonedust ( orMj , [ 3 + dX , -2, 2 ]  , [ 3 + dX ,  -2 , 2  ] , orSm )
   crtaj_redstonedust ( orMj , [ 3 + dX , -1, 3 ]  , [ 3 + dX ,  -1 , 3  ] , orSm )
   crtaj_redstonetorch ( orMj , [ 3 + dX , 1, 1 ]  ,  orSm  , "desno" )  
   crtaj_comparator ( orMj , [ 3 + dX , 0, 3 ]  , [ 3 + dX ,  0 , 3 ]  , orSm , rel_smjer  = "lijevo" )
   crtaj_repeater ( orMj , [ 3 + dX , -1, 1 ]  , [ 3 + dX ,  -1 , 1  ]  , orSm , rel_smjer  = "desno" )
   
   
   crtaj_hopper    ( orMj , [ 3 + dX , 1, 2 ]  , [ 3 + dX ,  1 , 3  ] , orSm , "desno" ) # dva doljnja
   crtaj_hopper    ( orMj , [ 3 + dX , 1, 4 ]  , [ 3 + dX ,  1 , 4  ] , orSm , "odmene" ) # gornji
   pisi = itemId.next ()
   sto =  '{TransferCooldown:0,Items:[0:{Slot:0b,id:"%s",CustomName:"Bla",CustomNameVisible:1b,Count:1b,Damage:%ss,},1:{Slot:1b,id:"%s",Count:2b,Damage:%ss,},2:{Slot:2b,id:"%s",Count:2b,Damage:%ss,},3:{Slot:3b,id:"%s",Count:5b,Damage:%ss,},4:{Slot:4b,id:"%s",Count:5b,Damage:%ss,},],id:"Hopper",Lock:"",}' % ( pisi [ 0 ] , pisi  [ 1 ]  , pisi  [ 0 ] , pisi [ 1 ] , pisi [ 0 ] , pisi  [ 1 ] , pisi [ 0 ] , pisi  [ 1 ] , pisi [ 0 ] , pisi  [ 1 ] )
   bla = rel2abs ( orMj , ( 3 + dX , 1 ,  3  ) , orSm )
   mc.postToChat("orginal: %s %s " %  ( dX , bla )    )
   time.sleep ( 0.1 )
   mc.setBlockWithNBT(bla,154,smjer_hoppera ( orSm , "desno")  , sto )   #hopper gleda na istok 
   bla = rel2abs ( orMj , ( 3 + dX , 1 ,  2  ) , orSm )
   mc.postToChat("orginal: %s %s " %  ( dX , bla )    )
   time.sleep ( 0.1 )
   sto =  '{TransferCooldown:0,Items:[0:{Slot:0b,id:"%s",Count:2b,Damage:%ss,},1:{Slot:1b,id:"%s",Count:2b,Damage:%ss,},2:{Slot:2b,id:"%s",Count:2b,Damage:%ss,},3:{Slot:3b,id:"%s",Count:5b,Damage:%ss,},4:{Slot:4b,id:"%s",Count:5b,Damage:%ss,},],id:"Hopper",Lock:"",}' % ( pisi [ 0 ] , pisi  [ 1 ]  , pisi  [ 0 ] , pisi [ 1 ] , pisi [ 0 ] , pisi  [ 1 ] , pisi [ 0 ] , pisi  [ 1 ] , pisi [ 0 ] , pisi  [ 1 ] )
   mc.setBlockWithNBT(bla,154,smjer_hoppera ( orSm , "desno")  , sto )   #hopper gleda na istok 
   #bla = rel2abs ( orMj , ( 3 + dX , 5 ,  2  ) , orSm )
   #mc.setBlock(bla,53,4  )       #oak wood stairs naopako, gledaju na istok
   crtaj_stepenice ( orMj , ( 3 + dX , 5 ,  2  ) , ( 3 + dX , 5 ,  2  ) , orSm , blok_id = 53 , rel_smjer  = "desno" , gore_dolje = "da"  )

   
   kutija = 54
   tkutija = 146
   if ( int ( dX ) % 2 == 1 ) :
      kmat = kutija
   else :
      kmat = tkutija
   crtaj_kutiju ( orMj , [ 3 + dX , 2, 2 ]  , [ 3 + dX ,  3 , 2  ] , orSm , rel_smjer  = "meni" , blok_id = kmat     )
   crtaj_hopper    ( orMj , [ 3 + dX , 3, 1 ]  , [ 3 + dX ,  3 , 0  ] , orSm , "desno" ) # hopper ispod kutije
   crtaj_kutiju ( orMj , [ 3 + dX , 4, 1 ]  , [ 3 + dX ,  5 , 0  ] , orSm , rel_smjer  = "meni" , blok_id = kmat     ) # dodatne kutije
   crtaj_comparator ( orMj , [ 3 + dX , 6, 0 ]  , [ 3 + dX ,  6 , 0  ]  , orSm , rel_smjer  = "desno" )
   
def kraj ( orMj , orSm , dX , duzina ) :
   dX += 1
   crtaj_hopper    ( orMj , [ 3 + dX , 1, 4 ]  , [ 3 + dX ,  1 , 4  ] , orSm , "odmene" ) # dovod i razmak od sortirke
   
   for brojalica in range ( 0 ,  duzina   ) :
      dX += 1                       # translacija "udalj"
      kutija = 54                   #materijali za kutije
      tkutija = 146
      if ( int ( dX ) % 2 == 1 ) :
         kmat = kutija
      else :
         kmat = tkutija

      crtaj_hopper    ( orMj , [ 3 + dX , 1, 4 ]  , [ 3 + dX ,  1 , 4  ] , orSm , "odmene" ) # gornji hopper
      crtaj_hopper    ( orMj , [ 3 + dX , 1, 0 ]  , [ 3 + dX ,  1 , 3  ] , orSm , "desno" ) # razvod po kutijama
      crtaj_kutiju ( orMj , [ 3 + dX , 2, 0 ]  , [ 3 + dX ,  3 , 3  ] , orSm , rel_smjer  = "meni" , blok_id = kmat     ) #kutije
      
 

 
def sorter  ( dX , dZ , dY , duzina , rep ):

   # origin ispred na sredini 
   orMj   = rel2abs ( orMjA ,  ( dX , dZ , dY )   , orSm  ) 
   bla = orMj [ 1 ]
   orMj [ 1 ] = orMj [ 2 ]
   orMj [ 2 ] = bla
   
   mc.postToChat("orginal: %s " %  orMj    )

   

   pocetak_sortera ( orMj )
   
   for br in range (  0, duzina ):
      crtaj_modul ( orMj , br )
   
   kraj (  orMj , br , rep) 
   

def blok_sortera (orMj , orSm):

   #lijevo ulaz
   pocetak_sortera ( orMj , orSm ) 
   for br in range (  0, 11 ):
      crtaj_modul ( orMj , orSm , br )
   crtaj_hopper    ( orMj , [ 14 , 1, 4 ]  , [ 14 ,  3 , 4  ] , orSm , "desno" )
   crtaj_hopper    ( orMj , [ 14 , 4, 4 ]  , [ 17 ,  4 , 4  ] , orSm , "odmene" )
   
   #lijevo krak
   orMj = premjesti_origin ( orMj , 17 , 7 , 0 ,  orSm )
   orSm = ortUlijevo ( orSm )
   for br in range (  0, 17 ):
      crtaj_modul ( orMj , orSm , br )
   crtaj_hopper    ( orMj , [ 18 , 1, 4 ]  , [ 24 ,  1 , 4  ] , orSm , "odmene" )
   crtaj_hopper    ( orMj , [ 25 , 1, 4 ]  , [ 25 ,  6 , 4  ] , orSm , "desno" )
   
   orSm2 = ortUlijevo ( orSm )
   modul_sorter (  orMj ,  orSm2 , iX=-6 , iZ=20 , iY=0  ,  materijal = 98, dv = 0  , kutija = "kutija" , crtaj_kutije = "ne" )  #PRVA TRI MODULA
   modul_sorter (  orMj ,  orSm2 , iX=-6 , iZ=21 , iY=0  ,  materijal = 98, dv = 0  , kutija = "kutija" , crtaj_kutije = "ne" )
   modul_sorter (  orMj ,  orSm2 , iX=-6 , iZ=22 , iY=0  ,  materijal = 98, dv = 0  , kutija = "kutija" , crtaj_kutije = "ne" )
   
   
   crtaj_hopper    ( orMj , [ -2 , 20, 2 ]  , [ -2 ,  23 , 2  ] , orSm2 , "desno" )
   
      
   # lijevo dolje
   orMj = premjesti_origin ( orMj , 26 , 4 , 0 ,  orSm )
   orSm = ortUdesno ( orSm )
   
   orSm2 = ortUlijevo ( orSm )
   modul_sorter (  orMj ,  orSm2 , iX=-6 , iZ=2 , iY=0  ,  materijal = 98, dv = 0  , kutija = "kutija" , crtaj_kutije = "ne" )   #DRUGA 4 MODULA
   modul_sorter (  orMj ,  orSm2 , iX=-6 , iZ=1 , iY=0  ,  materijal = 98, dv = 0  , kutija = "kutija" , crtaj_kutije = "ne" )
   modul_sorter (  orMj ,  orSm2 , iX=-6 , iZ=0 , iY=0  ,  materijal = 98, dv = 0  , kutija = "kutija" , crtaj_kutije = "ne" )
   modul_sorter (  orMj ,  orSm2 , iX=-6 , iZ=-1 , iY=0  ,  materijal = 98, dv = 0  , kutija = "kutija" , crtaj_kutije = "ne" )
   
   crtaj_hopper    ( orMj , [ -2 , 2, 2 ]  , [ -2 ,  -21 , 2  ] , orSm2 , "lijevo" )
   crtaj_hopper    ( orMj , [ -2 , -22, 2 ]  , [ -2 ,  -22 , -2  ] , orSm2 , "dolje" )
   crtaj_hopper    ( orMj , [ -2 ,  -22 , -3 ]  , [ -11 ,  -22 , -3  ] , orSm2 , "meni" )
   crtaj_hopper    ( orMj , [ -12 ,  -22 , -3 ]  , [ -12 ,  -20 , -3  ] , orSm2 , "desno" )
   crtaj_hopper    ( orMj , [  -12 ,  -19 , -3 ]  , [  -12 ,  -19 , -3  ] , orSm2 , "dolje" ) #spoj na kutije
   
   #izmedju 1 i 2 reda
   crtaj_hopper    ( orMj , [ 6 ,  -19 , -4 ]  , [ 6 ,  -9 , -4  ] , orSm2 , "desno" )
   crtaj_hopper    ( orMj , [ 6 ,  -8 , -4 ]  , [ 6 ,  -8 , -4  ] , orSm2 , "meni" )
   #izmedju 2 i 3 reda
   crtaj_hopper    ( orMj , [ -32 ,  -8 , -4 ]  , [ -32 ,  2 , -4  ] , orSm2 , "desno" )
   crtaj_hopper    ( orMj , [ -32 ,  3 , -4 ]  , [ -32 ,  3 , -4  ] , orSm2 , "odmene" )
   
   
   
   for br in range (  0, 10 ):
      crtaj_modul ( orMj , orSm , br )
   crtaj_hopper    ( orMj , [ 11 , 1, 4 ]  , [ 17 ,  1 , 4  ] , orSm , "odmene" )
   crtaj_hopper    ( orMj , [ 18 , 1, 4 ]  , [ 18 ,  6 , 4  ] , orSm , "desno" )
      

      # dugi
   orMj = premjesti_origin ( orMj , 19 , 4 , 0 ,  orSm )
   orSm = ortUdesno ( orSm )
   for br in range (  0, 51 ):
      crtaj_modul ( orMj , orSm , br )
   crtaj_hopper    ( orMj , [ 52 , 1, 4 ]  , [ 58 ,  1 , 4  ] , orSm , "odmene" )
   crtaj_hopper    ( orMj , [ 59 , 1, 4 ]  , [ 59 ,  6 , 4  ] , orSm , "desno" )
    
   # desno gore
   orMj = premjesti_origin ( orMj , 60 , 4 , 0 ,  orSm )
   orSm = ortUdesno ( orSm )
   for br in range (  0, 10 ):
      crtaj_modul ( orMj , orSm , br )
   crtaj_hopper    ( orMj , [ 11 , 1, 4 ]  , [ 17 ,  1 , 4  ] , orSm , "odmene" )
   crtaj_hopper    ( orMj , [ 18 , 1, 4 ]  , [ 18 ,  6 , 4  ] , orSm , "desno" )
    
      
   #desno krak
   orMj = premjesti_origin ( orMj , 19 , 4 , 0 ,  orSm )
   orSm = ortUdesno ( orSm )
   for br in range (  0, 17 ):
      crtaj_modul ( orMj , orSm , br )
   crtaj_hopper    ( orMj , [ 19 , 1, 4 ]  , [ 19 ,  -3 , 4  ] , orSm , "lijevo" )
   crtaj_hopper    ( orMj , [ 19 , -4, 4 ]  , [ 17 ,  -4 , 4  ] , orSm , "meni" )

      
   #desno ulaz
      
   orMj = premjesti_origin ( orMj , 15 , -1 , 0 ,  orSm )
   orSm = ortUlijevo ( orSm )   
   for br in range (  0, 9 ):
      crtaj_modul ( orMj , orSm , br )
   crtaj_hopper    ( orMj , [ 10 , 1, 4 ]  , [ 13 ,  1 , 4  ] , orSm , "odmene" )
   orMj = premjesti_origin ( orMj , 13 , 7 , 0 ,  orSm )
   orSm = ortUlijevo ( orSm ) 
   kraj ( orMj ,  orSm , 2 , 22 )
   


   
   
   

 
if __name__ == "__main__":    #direktan poziv
   orMj = gdjeSam ()
   orSm = gdjeGledam ()
   blok_sortera (  orMj , orSm   )
