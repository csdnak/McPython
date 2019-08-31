#ispred lika blok zadanih dimenzija i vrste - OBSOLETE

from mc import * #import api-ja
mc = Minecraft() #inicijalizacija sustava za rad sa Minecraftom

def crtaj_blok (X1,Y1,Z1,X2,Y2,Z2,koji_blok,dv=0):
   """
   funkcija za crtanje bloka neposredno ispred lika
   X1,Y1,Z1 - od
   X2,Y2,Z2 - do
   koji_blok - koji blok
   dv - data value za blok, default zrak
   """
   #gdje sam
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

      gdjeX1=radnaPozicija.x + Vx*X1 - Vz*Z1    # modificiraj pocetnu koordinatu
      gdjeY1=radnaPozicija.y + Y1
      gdjeZ1=radnaPozicija.z + Vx*Z1 + Vz*X1
   
      gdjeX2=radnaPozicija.x + Vx*X2 - Vz*Z2    # modificiraj zavrsnu koordinatu
      gdjeY2=radnaPozicija.y + Y2
      gdjeZ2=radnaPozicija.z + Vx*Z2 + Vz*X2   
   
      mc.setBlocks( gdjeX1 , gdjeY1 , gdjeZ1 , gdjeX2 , gdjeY2 , gdjeZ2 , koji_blok , dv )   # nacrtaj blok
   
   return 1
   

#crtaj_blok (1,-1,-1,50,-1,1,1)
   
