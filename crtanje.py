# crta objekt zadan u dostavljenoj listi
from mc import * # ajmo probati ovaj import
mc = Minecraft() #inicijalizacija sustava za rad sa Minecraftom

def crtanje (ulaz):
   """
   funkcija za crtanje prima listu listi sa po 4 parametra
   1. parametar x koordinata
   2. parametar z koordinata
   3. parametar y koordinata
   4. parametar id bloka koji se postavlja
   """
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
   if  abs ( Vx )  != abs ( Vz ) :		# ne pod 45
      for brojalica in ulaz :    		# prodji listu
         gdjex=radnaPozicija.x + Vx*brojalica [0] - Vz*brojalica[1]    		# pomak po x
         gdjez=radnaPozicija.z + Vx*brojalica[1] + Vz*brojalica[0]			# pomak po y
         #mc.postToChat("gdjex: %f gdjez: %f z-os: %f " % ( gdjex , gdjez , brojalica [1] ) )
         mc.setBlock(gdjex , brojalica[2] , gdjez , brojalica[3], brojalica[4])			#postavi blok
   return 1
   
def ortUlijevo ( orSm ):
   prijevod = {}
   prijevod [ ( 1 , 0  ) ] = (  0 , -1  ) # gledam north
   prijevod [ ( -1 , 0 ) ] = (  0 , 1 ) # gledam south
   prijevod [ ( 0 , 1 ) ] = (  1 , 0 )  # gledam east
   prijevod [ ( 0 , -1 ) ]= (  -1 , 0 )  # gledam weast
   buff = prijevod [ ( orSm [ 0 ] , orSm [ 1 ] )   ]
   return buff

def ortUdesno ( orSm ):
   prijevod = {}
   prijevod [ ( 1 , 0  ) ] = (  0 , 1  ) # gledam north
   prijevod [ ( -1 , 0 ) ] = (  0 , -1 ) # gledam south
   prijevod [ ( 0 , 1 ) ] = (  -1 , 0 )  # gledam east
   prijevod [ ( 0 , -1 ) ]= (  1 , 0 )  # gledam weast
   buff = prijevod [ ( orSm [ 0 ] , orSm [ 1 ] )   ]
   return buff
   
   
def rel2abs ( inPoz ,  dPoz  , smjer  ) :
   """
   funkcija za pretvaranje relativnih u apsolutne koordinate  prima parametre: 
   1. Parametar inPoz
      1. parametar origin x koordinata
      2. parametar origin z koordinata
      3. parametar origin y koordinata
   2. Parametar dPoz
      1. parametar dX
      2. parametar dZ
      3. parametar dY
   3. smjer
      1. Vx smjer
      2. Vy smjer gledanja
   
   DEFAULT: "gleda prema" X pozitivnoj osi
   
   vraca listu sa 3 koordinate
   1. x
   2. y
   3. z
   """
   if  abs ( smjer [0] )  != abs ( smjer [1] ) :		# ne pod 45
      gdjeX=inPoz [0] + smjer [0]*dPoz[0] - smjer [1]*dPoz[1]    		# pomak po x
      gdjeZ=inPoz [1] + smjer [0]*dPoz[1] + smjer [1]*dPoz[0]			# pomak po y
      gdjeY  = inPoz [2] + dPoz[2]  
   return (  [ gdjeX , gdjeY , gdjeZ  ] )
   

def premjesti_origin ( orMj , dX , dZ , dY ,  orSm ):
   # origin ispred na sredini 
   
   #korekcija polozaja
   orMjA   = rel2abs ( orMj ,  ( dX , dZ , dY )   , orSm  ) 
   bla = orMjA [ 1 ]
   orMjA [ 1 ] = orMjA [ 2 ]
   orMjA [ 2 ] = bla
   return orMjA
   
def crtaj_tocku ( inLista , blok_id , blok_dv = 0 , pomakX = 0 , pomakZ = 0 ) :
   """
   funkcija za crtanje tocke
   1. parametar lista sa koordinatama ( X , Y , Z )
   2. koji blok 
   3. koja varijanta bloka DFAULT osnovni oblik
   4. pomak po X osi
   5. pomak po Z osi 
   """
   mc.setBlock( inLista [ 0 ] , inLista [ 1 ], inLista [ 2 ] , blok_id , blok_dv )
   return
 

def crtaj_bitmap ( inOrigin ,  smjer , inBitmap , pomakX = 0 , pomakZ = 0) :
   """
   funkcija za crtanje bitmape
   funkcija za crtanje tocke
   1. parametar lista sa koordinatama ( X , Y , Z )
   2. smjer
   3. bitmapa
   4. pomak po X osi
   5. pomak po Z osi 
   Origin je zadan ili pozicija treba pretuci u apsolutne koordinate i nacrtati tocku za svaki red 
   """
   for red in inBitmap :
      crtaj_tocku ( rel2abs (  inOrigin ,  [ red  [0] + pomakX, red  [1] + pomakZ, red  [2] ] , smjer ) , red  [3] , red  [4] )
   return

def nadji_dno ( origin , polozaj , smjer ):
   """
   pronalazi bedrock dubinu
   """
   marker = 1
   dY = 0
   while marker  == 1 :
      dY -= 1
      for dX in range (-4 ,5):
         for dZ in range (-4 ,5):
            gdje = rel2abs ( origin ,  ( dX , dZ , dY )  , smjer  )
            if mc.getBlock ( gdje ) == BEDROCK.id :
               marker = 0
   return ( dY   )
            
            

   
