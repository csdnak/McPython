# lift crta se od dna prema gore
#definicija objekta i poziv rutine za crtanje
import time 
from crtanje import *		#tu je funkcija koju zovem

from mc import *			
mc = Minecraft() #inicijalizacija sustava za rad sa Minecraftom


def crtaj_lift_2 ( orMj , orSm , iX  , iZ ,  iY  , visina = 4 , materijal = 98 , dv = 2 ):

   orMj   = premjesti_origin ( orMj , iX  , iZ , iY ,  orSm )
   #minimalna visina je 4, broji se od reda sa chestom
   if visina < 4 :
      visina = 4
   #prvi red nivo: -3
   crtaj_kvadar ( orMj , ( 1  , 0, -3 )  , ( 4  , 0 , -3 ) , orSm , materijal , dv )
   #drugi red nivo -2 , crtam odozada prema naprijed zbog slijeda
   crtaj_redstonedust ( orMj , ( 4 , 0 , -2 ) , ( 4 , 0 , -2 ) , orSm )
   crtaj_repeater ( orMj , ( 3 , 0 , -2 ) , ( 3 , 0 , -2 ) , orSm , rel_smjer  = "meni" )
   crtaj_kvadar ( orMj , ( 2 , 0 , -2 ) , ( 2 , 0 , -2 ) , orSm , materijal , dv )
   crtaj_redstonetorch ( orMj , ( 1 , 0 , -2 )   ,  orSm  , "meni" )
   # treci red nivo -1 , crtam sprijeda zbog slijeda
   crtaj_hopper    ( orMj , ( 0 , 0 , -1 )  , ( 0 , 0 , -1 ) , orSm , "odmene" )
   crtaj_dropper    ( orMj , ( 1 , 0 , -1 )  , ( 1 , 0 , -1 )  , orSm , rel_smjer  = "gore" )
   crtaj_comparator ( orMj , ( 2 , 0 , -1 )  , ( 2 , 0 , -1 )  , orSm , rel_smjer  = "odmene" )
   crtaj_kvadar ( orMj , ( 3 , 0 , -1 ) , ( 3 , 0 , -1 ) , orSm , materijal , dv )
   crtaj_redstonetorch ( orMj , ( 4 , 0 , -1 )   ,  orSm  , "odmene" )
   #prije periodike na hopper staviti kutiju
   crtaj_kutiju ( orMj , ( 0 , 0 , 0 )  , ( 0 , 0 , 0 ) , orSm , rel_smjer  = "meni" , blok_id = 54     ) # ulazna kutija je ishodiste
   #mora zavrsiti sa gornjim redom periodike, visina mora biti parni broj
   if visina % 2 == 1 :
      visina += 1
   #crtaj uvis
   brojalica = 0
   while brojalica < visina :
      # dropper se uvijek jednako crta
      crtaj_dropper    ( orMj , ( 1 , 0 , brojalica )  , ( 1 , 0 , brojalica )  , orSm , rel_smjer  = "gore" )
      if brojalica % 2 == 0 :    # doljnji red periodike
         crtaj_kvadar ( orMj , ( 4 , 0 , brojalica ) , ( 4 , 0 , brojalica ) , orSm , materijal , dv ) #kocka
         crtaj_redstonetorch ( orMj , ( 3 , 0 , brojalica )   ,  orSm  , "meni" )   #baklja
      else :      #gornji red periodike
         crtaj_kvadar ( orMj , ( 3 , 0 , brojalica ) , ( 3 , 0 , brojalica ) , orSm , materijal , dv ) #kocka u sredini
         crtaj_redstonetorch ( orMj , ( 2 , 0 , brojalica )   ,  orSm  , "meni" )   #baklja napred
         crtaj_redstonetorch ( orMj , ( 4 , 0 , brojalica )   ,  orSm  , "odmene" )   #baklja nazad
      brojalica += 1
   #i na "visini"
   crtaj_kutiju ( orMj , ( 0 , 0 , visina )  , ( 1 , 0 , visina ) , orSm , rel_smjer  = "lijevo" , blok_id = 54     ) # izlazna kutija
         
         
      
   
   
   
   
   
   
   
   

