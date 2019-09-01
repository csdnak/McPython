#nekakve bitmape ??????
from crtanje import *		#tu je funkcija koju zovem
from crtanje2 import *		#tu je funkcija koju zovem
from mc import *			

mc = Minecraft() #inicijalizacija sustava za rad sa Minecraftom

#strelica
lik=[
[2,0,-1,STONE ,0],
[3,0,-1,STONE,0],
[4,-1,-1,STONE,0],
[4,0,-1,STONE,0],
[4,1,-1,GOLD_BLOCK,0],
[5,0,-1,STONE,0],
]

#"neshto" :)
lik2=[
[2,0,-1,STONE,0],
[3,0,-1,STONE,0],
[4,-1,-1,STONE,0],
[4,0,-1,STONE,0],
[4,0,1,STONE,0],
[4,1,-1,STONE,0],
[5,0,-1,STONE,0],
[6,1,0,GOLD_BLOCK,0],
]


#zid sa prozorom
zid_prozor=[
[4,-1,0,1,0],
[4,1,0,1,0],
[4,1,0,1,0],
[4,-1,1,1,0],
[4,0,1,102,0],
[4,1,1,1,0],
[4,-1,2,1,0],
[4,0,2,1,0],
[4,1,2,1,0],

]

#zid sa vratima 

zid_ulaz = [
[4,-1,0,1,0],	#prvo nacrtamo zid sa rupom za vrata
[4,1,0,1,0],
[4,-1,1,1,0],
[4,1,1,1,0],
[4,-1,2,1,0],
[4,0,2,1,0],
[4,1,2,1,0],
[4,1,0,195,0], #i na kraju postavimo vrata prvo doljnji dio
[4,0,1,195,8], #8 govori da je ovo gornji dio vrata
]

brlog = [
[4,-1,0,1,0],	#prvo nacrtamo zid sa rupom za vrata
[4,1,0,1,0],
[4,-1,1,1,0],
[4,1,1,1,0],
[4,-1,2,1,0],
[4,0,2,1,0],
[4,1,2,1,0],
[4,0,0,195,0], #i na kraju postavimo vrata prvo doljnji dio
[4,0,1,195,8], #8 govori da je ovo gornji dio vrata
[5,-1,0,1,0],	#bocni zidovi
[5,1,0,1,0],
[5,-1,1,1,0],
[5,1,1,1,0],
[5,-1,2,1,0],
[5,1,2,1,0],
[6,-1,0,1,0],	#zadnji zid
[6,0,0,1,0],
[6,1,0,1,0],
[6,-1,1,1,0],
[6,0,1,1,0],
[6,1,1,1,0],
[6,-1,2,1,0],
[6,0,2,1,0],
[6,1,2,1,0],
[5,0,3,1,0],		# "Krov"
]


# polje