def filter ( origin , polozaj , smjer ,  visina = 7 ,   sirina = 10 , dubina = 10, baklje="ne") : #ne dira ga polozaj
   """
   ispred lika cisti kvadratasto podrucje
   1. parametar lista sa koordinatama ( X , Y , Z )
   2. parametar lista sa koordinatama ( X , Y , Z )
   3. apsolutni smjer crtanja
   4. broj terasa
   5. dubina terase
   6. sirina terase
   """
   zaMaknuti = [ SANDSTONE.id , SAND.id , STONE.id , DIRT.id , GRAVEL.id , GRASS.id , GRASS_TALL.id , COBBLESTONE.id , WATER_FLOWING.id , WATER_STATIONARY.id , LAVA_FLOWING.id , LAVA_STATIONARY.id , 17 , 162, 87 ] # 17 , 162 wood , 87 nether rack
   zaMaknutiOpasno = [ WATER_FLOWING.id , WATER_STATIONARY.id , LAVA_FLOWING.id , LAVA_STATIONARY.id , SAND.id , GRAVEL.id ] # Dodani shljunak i pjesak jer padanja sve poremete
   origin = premjesti_origin ( origin , polozaj [0] , polozaj [1], polozaj [2],  smjer ) 
   for dY in range ( visina + 2 , -1 , -1 ) : # ozgora prema dolje
      #mc.postToChat("dY: %f" % ( dY ) )
      for dX in range ( 1 + dubina , -1 , -1 ) : # sprijeda prema nazad
         #mc.postToChat("dX: %f" % ( dX ) )
         for dZ in range ( -1 - sirina , sirina + 2 ) : #slijeva nadesno
            #gdjeX , gdjeY , gdjeZ = rel2abs ( inPoz ,  ( dX , dZ , dY )  , smjer  ) 
            gdje = rel2abs ( origin ,  ( dX , dZ , dY )  , smjer  ) # hodalica
            kojiBlok = mc.getBlock ( gdje ) # koji blok je tu
            if ( dX == 1 + dubina ) or ( abs ( dZ ) > abs ( sirina ) ) or dY >= visina :   #jeli prvi red ili krajnji lijevi ili krajnji desni blok ili "gornji" red
               # prvi je red -- mici opasno
               if kojiBlok in zaMaknutiOpasno :
                  mc.setBlock(gdje , STONE.id , 2 )	
            else :
               # ostali redovi -- filtriraj
               if kojiBlok in zaMaknuti :
                  mc.setBlock(gdje , AIR.id)			#postavi blok
            
            if (( dX ==  dubina ) or   (int ( dX ) % 5  == 0) ) and ( int ( dZ ) % 5 ) == 0 and ( dY == 0 ) and baklje == "da":
               mc.setBlock ( gdje , 50 , 5 )
            """
            #  Za dugacke korake
            if ( int ( dZ ) % 10 ) == 0 and ( int ( dX - 1 ) % 10 == 0 ) :
               mc.setBlock ( gdje , 50 , 5 )
            """
#            if ( dZ ==   0 ) and baklje == "da":
#               mc.setBlock ( gdje , 50 , 5 )

   #mc.postToChat("KRAJ !!"  )
             
   return 1

def filter2 ( origin , polozaj , smjer ,  visina = 7 ,   sirina = 10 , dubina = 10, baklje="ne") :
   """
   ispred lika cisti kvadratasto podrucje
   1. parametar lista sa koordinatama ( X , Y , Z )
   2. parametar lista sa koordinatama ( X , Y , Z )
   3. apsolutni smjer crtanja
   4. broj terasa
   5. dubina terase
   6. sirina terase
   """
   zaMaknuti = [ SANDSTONE.id , SAND.id , STONE.id , DIRT.id , GRAVEL.id , GRASS.id , GRASS_TALL.id , COBBLESTONE.id , WATER_FLOWING.id , WATER_STATIONARY.id , LAVA_FLOWING.id , LAVA_STATIONARY.id , 17 , 162 ] # 17 , 162 wood
   zaMaknutiOpasno = [ WATER_FLOWING.id , WATER_STATIONARY.id , LAVA_FLOWING.id , LAVA_STATIONARY.id , SAND.id , GRAVEL.id ] # Dodani shljunak i pjesak jer padanja sve poremete
   od = rel2abs ( origin , polozaj , smjer ) 
   for dY in range ( 0 , ( visina - 2 ) , -1 ) : # ozgora prema dolje
      mc.postToChat("dY: %f" % ( dY ) )
      for dX in range ( 1 + dubina , 0 , -1 ) : # sprijeda prema nazad
         mc.postToChat("dX: %f" % ( dX ) )
         for dZ in range ( -1 - sirina , sirina + 2 ) : #slijeva nadesno
            #gdjeX , gdjeY , gdjeZ = rel2abs ( inPoz ,  ( dX , dZ , dY )  , smjer  ) 
            gdje = rel2abs ( origin ,  ( dX , dZ , dY )  , smjer  ) # hodalica
            kojiBlok = mc.getBlock ( gdje ) # koji blok je tu
            if ( dX == 1 + dubina ) or ( abs ( dZ ) > abs ( sirina ) ) or dY == visina :   #jeli prvi red ili krajnji lijevi ili krajnji desni blok ili "gornji" red
               # prvi je red -- mici opasno
               if kojiBlok in zaMaknutiOpasno :
                  mc.setBlock(gdje , STONE.id , 2 )	
            else :
               # ostali redovi -- filtriraj
               if kojiBlok in zaMaknuti :
                  mc.setBlock(gdje , AIR.id)			#postavi blok
            
            if (( dX ==  dubina ) or   (int ( dX ) % 5  == 0) ) and ( int ( dZ ) % 5 ) == 0 and baklje == "da":
               mc.setBlock ( gdje , 50 , 5 )
            """
            #  Za dugacke korake
            if ( int ( dZ ) % 10 ) == 0 and ( int ( dX - 1 ) % 10 == 0 ) :
               mc.setBlock ( gdje , 50 , 5 )
            """
#            if ( dZ ==   0 ) and baklje == "da":
#               mc.setBlock ( gdje , 50 , 5 )

   mc.postToChat("KRAJ !!"  )
                  
   return 1

def rupa2 ( origin , polozaj , smjer ,  visina = 7 ,   sirina = 10 , dubina = 10, baklje="ne") :
   """
   ispred lika kopa rupu u dubinu
   1. 
   2. 
   3. 
   4. koliko je rupa duboka - visina
   5. 
   6. 
   """
   zaMaknuti = [ SANDSTONE.id , SAND.id , STONE.id , DIRT.id , GRAVEL.id , GRASS.id , GRASS_TALL.id , COBBLESTONE.id , WATER_FLOWING.id , WATER_STATIONARY.id , LAVA_FLOWING.id , LAVA_STATIONARY.id , 17 , 162 ] # 17 , 162 wood
   zaMaknutiOpasno = [ WATER_FLOWING.id , WATER_STATIONARY.id , LAVA_FLOWING.id , LAVA_STATIONARY.id , SAND.id , GRAVEL.id ] # Dodani shljunak i pjesak jer padanja sve poremete
   od = rel2abs ( origin , polozaj , smjer ) 
   for dY in range ( 8 , ( visina - 2 ) , -1 ) : # ozgora prema dolje
      mc.postToChat("dY: %f" % ( dY ) )
      for dX in range ( 1 + dubina , 0 , -1 ) : # sprijeda prema nazad
         #mc.postToChat("dX: %f" % ( dX ) )
         for dZ in range ( -1 - sirina , sirina + 2 ) : #slijeva nadesno
            #gdjeX , gdjeY , gdjeZ = rel2abs ( inPoz ,  ( dX , dZ , dY )  , smjer  ) 
            gdje = rel2abs ( origin ,  ( dX , dZ , dY )  , smjer  ) # hodalica
            kojiBlok = mc.getBlock ( gdje ) # koji blok je tu
            if ( dX == 1 + dubina ) or ( abs ( dZ ) > abs ( sirina ) ) or dY == visina :   #jeli prvi red ili krajnji lijevi ili krajnji desni blok ili "gornji" red
               # prvi je red -- mici opasno
               if kojiBlok in zaMaknutiOpasno :
                  mc.setBlock(gdje , STONE.id , 2 )	
            else :
               # ostali redovi -- filtriraj
               mc.setBlock(gdje , AIR.id)			#chisti rupu
                  
            

   mc.postToChat("KRAJ !!"  )
                  
   return 1

