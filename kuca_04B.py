# surival house 7 x 7 from http://www.minecraftforum.net/forums/minecraft-discussion/survival-mode/290440-minecraft-survival-starter-houses
#definicija objekta i poziv rutine za crtanje
from crtanje import *		#tu je funkcija koju zovem
from crtanje2 import *		#tu je funkcija koju zovem
from mc import *			
mc = Minecraft() #inicijalizacija sustava za rad sa Minecraftom

# origin ispred na sredini 
orMj = gdjeSam ()
orSm = gdjeGledam ()

#funkcije

def crtaj_blok ( dorigin  ) :

   dX = dorigin [ 0 ]
   dZ = dorigin [ 1 ]
   dY = dorigin [ 2 ]
   
   if dY < 2 :
      materijal_zidovi = 98 # nizi katovi od stonebricksa
   else :
      materijal_zidovi = 5 # visi katovi od oak wood dasaka
   
   # sobe podovi i zidovi
   crtaj_kvadar ( orMj , [ 0 + dX, 0 + dZ , 0 + dY ]  , [ 6 + dX, 6 + dZ , 3 + dY  ] , orSm , 0 , 0 ) # blok zrak sobe
   crtaj_kvadar ( orMj , [ 0 + dX, 0 + dZ , 0 + dY ]  , [ 6 + dX, 6 + dZ , 2 + dY  ] , orSm , materijal_zidovi , 0 ) # zidovi
   crtaj_kvadar ( orMj , [ 1 + dX, 1 + dZ , 0 + dY ]  , [ 5 + dX, 5 + dZ , 2 + dY  ] , orSm , 0 , 0 ) # rupa u sobi
   crtaj_kvadar ( orMj , [ 0 + dX, 0 + dZ , 3 + dY ]  , [ 6 + dX, 6 + dZ , 3 + dY  ] , orSm , 5 , 0 ) # blok oak wood strop i eventualno podd ssobe iznad pod
   
   # sobe grede
   #  uzduzne grede
   crtaj_deblo ( orMj , [ 0 + dX, 0 + dZ , 3 + dY ]  , [ 0 + dX, 6 + dZ , 3 + dY  ] , orSm , "lijevo_desno" , blok_id = 17 , podtip = 1   )  #prednja
   crtaj_deblo ( orMj , [ 6 + dX, 0 + dZ , 3 + dY ]  , [ 6 + dX, 6 + dZ , 3 + dY  ] , orSm , "lijevo_desno" , blok_id = 17 , podtip = 1   )  #zadnja
   #  poprecne grede
   crtaj_deblo ( orMj , [ 0 + dX, 0 + dZ , 3 + dY ]  , [ 6 + dX, 0 + dZ , 3 + dY  ] , orSm , "naprijed_nazad" , blok_id = 17 , podtip = 1   )   #lijeva
   crtaj_deblo ( orMj , [ 0 + dX, 6 + dZ , 3 + dY ]  , [ 6 + dX, 6 + dZ , 3 + dY  ] , orSm , "naprijed_nazad" , blok_id = 17 , podtip = 1   )   # desna
   #  uspravne grede
   crtaj_deblo ( orMj , [ 0 + dX, 0 + dZ , 0 + dY ]  , [ 0 + dX, 0 + dZ , 3 + dY  ] , orSm , "gore" , blok_id = 17 , podtip = 1   )   # prednja lijeva
   crtaj_deblo ( orMj , [ 6 + dX, 0 + dZ , 0 + dY ]  , [ 6 + dX, 0 + dZ , 3 + dY  ] , orSm , "gore" , blok_id = 17 , podtip = 1   )   # zadnja lijeva
   crtaj_deblo ( orMj , [ 0 + dX, 6 + dZ , 0 + dY ]  , [ 0 + dX, 6 + dZ , 3 + dY  ] , orSm , "gore" , blok_id = 17 , podtip = 1   )   # prednja desna
   crtaj_deblo ( orMj , [ 6 + dX, 6 + dZ , 0 + dY ]  , [ 6 + dX, 6 + dZ , 3 + dY  ] , orSm , "gore" , blok_id = 17 , podtip = 1   )   # zadnja desna
   
   # pomoc pri izradi OBRISI !!!!!!!!!!!!!!!!!!
   crtaj_baklju ( orMj , (1 + dX, 1 + dZ , 0 + dY) ,  orSm ,  "gore"   )
   
   # crtaj prozore
   if dY > -1 :
      crtaj_kvadar ( orMj , [ 0 + dX , 2 + dZ , 1 + dY ]  , [ 0 + dX , 4 + dZ , 1 + dY  ] , orSm , 102 , 0 ) #staklo za prozor prednji 
      crtaj_kvadar ( orMj , [ 6 + dX , 2 + dZ , 1 + dY ]  , [ 6 + dX , 4 + dZ , 1 + dY  ] , orSm , 102 , 0 ) #staklo za prozor zadnji
      crtaj_kvadar ( orMj , [ 2 + dX , 0 + dZ , 1 + dY ]  , [ 4 + dX , 0 + dZ , 1 + dY  ] , orSm , 102 , 0 ) #staklo za prozor lijevi
      crtaj_kvadar ( orMj , [ 2 + dX , 6 + dZ , 1 + dY ]  , [ 4 + dX , 6 + dZ , 1 + dY  ] , orSm , 102 , 0 ) #staklo za prozor desni
    
   
   
   
   


