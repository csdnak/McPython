#ispred lika crta more baklji po tlu

import time
from mc import * #import api-ja
from crtanje import *		#tu je funkcija koju zovem

mc = Minecraft() #inicijalizacija sustava za rad sa Minecraftom

def modul_kraj (  orMj ,  orSm , iX=0 , iZ=0 , iY=0  ,  materijal = 98, dv = 0  , kutija = "kutija" , crtaj_kutije = "da" ):

   dX = 0
   orMj = premjesti_origin ( orMj , iX , iZ , iY ,  orSm ) #mice gdje treba, crta ispred toon-a 
   orSm = ortUdesno ( orSm )
   orMj = premjesti_origin ( orMj , - 3 , -6 , 0 ,  orSm ) #mice gdje treba, crta ispred toon-a  korekcija naprijed udesno
   
   if ( kutija == "kutija" ) :
      kmat = 54
   else :
      kmat = 146
   crtaj_kutiju ( orMj , [ 3 + dX , 2, 4 ]  , [ 3 + dX ,  3 , 4  ] , orSm , rel_smjer  = "meni" , blok_id = kmat     )
   crtaj_hopper    ( orMj , [ 3 + dX , 3, 3 ]  , [ 3 + dX ,  3 , 0  ] , orSm , "desno" ) # hopper ispod kutije
   crtaj_kutiju ( orMj , [ 3 + dX , 4, 3 ]  , [ 3 + dX ,  5 , 0  ] , orSm , rel_smjer  = "meni" , blok_id = kmat     ) # dodatne kutije



