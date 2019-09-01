# Test novih funkcija iz modula CRTANJE.PY
#definicija objekta i poziv rutine za crtanje
from crtanje import *		#tu je funkcija koju zovem
from mc import *			
mc = Minecraft() #inicijalizacija sustava za rad sa Minecraftom

# test vrata ++++++

"""
crtaj_kvadar ( gdjeSam () , [ 4 , -1 , 0 ]  , [ 6 , 1 , 3  ] , gdjeGledam () , 1 , 0 ) #blok
crtaj_kvadar ( gdjeSam () , [ 5 , 0 , 0 ]  , [ 5 , 0 , 3  ] , gdjeGledam () , 0 , 0 ) #blok

crtaj_vrata ( gdjeSam () , ( 4,0,0 ) , gdjeGledam () , "meni"  , blok_id = 195     )
crtaj_vrata ( gdjeSam () , ( 6,0,0 ) , gdjeGledam () , "odmene"  , blok_id = 195     )
crtaj_vrata ( gdjeSam () , ( 5,-1,0 ) , gdjeGledam () , "lijevo"  , blok_id = 195     )
crtaj_vrata ( gdjeSam () , ( 5,1,0 ) , gdjeGledam () , "desno"  , blok_id = 195     )
"""


#test vrata ograde ++++++

"""
crtaj_kvadar ( gdjeSam () , [ 4 , -3 , 0 ]  , [ 11 , 3 , 0  ] , gdjeGledam () , 85 , 0 ) #blok
crtaj_kvadar ( gdjeSam () , [ 5 , -2 , 0 ]  , [ 10 , 2 , 0  ] , gdjeGledam () , 0 , 0 ) #blok

crtaj_vrataograde ( gdjeSam () , ( 4,0,0 ) ,  gdjeGledam () ,  "lijevo_desno"  , blok_id = 107    )
crtaj_vrataograde ( gdjeSam () , ( 7,3,0  ) ,  gdjeGledam () ,  "naprijed_nazad"  , blok_id = 107    )
crtaj_vrataograde ( gdjeSam () , ( 11,0,0 ) ,  gdjeGledam () ,  "lijevo_desno"  , blok_id = 107    )
crtaj_vrataograde ( gdjeSam () , ( 7,-3,0  ) ,  gdjeGledam () ,  "naprijed_nazad"  , blok_id = 107    )
"""

#test crtanja debla  +++

"""
crtaj_deblo ( gdjeSam () , (4 , -3 , 0) , ( 4 , -3 , 4) , gdjeGledam () , "gore" , blok_id = 17 , podtip = 0   )
crtaj_deblo ( gdjeSam () , (4 , -3 , 0) , ( 4, 3 , 0 ) , gdjeGledam () , "lijevo_desno" , blok_id = 17 , podtip = 0   )
crtaj_deblo ( gdjeSam () , (4 , -3 , 0) , ( 8 , -3 , 0) , gdjeGledam () , "naprijed_nazad" , blok_id = 17 , podtip = 0   )
"""

#test crtanja baklji +++

"""
crtaj_deblo ( gdjeSam () , ( 3 , 0 , 0 ) , (3 ,0 , 5 ) , gdjeGledam () , "gore" , 17, 0  )

crtaj_baklju ( gdjeSam () , ( 2 , 0 , 1 ) ,  gdjeGledam () ,  "meni"   )
crtaj_baklju ( gdjeSam () , ( 3 , 1 , 2 ) ,  gdjeGledam () ,  "desno"   )
crtaj_baklju ( gdjeSam () , ( 4 , 0 , 3 ) ,  gdjeGledam () ,  "odmene"   )
crtaj_baklju ( gdjeSam () , ( 3 , -1 , 4 ) ,  gdjeGledam () , "lijevo"   )
crtaj_baklju ( gdjeSam () , ( 3 , 0 , 5 ) ,  gdjeGledam () ,  "gore"   )
"""

#test crtanja stepenica +++++

