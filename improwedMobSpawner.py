# mob spawner - simple
#definicija objekta i poziv rutine za crtanje

import time 
from crtanje import *		#tu je funkcija koju zovem
from mc import *			
mc = Minecraft() #inicijalizacija sustava za rad sa Minecraftom

# origin ispred na sredini 
orMjA = gdjeSam ()
orSm = gdjeGledam ()

#sandstone glatki
materijal = 24
dv = 2
stepenice = 128 
slab = 44
dv_slab = 1
uZraku = 34    # because of witchs
nivoa=5        # base on Y = 190
visinaNivoa = 5
spawnerBase = 190


surfaceLevel = nadji_dno ( orMjA , ( 0 , 0 , 0 ) , orSm )
relativeHigh = spawnerBase + surfaceLevel - 5


#Base
mc.postToChat("Baza !!"  )
crtaj_kvadar ( orMjA , ( -2  , -2 , -0 )  , (  20 , 20 , 4 ) , orSm ,  0 , 0 ) # clear the deck
crtaj_kvadar ( orMjA , ( -2  , -2 , -2 )  , (  20 , 20 , -1 ) , orSm ,  materijal , dv ) # sandstone edge platforma
crtaj_kvadar ( orMjA , ( -1  , -1 , -2 )  , (  19 , 19 , -1 ) , orSm ,  89 , 0 ) # glowstone platforma
time.sleep ( 15 )
crtaj_kvadar ( orMjA , ( 7  ,7 , -1 )  , (  12 , 12 , 0 ) , orSm ,  materijal , dv ) # pool frame
crtaj_kvadar ( orMjA , ( 8  , 8 , -1 )  , (  11 , 11 , 0 ) , orSm ,  WATER.id , 0 ) # pool

time.sleep ( 15 )
#legs

coord = (
(0,5),      #down left
(0,13),     #down right
(5,0),      #middle down left
(5,18),     #middle down rigt
(13,0),     #middle up left
(13,18),    #middle up right
(18,5),     #top left
(18,13)     #top right
)
mc.postToChat("Noge !!"  )
for br in coord :
   crtaj_kvadar ( orMjA , ( br [ 0 ] , br[ 1 ], 0 -5 )  , (  br [ 0 ] , br[ 1 ], relativeHigh  + uZraku ) , orSm , materijal , dv ) #make "leg"
   time.sleep ( 15 )

orFirst = orMjA
orMj = premjesti_origin ( orMjA , 0 ,0 , relativeHigh ,  orSm )

#Estetika

mc.postToChat("Krila !!"  )
for br in range ( nivoa ) :
   crtaj_kvadar ( orMj , ( -5 - br * 2 , -5 - br * 2, uZraku + 4 + br * visinaNivoa )  , (  23 + br * 2 , 23 + br * 2 , uZraku + 4 + br * visinaNivoa ) , orSm ,  materijal , dv ) # sandstone edge platforma
   time.sleep ( 3 )
   crtaj_kvadar ( orMj , ( -4 - br * 2 , -4 - br * 2, uZraku + 4 + br * visinaNivoa )  , (  22 + br * 2, 22 + br * 2 , uZraku + 4 + br * visinaNivoa ) , orSm ,  89 , 0 ) # glowstone platforma
   time.sleep ( 3 )
   crtaj_kvadar ( orMj ,   ( -2 , -2 , uZraku + 4 + br * visinaNivoa )  , ( 20 , 20 , uZraku + 4 + br * visinaNivoa ) , orSm ,  materijal , dv ) # hole frame
   time.sleep ( 3 )
   crtaj_kvadar ( orMj , ( -1 , -1 , uZraku + 4 + br * visinaNivoa )  , ( 19 , 19 , uZraku + 4 + br * visinaNivoa   ) , orSm ,  0 , 0 )
   time.sleep ( 25 )
   
   #crtaj_kvadar ( orMj , ( 8  , 8 , uZraku + 3 + br * visinaNivoa )  , (  11 , 11 , uZraku + 3 + br * visinaNivoa ) , orSm ,  0 , 0 ) # hole

   


