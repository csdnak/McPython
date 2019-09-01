# crta osmatracnicu ispred lika, radi sirovo i primitivno

from mc import * #import api-ja
from crtaj_vrata import *
from crtaj_blok import *
mc = Minecraft() #inicijalizacija sustava za rad sa Minecraftom

#gdje sam
radnaPozicija = mc.player.getPos()		
#kamo gledam
smjerRada = mc.player.getDirection ()			#uzmem kamo gledam
#smjer gledanja radi preglednosti spremimo u "vektor""
Vx=0												#pocetne vrijednosti su nule
Vz=0
if abs (smjerRada.x) > abs (smjerRada.z): 		#nadje se dominanti smjer i spremi u vektor
   Vx=int(round(smjerRada.x))
else:
   Vz=int(round(smjerRada.z))
if Vx == 1 :										#Korektor za smjer stepenica udesno gore
   st_korektor = 0x2
if Vx == -1 :
   st_korektor = 0x3
if Vz == 1 :
   st_korektor = 0x1
if Vz == -1 :
   st_korektor = 0x0


for br in range ( 9 ) :
   korektor = br * 4
   
   crtaj_blok ( 1 , -1 + korektor , -3 , 5 , -1 + korektor, 3 , 1 )   # stone temelji
   crtaj_blok ( 4 , -1 + korektor, -1 , 4 , -1 + korektor, 2 , 0 )   # rupa za stepenice
   crtaj_blok ( 1 , 0 + korektor, -3 , 1 , 2 + korektor, -3 , 1  ) # lijevi prednji stup
   crtaj_blok ( 1 , 0 + korektor, 3 , 1 , 2 + korektor, 3 , 1  ) # desni prednji stup
   crtaj_blok ( 5 , 0 + korektor, -3 , 5 , 2 + korektor, -3 , 1  ) # lijevi zadnji stup
   crtaj_blok ( 5 , 0 + korektor, 3 , 5 , 2 + korektor, 3 , 1  ) # desni zadnji stup
   
   crtaj_blok ( 4, -1 + korektor, 2 ,4, -1 + korektor, 2 , 109 , st_korektor ) # stepenica cobblestone
   crtaj_blok ( 4, 0 + korektor, - 1 ,4, 0 + korektor, - 1 , 109 , st_korektor ) # stepenica cobblestone
   crtaj_blok ( 4, 1 + korektor, 0 ,4, 1+ korektor , 0 , 109 , st_korektor ) # stepenica cobblestone
   crtaj_blok ( 4, 2 + korektor, 1 ,4, 2 + korektor, 1 , 109 , st_korektor ) # stepenica cobblestone
   