# reset
crtaj_kvadar ( orMj , [  1 , -10 , -6 ]  , [ 15 , 10 , 0  ] , orSm , 2 , 0 ) # zemlja
crtaj_kvadar ( orMj , [ 1 , -10 , 0 ]  , [ 15 , 10 , 22  ] , orSm , 0 , 0 ) # zrak
crtaj_kvadar ( orMj , [ 1 , -9 , -5 ]  , [ 14 , 9 , -5  ] , orSm , 98 , 0 ) # temelj


# sobe pozadi lijevo
crtaj_blok ( ( 8 , -9 , -4 )  )
crtaj_blok ( ( 8 , -9 , 0 )  )
crtaj_blok ( ( 8 , -9 , 4 )  )
crtaj_blok ( ( 8 , -9 , 8 )  )
crtaj_blok ( ( 8 , -9 , 12 )  )
# sobe naprijed lijevo
crtaj_blok ( ( 2 , -9 , -4 )  )
crtaj_blok ( ( 2 , -9 , 0 )  )
crtaj_blok ( ( 2 , -9 , 4 )  )
# sobe pozadi sredina
crtaj_blok ( ( 8 , -3 , -4 )  )
crtaj_blok ( ( 8 , -3 , 0 )  )
crtaj_blok ( ( 8 , -3 , 4 )  )
# sobe naprijed sredina
crtaj_blok ( ( 2 , -3 , -4 )  )
# sobe pozadi desno
crtaj_blok ( ( 8 , 3 , -4 )  )
crtaj_blok ( ( 8 , 3 , 0 )  )
crtaj_blok ( ( 8 , 3 , 4 )  )
# sobe naprijed desno
crtaj_blok ( ( 2 , 3 , -4 )  )
crtaj_blok ( ( 2 , 3 , 0 )  )

# makni poprecne zidove 
crtaj_kvadar ( orMj , [ 9 , -3 , -4 ]  , [ 13 , 3 , -2  ] , orSm , 0 , 0 ) # u podrumu
crtaj_kvadar ( orMj , [ 9 , -3 , 0 ]  , [ 13 , 3 , 2  ] , orSm , 0 , 0 ) # u prizemlju
crtaj_kvadar ( orMj , [ 9 , -3 , -1 ]  , [ 13 , 3 , -1  ] , orSm , 5 , 0 ) # korekcija poda
crtaj_kvadar ( orMj , [ 9 , -3 , 4 ]  , [ 13 , 3 , 6  ] , orSm , 0 , 0 ) # na katu
crtaj_kvadar ( orMj , [ 9 , -3 , 3 ]  , [ 13 , 3 , 3  ] , orSm , 5 , 0 ) # korekcija poda