mc.postToChat("Tijelo !!"  )
#crtaj_kvadar ( orMj , [ 8 , 8, uZraku -6 ]  , [ 11 , 11 , uZraku - 1   ] , orSm , STONE.id , 2 ) # lijevak ispod netreba
crtaj_kvadar ( orMj , [ 0 , 0 , uZraku ]  , [ 18 , 18 , uZraku + nivoa*visinaNivoa   ] , orSm ,  materijal , dv ) # main body
crtaj_kvadar ( orMj , [ 9 , 9, uZraku  ]  , [ 9 , 9 , uZraku + nivoa*visinaNivoa -1   ] , orSm , AIR.id , 2 ) # sredisnja rupa
time.sleep ( 15 )
# estetika
crtaj_kvadar ( orMj , [ 0 , 0, uZraku - 6 ]  , [ 4 , 4 , uZraku + nivoa*visinaNivoa + 1   ] , orSm , AIR.id , 2 ) # lijeva dolje rupa
time.sleep ( 15 )
crtaj_kvadar ( orMj , [ 0 , 14, uZraku - 6 ]  , [ 4 , 18 , uZraku + nivoa*visinaNivoa + 1   ] , orSm , AIR.id , 2 ) # desna dolje rupa
time.sleep ( 15 )
crtaj_kvadar ( orMj , [ 14 , 0, uZraku - 6 ]  , [ 18 , 4 , uZraku + nivoa*visinaNivoa + 1   ] , orSm , AIR.id , 2 ) # lijeva gore rupa
time.sleep ( 15 )
crtaj_kvadar ( orMj , [ 14 , 14, uZraku - 6 ]  , [ 18 , 18 , uZraku + nivoa*visinaNivoa + 1   ] , orSm , AIR.id , 2 ) # desna gore rupa
time.sleep ( 15 )


