# mob spawner - simple
#definicija objekta i poziv rutine za crtanje

from crtanje import *		#tu je funkcija koju zovem
from mc import *			
mc = Minecraft() #inicijalizacija sustava za rad sa Minecraftom

# origin ispred na sredini 
orMj = gdjeSam ()
orSm = gdjeGledam ()

#sandstone glatki
materijal = 1
dv = 1
uZraku = 40
nivoa=5
visinaNivoa = 5


crtaj_kvadar ( orMj , [ 8 , 8, uZraku -6 ]  , [ 11 , 11 , uZraku - 1   ] , orSm , STONE.id , 2 ) # lijevak ispod
crtaj_kvadar ( orMj , [ 0 , 0, uZraku ]  , [ 19 , 19 , uZraku + nivoa*visinaNivoa + 1   ] , orSm , STONE.id , 2 ) # main body
crtaj_kvadar ( orMj , [ 9 , 9, uZraku - 6 ]  , [ 10 , 10 , uZraku + nivoa*visinaNivoa    ] , orSm , AIR.id , 2 ) # sredisnja rupa
for br in range ( nivoa ) :
   crtaj_kvadar ( orMj , [ 1 , 1, uZraku + 3 + br * visinaNivoa ]  , [ 18 , 18 , uZraku +  4 + br * visinaNivoa  ] , orSm , AIR.id , 0 ) # main hole
   crtaj_kvadar ( orMj , [ 1 , 9, uZraku + 1 + br * visinaNivoa ]  , [ 18 , 10 , uZraku +  4 + br * visinaNivoa  ] , orSm , AIR.id , 0 ) # uzduzna
   crtaj_kvadar ( orMj , [ 9 , 1, uZraku + 1 + br * visinaNivoa ]  , [ 10 , 18 , uZraku +  4 + br * visinaNivoa  ] , orSm , AIR.id , 0 ) # poprecna
   
   crtaj_kvadar ( orMj , [ 9 , 1, uZraku + 1 + br * visinaNivoa ]  , [ 10 , 1 , uZraku +  1 + br * visinaNivoa  ] , orSm , 9 , 0 ) # water uzduzno blizi
   crtaj_kvadar ( orMj , [ 9 , 18, uZraku + 1 + br * visinaNivoa ]  , [ 10 , 18 , uZraku +  1 + br * visinaNivoa  ] , orSm , 9 , 0 ) # water uzduzno dalji
   
   crtaj_kvadar ( orMj , [ 1 , 9, uZraku + 1 + br * visinaNivoa ]  , [ 1 , 10 , uZraku +  1 + br * visinaNivoa  ] , orSm , 9 , 0 ) # water poprecno blizi
   crtaj_kvadar ( orMj , [ 18 , 9, uZraku + 1 + br * visinaNivoa ]  , [ 18 , 10 , uZraku +  1 + br * visinaNivoa  ] , orSm , 9 , 0 ) # water poprecno dalji
   
# lampe na vrhu

for dX in range ( 0 , 21 , 5 ) :
   for dY in range ( 0 , 21 , 5 ) :
      crtaj_kvadar ( orMj , [ dX , dY , uZraku + nivoa*visinaNivoa + 2 ]  , [ dX , dY , uZraku + nivoa*visinaNivoa + 2   ] , orSm , 89 , 0 ) # on top


# razbijalica
crtaj_kvadar ( orMj , ( 7  , 7 , 1 )  , (  12 , 12 , 1 ) , orSm , 44 , 5 ) # stonebrick slab kocka


crtaj_kvadar ( orMj , ( 8  , 7 , 0 )  , (  12 , 12 , 0 ) , orSm , 154 , smjer_hoppera ( orSm , "meni" ) ) # hopperi spod stoneslaba
crtaj_kvadar ( orMj , ( 7  , 7 , 0 )  , (  7 , 12 , 0 ) , orSm , 154 , smjer_hoppera ( orSm , "lijevo" ) ) # hopperi spod stoneslaba za skupljanje
crtaj_kutiju ( orMj , ( 7  , 5 , 0 )  , (  7 ,6 , 0 ) , orSm , rel_smjer  = "meni" , blok_id = 54     )
   