# vrata
#  Vanjska vrata
crtaj_vrata ( orMj , [ 8 , -1 , 0 ] , orSm , "meni"  , blok_id = 64     )  # ulazna vrata
crtaj_kvadar ( orMj , [ 8 , 0 , 1 ]  , [ 8 , 0 , 1 ] , orSm , 98 , 0 ) #korekcija prozora
crtaj_vrata ( orMj , [ 8 , 5 , 4 ] , orSm , "meni"  , blok_id = 64     )  # balkonska vrata
crtaj_kvadar ( orMj , [ 8 , 6 , 5 ]  , [ 8 , 6 , 5  ] , orSm , 5 , 0 ) #korekcija prozora
#  podrumska vrata
crtaj_vrata ( orMj , [ 8 , -6 , -4 ] , orSm , "odmene"  , blok_id = 64     )  # lijeva soba
crtaj_vrata ( orMj , [ 8 , 0 , -4 ] , orSm , "odmene"  , blok_id = 64     )  # srednja soba
crtaj_vrata ( orMj , [ 8 , 6 , -4 ] , orSm , "odmene"  , blok_id = 64     )  # desna soba
#  prizemlje vrata
crtaj_kvadar ( orMj , [ 8 , -5 , 1 ]  , [ 8 , -7 , 1 ] , orSm , 98 , 0 ) #korekcija prozora
crtaj_vrata ( orMj , [ 8 , -6 , 0 ] , orSm , "odmene"  , blok_id = 64     )  # lijeva soba
crtaj_kvadar ( orMj , [ 8 , 5 , 1 ]  , [ 8 , 7 , 1 ] , orSm , 98 , 0 ) #korekcija prozora
crtaj_vrata ( orMj , [ 8 , 6 , 0 ] , orSm , "odmene"  , blok_id = 64     )  # desna soba
#  kat vrata
crtaj_kvadar ( orMj , [ 8 , -5 , 5 ]  , [ 8 , -7 , 5 ] , orSm , 5 , 0 ) #korekcija prozora
crtaj_vrata ( orMj , [ 8 , -6 , 4 ] , orSm , "odmene"  , blok_id = 64     )  # lijeva soba
# attic vrata
#  kat vrata
crtaj_kvadar ( orMj , [ 8 , -5 , 9 ]  , [ 8 , -7 , 9 ] , orSm , 5 , 0 ) #korekcija prozora
crtaj_vrata ( orMj , [ 8 , -6 , 8 ] , orSm , "odmene"  , blok_id = 64     )  # lijeva soba
crtaj_kvadar ( orMj , [ 10 , -3 , 9 ]  , [ 12 , -3 , 9 ] , orSm , 5 , 0 ) #korekcija prozora
crtaj_vrata ( orMj , [ 11 , -3 , 8 ] , orSm , "lijevo"  , blok_id = 64     )  # lijeva soba



# stepenice

crtaj_kvadar ( orMj , [ 10 , -7 , -4 ]  , [ 13 , -8 , 15  ] , orSm , 0 , 0 ) # zrak
crtaj_kvadar ( orMj , [ 12 , -8 , -4 ]  , [ 13 , -5 , 15  ] , orSm , 0 , 0 ) # zrak
for ha in ( -3 , 1 , 5 , 9 , 13 ):
   crtaj_kvadar ( orMj , [ 12 , -7 , ha ]  , [ 13 , -8 , ha ] , orSm , 5 , 0 )#prvo podest
   crtaj_stepenice ( orMj , ( 12 , - 5 , ha - 1 ) , ( 13 , -5 , ha - 1 ) , orSm , blok_id = 53 , rel_smjer  = "desno" ) # prva stepenica
   crtaj_stepenice ( orMj , ( 12 , - 6 , ha  ) , ( 13 , -6 , ha  ) , orSm , blok_id = 53 , rel_smjer  = "desno" ) # druga stepenica
   crtaj_stepenice ( orMj , ( 11 , - 7 , ha + 1 ) , ( 11 , -8 , ha + 1 ) , orSm , blok_id = 53 , rel_smjer  = "odmene" ) # treca stepenica
   crtaj_stepenice ( orMj , ( 10 , - 7 , ha + 2 ) , ( 10 , -8 , ha + 2 ) , orSm , blok_id = 53 , rel_smjer  = "odmene" ) # cetvrta stepenica
   crtaj_kvadar ( orMj , [ 11 , -5 , ha - 1 ]  , [ 11 , -6 , ha + 1 ] , orSm , 85 , 0 ) # ograda oko stepenica
   crtaj_kvadar ( orMj , [ 11 , -6 , ha - 1 ]  , [ 10 , -6 , ha + 1 ] , orSm , 85 , 0 ) # ograda oko stepenica
   