def crtanje_stepenastiTunel ( orUlazni  , smjer ,  visina=3 , sirina = 5 , duzina = 10  , uspon = 0 ):
   """
   ispred polukruzni tunel  
   iX, - relativni pomak po X
   iZ, - relativni pomak po Z
   iY , - relativni pomak po Y
   sirina - sirina tunela default 5.0 
   duzina - duzina tunela default 5, 
   uspon - korekcija smjera koliko gore dolje  default  0
   """
   #gdje sam
 

   dYmodifikator = 0.0     # pocetna vrijednost promjene visine
   for dX in  range( 1 , duzina + 1 ) :    		# prodji cijeli pravokutnik
      for dZ  in  range ( - sirina , sirina + 1 ) : 
         for dY in  range ( 0 , visina ) :     
            gdje = rel2abs ( orUlazni ,  ( dX , dZ , dY + dYmodifikator )  , smjer  )  #relativne koordinate u apsolutne worlda
            mc.setBlock(gdje , AIR.id , 0 )			#postavi blok
      dYmodifikator += uspon
   return 1   
   
def crtaj_terase ( origin ,   smjer , iX = 0  , iZ = 0  , iY = 0 ,  visina = 7 ,  korak = 1 , sirina = 10 , baklje="ne") :
   """
   ispred lika cisti terasasto podrucje
   1. parametar lista sa koordinatama ( X , Y , Z )
   2. parametar lista sa koordinatama ( X , Y , Z )
   3. apsolutni smjer crtanja
   4. broj terasa
   5. dubina terase
   6. sirina terase
   """
   zaMaknuti = [ SANDSTONE.id , SAND.id , STONE.id , DIRT.id , GRAVEL.id , GRASS.id , GRASS_TALL.id , COBBLESTONE.id , WATER_FLOWING.id , WATER_STATIONARY.id , LAVA_FLOWING.id , LAVA_STATIONARY.id , 17 , 162 ] # 17 , 162 wood
   zaMaknutiOpasno = [ WATER_FLOWING.id , WATER_STATIONARY.id , LAVA_FLOWING.id , LAVA_STATIONARY.id , SAND.id , GRAVEL.id ] # Dodani shljunak i pjesak jer padanja sve poremete
   origin  = premjesti_origin ( origin , iX , iZ , iY ,  smjer ) #mice ishodiste
   #od = rel2abs ( origin ,  smjer ) 
   for dY in range ( visina - 1, -1 , -1 ) : # ozgora prema dolje
      mc.postToChat("dY: %f" % ( dY ) )
      for dX in range ( 1 + korak * ( dY + 1 ) , 0 , -1 ) : # sprijeda prema nazad
         mc.postToChat("dX: %f" % ( dX ) )
         for dZ in range ( -1 - sirina , sirina + 2 ) : #slijeva nadesno
            #gdjeX , gdjeY , gdjeZ = rel2abs ( inPoz ,  ( dX , dZ , dY )  , smjer  ) 
            gdje = rel2abs ( origin ,  ( dX , dZ , dY )  , smjer  ) # hodalica
            kojiBlok = mc.getBlock ( gdje ) # koji blok je tu
            if ( dX == 1 + korak * ( dY + 1 ) ) or ( abs ( dZ ) > abs ( sirina ) ):   #jeli prvi red ili krajnji lijevi ili krajnji desni blok
               # prvi je red -- mici opasno
               if kojiBlok in zaMaknutiOpasno :
                  mc.setBlock(gdje , STONE.id , 2 )	
            else :
               # ostali redovi -- filtriraj
               if kojiBlok in zaMaknuti :
                  mc.setBlock(gdje , AIR.id)			#postavi blok
            
            if ( dX ==  korak * ( dY + 1 ) ) and ( int ( dZ ) % 10 ) == 0 and baklje == "da":
               mc.setBlock ( gdje , 50 , 5 )
            """
            #  Za dugacke korake
            if ( int ( dZ ) % 10 ) == 0 and ( int ( dX - 1 ) % 10 == 0 ) :
               mc.setBlock ( gdje , 50 , 5 )
            """
#            if ( dZ ==   0 ) and baklje == "da":
#               mc.setBlock ( gdje , 50 , 5 )

   mc.postToChat("KRAJ !!"  )
                  
   return 1
         



def crtaj_klopku   ( origin , polozaj , smjer , rel_smjer  , stanje="zatvoreno" , visina = "dolje" ,blok_id = 96    ) :
   """
   funkcija za trapdora
   1. parametar lista sa koordinatama ( X , Y , Z )
   2. parametar lista sa koordinatama ( X , Y , Z )
   3. apsolutni smjer crtanja
   4. relativni smjer crtanja "meni"  , "odmene" , "lijevo" , "desno"
   5. crta se otvoren ili zatvoren  [ "zatvoreno" , "otvoreno" ]
   6. crta se na dnu ili vrhu bloka [ "dolje" , "gore" ]

   na kraju rel_smjer 0 - premameni 1 - odmene 2 - lijevo 3 - desno
   kvaka moze biti kvaka = "lijevo" ili "desno"
   
   vrata imaju zadano u Minecraftu
   0: Facing west
   1: Facing north
   2: Facing east
   3: Facing south
   """
   
   lista_smjera = [ "meni"  , "odmene" , "lijevo" , "desno" ] # transformacija opisa u vrijednost u kojem smjeru "gleda"
   lista_stanja = [ "zatvoreno" , "otvoreno" ]
   lista_polozaja = [ "dolje" , "gore" ]     # na dnu ili vrhu bloka
   pomoc = lista_smjera.index ( rel_smjer )
   rel_smjer = pomoc
   
   tablica_smjera = {}     # definira se tablica prevoda
   tablica_smjera [ ( 1 , 0  ) ] = ( 2 , 3  , 0 , 1 ,  ) # gledam north
   tablica_smjera [ ( -1 , 0 ) ] = ( 3 , 2 , 1 , 0 ) # gledam south
   tablica_smjera [ ( 0 , 1 ) ] = ( 0  , 1 , 3 , 2 )  # gledam east
   tablica_smjera [ ( 0 , -1 ) ]= ( 1 , 0 , 2 , 3 )  # gledam weast
   
   buff = tablica_smjera [ ( smjer [ 0 ] , smjer [ 1 ] )   ]
   blok_dv =  buff [ rel_smjer ]
   od = rel2abs ( origin , polozaj , smjer )
   mc.setBlock (  od , blok_id , blok_dv  +  lista_stanja.index ( stanje ) * 4  + lista_polozaja.index ( visina ) * 8  )   #stavi trapdor 4-bit otvoreno zatvoreno, 8-mi bit gore dolje
   return
   