for br in range ( nivoa ) :
   mc.postToChat("lavirint  !!"  )
   crtaj_kvadar ( orMj , [ 2 , 6, uZraku + 3 + br * visinaNivoa ]  , [ 16 , 12 , uZraku +  4 + br * visinaNivoa  ] , orSm , AIR.id , 0 ) # main hole uzduzna
   crtaj_kvadar ( orMj , [ 6 , 2, uZraku + 3 + br * visinaNivoa ]  , [ 12 , 16 , uZraku +  4 + br * visinaNivoa  ] , orSm , AIR.id , 0 ) # main hole popprecna
   time.sleep ( 3 )
   crtaj_kvadar ( orMj , [ 1 , 9, uZraku + 1 + br * visinaNivoa ]  , [ 17 , 9 , uZraku +  4 + br * visinaNivoa  ] , orSm , AIR.id , 0 ) # uzduzna voda duga
   crtaj_kvadar ( orMj , [ 5 , 5, uZraku + 1 + br * visinaNivoa ]  , [ 13 , 5 , uZraku +  4 + br * visinaNivoa  ] , orSm , AIR.id , 0 ) # uzduzna voda lijeva
   time.sleep ( 3 )
   crtaj_kvadar ( orMj , [ 5 , 13, uZraku + 1 + br * visinaNivoa ]  , [ 13 , 13 , uZraku +  4 + br * visinaNivoa  ] , orSm , AIR.id , 0 ) # uzduzna voda desna
   crtaj_kvadar ( orMj , [ 9 , 1, uZraku + 1 + br * visinaNivoa ]  , [ 9 , 17 , uZraku +  4 + br * visinaNivoa  ] , orSm , AIR.id , 0 ) # poprecna voda duga
   time.sleep ( 3 )
   crtaj_kvadar ( orMj , [ 5 , 5, uZraku + 1 + br * visinaNivoa ]  , [ 5 , 13 , uZraku +  4 + br * visinaNivoa  ] , orSm , AIR.id , 0 ) # poprecna voda bliza
   crtaj_kvadar ( orMj , [ 13 , 5, uZraku + 1 + br * visinaNivoa ]  , [ 13 , 13 , uZraku +  4 + br * visinaNivoa  ] , orSm , AIR.id , 0 ) # poprecna voda dalja
   time.sleep ( 3 )
   crtaj_kvadar ( orMj , [ 9 , 1, uZraku + 1 + br * visinaNivoa ]  , [ 9 , 1 , uZraku +  1 + br * visinaNivoa  ] , orSm , 9 , 0 ) # water uzduzno blizi
   crtaj_kvadar ( orMj , [ 9 , 17, uZraku + 1 + br * visinaNivoa ]  , [ 9 , 17 , uZraku +  1 + br * visinaNivoa  ] , orSm , 9 , 0 ) # water uzduzno dalji
   time.sleep ( 3 )
   crtaj_kvadar ( orMj , [ 1 , 9, uZraku + 1 + br * visinaNivoa ]  , [ 1 , 9 , uZraku +  1 + br * visinaNivoa  ] , orSm , 9 , 0 ) # water poprecno blizi
   crtaj_kvadar ( orMj , [ 17 , 9, uZraku + 1 + br * visinaNivoa ]  , [ 17 , 9 , uZraku +  1 + br * visinaNivoa  ] , orSm , 9 , 0 ) # water poprecno dalji
   time.sleep ( 3 )

   crtaj_kvadar ( orMj , [ 9 , 1, uZraku + 2 + br * visinaNivoa ]  , [ 9 , 1 , uZraku +  4 + br * visinaNivoa  ] , orSm ,  materijal , dv ) #kamen iznad water water uzduzno blizi
   crtaj_kvadar ( orMj , [ 9 , 17, uZraku + 2 + br * visinaNivoa ]  , [ 9 , 17 , uZraku +  4 + br * visinaNivoa  ] , orSm , materijal , dv ) #kamen iznad water water uzduzno dalji
   time.sleep ( 3 )
   crtaj_kvadar ( orMj , [ 1 , 9, uZraku + 2 + br * visinaNivoa ]  , [ 1 , 9 , uZraku +  4 + br * visinaNivoa  ] , orSm , materijal , dv ) #kamen iznad water water poprecno blizi
   crtaj_kvadar ( orMj , [ 17 , 9, uZraku + 2 + br * visinaNivoa ]  , [ 17 , 9 , uZraku +  4 + br * visinaNivoa  ] , orSm , materijal , dv ) #kamen iznad water water poprecno dalji
   time.sleep ( 3 )

   
   crtaj_kvadar ( orMj , [ 5 , 5, uZraku + 1 + br * visinaNivoa ]  , [ 5 , 5 , uZraku +  1 + br * visinaNivoa  ] , orSm , 9 , 0 ) # water dolje lijevo
   time.sleep ( 3 )
   crtaj_kvadar ( orMj , [ 5 , 13, uZraku + 1 + br * visinaNivoa ]  , [ 5 , 13 , uZraku +  1 + br * visinaNivoa  ] , orSm , 9 , 0 ) # water dolje desno
   time.sleep ( 3 )
   crtaj_kvadar ( orMj , [ 13 , 5, uZraku + 1 + br * visinaNivoa ]  , [ 13 , 5 , uZraku +  1 + br * visinaNivoa  ] , orSm , 9 , 0 ) # water gore lijevo
   time.sleep ( 3 )
   crtaj_kvadar ( orMj , [ 13 , 13, uZraku + 1 + br * visinaNivoa ]  , [ 13 , 13 , uZraku +  1 + br * visinaNivoa  ] , orSm , 9 , 0 ) # water gore desno

   crtaj_kvadar ( orMj , [ 5 , 5, uZraku + 2 + br * visinaNivoa ]  , [ 5 , 5 , uZraku +  4 + br * visinaNivoa  ] , orSm , materijal , dv ) #kamen iznad water dolje lijevo
   crtaj_kvadar ( orMj , [ 5 , 13, uZraku + 2 + br * visinaNivoa ]  , [ 5 , 13 , uZraku + 4 + br * visinaNivoa  ] , orSm ,  materijal , dv ) #kamen iznad  water dolje desno
   time.sleep ( 3 )
   crtaj_kvadar ( orMj , [ 13 , 5, uZraku + 2 + br * visinaNivoa ]  , [ 13 , 5 , uZraku +  4 + br * visinaNivoa  ] , orSm ,  materijal , dv ) #kamen iznad  water gore lijevo
   crtaj_kvadar ( orMj , [ 13 , 13, uZraku + 2 + br * visinaNivoa ]  , [ 13 , 13 , uZraku +  4 + br * visinaNivoa  ] , orSm ,  materijal , dv ) #kamen iznad  water gore desno
   
   time.sleep ( 15 )
   
   #slabstoni   
   for dX in range ( 3 , 16 , 4 ) :
      for dY in range ( 3 , 16 , 4 ) :
         crtaj_kvadar ( orMj , [ dX , dY, uZraku + 2 + br * visinaNivoa ]  , [ dX , dY , uZraku +  2 + br * visinaNivoa  ] , orSm , 44 , 5 ) # stoneslabi protiv pauka
         time.sleep ( 5 )
   
   