# ulaz

crtaj_kvadar ( orMj , [ 2 , -2 , 0 ]  , [ 2 , 2 , 0 ] , orSm , 85 , 0 ) # ulazna ograda
crtaj_vrataograde ( orMj , [ 2 , 0 , 0 ] ,  orSm ,  "lijevo_desno" )  

#terasa
crtaj_kvadar ( orMj , [ 2 , 3 , 4 ]  , [ 7 , 9 , 4 ] , orSm , 85 , 0 ) # brze je napuni se terasa ogradom
crtaj_kvadar ( orMj , [ 3 , 4 , 4 ]  , [ 7 , 8 , 4 ] , orSm , 0 , 0 ) # pa se izbusi rupa

#gornja terasa

crtaj_kvadar  ( orMj , ( 7  , - 10  , 15 ) , ( 7  , - 2  ,  15  ) , orSm , 126 , 9 ) # slabs prednja kosina 
crtaj_kvadar  ( orMj , ( 15  , - 10  ,  15 ) , ( 15  , - 2  ,  15  ) , orSm , 126 , 9 ) # slabs zadnja kosina
crtaj_kvadar  ( orMj , ( 7  , - 10  ,  15 ) , ( 15  , - 10  ,  15  ) , orSm , 126 , 9 ) # slabs lijeva kosina
crtaj_kvadar  ( orMj , ( 7  ,  - 2  ,  15 ) , ( 15  ,  - 2  ,  15  ) , orSm , 126 , 9 ) # slabs lijeva kosina
crtaj_kvadar ( orMj ,  ( 7  , - 10  , 16 )  , ( 15  , - 2  ,  16  ) , orSm , 85 , 0 ) # brze je napuni se terasa ogradom
crtaj_kvadar ( orMj , [ 8 , -9 , 16  ]  , [ 14 , -3 , 16  ] , orSm , 0 , 0 ) # pa se izbusi rupa
# 4 stupca visine 3
crtaj_kvadar  ( orMj , ( 7  , - 10  , 17 ) , ( 7  , - 10  , 19 ) , orSm , 85 , 0 ) # slabs prednja kosina 
crtaj_kvadar  ( orMj , ( 15  , - 10  ,  17 ) , ( 15  , - 10  ,  19 ) , orSm , 85 , 0 ) # slabs zadnja kosina
crtaj_kvadar  ( orMj , ( 7  , - 2  ,  17  ) , ( 7  , - 2  ,  19  ) , orSm , 85 , 0 ) # slabs lijeva kosina
crtaj_kvadar  ( orMj , (  15  , - 2  ,  17  ) , ( 15  , - 2  ,  19  ) , orSm , 85 , 0 ) # slabs lijeva kosina
   
   

#kutije i banak na ulazu

crtaj_kutiju ( orMj , (13,1,0) , (13,2,0) , orSm , rel_smjer  = "meni" )
crtaj_kutiju ( orMj , (13,4,0) , (13,5,0) , orSm , rel_smjer  = "meni" )
crtaj_banak ( orMj , (13,3,0) , (13,3,0) , orSm )