def crtaj_vrata ( origin , polozaj , smjer , rel_smjer  , blok_id = 64  , kvaka = "lijevo"  ) :
   """
   funkcija za crtanje vrata
   1. parametar lista sa koordinatama ( X , Y , Z )
   2. parametar lista sa koordinatama ( X , Y , Z )
   3. apsolutni smjer crtanja
   4. relativni smjer crtanja "meni"  , "odmene" , "lijevo" , "desno"
   5. tip vrata koja se crtaju 

   na kraju rel_smjer 0 - premameni 1 - odmene 2 - lijevo 3 - desno
   kvaka moze biti kvaka = "lijevo" ili "desno"
   
   vrata imaju zadano u Minecraftu
   0: Facing west
   1: Facing north
   2: Facing east
   3: Facing south
   """
   
   lista_smjera = [ "meni"  , "odmene" , "lijevo" , "desno" ] # transformacija opisa u vrijednost
   pomoc = lista_smjera.index ( rel_smjer )
   rel_smjer = pomoc
   
   tablica_smjera = {}     # definira se tablica prevoda
   tablica_smjera [ ( 1 , 0  ) ] = ( 0 , 2 , 1 , 3 ) # gledam north
   tablica_smjera [ ( -1 , 0 ) ] = ( 2 , 0 , 3 , 1 ) # gledam south
   tablica_smjera [ ( 0 , 1 ) ] = ( 1 , 3 , 2 , 0 )  # gledam east
   tablica_smjera [ ( 0 , -1 ) ]= ( 3 , 1 , 0 , 2 )  # gledam weast
   
   buff = tablica_smjera [ ( smjer [ 0 ] , smjer [ 1 ] )   ]
   blok_dv =  buff [ rel_smjer ]
   od = rel2abs ( origin , polozaj , smjer )
   mc.setBlock (  od , blok_id , blok_dv )   #doljnji dio vrata
   do = ( od [ 0 ] , od [ 1 ] +1  , od [ 2 ]  )
   blok_dv = 8
   if kvaka == "desno" :
      blok_dv = 8
   mc.setBlock (  do , blok_id , blok_dv )         #gornji dio vrata
   
   
def crtaj_repeater ( origin , poc , kraj , smjer , rel_smjer  = "meni" , blok_id = 93 , dv = 0 ) :
   """
   funkcija za crtanje stepenica
   1. parametar lista sa koordinatama ( X , Y , Z )
   2. parametar lista sa koordinatama ( X , Y , Z )
   3. parametar lista sa koordinatama ( X , Y , Z )
   4. smjer crtanja apsolutni
   5. gdje su okrenute 
   6. koji blok 
   7. stanje prekidaca
 
   stepenice se crtaju "u rupi"
   rel_smjer 0 - lijevo 1 - desno 2 - odmene 3 - meni
   
   stepenice imaju zadano u Minecraftu
   0: North
   1: East
   2: South
   3: west
   """
   
   lista_smjera = [   "meni",  "odmene"      ,"lijevo"     , "desno" ] # transformacija opisa u vrijednost
   pomoc = lista_smjera.index ( rel_smjer )
   rel_smjer = pomoc  
   
   tablica_smjera = {}     # definira se tablica prevoda
   tablica_smjera [ ( 1 , 0  ) ] = (  3 , 1 , 0 , 2  ) # gledam north
   tablica_smjera [ ( -1 , 0 ) ] = (  1 , 3 , 2 , 0 ) # gledam south
   tablica_smjera [ ( 0 , 1 ) ] = ( 0 , 2 , 1 , 3 )  # gledam east
   tablica_smjera [ ( 0 , -1 ) ]= ( 2 , 0 , 3 , 1  )  # gledam weast
   
   buff = tablica_smjera [ ( smjer [ 0 ] , smjer [ 1 ] )   ]
   blok_dv =  buff [ rel_smjer ] + dv
   od = rel2abs ( origin , poc , smjer )
   do = rel2abs ( origin , kraj , smjer )
   mc.setBlocks ( od , do , blok_id , blok_dv )
   return

def crtaj_comparator ( origin , poc , kraj , smjer , rel_smjer  = "meni" , blok_id = 149 , dv = 0 ) :
   """
   funkcija za crtanje stepenica
   1. parametar lista sa koordinatama ( X , Y , Z )
   2. parametar lista sa koordinatama ( X , Y , Z )
   3. parametar lista sa koordinatama ( X , Y , Z )
   4. smjer crtanja apsolutni
   5. gdje su okrenute 
   6. koji blok 
   7. stanje prekidaca
 
   stepenice se crtaju "u rupi"
   rel_smjer 0 - lijevo 1 - desno 2 - odmene 3 - meni
   
   stepenice imaju zadano u Minecraftu
   0: North
   1: East
   2: South
   3: west
   """
   
   lista_smjera = [   "meni",  "odmene"      ,"lijevo"     , "desno" ] # transformacija opisa u vrijednost
   pomoc = lista_smjera.index ( rel_smjer )
   rel_smjer = pomoc  
   
   tablica_smjera = {}     # definira se tablica prevoda
   tablica_smjera [ ( 1 , 0  ) ] = (  1 , 3 , 2 , 0 ) # gledam north
   tablica_smjera [ ( -1 , 0 ) ] = (  3 , 1 , 0 , 2  ) # gledam south
   tablica_smjera [ ( 0 , 1 ) ] = ( 2 , 0 , 3 , 1 )  # gledam east
   tablica_smjera [ ( 0 , -1 ) ]= ( 0 , 2 , 1 , 3  )  # gledam weast
   
   buff = tablica_smjera [ ( smjer [ 0 ] , smjer [ 1 ] )   ]
   blok_dv =  buff [ rel_smjer ] + 2
   od = rel2abs ( origin , poc , smjer )
   do = rel2abs ( origin , kraj , smjer )
   mc.setBlocks ( od , do , blok_id , blok_dv )
   return



def crtaj_vrataograde ( origin , poc ,  smjer ,  rel_smjer  , blok_id = 107    ) :
   """
   funkcija za crtanje vrata ograde
   1. parametar lista sa koordinatama ( X , Y , Z )
   2. parametar lista sa koordinatama ( X , Y , Z )
   3. smjer crtanja apsolutni
   4. smjer crtanja relativni
   5. koji blok ( 107 ili 162) prva ili druga grupa 

   rel_smjer 0 - lijevo/desno 1 - napred/nazad
  
   vrata ograde  imaju zadano u Minecraftu
    3. i 4 bit
   0: Facing south
   1: Facing west
   2: Facing north
   3: Facing east
   """   
   
   lista_smjera = [ "lijevo_desno" , "naprijed_nazad" ] # transformacija opisa u vrijednost
   pomoc = lista_smjera.index ( rel_smjer )
   rel_smjer = pomoc   
   
   tablica_smjera = {}     # definira se tablica prevoda
   tablica_smjera [ ( 1 , 0  ) ] = ( 1  , 0 ) # gledam north
   tablica_smjera [ ( -1 , 0 ) ] = (  1 , 0 ) # gledam south
   tablica_smjera [ ( 0 , 1 ) ] = ( 0 , 1 )  # gledam east
   tablica_smjera [ ( 0 , -1 ) ]= ( 0 , 1 )  # gledam weast
   
   buff = tablica_smjera [ ( smjer [ 0 ] , smjer [ 1 ] )   ]
   blok_dv =  buff [ rel_smjer ] 
 
   od = rel2abs ( origin , poc , smjer )
   mc.setBlocks ( od , od , blok_id , blok_dv )