polje = [
[1 , -5 , 0 , 1 ,0 ],
[1 , -4 , 0 , 1,0 ],
[1 , -3 , 0 , 1,0 ],
[1 , -2 , 0 , 1,0 ],
[1 , -1 , 0 , 1,0 ],
[1 , 0 , 0 , 1,0 ],
[1 , 1 , 0 , 1,0 ],
[1 , 2 , 0 , 1,0 ],
[1 , 3 , 0 , 1,0 ],
[1 , 4 , 0 , 1,0 ],
[1 , 5 , 0 , 1,0 ],
[2 , -5 , 0 , 1,0 ],
[2 , -4 , 0 , 60,0 ],
[2 , -3 , 0 , 60,0 ],
[2 , -2 , 0 , 60,0 ],
[2 , -1 , 0 , 60,0 ],
[2 , 0 , 0 , 60,0 ],
[2 , 1 , 0 , 60,0 ],
[2 , 2 , 0 , 60,0 ],
[2 , 3 , 0 , 60,0 ],
[2 , 4 , 0 , 60,0 ],
[2 , 5 , 0 , 1,0 ],
[3 , -5 , 0 , 1,0 ],
[3 , -4 , 0 , 60,0 ],
[3 , -3 , 0 , 60,0 ],
[3 , -2 , 0 , 60,0 ],
[3 , -1 , 0 , 60,0 ],
[3 , 0 , 0 , 60,0 ],
[3 , 1 , 0 , 60,0 ],
[3 , 2 , 0 , 60,0 ],
[3 , 3 , 0 , 60,0 ],
[3 , 4 , 0 , 60,0 ],
[3 , 5 , 0 , 1,0 ],
[4 , -5 , 0 , 1,0 ],
[4 , -4 , 0 , 60,0 ],
[4 , -3 , 0 , 60,0 ],
[4 , -2 , 0 , 60,0 ],
[4 , -1 , 0 , 60,0 ],
[4 , 0 , 0 , 60,0 ],
[4 , 1 , 0 , 60,0 ],
[4 , 2 , 0 , 60,0 ],
[4 , 3 , 0 , 60,0 ],
[4 , 4 , 0 , 60,0 ],
[4 , 5 , 0 , 1,0 ],
[5 , -5 , 0 , 1,0 ],
[5 , -4 , 0 , 60,0 ],
[5 , -3 , 0 , 60,0 ],
[5 , -2 , 0 , 60,0 ],
[5 , -1 , 0 , 60,0 ],
[5 , 0 , 0 , 60,0 ],
[5 , 1 , 0 , 60,0 ],
[5 , 2 , 0 , 60,0 ],
[5 , 3 , 0 , 60,0 ],
[5 , 4 , 0 , 60,0 ],
[5 , 5 , 0 , 1,0 ],
[6 , -5 , 0 , 1,0 ],		# VODA
[6 , -4 , 0 , 60,0 ],
[6 , -3 , 0 , 60,0 ],
[6 , -2 , 0 , 60,0 ],
[6 , -1 , 0 , 60,0 ],
[6 , 0 , 0 , 9,0 ],
[6 , 1 , 0 , 60,0 ],
[6 , 2 , 0 , 60,0 ],
[6 , 3 , 0 , 60,0 ],
[6 , 4 , 0 , 60,0 ],
[6 , 5 , 0 , 1,0 ],
[7 , -5 , 0 , 1,0 ],
[7 , -4 , 0 , 60,0 ],
[7 , -3 , 0 , 60,0 ],
[7 , -2 , 0 , 60,0 ],
[7 , -1 , 0 , 60,0 ],
[7 , 0 , 0 , 60,0 ],
[7 , 1 , 0 , 60,0 ],
[7 , 2 , 0 , 60,0 ],
[7 , 3 , 0 , 60,0 ],
[7 , 4 , 0 , 60,0 ],
[7 , 5 , 0 , 1,0 ],
[8 , -5 , 0 , 1,0 ],
[8 , -4 , 0 , 60,0 ],
[8 , -3 , 0 , 60,0 ],
[8 , -2 , 0 , 60,0 ],
[8 , -1 , 0 , 60,0 ],
[8 , 0 , 0 , 60,0 ],
[8 , 1 , 0 , 60,0 ],
[8 , 2 , 0 , 60,0 ],
[8 , 3 , 0 , 60,0 ],
[8 , 4 , 0 , 60,0 ],
[8 , 5 , 0 , 1,0 ],
[9 , -5 , 0 , 1,0 ],
[9 , -4 , 0 , 60,0 ],
[9 , -3 , 0 , 60,0 ],
[9 , -2 , 0 , 60,0 ],
[9 , -1 , 0 , 60,0 ],
[9 , 0 , 0 , 60,0 ],
[9 , 1 , 0 , 60,0 ],
[9 , 2 , 0 , 60,0 ],
[9 , 3 , 0 , 60,0 ],
[9 , 4 , 0 , 60,0 ],
[9 , 5 , 0 , 1,0 ],
[10 , -5 , 0 , 1,0 ],
[10 , -4 , 0 , 60,0 ],
[10 , -3 , 0 , 60,0 ],
[10 , -2 , 0 , 60,0 ],
[10 , -1 , 0 , 60,0 ],
[10 , 0 , 0 , 60,0 ],
[10 , 1 , 0 , 60,0 ],
[10 , 2 , 0 , 60,0 ],
[10 , 3 , 0 , 60,0 ],
[10 , 4 , 0 , 60,0 ],
[10 , 5 , 0 , 1,0 ],
[11 , -5 , 0 , 1,0 ],
[11 , -4 , 0 , 1,0 ],
[11 , -3 , 0 , 1,0 ],
[11 , -2 , 0 , 1,0 ],
[11 , -1 , 0 , 1,0 ],
[11 , 0 , 0 , 1,0 ],
[11 , 1 , 0 , 1,0 ],
[11 , 2 , 0 , 1,0 ],
[11 , 3 , 0 , 1,0 ],
[11 , 4 , 0 , 1,0 ],
[11 , 5 , 0 , 1,0 ],
]


#gdje sam detaljno
radnaPozicija = mc.player.getPos()		
#kamo gledam
smjerRada = mc.player.getDirection ()			#uzmem kamo gledam
#smjer gledanja radi preglednosti spremimo u "vektor""
Vx=0												#pocetne vrijednosti su nule
Vz=0
if abs (smjerRada.x) > abs (smjerRada.z): 		#nadje se dominanti smjer i spremi u vektor
   Vx=round(smjerRada.x)
else:
   Vz=round(smjerRada.z)
#crtanje
pozicija = gdjeSam ()
if  abs ( Vx )  != abs ( Vz ) :		# ne pod 45
   """
   for nr in range ( 0 , 20 , 6 ):
      crtaj_tocku ( rel2abs ( gdjeSam (), [3 + nr , 0 , 0 ],  gdjeGledam () ) , 1,0  )
      crtaj_tocku ( rel2abs ( gdjeSam (), [3 + nr , 1 , 0 ],  gdjeGledam () ) , 1,2  )
      crtaj_tocku ( rel2abs ( gdjeSam (), [4 + nr , -1 , 0 ], gdjeGledam () ) , 1,3  )
      
      #crtaj_kvadar ( rel2abs ( [radnaPozicija.x , radnaPozicija.z , radnaPozicija.y   , 1 , 4) 
      
      crtaj_bitmap ( [ pozicija[0] , pozicija [1] , pozicija [2] ],  gdjeGledam ()  , lik  , nr ,  nr/2 ) 
   """
   
   #crtaj_kvadar ( gdjeSam () , [ 2 , -1 , 2 ]  , [ 6 , 2 , 4  ] , gdjeGledam () , 1 , 2 )
   
   for nr in range ( 9 ) :
      pomak = nr * 15
      crtaj_kvadar ( gdjeSam () , [ 1 + pomak , -5 , 0 ]  , [ 11 + pomak , 5 , 0  ] , gdjeGledam () , 1 , 0 )
      crtaj_kvadar ( gdjeSam () , [ 2 + pomak , -4 , 0 ]  , [ 10 + pomak , 4 , 0  ] , gdjeGledam () , 60 , 0 )
      crtaj_kvadar ( gdjeSam () , [ 6 + pomak , 0 , 0 ]  , [ 6 + pomak , 0 , 0  ] , gdjeGledam () , WATER.id , 0 )