#krov 
for br in range ( 0 , 4 ) :
   #gornji krov
   crtaj_stepenice ( orMj , ( 7 + br , - 10 + br , 5 + 15 + br) , ( 7 + br , - 2 - br , 5 + 15 + br ) , orSm , blok_id = 134 , rel_smjer  = "meni" ) # prednja kosina
   crtaj_stepenice ( orMj , ( 15 - br , - 10 + br , 5 + 15 + br) , ( 15 - br , - 2 - br , 5 + 15 + br ) , orSm , blok_id = 134 , rel_smjer  = "odmene" ) # zadnja kosina
   crtaj_stepenice ( orMj , ( 7 + br , - 10 + br , 5 + 15 + br) , ( 15 - br , - 10 + br , 5 + 15 + br ) , orSm , blok_id = 134 , rel_smjer  = "lijevo" ) # lijeva kosina
   crtaj_stepenice ( orMj , ( 7 + br ,  - 2 - br , 5 + 15 + br) , ( 15 - br ,  - 2 - br , 5 + 15 + br ) , orSm , blok_id = 134 , rel_smjer  = "desno" ) # lijeva kosina
   #prednji krov
   crtaj_stepenice ( orMj , ( 1 + br , - 10 + br , 7 + br) , ( 1 + br , - 2 - br , 7 + br ) , orSm , blok_id = 134 , rel_smjer  = "meni" ) # prednja kosina
   #crtaj_stepenice ( orMj , ( 15 + br , - 10 - br , 7 + br) , ( 15 + br , - 2 - br , 7 + br ) , orSm , blok_id = 53 , rel_smjer  = "odmene" ) # zadnja kosina
   crtaj_stepenice ( orMj , ( 1 + br , - 10 + br , 7 + br) , ( 7  , - 10 + br , 7 + br ) , orSm , blok_id = 134 , rel_smjer  = "lijevo" ) # lijeva kosina
   crtaj_stepenice ( orMj , ( 1 + br ,  - 2 - br , 7 + br) , ( 7  ,  - 2 - br , 7 + br ) , orSm , blok_id = 134 , rel_smjer  = "desno" ) # lijeva kosina
   #desni krov
   crtaj_stepenice ( orMj , ( 7 + br , - 2 , 7 + br) , ( 7 + br , 10 - br , 7 + br ) , orSm , blok_id = 134 , rel_smjer  = "meni" ) # prednja kosina
   crtaj_stepenice ( orMj , ( 15 - br , - 2 , 7 + br) , ( 15 - br , 10 - br , 7 + br ) , orSm , blok_id = 134 , rel_smjer  = "odmene" ) # zadnja kosina
   #crtaj_stepenice ( orMj , ( 7 + br , - 10 + br , 15 + br) , ( 15 - br , - 10 + br , 15 + br ) , orSm , blok_id = 134 , rel_smjer  = "lijevo" ) # lijeva kosina
   crtaj_stepenice ( orMj , ( 7 + br ,  10 - br , 7 + br) , ( 15 - br ,  10 - br , 7 + br ) , orSm , blok_id = 134 , rel_smjer  = "desno" ) # lijeva kosina

crtaj_kvadar ( orMj , [ 11 , -6 , 18 + 5 ]  , [ 11 , -6 , 18 + 5 ] , orSm , 126 , 9 ) # toranj - slabovi za zatvoriti rupu u sredini krova   wooden Upper Oak Wood Slab   
crtaj_kvadar ( orMj , [ 5 , -6 , 10 ]  , [ 7 , -6 , 10  ] , orSm , 126 , 9 ) # prednji krov - slabovi za zatvoriti rupu u sredini krova   wooden Upper Oak Wood Slab   
crtaj_kvadar ( orMj , [ 11 , -2 , 10 ]  , [ 11 , 6 , 10  ] , orSm , 126 , 9 ) # desni krov - slabovi za zatvoriti rupu u sredini krova   wooden Upper Oak Wood Slab   
   