def crtaj_deblo ( origin , poc , kraj , smjer , rel_smjer , blok_id = 17 , podtip = 0   ) :
   """
   funkcija za crtanje debla
   1. parametar lista sa koordinatama ( X , Y , Z )
   2. parametar lista sa koordinatama ( X , Y , Z )
   3. parametar lista sa koordinatama ( X , Y , Z )
   4. smjer crtanja apsolutni
   5. smjer crtanja relativni 
   6. koji blok ( 17 ili 162) prva ili druga grupa 
   7. koji podtip debla
 
   rel_smjer 0 - gore/dolje 1 - lijev/desno 2 - napred/nazad
  
   debla imaju zadano u Minecraftu
    3. i 4 bit
    0:    Facing Up/Down
    1:    Facing East/West
    2:    Facing North/South
    3:    Only bark
   """   
   
   lista_smjera = [ "gore", "lijevo_desno" , "naprijed_nazad" ] # transformacija opisa u vrijednost
   pomoc = lista_smjera.index ( rel_smjer )
   rel_smjer = pomoc  
   
   tablica_smjera = {}     # definira se tablica prevoda
   tablica_smjera [ ( 1 , 0  ) ] = (  0 , 8 , 4 ) # gledam north
   tablica_smjera [ ( -1 , 0 ) ] = (  0 , 8 , 4 ) # gledam south
   tablica_smjera [ ( 0 , 1 ) ] = ( 0 , 4 , 8 )  # gledam east
   tablica_smjera [ ( 0 , -1 ) ]= ( 0 , 4 , 8 )  # gledam weast
   
   buff = tablica_smjera [ ( smjer [ 0 ] , smjer [ 1 ] )   ]
   blok_dv =  buff [ rel_smjer ] + podtip
 
   od = rel2abs ( origin , poc , smjer )
   do = rel2abs ( origin , kraj , smjer )
   mc.setBlocks ( od , do , blok_id , blok_dv )

   
def crtaj_dropper    ( origin , poc , kraj , smjer ,  rel_smjer , blok_id = 158 , blok_dv = 0 ) :
   crtaj_dispenser    ( origin , poc , kraj , smjer ,  rel_smjer , blok_id = 158 , blok_dv = 0 )


def crtaj_sticky_piston    ( origin , poc , kraj , smjer ,  rel_smjer , blok_id = 23 , blok_dv = 0 ) :
   crtaj_piston    ( origin , poc , kraj , smjer ,  rel_smjer , blok_id = 29 , blok_dv = 0 )
   return 1
   
   
def  crtaj_button ( origin , poc , kraj , smjer ,  rel_smjer , blok_id = 77 , blok_dv = 0 ) :
   """
   funkcija za crtanje dispensera
   1. parametar lista sa koordinatama ( X , Y , Z )
   2. parametar lista sa koordinatama ( X , Y , Z )
   3. smjer crtanja apsolutni
   4. gdje su okrenute 
   5. blok_id  , 33 standardni , 29 -sticky

   
   """
   lista_smjera = [ "dolje", "gore" , "desno" , "lijevo" , "meni"  , "odmene"   ] # transformacija opisa u vrijednost
   pomoc = lista_smjera.index ( rel_smjer )
   rel_smjer = pomoc  
   
   tablica_smjera = {}     # definira se tablica prevoda
   tablica_smjera [ ( 1 , 0  ) ] = ( 5 , 0  , 3 , 4 , 1 , 2  ) # gledam north
   tablica_smjera [ ( -1 , 0 ) ] = ( 5 , 0 ,  4 , 3 , 1 , 2  ) # gledam south
   tablica_smjera [ ( 0 , 1 ) ] = ( 5 , 0 , 2 , 1 , 3 , 4   )  # gledam east
   tablica_smjera [ ( 0 , -1 ) ]= ( 5 , 0 , 1 , 2 , 3 , 4  )  # gledam weast
   
   buff = tablica_smjera [ ( smjer [ 0 ] , smjer [ 1 ] )   ]
   blok_dv =  buff [ rel_smjer ]
   od = rel2abs ( origin , poc , smjer )
   do = rel2abs ( origin , kraj , smjer )
   mc.setBlocks ( od , do , blok_id , blok_dv  )
   
def  crtaj_piston ( origin , poc , kraj , smjer ,  rel_smjer , blok_id = 33 , blok_dv = 0 ) :
   """
   funkcija za crtanje dispensera
   1. parametar lista sa koordinatama ( X , Y , Z )
   2. parametar lista sa koordinatama ( X , Y , Z )
   3. smjer crtanja apsolutni
   4. gdje su okrenute 
   5. blok_id  , 33 standardni , 29 -sticky

   
   """
   lista_smjera = [ "dolje", "gore" , "desno" , "lijevo" , "meni"  , "odmene"   ] # transformacija opisa u vrijednost
   pomoc = lista_smjera.index ( rel_smjer )
   rel_smjer = pomoc  
   
   tablica_smjera = {}     # definira se tablica prevoda
   tablica_smjera [ ( 1 , 0  ) ] = ( 0 , 1 , 3 , 2 , 4 , 5   ) # gledam north
   tablica_smjera [ ( -1 , 0 ) ] = ( 0 , 1 ,  2 , 3 , 5 , 4  ) # gledam south
   tablica_smjera [ ( 0 , 1 ) ] = ( 0 , 1 ,  4 , 5 , 2 , 3   )  # gledam east
   tablica_smjera [ ( 0 , -1 ) ]= ( 0 , 1 ,  5 , 4 , 3 , 2  )  # gledam weast
   
   buff = tablica_smjera [ ( smjer [ 0 ] , smjer [ 1 ] )   ]
   blok_dv =  buff [ rel_smjer ]
   od = rel2abs ( origin , poc , smjer )
   do = rel2abs ( origin , kraj , smjer )
   mc.setBlocks ( od , do , blok_id , blok_dv  )

   
   
