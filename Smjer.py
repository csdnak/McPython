# napravi crtu u zemlji u smjeru u kojem gleda

#uvod
from mc import * # ajmo probati ovaj import
mc = Minecraft()

#gdje sam
radnaPozicija = mc.player.getPos()		

#kamo gledam
smjerRada = mc.player.getDirection ()	#uzmem kamo gledam
smjerRada.y = radnaPozicija.y - 1		#radimo na levelu ispod

#smjer gledanja radi preglednosti spremimo u "vektor""
yLevelRada=smjerRada.y
Vx=0	#pocetne vrijednosti su nule
Vz=0
if abs (smjerRada.x) > abs (smjerRada.z): 	#nadje se dominanti smjer i spremi u vektor
   Vx=round(smjerRada.x)
else:
   Vz=round(smjerRada.z)

#crtaj liniju
if  abs ( Vx )  != abs ( Vz ) :		# ne pod 45
   for brojalica in range(1,15) :    # 15 duzina
      gdjex=radnaPozicija.x + Vx*brojalica + Vx*0    # pomak po x
      gdjez=radnaPozicija.z + Vz*0 + Vz*brojalica	# pomak po y
      #mc.postToChat("gdjex: %f gdjez: %f brojalica %f" % ( gdjex , gdjez , brojalica) )
      mc.setBlock(gdjex , smjerRada.y , gdjez , GOLD_BLOCK)		#postavi blok