"""
crtaj_stepenice ( gdjeSam () , ( 5 , -2 , 0) , ( 5 , 2 , 0) , gdjeGledam () , rel_smjer  ="meni" ,gore_dolje = "da" )
crtaj_stepenice ( gdjeSam () , ( 6 , 3 , 0) , ( 11 , 3 , 0) , gdjeGledam () , rel_smjer  ="desno" , gore_dolje = "da")
crtaj_stepenice ( gdjeSam () , ( 12 , -2 , 0) , ( 12 , 2 , 0) , gdjeGledam () , rel_smjer  ="odmene" )
crtaj_stepenice ( gdjeSam () , ( 6 , -3 , 0) , ( 11 , -3 , 0) , gdjeGledam () , rel_smjer  ="lijevo" )
crtaj_stepenice ( gdjeSam () , ( 5 , 3 , 0) , ( 5 , 3 , 0) , gdjeGledam () , rel_smjer  ="meni" , gore_dolje = "da")
crtaj_stepenice ( gdjeSam () , ( 12 , 3 , 0) , ( 12 , 3 , 0) , gdjeGledam () , rel_smjer  ="desno" )
crtaj_stepenice ( gdjeSam () , ( 12 , -3 , 0) , ( 12 , -3 , 0) , gdjeGledam () , rel_smjer  ="odmene" )
crtaj_stepenice ( gdjeSam () , ( 5 , -3 , 0) , ( 5 , -3 , 0) , gdjeGledam () , rel_smjer  ="lijevo" )
"""

#test crtanja  ljestvi +++

"""
crtaj_kvadar ( gdjeSam () , [ 4 , -1 , 0 ]  , [ 6 , 1 , 2  ] , gdjeGledam () , 1 , 0 ) #blok
#crtaj_kvadar ( gdjeSam () , [ 5 , 0 , 0 ]  , [ 5 , 0 , 2  ] , gdjeGledam () , 0 , 0 ) #blok

crtaj_ljestve  ( gdjeSam () , ( 7 , 0 , 0 )  , ( 7 , 0 , 2 ) , gdjeGledam ()  , rel_smjer  = "meni" )
crtaj_ljestve  ( gdjeSam () , ( 3 , 0 , 0 )  , ( 3 , 0 , 2 ) , gdjeGledam ()  , rel_smjer  = "odmene" )
crtaj_ljestve  ( gdjeSam () , ( 5 , 2 , 0 )  , ( 5 , 2 , 2 ) , gdjeGledam ()  , rel_smjer  = "lijevo" )
crtaj_ljestve  ( gdjeSam () , ( 5 , -2 , 0 )  , ( 5 , -2 , 2 ) , gdjeGledam ()  , rel_smjer  = "desno" )
"""

#test crtanja  peci ++++
"""
crtaj_pec   ( gdjeSam () , [ 5 , 0 , 0 ]  , [ 5 , 0 , 1  ] , gdjeGledam (), rel_smjer  = "meni"    ) 
crtaj_pec   ( gdjeSam () , [ 5 , -1 , 0 ]  , [ 5 , -1 , 1  ] , gdjeGledam (), rel_smjer  = "odmene"    ) 
crtaj_pec   ( gdjeSam () , [ 4 , -2 , 0 ]  , [ 4 , -2 , 1  ] , gdjeGledam (), rel_smjer  = "lijevo"    ) 
crtaj_pec   ( gdjeSam () , [ 4 , 2 , 0 ]  , [ 4 , 2 , 1  ] , gdjeGledam (), rel_smjer  = "desno"    ) 
"""

#test crtanja kutije +++++
"""
crtaj_kutiju   ( gdjeSam () , [ 5 , 1 , 0 ]  , [ 5 , 2 , 1  ] , gdjeGledam (), rel_smjer  = "meni"    ) 
crtaj_kutiju   ( gdjeSam () , [ 5 , -1 , 0 ]  , [ 5 , -1 , 1  ] , gdjeGledam (), rel_smjer  = "odmene"    ) 
crtaj_kutiju   ( gdjeSam () , [ 4 , -2 , 0 ]  , [ 4 , -2 , 1  ] , gdjeGledam (), rel_smjer  = "lijevo"    ) 
crtaj_kutiju   ( gdjeSam () , [ 4 , 4 , 0 ]  , [ 3 , 4 , 1  ] , gdjeGledam (), rel_smjer  = "desno"    ) 
"""