def crtaj_dispenser    ( origin , poc , kraj , smjer ,  rel_smjer , blok_id = 23 , blok_dv = 0 ) :
   """
   funkcija za crtanje dispensera
   1. parametar lista sa koordinatama ( X , Y , Z )
   2. parametar lista sa koordinatama ( X , Y , Z )
   3. smjer crtanja apsolutni
   4. gdje su okrenute 

   
   """
   lista_smjera = [ "dolje", "gore" , "desno" , "lijevo" , "meni"  , "odmene"   ] # transformacija opisa u vrijednost
   pomoc = lista_smjera.index ( rel_smjer )
   rel_smjer = pomoc  
   
   tablica_smjera = {}     # definira se tablica prevoda
   tablica_smjera [ ( 1 , 0  ) ] = ( 0 , 1 , 3 , 2 , 4 , 5   ) # gledam north
   tablica_smjera [ ( -1 , 0 ) ] = ( 0 , 1 ,  2 , 3 , 5 , 4  ) # gledam south
   tablica_smjera [ ( 0 , 1 ) ] = ( 0 , 1 ,  4 , 5 , 2 , 3   )  # gledam east
   tablica_smjera [ ( 0 , -1 ) ]= ( 0 , 1 ,  5 , 4 , 3 , 2  )  # gledam weast
   
   buff = tablica_smjera [ ( smjer [ 0 ] , smjer [ 1 ] )   ]
   blok_dv =  buff [ rel_smjer ]
   od = rel2abs ( origin , poc , smjer )
   do = rel2abs ( origin , kraj , smjer )
   mc.setBlocks ( od , do , blok_id , blok_dv  )
   
def smjer_hoppera ( smjer ,  rel_smjer) :
   lista_smjera = [ "dolje", "nista" , "desno" , "lijevo" , "meni"  , "odmene"   ] # transformacija opisa u vrijednost
   pomoc = lista_smjera.index ( rel_smjer )
   rel_smjer = pomoc  
   
   tablica_smjera = {}     # definira se tablica prevoda
   tablica_smjera [ ( 1 , 0  ) ] = ( 0 , 0 , 3 , 2 , 4 , 5   ) # gledam north
   tablica_smjera [ ( -1 , 0 ) ] = ( 0 , 0 ,  2 , 3 , 5 , 4  ) # gledam south
   tablica_smjera [ ( 0 , 1 ) ] = ( 0 , 0 ,  4 , 5 , 2 , 3   )  # gledam east
   tablica_smjera [ ( 0 , -1 ) ]= ( 0 , 0 ,  5 , 4 , 3 , 2  )  # gledam weast
   
   buff = tablica_smjera [ ( smjer [ 0 ] , smjer [ 1 ] )   ]
   blok_dv =  buff [ rel_smjer ]
   return blok_dv
   
def crtaj_hopper    ( origin , poc , kraj , smjer ,  rel_smjer , blok_id = 154 , blok_dv = 0 ) :
   """
   funkcija za crtanje hoppera
   1. parametar lista sa koordinatama ( X , Y , Z )
   2. parametar lista sa koordinatama ( X , Y , Z )
   3. smjer crtanja apsolutni
   4. gdje su okrenute 

   rel_smjer 0 - desno 1 - lijevo 2 - prema 3 - odmene  4 - gore  pokazuje smjer u kojem baklja "gleda"

   stepenice imaju zadano u Minecraftu
   0: Facing north.
   1: Facing south.
   2: Facing east.
   3: Facing west.
   5: up
   """
   lista_smjera = [ "dolje", "nista" , "desno" , "lijevo" , "meni"  , "odmene"   ] # transformacija opisa u vrijednost
   pomoc = lista_smjera.index ( rel_smjer )
   rel_smjer = pomoc  
   
   tablica_smjera = {}     # definira se tablica prevoda
   tablica_smjera [ ( 1 , 0  ) ] = ( 0 , 0 , 3 , 2 , 4 , 5   ) # gledam north
   tablica_smjera [ ( -1 , 0 ) ] = ( 0 , 0 ,  2 , 3 , 5 , 4  ) # gledam south
   tablica_smjera [ ( 0 , 1 ) ] = ( 0 , 0 ,  4 , 5 , 2 , 3   )  # gledam east
   tablica_smjera [ ( 0 , -1 ) ]= ( 0 , 0 ,  5 , 4 , 3 , 2  )  # gledam weast
   
   buff = tablica_smjera [ ( smjer [ 0 ] , smjer [ 1 ] )   ]
   blok_dv =  buff [ rel_smjer ]
   od = rel2abs ( origin , poc , smjer )
   do = rel2abs ( origin , kraj , smjer )
   mc.setBlocks ( od , do , blok_id , blok_dv  )
   

def crtaj_baklju ( origin , poc ,  smjer ,  rel_smjer   ) :
   """
   funkcija za crtanje stepenica
   1. parametar lista sa koordinatama ( X , Y , Z )
   2. parametar lista sa koordinatama ( X , Y , Z )
   4. smjer crtanja apsolutni
   6. gdje su okrenute 

   rel_smjer 0 - desno 1 - lijevo 2 - prema 3 - odmene  4 - gore  pokazuje smjer u kojem baklja "gleda"

   stepenice imaju zadano u Minecraftu
   0: Facing north.
   1: Facing east.
   2: Facing south.
   3: Facing west.
   5: up
   """
   lista_smjera = [  "desno" , "lijevo" , "meni"  , "odmene" , "gore" ] # transformacija opisa u vrijednost
   pomoc = lista_smjera.index ( rel_smjer )
   rel_smjer = pomoc  
   
   tablica_smjera = {}     # definira se tablica prevoda
   tablica_smjera [ ( 1 , 0  ) ] = (  3 , 4 , 2 , 1 , 5 ) # gledam north
   tablica_smjera [ ( -1 , 0 ) ] = (  4 , 3 , 1 , 2 , 5 ) # gledam south
   tablica_smjera [ ( 0 , 1 ) ] = (  2 , 1 , 4 , 3  ,5 )  # gledam east
   tablica_smjera [ ( 0 , -1 ) ]= (  1 , 2 , 3 , 4 , 5 )  # gledam weast
   
   buff = tablica_smjera [ ( smjer [ 0 ] , smjer [ 1 ] )   ]
   blok_dv =  buff [ rel_smjer ]
   od = rel2abs ( origin , poc , smjer )
   mc.setBlocks ( od , od , 50 , blok_dv )
   return

