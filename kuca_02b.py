# surival house 7 x 5 from https://www.youtube.com/watch?v=Gxw3zMfMYTs
#definicija objekta i poziv rutine za crtanje
from crtanje import *		#tu je funkcija koju zovem
from crtanje2 import *		#tu je funkcija koju zovem
from mc import *			
mc = Minecraft() #inicijalizacija sustava za rad sa Minecraftom

# origin ispred na sredini 
orMj = gdjeSam ()
orSm = gdjeGledam ()

# reset
crtaj_kvadar ( orMj , [  1 , -5 , -2 ]  , [ 11 , 6 , 0  ] , orSm , 2 , 0 ) # zemlja
crtaj_kvadar ( orMj , [ 1 , -5 , 0 ]  , [ 11 , 6 , 8  ] , orSm , 0 , 0 ) #zrak

# bazni oak-wood volumen
crtaj_kvadar ( orMj , [ 5 , -3 , -1 ]  , [ 9 , 3 , 3  ] , orSm , 5 , 0 ) # blok oak wood
crtaj_kvadar ( orMj , [ 6 , -2 , 0 ]  , [ 8 , 2 , 4  ] , orSm , 0 , 0 ) # praznina

# vrata
crtaj_vrata ( orMj , [ 5 , -1 , 0 ] , orSm , "meni"  , blok_id = 64     ) 

#prozori
crtaj_kvadar ( orMj , [ 5 , 1 , 1 ]  , [ 5 , 1 , 1  ] , orSm , 102 , 0 ) #staklo za prozor prednji desni
crtaj_kvadar ( orMj , [ 6 , -3 , 1 ]  , [ 8 , -3 , 1  ] , orSm , 102 , 0 ) #staklo za prozor lijevi veliki
crtaj_kvadar ( orMj , [ 6 , 3 , 1 ]  , [ 8 , 3 , 1  ] , orSm , 102 , 0 ) #staklo za prozor desni veliki
crtaj_kvadar ( orMj , [ 9 , -2 , 1 ]  , [ 9 , -1 , 1  ] , orSm , 102 , 0 ) #staklo za prozor zadnji lijevi veliki
crtaj_kvadar ( orMj , [ 9 , 2 , 1 ]  , [ 9 , 1 , 1  ] , orSm , 102 , 0 ) #staklo za prozor zadnji desni veliki

# oprema iznutra - baklje
crtaj_baklju ( orMj , ( 4 , -2 , 1 ) ,  orSm ,  "meni"   ) # torch na ulazu izvana lijeva
crtaj_baklju ( orMj , ( 4 , 0 , 1 ) ,  orSm ,  "meni"   ) # torch na ulazu izvana desna
crtaj_baklju ( orMj , ( 6 , -2 , 2 ) ,  orSm ,  "desno"   ) # torch  iznutra lijeva
crtaj_baklju ( orMj , ( 8 , -2 , 2 ) ,  orSm ,  "desno"   ) # torch  iznutra lijeva
crtaj_baklju ( orMj , ( 6 , 2 , 2 ) ,  orSm ,  "lijevo"   ) # torch  iznutra desna
crtaj_baklju ( orMj , ( 8 , 2 , 2 ) ,  orSm ,  "lijevo"   ) # torch  iznutra desna

# oprema iznutra - banak
crtaj_banak ( orMj , ( 8 , -2 , 0 ) , ( 8 , -2 , 0 ) , orSm ) 

# oprema iznutra - kutije
crtaj_kutiju ( orMj  , ( 6 , -2 , 0 ) , ( 7 , -2 , 0 ) , orSm , "desno")  #lijeva kutija 
crtaj_kutiju ( orMj  , ( 6 , 1 , 0 ) , ( 6 , 1 , 0 ) , orSm , "odmene")  #desna kutija

# oprema iznutra - peci
crtaj_pec ( orMj  , ( 6 , 2 , 0 ) , ( 6 , 2 , 0 ) , orSm , "odmene")  #pec 
 
# oprema iznutra - krevet
crtaj_krevet  ( orMj  , ( 8 , 1 , 0 ) , ( 8 , 2 , 0 ) , orSm , "desno") #krevet udesno