#test crtanja workbencha+++++
"""
crtaj_banak   ( gdjeSam () , [ 5 , 1 , 0 ]  , [ 5 , 2 , 1  ] , gdjeGledam ()   ) 
crtaj_banak   ( gdjeSam () , [ 5 , -1 , 0 ]  , [ 5 , -1 , 1  ] , gdjeGledam ()   ) 
crtaj_banak   ( gdjeSam () , [ 4 , -2 , 0 ]  , [ 4 , -2 , 1  ] , gdjeGledam ()    ) 
crtaj_banak   ( gdjeSam () , [ 4 , 4 , 0 ]  , [ 3 , 4 , 1  ] , gdjeGledam ()   ) 
"""

#test crtanja kreveta
"""
crtaj_krevet  ( gdjeSam () , ( 3 , -1 , 0 ) , ( 2 , -1 , 0 )  , gdjeGledam () , "meni"  )
crtaj_krevet  ( gdjeSam () , ( 2 , 1 , 0 ) , ( 3 , 1 , 0 )   , gdjeGledam () , "odmene")
crtaj_krevet  ( gdjeSam () , ( 5 , 0 , 0 ) , ( 5 , -1 , 0 )   , gdjeGledam () , "lijevo")
crtaj_krevet  ( gdjeSam () , ( 5 , 1 , 0 ) , ( 5 , 2 , 0 )   , gdjeGledam () , "desno")
"""

#test crtanja kapka
"""
crtaj_klopku  ( gdjeSam () , ( 3 , 0 , 0 ) ,  gdjeGledam () , "meni", visina = "dolje")
crtaj_klopku  ( gdjeSam () , ( 5 , 0 , 0 ) ,  gdjeGledam () , "odmene" , "otvoreno")
crtaj_klopku  ( gdjeSam () , ( 7 , 0 , 0 ) ,  gdjeGledam () , "lijevo" , visina = "gore")
crtaj_klopku  ( gdjeSam () , ( 9 , 0 , 0 ) ,  gdjeGledam () ,  "desno" , stanje="zatvoreno" , visina = "gore")
"""

#test crtanja terasa

#rudnik
#crtaj_terase ( gdjeSam () , ( 0 , 0 , 0 ) ,  gdjeGledam () , korak = 1 , visina = 9 , sirina = 11 , baklje="da")

# terasa
#crtaj_terase ( gdjeSam () , ( 0 , 0 , 0 ) ,  gdjeGledam () , korak = 3 , visina = 20 , sirina = 20, baklje="da")

#strmina

#crtaj_terase ( gdjeSam () , ( 0 , 0 , 0 ) ,  gdjeGledam () , korak = 2 , visina = 50 , sirina = 50, baklje="ne")

# kopanje

"""
filter (  gdjeSam () , ( 0 , 0 , 0 ) ,  gdjeGledam (),   7 ,    11 ,  11, "da") 
crtaj_terase ( gdjeSam () , ( 11 , 0 , 0 ) ,  gdjeGledam () , korak = 1 , visina = 9 , sirina = 11 , baklje="da")
"""

#test crtanja redstone baklji +++

"""
crtaj_deblo ( gdjeSam () , ( 3 , 0 , 0 ) , (3 ,0 , 5 ) , gdjeGledam () , "gore" , 17, 0  )

crtaj_redstonetorch ( gdjeSam () , ( 2 , 0 , 1 ) ,  gdjeGledam () ,  "meni"   )
crtaj_redstonetorch ( gdjeSam () , ( 3 , 1 , 2 ) ,  gdjeGledam () ,  "desno"   )
crtaj_redstonetorch ( gdjeSam () , ( 4 , 0 , 3 ) ,  gdjeGledam () ,  "odmene"   )
crtaj_redstonetorch ( gdjeSam () , ( 3 , -1 , 4 ) ,  gdjeGledam () , "lijevo"   )
crtaj_redstonetorch ( gdjeSam () , ( 3 , 0 , 5 ) ,  gdjeGledam () ,  "gore"   )
"""