# lampe na vrhu
mc.postToChat("Lampe !!"  )
for dX in range ( 1 , 19 , 5 ) :
   for dY in range ( 1 , 19 , 5 ) :
      crtaj_kvadar ( orMj , [ dX , dY , uZraku + nivoa*visinaNivoa + 2 ]  , [ dX , dY , uZraku + nivoa*visinaNivoa + 2   ] , orSm , 89 , 0 ) # on top
      time.sleep ( 3 )

""" duplo ??
# estetika
crtaj_kvadar ( orMj , [ 0 , 0, uZraku - 6 ]  , [ 4 , 4 , uZraku + nivoa*visinaNivoa + 1   ] , orSm , AIR.id , 2 ) # lijeva dolje rupa
crtaj_kvadar ( orMj , [ 0 , 14, uZraku - 6 ]  , [ 4 , 18 , uZraku + nivoa*visinaNivoa + 1   ] , orSm , AIR.id , 2 ) # desna dolje rupa
crtaj_kvadar ( orMj , [ 14 , 0, uZraku - 6 ]  , [ 18 , 4 , uZraku + nivoa*visinaNivoa + 1   ] , orSm , AIR.id , 2 ) # lijeva dolje rupa
crtaj_kvadar ( orMj , [ 14 , 14, uZraku - 6 ]  , [ 18 , 18 , uZraku + nivoa*visinaNivoa + 1   ] , orSm , AIR.id , 2 ) # desna dolje rupa

"""

# razbijalica
mc.postToChat("Razbijalica !!"  )
crtaj_kvadar ( orMj , ( -2  , -2 , -1 )  , (  20 , 20 , 0 ) , orSm ,  materijal , dv ) # sandstone edge platforma
crtaj_kvadar ( orMj , ( -1  , -1 , -1 )  , (  19 , 19 , 0 ) , orSm ,  89 , 0 ) # glowstone platforma

time.sleep ( 15 )
crtaj_kvadar ( orMj , ( 6  , 6 , 1 )  , (  13 , 13 , 1 ) , orSm ,  89 , 0 ) # glowstone okolo
crtaj_kvadar ( orMj , ( 7  , 7 , 1 )  , (  12 , 12 , 1 ) , orSm , slab , dv_slab ) # stonebrick slab kocka