def crtaj_redstonetorch ( origin , poc ,  smjer ,  rel_smjer   ) :
   """
   funkcija za crtanje stepenica
   1. parametar lista sa koordinatama ( X , Y , Z )
   2. parametar lista sa koordinatama ( X , Y , Z )
   4. smjer crtanja apsolutni
   6. gdje su okrenute 

   rel_smjer 0 - desno 1 - lijevo 2 - prema 3 - odmene  4 - gore  pokazuje smjer u kojem baklja "gleda"

   stepenice imaju zadano u Minecraftu
   0: Facing north.
   1: Facing east.
   2: Facing south.
   3: Facing west.
   5: up
   """
   lista_smjera = [  "desno" , "lijevo" , "meni"  , "odmene" , "gore" ] # transformacija opisa u vrijednost
   pomoc = lista_smjera.index ( rel_smjer )
   rel_smjer = pomoc  
   
   tablica_smjera = {}     # definira se tablica prevoda
   tablica_smjera [ ( 1 , 0  ) ] = (  3 , 4 , 2 , 1 , 5 ) # gledam north
   tablica_smjera [ ( -1 , 0 ) ] = (  4 , 3 , 1 , 2 , 5 ) # gledam south
   tablica_smjera [ ( 0 , 1 ) ] = (  2 , 1 , 4 , 3  ,5 )  # gledam east
   tablica_smjera [ ( 0 , -1 ) ]= (  1 , 2 , 3 , 4 , 5 )  # gledam weast
   
   buff = tablica_smjera [ ( smjer [ 0 ] , smjer [ 1 ] )   ]
   blok_dv =  buff [ rel_smjer ]
   od = rel2abs ( origin , poc , smjer )
   mc.setBlocks ( od , od , 76 , blok_dv )
   return
   
   
def crtaj_banak ( origin , poc , kraj , smjer , rel_smjer  = "meni" , blok_id = 58     ) :
   crtaj_ljestve  ( origin , poc , kraj , smjer , rel_smjer   , blok_id    )
   
   
def crtaj_kutiju ( origin , poc , kraj , smjer , rel_smjer  = "meni" , blok_id = 54     ) :
   crtaj_pec  ( origin , poc , kraj , smjer , rel_smjer   , blok_id    )
   
def crtaj_pec   ( origin , poc , kraj , smjer , rel_smjer  = "meni" , blok_id = 61    ) :
   if rel_smjer  ==  "meni" :
      rel_smjer  = "odmene"
   elif rel_smjer  ==  "odmene" :
      rel_smjer  = "meni"
   """
   elif rel_smjer  ==  "lijevo" :
      rel_smjer  = "desno"
   elif rel_smjer  ==  "desno" :
      rel_smjer  = "lijevo"
   """

 
   crtaj_ljestve  ( origin , poc , kraj , smjer , rel_smjer   , blok_id    )

def crtaj_krevet  ( origin , noge , glava  , smjer , rel_smjer = "odmene",   blok_id = 26  , blok_dv = 0  ) :
   """
   funkcija za crtanje stepenica
   1. parametar lista sa koordinatama ( X , Y , Z )
   3. parametar lista sa koordinatama ( X , Y , Z )
   4. smjer crtanja apsolutni
   5. gdje su okrenute 
   6. koji blok 
 
   rel_smjer 0 - lijevo 1 - desno 2 - odmene 3 - meni
   
   krevet  imaju zadano u Minecraftu
   dv = 0 za nizi dio
   dv = 8 za jastuk
   """
   lista_smjera = [   "meni",  "odmene"      ,"lijevo"     , "desno" ] # transformacija opisa u vrijednost
   pomoc = lista_smjera.index ( rel_smjer )
   rel_smjer = pomoc  
   
   tablica_smjera = {}     # definira se tablica prevoda
   tablica_smjera [ ( 1 , 0  ) ] = (  1 , 3 , 2 , 0 ) # gledam north
   tablica_smjera [ ( -1 , 0 ) ] = (  3 , 1 , 0 , 2  ) # gledam south
   tablica_smjera [ ( 0 , 1 ) ] = ( 2 , 0 , 3 , 1 )  # gledam east
   tablica_smjera [ ( 0 , -1 ) ]= ( 0 , 2  , 1 , 3  )  # gledam weast
   
   buff = tablica_smjera [ ( smjer [ 0 ] , smjer [ 1 ] )   ]
   blok_dv =  buff [ rel_smjer ]
   
   od = rel2abs ( origin , noge , smjer )
   mc.setBlock (  od , blok_id , blok_dv )   #doljnji dio vrata
   do = rel2abs ( origin , glava , smjer )
   mc.setBlock (  do , blok_id , blok_dv + 8 )   #doljnji dio vrata
   return
   
   
def crtaj_ljestve  ( origin , poc , kraj , smjer , rel_smjer  = "meni" , blok_id = 65    ) :
   """
   funkcija za crtanje stepenica
   1. parametar lista sa koordinatama ( X , Y , Z )
   2. parametar lista sa koordinatama ( X , Y , Z )
   3. parametar lista sa koordinatama ( X , Y , Z )
   4. smjer crtanja apsolutni
   5. gdje su okrenute 
   6. koji blok 
 
   stepenice se crtaju "u rupi"
   rel_smjer 0 - lijevo 1 - desno 2 - odmene 3 - meni
   
   stepenice imaju zadano u Minecraftu
   0: East
   1: West
   2: South
   3: North
   """
   
   lista_smjera = [   "meni",  "odmene"      ,"lijevo"     , "desno" ] # transformacija opisa u vrijednost
   pomoc = lista_smjera.index ( rel_smjer )
   rel_smjer = pomoc  
   
   tablica_smjera = {}     # definira se tablica prevoda
   tablica_smjera [ ( 1 , 0  ) ] = (  3 , 2 , 1 , 0 ) # gledam north
   tablica_smjera [ ( -1 , 0 ) ] = (  2 , 3 , 0 , 1  ) # gledam south
   tablica_smjera [ ( 0 , 1 ) ] = ( 1 , 0 , 2 , 3 )  # gledam east
   tablica_smjera [ ( 0 , -1 ) ]= ( 0 , 1 , 3 , 2  )  # gledam weast
   
   buff = tablica_smjera [ ( smjer [ 0 ] , smjer [ 1 ] )   ]
   blok_dv =  buff [ rel_smjer ] + 2
   od = rel2abs ( origin , poc , smjer )
   do = rel2abs ( origin , kraj , smjer )
   mc.setBlocks ( od , do , blok_id , blok_dv )
   return

   
def crtaj_stepenice ( origin , poc , kraj , smjer , blok_id = 53 , rel_smjer  = "meni " , gore_dolje = "ne"  ) :
   """
   funkcija za crtanje stepenica
   1. parametar lista sa koordinatama ( X , Y , Z )
   2. parametar lista sa koordinatama ( X , Y , Z )
   3. parametar lista sa koordinatama ( X , Y , Z )
   4. smjer crtanja apsolutni
   5. koji blok 
   6. gdje su okrenute 
   7. naopravo ili naopako
   
   gore_dolje = 4 stepenice su "naopako"
   rel_smjer 0 - lijevo 1 - desno 2 - odmene 3 - prema
   
   stepenice imaju zadano u Minecraftu
   0: East
   1: West
   2: South
   3: North
   """
   lista_smjera = [  "lijevo" , "desno" ,  "odmene" , "meni"   ] # transformacija opisa u vrijednost
   pomoc = lista_smjera.index ( rel_smjer )
   rel_smjer = pomoc  
   
   tablica_smjera = {}     # definira se tablica prevoda
   tablica_smjera [ ( 1 , 0  ) ] = ( 2 , 3 , 1 , 0 ) # gledam north
   tablica_smjera [ ( -1 , 0 ) ] = ( 3 , 2 , 0 , 1 ) # gledam south
   tablica_smjera [ ( 0 , 1 ) ] = ( 1 , 0 , 3 , 2 )  # gledam east
   tablica_smjera [ ( 0 , -1 ) ]= ( 0 , 1 , 2 , 3 )  # gledam weast
   
   buff = tablica_smjera [ ( smjer [ 0 ] , smjer [ 1 ] )   ]
   blok_dv =  buff [ rel_smjer ]
   if gore_dolje != "ne" :
      blok_dv +=  4  # okreni naopako ako treba
   od = rel2abs ( origin , poc , smjer )
   do = rel2abs ( origin , kraj , smjer )
   mc.setBlocks ( od , do , blok_id , blok_dv )
   return