def modul_sorter (  orMj ,  orSm , iX=0 , iZ=0 , iY=0  ,  materijal = 98, dv = 0  , kutija = "kutija" , crtaj_kutije = "da" ):

   orMj = premjesti_origin ( orMj , iX , iZ , iY ,  orSm ) #mice gdje treba, crta ispred toon-a 
   orSm = ortUdesno ( orSm )
   orMj = premjesti_origin ( orMj , - 3 , -6 , 0 ,  orSm ) #mice gdje treba, crta ispred toon-a  korekcija naprijed udesno

   crtaj_kvadar ( orMj , [ 3   , 0, 0 ]  , [ 3   , -2 , 2  ] , orSm , materijal , 2 ) # blok
   crtaj_kvadar ( orMj , [ 3   , -2, 2 ]  , [ 3   ,  -2 , 2  ] , orSm , 0 , 0 ) # zrak
   crtaj_kvadar ( orMj , [ 3   , -1, 1 ]  , [ 3   ,  -1 , 1  ] , orSm , 0 , 0 ) # zrak
   crtaj_kvadar ( orMj , [ 3   , 0, 0 ]  , [ 3   ,  0 , 0  ] , orSm , 0 , 0 ) # zrak
   crtaj_kvadar ( orMj , [ 3   , -2, 0 ]  , [ 3   ,  -2 , 0  ] , orSm , 0 , 0 ) # zrak
   crtaj_redstonedust ( orMj , [ 3   , -2, 2 ]  , [ 3   ,  -2 , 2  ] , orSm )
   crtaj_redstonedust ( orMj , [ 3   , -1, 3 ]  , [ 3   ,  -1 , 3  ] , orSm )
   crtaj_redstonetorch ( orMj , [ 3   , 1, 1 ]  ,  orSm  , "desno" )  
   crtaj_comparator ( orMj , [ 3   , 0, 3 ]  , [ 3   ,  0 , 3 ]  , orSm , rel_smjer  = "lijevo" )
   crtaj_repeater ( orMj , [ 3   , -1, 1 ]  , [ 3   ,  -1 , 1  ]  , orSm , rel_smjer  = "desno" )
   crtaj_hopper    ( orMj , [ 3   , 1, 2 ]  , [ 3   ,  1 , 3  ] , orSm , "desno" ) # dva doljnja
   crtaj_hopper    ( orMj , [ 3   , 1, 4 ]  , [ 3   ,  1 , 4  ] , orSm , "odmene" ) # gornji
   pisi = ( "minecraft:item_frame" , "0")
   sto =  '{TransferCooldown:0,Items:[0:{Slot:0b,id:"%s",Count:4b,Damage:%ss,},1:{Slot:1b,id:"%s",Count:5b,Damage:%ss,},2:{Slot:2b,id:"%s",Count:5b,Damage:%ss,},3:{Slot:3b,id:"%s",Count:5b,Damage:%ss,},4:{Slot:4b,id:"%s",Count:5b,Damage:%ss,},],id:"Hopper",Lock:"",}' % ( pisi [ 0 ] , pisi  [ 1 ]  , pisi  [ 0 ] , pisi [ 1 ] , pisi [ 0 ] , pisi  [ 1 ] , pisi [ 0 ] , pisi  [ 1 ] , pisi [ 0 ] , pisi  [ 1 ] )
   bla = rel2abs ( orMj , ( 3   , 1 ,  3  ) , orSm )

   time.sleep ( 0.1 )
   mc.setBlockWithNBT(bla,154,smjer_hoppera ( orSm , "desno")  , sto )   #hopper gleda na istok 
   bla = rel2abs ( orMj , ( 3   , 1 ,  2  ) , orSm )
   #mc.postToChat("orginal: %s %s " %  ( dX , bla )    )
   time.sleep ( 0.1 )
   sto =  '{TransferCooldown:0,Items:[0:{Slot:0b,id:"%s",Count:2b,Damage:%ss,},1:{Slot:1b,id:"%s",Count:2b,Damage:%ss,},2:{Slot:2b,id:"%s",Count:2b,Damage:%ss,},3:{Slot:3b,id:"%s",Count:5b,Damage:%ss,},4:{Slot:4b,id:"%s",Count:5b,Damage:%ss,},],id:"Hopper",Lock:"",}' % ( pisi [ 0 ] , pisi  [ 1 ]  , pisi  [ 0 ] , pisi [ 1 ] , pisi [ 0 ] , pisi  [ 1 ] , pisi [ 0 ] , pisi  [ 1 ] , pisi [ 0 ] , pisi  [ 1 ] )
   mc.setBlockWithNBT(bla,154,smjer_hoppera ( orSm , "desno")  , sto )   #hopper gleda na istok 
   #bla = rel2abs ( orMj , ( 3   , 5 ,  2  ) , orSm )
   #mc.setBlock(bla,53,4  )       #oak wood stairs naopako, gledaju na istok
   
   if ( crtaj_kutije != "da" ) :
      return 1
	  
   crtaj_stepenice ( orMj , ( 3   , 5 ,  2  ) , ( 3   , 5 ,  2  ) , orSm , blok_id = 53 , rel_smjer  = "lijevo" , gore_dolje = "da"  )

   if ( kutija == "kutija" ) :
      kmat = 54
   else :
      kmat = 146
   crtaj_kutiju ( orMj , [ 3   , 2, 2 ]  , [ 3   ,  3 , 2  ] , orSm , rel_smjer  = "meni" , blok_id = kmat     )
   crtaj_hopper    ( orMj , [ 3   , 3, 1 ]  , [ 3   ,  3 , 0  ] , orSm , "desno" ) # hopper ispod kutije
   crtaj_kutiju ( orMj , [ 3   , 4, 1 ]  , [ 3   ,  5 , 0  ] , orSm , rel_smjer  = "meni" , blok_id = kmat     ) # dodatne kutije

   mc.postToChat("orginal:  %s  " %    iZ )
   return 1
   
if __name__ == "__main__":    #direktan poziv
   orMj = gdjeSam ()
   orSm = gdjeGledam ()
   modul_sorter ( orMj , orSm , crtaj_kutije = "ne")   
   