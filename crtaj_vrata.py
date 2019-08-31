#crta vrata na zadanim koordinatama zadane vrste - OBSOLETE

from mc import * #import api-ja
mc = Minecraft() #inicijalizacija sustava za rad sa Minecraftom

def crtaj_vrata (X1,Y1,Z1,koja_vrata=195 , rel_smjer = 0):   
   """
   funkcija za crtanje vrata na zadanim koordinatama zadane vrste
   X1,Y1,Z1 - pozicija
   koja_vrata - koja vrata default obicna
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

   # rel_smjer == 0 naprijed 1 lijevo 2 desno 3 iza 
   
   if Vx == 1 :
      pass   
   if Vx == -1 :      
      rel_smjer += 2
      if rel_smjer > 3 :
         rel_smjer -= 4
 
         
   if Vz == -1 :      
      rel_smjer += 1
      if rel_smjer > 3  :
         rel_smjer -= 4  
   if Vz == 1 :      
      rel_smjer += 3
      if rel_smjer > 3 :
         rel_smjer -= 4  
         
   if Vz != 0 :
      if rel_smjer == 1 :
         buffer = 3
      if rel_smjer == 3 :
         buffer = 1
      if ( rel_smjer == 1 ) or  ( rel_smjer == 3 ) :
         rel_smjer = buffer

      

         
   #crtanje
   
   
   
   if  abs ( Vx )  != abs ( Vz ) :		# ne pod 45

      gdjeX1=radnaPozicija.x + Vx*X1 + Vz*Z1    # modificiraj pocetnu koordinatu
      gdjeY1=radnaPozicija.y + Y1
      gdjeZ1=radnaPozicija.z + Vx*Z1 + Vz*X1
      mc.setBlock ( gdjeX1 , gdjeY1 , gdjeZ1 , koja_vrata , 0 + rel_smjer ) # doljnji dio vrata
      gdjeY1=radnaPozicija.y + 1
      mc.setBlock ( gdjeX1 , gdjeY1 , gdjeZ1 , koja_vrata , 8 + rel_smjer ) # gornji dio vrata
   return 1
   

   