def crtaj_redstonedust ( origin , poc  , kraj , smjer ) :
   crtaj_kvadar ( origin , poc  , kraj , smjer , 55 , blok_dv = 0 )
   
def crtaj_kvadar ( origin , poc  , kraj , smjer , blok_id , blok_dv = 0 ) :
   """
   funkcija za crtanje tocke
   1. parametar lista sa koordinatama ( X , Z , Y )
   2. parametar lista sa koordinatama ( X , Z , Y )
   3. parametar lista sa koordinatama ( X , Z , Y )
   4. smjer crtanja
   3. koji blok 
   4. koja varijanta bloka DFAULT osnovni oblik
   
   
   """
   od = rel2abs ( origin , poc , smjer )
   do = rel2abs ( origin , kraj , smjer )
   mc.setBlocks ( od , do , blok_id , blok_dv )
   return

   
   
def gdjeSam ():
   """
   odredjuje trenutnu poziciju lika i vraca je u listi:
   1. X
   2. Z
   3. Y
   formatirano za rel2abs
   """
   
   #gdje sam detaljno
   radnaPozicija = mc.player.getPos()	
   return (  [radnaPozicija.x , radnaPozicija.z , radnaPozicija.y  ] )

   
def gdjeGledam () :
   """
   odredjuje trenutni smjer lika i vraca ga u listi:
   1. Vx
   2. Vz
   formatirano za rel2abs
   """
   
   smjerRada = mc.player.getDirection ()			#uzmem kamo gledam
   #smjer gledanja radi preglednosti spremimo u "vektor""
   Vx=0												#pocetne vrijednosti su nule
   Vz=0
   if abs (smjerRada.x) > abs (smjerRada.z): 		#nadje se dominanti smjer i spremi u vektor
      Vx=round(smjerRada.x)
   else:
      Vz=round(smjerRada.z)   
   return ( [Vx , Vz] )

   
def makeVillager (orMj , dX , dZ , dY ,  orSm ,  Profession = 0 , Career = 1):
   sto =  '{Profession:%s,Career:%s}' % ( int ( Profession ) , int ( Career )  )
   gdje = rel2abs ( orMj , (  dX , dZ , dY )   , orSm  )
   id = mc.spawnEntity('Villager',  int (gdje [0])  ,int (gdje [1]) ,int (gdje [2]) , sto) 

def makeFarmer (orMj , dX , dZ , dY ,  orSm ,  Profession = 0 , Career = 1):
   makeVillager (orMj , dX , dZ , dY ,  orSm ,  Profession = Profession , Career = Career) 

def makeLibrarian (orMj , dX , dZ , dY ,  orSm ,  Profession = 1 , Career = 1):
   makeVillager (orMj , dX , dZ , dY ,  orSm ,  Profession = Profession , Career = Career) 

def makePriest (orMj , dX , dZ , dY ,  orSm ,  Profession = 2 , Career = 1):
   makeVillager (orMj , dX , dZ , dY ,  orSm ,  Profession = Profession , Career = Career) 

def makeBlacksmith (orMj , dX , dZ , dY ,  orSm ,  Profession = 3 , Career = 1):
   makeVillager (orMj , dX , dZ , dY ,  orSm ,  Profession = Profession , Career = Career) 

def makeButcher (orMj , dX , dZ , dY ,  orSm ,  Profession = 4 , Career = 1):
   makeVillager (orMj , dX , dZ , dY ,  orSm ,  Profession = Profession , Career = Career) 


   
   
# punjenje kutija za iskop programe

def obradi_kutiju ( uJednaKutija, uBrojKutija, orMj, orSm):
    #mc.postToChat("%s . kutija: %s " % (uBrojKutija, uJednaKutija))
    sadrzaj = list ()
    sadrzaj=""
    sadrzaj += '{Items:[' 
    sadrzaj += uJednaKutija
    sadrzaj += '],id:"minecraft:chest",Lock:"",}'
    orMj = gdjeSam()
    orSm = gdjeGledam()
    polozaj = rel2abs ( orMj , ( -2 - 2 * uBrojKutija , 0 , 0  ) , orSm )
    mc.setBlockWithNBT(polozaj,54,1, sadrzaj )
    
    
#pripremaju se NBT-i za generiranje kutija        
    
def slozi_NBT_za_kutije ( orMj, orSm , popis )    : 

    # slaze stringove
    jednaKutija = ''
    brojKutija = 0
    brojalica = 0
    mali_string = "" #jedan element
    for bla in popis.keys():
        blok = bla[0]
        modifikacija = bla[1]
        # prijevodi:
        # diamond
        # 56 : 264,
        if bla[0] == 56:
            blok = 264
        # redstone
        # 73 : 331 ,
        if bla[0] == 73:
            blok = 331
        # lapis
        # 21 : 351 , 4
        if bla[0] == 21:
            blok = 351
            modifikacija = 4
        # emerald
        # 129 :  388
        if bla[0] == 129:
            blok = 388
            # coal COAL_ORE.id  263
        if bla[0] == COAL_ORE.id:
            blok = 263
            modifikacija = 0

        if bla[0] == 153:   #nether quartz
            blok = 406
            modifikacija = 0
        # cobweb
        if bla[0] == 30:
            blok = 287
            modifikacija = 0            
        # rail
        if bla[0] == 66:
            blok = 66
            modifikacija = 0   
            
        while popis[bla] > 0:
            if popis[bla] > 64:
                count = 64
            else:
                count = popis[bla]
            popis[bla] -= 64

            #ovo trebamo dobiti 2:{Slot:2b,id:"3",Count:64b,Damage:0s,},
            mali_string = '{Slot:%sb,id:"%s",Count:%sb,Damage:%ss,},' % ( brojalica, blok, count, modifikacija )
            nesto = jednaKutija
            jednaKutija= nesto + mali_string
            brojalica += 1
            if brojalica > 25:
                obradi_kutiju (  jednaKutija, brojKutija, orMj, orSm ) 
                brojalica = 0
                jednaKutija = ""
                brojKutija += 1

    obradi_kutiju( jednaKutija, brojKutija, orMj, orSm) 

 