time.sleep ( 15 )
crtaj_kvadar ( orMj , ( 8  , 7 , 0 )  , (  12 , 12 , 0 ) , orSm , 154 , smjer_hoppera ( orSm , "meni" ) ) # hopperi spod stoneslaba
crtaj_kvadar ( orMj , ( 7  , 6 , 0 )  , (  7 , 12 , 0 ) , orSm , 154 , smjer_hoppera ( orSm , "lijevo" ) ) # hopperi ispod stoneslaba za skupljanje
time.sleep ( 3 )
crtaj_kvadar ( orMj , ( 6  , 3 , 0 )  , ( 8 , 5 , 0 ) , orSm ,  materijal , dv )    #frame around chest
crtaj_kutiju ( orMj , ( 7  , 4 , 0 )  , (  7 ,5 , 0 ) , orSm , rel_smjer  = "meni" , blok_id = 54     )  #kutija je malo pomaknuta da stanu glowestoni
time.sleep ( 15 )
#stairways hole
crtaj_kvadar ( orMj , ( 0 , 4 , -1 )  , (  4 , 14 , 0 ) , orSm ,  materijal , dv  )  #edge
crtaj_kvadar ( orMj , ( 1 , 5 , -1 )  , (  2 , 13 , 0 ) , orSm ,  0 , 0 )     #hole

time.sleep ( 15 )
countdown = relativeHigh  #how much down
counter = 0    # down counter
pomak = 0      # from podium
smjer = 1      # where to go on relative Z axis
r_smjer="desno"   # sirection for stairway function
dX = 0         # move on relative X axis

#stairways down
mc.postToChat("Stepenice !!"  )
while - counter <= countdown :
   time.sleep ( 1 )
   crtaj_stepenice ( orMj , ( 1 + dX, 5 + pomak  , counter )  , (  2 + dX, 5 + pomak  , counter ) , orSm , blok_id = stepenice , rel_smjer  = r_smjer  )
   pomak  += smjer   # zig - zag
   counter -= 1
   if pomak == 9 :   # podium
      pomak = 8
      crtaj_kvadar ( orMj , ( 2  , 5 + pomak  , counter )  , ( -2 , 5 + pomak + 3 , counter ) , orSm ,  materijal , dv )
      crtaj_kvadar ( orMj , ( 1  , 5 + pomak + 1 , counter )  , ( -1 , 5 + pomak + 2 , counter ) , orSm ,  89 , 0 )
   if pomak == -1 :   # podium
      pomak = 0
      crtaj_kvadar ( orMj , ( 2  , 5 +pomak  , counter )  , ( -2 , 5 + pomak - 3 , counter ) , orSm ,   materijal , dv  )
      crtaj_kvadar ( orMj , ( 1  , 5 +pomak - 1 , counter )  , ( -1 , 5 + pomak - 2 , counter ) , orSm ,  89 , 0 )
   if ( counter % 9  ) == 0 :
      smjer *= -1
      if smjer == 1 :
         r_smjer="desno"
         dX = 0
      else:
         r_smjer="lijevo"
         dX = -3

# optimal AFK platform

mc.postToChat("Platforma !!"  )
crtaj_kvadar ( orMj , ( -2  , -2 , 10 )  , (  20 , 20 , 10 ) , orSm ,  materijal , dv ) # sandstone edge platforma
crtaj_kvadar ( orMj , ( -1  , -1 , 10 )  , (  19 , 19 , 10 ) , orSm ,  89 , 0 ) # glowstone platforma
time.sleep ( 3 )
crtaj_kvadar ( orMj , ( 6  ,6 , 10 )  , (  13 , 13 , 10 ) , orSm ,  materijal , dv ) # hole frame
crtaj_kvadar ( orMj , ( 7  , 7 , 10 )  , (  12 , 12 , 10 ) , orSm ,  0 , 0 ) # hole

time.sleep ( 15 )
crtaj_kvadar ( orMj , ( 18  , 3 , 10 )  , (  15 , 15 , 10 ) , orSm ,  materijal , dv ) # hole frame
crtaj_kvadar ( orMj , ( 17  , 4 , 10 )  , (  16 , 14 , 10 ) , orSm ,  0 , 0 ) # hole for stairway
time.sleep ( 15 )
for br in range ( 1 , 11 , 1 ):    #stairway to platform
   crtaj_stepenice ( orMj , ( 17 , 4 + br ,  br )  , (  16  , 4 + br , br ) , orSm , blok_id = stepenice , rel_smjer  = "lijevo"  )

time.sleep ( 15 )


mc.postToChat("Finished !!"  )

   