def crtaj_lift ( orMj , orSm , iX  , iZ ,  iY  , visina = 12 ):

   orMj   = premjesti_origin ( orMj , iX  , iZ , iY ,  orSm )

   
   korekcija = 0
   if ( visina % 2 == 1 ) : #nesmije biti neparna visina
      mc.postToChat("NEPARNA "   )
      visina += 1
      korekcija = 1
      
   else:
      mc.postToChat("PPPPPARNA "   )
      
   
   #sandstone glatki
   materijal = 24
   dv = 2

   # zashtita oko stupa
   crtaj_kvadar ( orMj , [ 0  , -2, -1 ]  , [ 4  , 5 , visina -7 ] , orSm , materijal , dv ) # zashtita i red ispod   pa do ispod nogu
   
   #rupa oko stupa
   crtaj_kvadar ( orMj , [ 1  , -1, 0 ]  , [ 3  , 4 , visina + 2 ] , orSm , 0 , 0 ) # zrak

   #prvi red
   crtaj_kvadar ( orMj , [ 2  , 0, 0 ]  , [ 2  , 4 , 0  ] , orSm , materijal , dv ) # temeljniblok
   crtaj_redstonedust ( orMj , [ 2 , 0, 1 ]  , [ 2 ,  0 , 1  ] , orSm )
   crtaj_repeater ( orMj , [ 2 , 1, 1 ]  , [ 2 ,  1 , 1  ] , orSm , rel_smjer  = "desno" )
   crtaj_kvadar ( orMj , [ 2  , 2, 1 ]  , [ 2  , 2 , 1  ] , orSm , materijal , dv )
   crtaj_redstonetorch ( orMj , [ 2  , 3, 1 ]   ,  orSm  , "desno" ) 
   

   #drugi red
   crtaj_kvadar ( orMj , [ 2  , 1, 2 ]  , [ 2  , 1 , 2  ] , orSm , materijal , dv )
   crtaj_redstonetorch ( orMj , [ 2  , 0, 2 ]   ,  orSm  , "lijevo" )  
   crtaj_comparator ( orMj , [ 2  , 2, 2 ]  , [ 2  , 2 , 2  ]  , orSm , rel_smjer  = "lijevo" )
   crtaj_dropper    ( orMj , [ 2  , 3, 2 ]  , [ 2  , 3 , 2  ]  , orSm , rel_smjer  = "gore" )
   crtaj_hopper    ( orMj , [ 2  , 4, 2 ]  , [ 2  , 4 , 2  ] , orSm , "lijevo" )
  

   #treci red
   crtaj_kvadar ( orMj , [ 2  , 0, 3 ]  , [ 2  , 0 , 3  ] , orSm , materijal , dv )
   crtaj_redstonetorch ( orMj , [ 2  , 1, 3 ]   ,  orSm  , "desno" )
   crtaj_dropper    ( orMj , [ 2  , 3, 3 ]  , [ 2  , 3 , 3  ]  , orSm , rel_smjer  = "gore" )
   crtaj_kutiju ( orMj , [ 2 , 4, 3 ]  , [ 1 ,  4 , 3  ] , orSm , rel_smjer  = "desno" , blok_id = 54     )
   

   korigirana_visina = int ( ( visina -3  )  )
   for br in range ( 0 , korigirana_visina , 2 ):
      #cetvrti red

      crtaj_kvadar ( orMj , [ 2  , 1, 4 + br  ]  , [ 2  , 1 , 4  + br ] , orSm , materijal , dv )
      crtaj_redstonetorch ( orMj , [ 2  , 0, 4 + br ]   ,  orSm  , "lijevo" )  
      crtaj_redstonetorch ( orMj , [ 2  , 2, 4 + br ]   ,  orSm  , "desno" )
      crtaj_dropper    ( orMj , [ 2  , 3, 4 + br ]  , [ 2  , 3 , 4 + br  ]  , orSm , rel_smjer  = "gore" )
      #time.sleep ( 1 )

      # peti red

      crtaj_kvadar ( orMj , [ 2  , 0, 5 + br ]  , [ 2  , 0 , 5  + br ] , orSm , materijal , dv )
      crtaj_redstonetorch ( orMj , [ 2  , 1, 5  + br]   ,  orSm  , "desno" )
      crtaj_dropper    ( orMj , [ 2  , 3, 5 + br ]  , [ 2  , 3 , 5  + br ]  , orSm , rel_smjer  = "gore" )
      #time.sleep ( 1 )
   
   
   crtaj_kvadar ( orMj , [ 2  , 1, visina  ]  , [ 2  , 1 , visina ] , orSm , materijal , dv )
   crtaj_redstonetorch ( orMj , [ 2  , 0, visina ]   ,  orSm  , "lijevo" )  
   crtaj_redstonetorch ( orMj , [ 2  , 2, visina ],  orSm  , "desno" )
   crtaj_dropper    ( orMj , [ 2  , 3, visina ]  , [ 2  , 3 , visina  ]  , orSm , rel_smjer  = "gore" )
   
   #kutija na vrhu

   crtaj_kutiju ( orMj , [ 2 , 3, visina + 1  ]  , [ 2 ,  4 , visina + 1  ] , orSm , rel_smjer  = "meni" , blok_id = 54     )
   if korekcija == 1 :
      crtaj_hopper    ( orMj , [ 2 ,  4 , visina   ]  , [ 2 ,  4 , visina   ] , orSm , "dolje" ) # spust iz kutija
      crtaj_hopper    ( orMj , [ 2 ,  4 , visina - 1  ]  , [ 2 ,  4 , visina - 1  ] , orSm , "desno" ) # desno
   else :
      crtaj_hopper    ( orMj , [ 2 ,  4 , visina  ]  , [ 2 ,  4 , visina  ] , orSm , "desno" ) # desno


def lift (orMj , orSm ):
   #pozicioniranje na soreter, ispod kutije , dva natrag, jedan lijevo
   

   bedrock = nadji_dno ( orMj , ( 0 , 0 , 0 ) , orSm ) + 2 # maknuti crne tocke u pregledu
   crtaj_lift ( orMj ,  orSm ,  iX=0, iZ=-4 , iY=bedrock  , visina = -bedrock ) # crta se od dna prema gore
   
def lift2 (orMj , orSm ):
   """ test okretanja
   orSm2 = ortUlijevo ( ortUlijevo ( orSm ))
   crtaj_lift_2 ( orMj ,  orSm2 ,  iX=-5, iZ=0 , iY=0  , visina = 3 ) # 
   """
   crtaj_lift_2 ( orMj ,  orSm ,  iX=1, iZ=0 , iY=-1
   , visina = 3 )

if __name__ == "__main__":    #direktan poziv
   
   orMj = gdjeSam ()
   orSm = gdjeGledam ()
   lift2 (orMj , orSm ) 