# test crtanja repeatera +++
"""
crtaj_repeater   ( gdjeSam () , [ 5 , 0 , 0 ]  , [ 5 , 0 , 0  ] , gdjeGledam (), rel_smjer  = "meni"    ) 
crtaj_repeater   ( gdjeSam () , [ 6 , 0 , 0 ]  , [ 6 , 0 , 0  ] , gdjeGledam (), rel_smjer  = "odmene"    ) 
crtaj_repeater   ( gdjeSam () , [ 7 , 0 , 0 ]  , [ 7 , 0 , 0  ] , gdjeGledam (), rel_smjer  = "lijevo"    ) 
crtaj_repeater   ( gdjeSam () , [ 8 , 0 , 0 ]  , [ 8 , 0 , 0  ] , gdjeGledam (), rel_smjer  = "desno"    ) 
"""

# test crtanja comparatora +++
"""
crtaj_comparator   ( gdjeSam () , [ 5 , 0 , 0 ]  , [ 5 , 0 , 0  ] , gdjeGledam (), rel_smjer  = "meni"    ) 
crtaj_comparator   ( gdjeSam () , [ 6 , 0 , 0 ]  , [ 6 , 0 , 0  ] , gdjeGledam (), rel_smjer  = "odmene"    ) 
crtaj_comparator   ( gdjeSam () , [ 7 , 0 , 0 ]  , [ 7 , 0 , 0  ] , gdjeGledam (), rel_smjer  = "lijevo"    ) 
crtaj_comparator   ( gdjeSam () , [ 8 , 0 , 0 ]  , [ 8 , 0 , 0  ] , gdjeGledam (), rel_smjer  = "desno"    ) 
"""

#test crtanja redstone zhica +++
"""
crtaj_redstonedust ( gdjeSam () , [ 5 , 2 , 0 ]  , [ 8 , 9 , 0  ] , gdjeGledam () )
"""

# test crtanja hoppera 
"""
crtaj_hopper    ( gdjeSam () , [ 4 , 0 , 0 ]  , [ 4 , 0 , 0  ] , gdjeGledam (), rel_smjer  = "dolje"   )
crtaj_hopper   ( gdjeSam () , [ 6 , 0 , 0 ]  , [ 6 , 0 , 0  ] , gdjeGledam (), rel_smjer  = "meni"    ) 
crtaj_hopper   ( gdjeSam () , [ 8 , 0 , 0 ]  , [ 8 , 0 , 0  ] , gdjeGledam (), rel_smjer  = "odmene"    ) 
crtaj_hopper   ( gdjeSam () , [ 10 , 0 , 0 ]  , [ 10 , 0 , 0  ] , gdjeGledam (), rel_smjer  = "lijevo"    ) 
crtaj_hopper   ( gdjeSam () , [ 12  , 0 , 0 ]  , [ 12 , 0 , 0  ] , gdjeGledam (), rel_smjer  = "desno"    ) 
"""

# test crtanja dispensers 
"""
crtaj_dispenser    ( gdjeSam () , [ 2 , 0 , 0 ]  , [ 4 , 0 , 0  ] , gdjeGledam (), rel_smjer  = "gore"   )
crtaj_dispenser    ( gdjeSam () , [ 4 , 0 , 0 ]  , [ 4 , 0 , 0  ] , gdjeGledam (), rel_smjer  = "dolje"   )
crtaj_dispenser   ( gdjeSam () , [ 6 , 0 , 0 ]  , [ 6 , 0 , 0  ] , gdjeGledam (), rel_smjer  = "meni"    ) 
crtaj_dispenser   ( gdjeSam () , [ 8 , 0 , 0 ]  , [ 8 , 0 , 0  ] , gdjeGledam (), rel_smjer  = "odmene"    ) 
crtaj_dispenser   ( gdjeSam () , [ 10 , 0 , 0 ]  , [ 10 , 0 , 0  ] , gdjeGledam (), rel_smjer  = "lijevo"    ) 
crtaj_dispenser   ( gdjeSam () , [ 12  , 0 , 0 ]  , [ 12 , 0 , 0  ] , gdjeGledam (), rel_smjer  = "desno"    ) 
"""

# test crtanja pistona

