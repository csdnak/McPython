# skica - LAME
#definicija objekta i poziv rutine za crtanje
import time 
import sys
from crtanje import *		#tu je funkcija koju zovem
from popis_blokova import *
from mc import *			
mc = Minecraft() #inicijalizacija sustava za rad sa Minecraftom

# origin ispred na sredini 
orMj = gdjeSam ()
orSm = gdjeGledam ()
time.sleep ( 10 )
vrtilica = 1
for br in popis :
   mc.postToChat( " %s %f " % ( br [ 0 ] , vrtilica ) )
   sto =  '{TransferCooldown:0,Items:[0:{Slot:0b,id:"%s",Count:4b,Damage:%ss,},1:{Slot:1b,id:"%s",Count:5b,Damage:%ss,},2:{Slot:2b,id:"%s",Count:5b,Damage:%ss,},3:{Slot:3b,id:"%s",Count:5b,Damage:%ss,},4:{Slot:4b,id:"%s",Count:5b,Damage:%ss,},],id:"Hopper",Lock:"",}' % ( br [ 0 ] , br [ 1 ]  , br [ 0 ] , br [ 1 ] , br [ 0 ] , br [ 1 ] , br [ 0 ] , br [ 1 ] , br [ 0 ] , br [ 1 ] )
   bla = rel2abs ( orMj , ( 1 + vrtilica , -1 ,  0  ) , orSm )
   mc.setBlockWithNBT(bla,154,5 , sto )   #hopper gleda na istok 
   bla = rel2abs ( orMj , ( 1 + vrtilica , 3 ,  -1  ) , orSm )
   mc.setBlock(bla,53,4  )       #oak wood stairs naopako, gledaju na istok
   time.sleep ( 1 )
   vrtilica = vrtilica + 1
