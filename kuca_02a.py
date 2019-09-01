# surival house 7 x 7 from http://www.minecraftforum.net/forums/minecraft-discussion/survival-mode/290440-minecraft-survival-starter-houses
#definicija objekta i poziv rutine za crtanje
from crtanje import *		#tu je funkcija koju zovem
from crtanje2 import *		#tu je funkcija koju zovem
from mc import *			
mc = Minecraft() #inicijalizacija sustava za rad sa Minecraftom

# origin ispred na sredini 
orMj = gdjeSam ()
orSm = gdjeGledam ()

# reset
crtaj_kvadar ( orMj , [  1 , -5 , -2 ]  , [ 12 , 5 , 0  ] , orSm , 2 , 0 ) # zemlja
crtaj_kvadar ( orMj , [ 1 , -5 , 0 ]  , [ 12 , 5 , 5  ] , orSm , 0 , 0 ) #zrak

# bazni oak-wood volumen
crtaj_kvadar ( orMj , [ 3 , -4 , -1 ]  , [ 11 , 4 , 1  ] , orSm , 5 , 0 ) # blok oak wood
crtaj_kvadar ( orMj , [ 4 , -3 , 0 ]  , [ 10 , 3 , 1  ] , orSm , 0 , 0 ) # praznina

# ukrasne crte
crtaj_kvadar ( orMj , [ 3 , -4 , 0 ]  , [ 11 , 4 , 0  ] , orSm , 4 , 0 ) # blok coblestonea
crtaj_kvadar ( orMj , [ 4 , -3 , 0 ]  , [ 10 , 3 , 0  ] , orSm , 0 , 0 ) # praznina

#uglovi coblestone
crtaj_kvadar ( orMj , [ 3 , -4 , 1 ]  , [ 3 , -4 , 1  ] , orSm , 4 , 0 ) # blok coblestonea
crtaj_kvadar ( orMj , [ 3 , 4 , 1 ]  , [ 3 , 4 , 1  ] , orSm , 4 , 0 ) # blok coblestonea
crtaj_kvadar ( orMj , [ 11 , 4 , 1 ]  , [ 11 , 4 , 1  ] , orSm , 4 , 0 ) # blok coblestonea
crtaj_kvadar ( orMj , [ 11 , -4 , 1 ]  , [ 11 , -4 , 1  ] , orSm , 4 , 0 ) # blok coblestonea

# vrata
crtaj_vrata ( orMj , [ 3 , 0 , 0 ] , orSm , "meni"  , blok_id = 64     ) 

#prozori
crtaj_kvadar ( orMj , [ 3 , -2 , 1 ]  , [ 3 , -2 , 1  ] , orSm , 102 , 0 ) #staklo za prozor prednji lijevi
crtaj_kvadar ( orMj , [ 3 , 2 , 1 ]  , [ 3 , 2 , 1  ] , orSm , 102 , 0 ) #staklo za prozor prednji desni
crtaj_kvadar ( orMj , [ 6 , -4 , 1 ]  , [ 8 , -4 , 1  ] , orSm , 102 , 0 ) #staklo za prozor lijevi veliki
crtaj_kvadar ( orMj , [ 8 , 4 , 1 ]  , [ 8 , 4 , 1  ] , orSm , 102 , 0 ) #staklo za prozor desni mali
crtaj_kvadar ( orMj , [ 11 , -2 , 1 ]  , [ 11 , -1 , 1  ] , orSm , 102 , 0 ) #staklo za prozor zadnji lijevi veliki
crtaj_kvadar ( orMj , [ 11 , 2 , 1 ]  , [ 11 , 1 , 1  ] , orSm , 102 , 0 ) #staklo za prozor zadnji desni veliki

# oprema iznutra - baklje
crtaj_baklju ( orMj , ( 2 , -1 , 1 ) ,  orSm ,  "meni"   ) # torch na ulazu izvana lijeva
crtaj_baklju ( orMj , ( 2 , 1 , 1 ) ,  orSm ,  "meni"   ) # torch na ulazu izvana desna
crtaj_baklju ( orMj , ( 4 , -1 , 1 ) ,  orSm ,  "odmene"   ) # torch na ulazu iznutra lijeva
crtaj_baklju ( orMj , ( 4 , 1 , 1 ) ,  orSm ,  "odmene"   ) # torch na ulazu iznutra desna
crtaj_baklju ( orMj , ( 9 , -3 , 1 ) ,  orSm ,  "desno"   ) # torch  iznutra lijeva
crtaj_baklju ( orMj , ( 7 , 3 , 1 ) ,  orSm ,  "lijevo"   ) # torch na ulazu iznutra desna

# oprema iznutra - banak
crtaj_banak ( orMj , ( 7 , -3 , 0 ) , ( 7 , -3 , 0 ) , orSm ) 

# oprema iznutra - kutije
crtaj_kutiju ( orMj  , ( 5 , -3 , 0 ) , ( 6 , -3 , 0 ) , orSm , "desno")  #bliza kutija 
crtaj_kutiju ( orMj  , ( 8 , -3 , 0 ) , ( 9 , -3 , 0 ) , orSm , "desno")  #dalja kutija 

# oprema iznutra - peci
crtaj_pec ( orMj  , ( 4 , -3 , 0 ) , ( 4 , -3 , 0 ) , orSm , "desno")  #bliza pec 
crtaj_pec ( orMj  , ( 10 , -3 , 0 ) , ( 10 , -3 , 0 ) , orSm , "desno")  #dalja pec

# oprema iznutra - krevet
crtaj_krevet  ( orMj  , ( 9 , 3 , 0 ) , ( 10 , 3 , 0 ) , orSm , "odmene") #krevet odmene

#krov

for br in range ( 0 , 3 ) :
   crtaj_stepenice ( orMj , ( 2 + br , - 4 + br , 2 + br) , ( 2 + br , 4 - br , 2 + br ) , orSm , blok_id = 53 , rel_smjer  = "meni" ) # prednja kosina
   crtaj_stepenice ( orMj , ( 12 - br , - 4 + br , 2 + br) , ( 12 - br , 4 - br , 2 + br ) , orSm , blok_id = 53 , rel_smjer  = "odmene" ) # zadnja kosina
   crtaj_stepenice ( orMj , ( 2 + br , - 5 + br , 2 + br) , ( 12 - br , - 5 + br , 2 + br ) , orSm , blok_id = 53 , rel_smjer  = "lijevo" ) # lijeva kosina
   crtaj_stepenice ( orMj , ( 2 + br ,  5 - br , 2 + br) , ( 12 - br ,  5 - br , 2 + br ) , orSm , blok_id = 53 , rel_smjer  = "desno" ) # lijeva kosina

crtaj_kvadar ( orMj , [ 5 , -2 , 4 ]  , [ 9 , 2 , 4  ] , orSm , 126 , 8 ) # slabovi za zatvoriti rupu u sredini krova   wooden Upper Oak Wood Slab