#crtaj_piston  ( gdjeSam () , [ 2 , -5 , 0 ]  , [ 8 , -5 , 0  ] , gdjeGledam (), rel_smjer  = "gore"   )
#crtaj_piston    ( gdjeSam () , [ 2 , -3 , 1 ]  , [ 8 , -3 , 1  ] , gdjeGledam (), rel_smjer  = "dolje"   )
#crtaj_piston   ( gdjeSam () , [ 2 , -1 , 2 ]  , [2 , 1 , 2  ] , gdjeGledam (), rel_smjer  = "meni"    ) 
#crtaj_piston   ( gdjeSam () , [ 2 , 1 , 3 ]  , [ 8 , 1 , 3  ] , gdjeGledam (), rel_smjer  = "odmene"    ) 
#crtaj_piston   ( gdjeSam () , [ 2 , 3 , 4 ]  , [ 8 , 3 , 4  ] , gdjeGledam (), rel_smjer  = "lijevo"    ) 
#crtaj_piston   ( gdjeSam () , [ 2 , 5 , 5 ]  , [ 8 , 5 , 5  ] , gdjeGledam (), rel_smjer  = "desno"    ) 

"""
crtaj_kvadar ( gdjeSam () , [ 4 , -1 , 0 ]  , [ 6 , 1 , 2  ] , gdjeGledam () , 1 , 0 ) #blok
crtaj_comparator   ( gdjeSam () , [ 7 , 0 , 0 ]  , [ 7 , 0 , 0  ] , gdjeGledam (), rel_smjer  = "lijevo"    ) 
"""

"""
for br in range ( -3 , 3 ):
   crtaj_piston   ( gdjeSam () , [ 1 , br , 6 ]  , [5 , br , 6  ] , gdjeGledam (), rel_smjer  = "odmene"    )
"""


"""
makeFarmer (orMj , 5 , -2 , 0 ,  orSm ,  Profession = 0 , Career = 1)
=======

for br in range ( 5 ):
   makeFarmer (orMj , 5 + br , -2 , 0 ,  orSm ,  Profession = 0 , Career = 1)

"""

"""
makeLibrarian (orMj , 5 , -1 , 0 ,  orSm ,  Profession = 1 , Career = 1)
makePriest (orMj , 5 , 0 , 0 ,  orSm ,  Profession = 2 , Career = 1)
makeBlacksmith (orMj , 5 , 1 , 0 ,  orSm ,  Profession = 3 , Career = 1)
makeButcher (orMj , 5 , 2 , 0 ,  orSm ,  Profession = 4 , Career = 1)
"""

"""
from modul_sorter import * 
modul_sorter (  orMj ,  orSm , iX=0 , iZ=0 , iY=0  ,  materijal = 98, dv = 0  , kutija = "ne" ,crtaj_kutije = "ne" )
=======
"""

orMj = gdjeSam ()
orSm = gdjeGledam ()

#test crtanja  buttona


#for br in range ( 4 , 16 , 2 ):
#   crtaj_kvadar ( gdjeSam () , [ br , 0 , 1 ]  , [ br , 0 , 1  ] , gdjeGledam () , 1 , 0 ) #blok
#crtaj_kvadar ( gdjeSam () , [ 5 , 0 , 0 ]  , [ 5 , 0 , 2  ] , gdjeGledam () , 0 , 0 ) #blok

crtaj_button  ( gdjeSam () , ( 4 , 0 , 1 )  , ( 4 , 0 , 1 ) , gdjeGledam ()  , rel_smjer  = "gore" )
crtaj_button  ( gdjeSam () , ( 6 , 0 , 1 )  , ( 6 , 0 , 1 ) , gdjeGledam ()  , rel_smjer  = "dolje" )



crtaj_button  ( gdjeSam () , ( 8 , 0 , 1 )  , ( 8 , 0 , 1 ) , gdjeGledam ()  , rel_smjer  = "lijevo" )
crtaj_button  ( gdjeSam () , ( 10 , 0 , 1 )  , ( 10 , 0 , 1 ) , gdjeGledam ()  , rel_smjer  = "desno" )
crtaj_button  ( gdjeSam () , ( 12 , 0 , 1 )  , ( 12 , 0 , 1 ) , gdjeGledam ()  , rel_smjer  = "meni" )
crtaj_button  ( gdjeSam () , ( 14 , 0 , 1 )  , ( 14 , 0 , 1 ) , gdjeGledam ()  , rel_smjer  = "odmene" )
