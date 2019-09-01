# Nekakva kuca - ruzna !!!
#definicija objekta i poziv rutine za crtanje
from crtanje import *		#tu je funkcija koju zovem
from crtanje2 import *		#tu je funkcija koju zovem
from mc import *			

mc = Minecraft() #inicijalizacija sustava za rad sa Minecraftom

# reset

crtaj_kvadar ( gdjeSam () , [ 1 , 1 , -1 ]  , [ 10 , 10 , 0  ] , gdjeGledam () , 53 , 2 )
crtaj_kvadar ( gdjeSam () , [ 1 , 1 , 1 ]  , [ 10 , 10 , 10  ] , gdjeGledam () , 0 , 0 ) #cijeli blok


#temelji 10 x 10 od stone bricksa

crtaj_kvadar ( gdjeSam () , [ 1 , 1 , -1 ]  , [ 10 , 10 , 0  ] , gdjeGledam () , 98 , 0 )

#doljnji blok  
crtaj_kvadar ( gdjeSam () , [ 1 , 1 , 1 ]  , [ 10 , 10 , 5  ] , gdjeGledam () , 5 , 0 ) #cijeli blok
crtaj_kvadar ( gdjeSam () , [ 1 , 1 , 1 ]  , [ 4 , 4 , 5  ] , gdjeGledam () , 0 , 0 ) #izrezi terasu

for br in range (2,5) :
   crtaj_stepenice ( gdjeSam () , [ 0 , br  , 0 ]  , [ 0 , br  , 0  ] , gdjeGledam () , 109 , "meni" ) # ulazne stepenice , stone brick east 0

#crtaj_kvadar ( gdjeSam () , [ 5 , 3 , 1 ]  , [ 5 , 3 , 2  ] , gdjeGledam () , 0 , 0 ) #rupa za vrata
crtaj_vrata ( gdjeSam () , [ 5 , 3 , 1 ]  ,  gdjeGledam ()  , "meni" , 64  ) #doljnja vrata doljnji dio



crtaj_kvadar ( gdjeSam () , [ 6 , 2 , 1 ]  , [ 9 , 9 , 4  ] , gdjeGledam () , 0 , 0 ) #rupa za dnevni boravak
crtaj_kvadar ( gdjeSam () , [ 2 , 6 , 1 ]  , [ 5 , 9 , 4  ] , gdjeGledam () , 0 , 0 ) #rupa za sobicu

crtaj_kvadar ( gdjeSam () , [ 1 , 7 , 2 ]  , [ 1 , 8 ,2  ] , gdjeGledam () , 0 , 0 ) #rupa za prozor prednji
crtaj_kvadar ( gdjeSam () , [ 1 , 7 , 2 ]  , [ 1 , 8 ,2  ] , gdjeGledam () , 102 , 0 ) #staklo za prozor prednji



crtaj_kvadar ( gdjeSam () , [ 3 , 10 , 2 ]  , [ 5 , 10 ,2  ] , gdjeGledam () , 0 , 0 ) #rupa za prozor desno
crtaj_kvadar ( gdjeSam () , [ 7 , 10 , 2 ]  , [ 8 , 10 ,2  ] , gdjeGledam () , 0 , 0 ) #rupa za prozor desno
crtaj_kvadar ( gdjeSam () , [ 3 , 10 , 2 ]  , [ 5 , 10 ,2  ] , gdjeGledam () , 102 , 0 ) #staklo za prozor desno
crtaj_kvadar ( gdjeSam () , [ 7 , 10 , 2 ]  , [ 8 , 10 ,2  ] , gdjeGledam () , 102 , 0 ) #staklo za prozor desno

crtaj_kvadar ( gdjeSam () , [ 7 , 1 , 2 ]  , [ 8 , 1 ,2  ] , gdjeGledam () , 0 , 0 ) #rupa za prozor lijevo
crtaj_kvadar ( gdjeSam () , [ 7 , 1 , 2 ]  , [ 8 , 1 ,2  ] , gdjeGledam () , 102 , 0 ) #rupa za prozor lijevo





#gornji blok

crtaj_kvadar ( gdjeSam () , [ 6 , 1 , 6 ]  , [ 10 , 10 , 10  ] , gdjeGledam () , 5 , 0 ) #cijeli blok
crtaj_kvadar ( gdjeSam () , [ 7 , 2 , 6 ]  , [ 9 , 9 , 9  ] , gdjeGledam () , 0 , 0 ) #izrezi sobicu

#crtaj_kvadar ( gdjeSam () , [ 6 , 6 , 6 ]  , [ 6 , 6 , 7  ] , gdjeGledam () , 0 , 0 ) #rupa za vrata
crtaj_vrata ( gdjeSam () , [ 6 , 6 , 6 ]  , gdjeGledam () , "meni" , 64  ) #gornja vrata doljnji dio
#crtaj_kvadar ( gdjeSam () , [ 6 , 6 , 7 ]  , [ 6 , 6 ,7  ] , gdjeGledam () , 64 , 2 + 8 ) #gornja vrata gornji dio

crtaj_kvadar ( gdjeSam () , [ 6 , 8 , 7 ]  , [ 6 , 9 , 7  ] , gdjeGledam () , 0 , 0 ) #rupa za prozor prednji dupli
crtaj_kvadar ( gdjeSam () , [ 6 , 8 , 7 ]  , [ 6 , 9 , 7  ] , gdjeGledam () , 102 , 0 ) #staklo za prozor prednji dupli


crtaj_kvadar ( gdjeSam () , [ 6 , 2 , 7 ]  , [ 6 , 3 , 7  ] , gdjeGledam () , 0 , 0 ) #rupa za prozor mali prednji
crtaj_kvadar ( gdjeSam () , [ 6 , 2 , 7 ]  , [ 6 , 3 , 7  ] , gdjeGledam () , 102 , 0 ) #staklo za prozor mali prednji

# stepenice na kat
crtaj_kvadar ( gdjeSam () , [ 9 , 2 , 5 ]  , [ 9 , 9 , 5  ] , gdjeGledam () , 0 , 0 ) #izrezi prolaz

for br in range ( 1 , 6 ) :
   crtaj_stepenice ( gdjeSam () , [ 9 , br + 3 , br ]  , [ 9 , br + 3 , br  ] , gdjeGledam () , 53 , "lijevo" )  # drvene stepenice gledaju na jug 2

crtaj_kvadar ( gdjeSam () , [ 9 , 9 , 5 ]  , [ 9 , 9 , 5  ] , gdjeGledam () , 5 , 0 ) # podest iza stepenica

# terasa

crtaj_kvadar ( gdjeSam () , [ 1 , 1 , 5 ]  , [ 4 , 4 , 5  ] , gdjeGledam () , 126 , 0 ) #tenda iznad terase
crtaj_kvadar ( gdjeSam () , [ 1 , 1 , 1 ]  , [ 1 , 1 , 4  ] , gdjeGledam () , 85 , 0 ) #stup

# gornja terasa
crtaj_kvadar ( gdjeSam () , [ 1 , 5 , 6 ]  , [ 5 , 10 , 6  ] , gdjeGledam () , 85 , 0 ) #prednja ograda
crtaj_kvadar ( gdjeSam () , [ 2 , 6 , 6 ]  , [ 5 , 9 , 6  ] , gdjeGledam () , 0 , 0 ) #prednja ograda