#krov na dvije vode od red_sandstone_stairs
for br in range ( 0 , 3 ) :
   crtaj_stepenice ( orMj , ( 4 + br , - 4  , 2 + br) , ( 4   + br , 4  , 2 + br ) , orSm , blok_id = 180 , rel_smjer  = "meni" ) # prednja kosina
   crtaj_stepenice ( orMj , ( 10 - br , - 4  , 2 + br) , ( 10 - br , 4 , 2 + br ) , orSm , blok_id = 180 , rel_smjer  = "odmene" ) # zadnja kosina

crtaj_kvadar ( orMj , [ 7 , -4 , 4 ]  , [ 7 , 4 , 4  ] , orSm , 182 , 8 ) # slabovi za zatvoriti rupu u sredini krova   Red Sandstone Slab

#Dimnjak 
crtaj_kvadar ( orMj , ( 5 , 2 , 0 ) , ( 5 , 2 , 5 ) , orSm , 4 , 0 ) # blok coblestonea
crtaj_kvadar ( orMj , ( 5 , 2 , 6 ) , ( 5 , 2 , 6 ) , orSm , 139 , 0 ) # blok coblestonea wall

#Ograde
crtaj_kvadar ( orMj , ( 1 , -4  , 0 ) , ( 4 , 5 , 0 ) , orSm , 188 , 0 ) # spruce_fence ograda
crtaj_kvadar ( orMj , ( 5 , -4  , 0 ) , ( 5 , -4 , 0 ) , orSm , 188 , 0 ) # spruce_fence ograda
crtaj_kvadar ( orMj , ( 5 , 4  , 0 ) , ( 5 , 5 , 0 ) , orSm , 188 , 0 ) # spruce_fence ograda
crtaj_kvadar ( orMj , ( 2 , -3  , 0 ) , ( 4 , -1 , 0 ) , orSm , 0 , 0 ) # lijevo dvoriste
crtaj_kvadar ( orMj , ( 2 , 1  , 0 ) , ( 4 , 4 , 0 ) , orSm ,  0 , 0 ) # desno dvoriste

# vrata na ogradi
crtaj_vrataograde ( orMj , ( 1 , -1  , 0 ),  orSm ,  "lijevo_desno"    , blok_id = 183    ) # prednja vrata spruce_fence_gate
crtaj_vrataograde ( orMj , ( 2 , 0  , 0 ) ,  orSm ,  "naprijed_nazad"  , blok_id = 183     ) # poprecna vrata spruce_fence_gate

# nadstresnica
crtaj_kvadar ( orMj , ( 3 , -4   , 2 ) , ( 3 , 0 , 2 ) , orSm ,  182 , 0 ) #  Red Sandstone Slab
crtaj_kvadar ( orMj , ( 3 , -4  , 1 ) , ( 3 , -4 , 1 ) , orSm , 188 , 0 ) # spruce_fence ograda
crtaj_kvadar ( orMj , ( 3 , 0  , 1 ) , ( 3 , 0 , 1 ) , orSm , 188 , 0 ) # spruce_fence ograda


#vrt
crtaj_kvadar ( orMj , ( 2 , 1  , -1 ) , ( 4 , 4 , -1 ) , orSm ,  60 , 0 ) # desno dvoriste farmland
crtaj_kvadar ( orMj , ( 3 , 4  , -1 ) , ( 3 , 4 , -1 ) , orSm ,  9 , 0 ) # desno dvoriste voda
crtaj_kvadar ( orMj , ( 4 , 1  , 0 ) , ( 4 , 4 , 0 ) , orSm ,  59 , 2 ) # desno dvoriste corp
crtaj_kvadar ( orMj , ( 3 , 1  , 0 ) , ( 3 , 3 , 0 ) , orSm ,  141 , 2 ) # desno dvoriste mrkva
crtaj_kvadar ( orMj , ( 2 , 1  , 0 ) , ( 2 , 4 , 0 ) , orSm ,  142 , 2 ) # desno dvoriste krumpir






"""
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

"""


