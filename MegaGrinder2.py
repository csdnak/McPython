#ispred lika crta more baklji po tlu

import time
from mc import * #import api-ja
from crtanje import *		#tu je funkcija koju zovem
mc = Minecraft() #inicijalizacija sustava za rad sa Minecraftom
import time


zaObradu = [  STONE.id , GRASS.id , SANDSTONE.id , SAND.id ,  DIRT.id , GRAVEL.id , COBBLESTONE.id , CLAY.id ,GOLD_ORE.id , IRON_ORE.id , COAL_ORE.id ,  DIAMOND_ORE.id , OBSIDIAN.id , REDSTONE_ORE.id , LAPIS_LAZULI_ORE.id , 129 ] # 129 emerald

popis = {}

def MegaGrinder ( orMj , orSm ,  dimenzije = 5 , visina = 5):
   a = 1
   for dY in range ( visina  , -1 , -1 ):
      mc.postToChat("Level: %s " % dY )
      for dZ  in range ( -dimenzije - 1 * dY , dimenzije + 1 * dY + 1 ):
         for dX in range ( -dimenzije - 1 * dY , dimenzije + 1 * dY + 1 ):
 
            gdje = rel2abs ( ( int ( orMj [ 0 ] ) , int ( orMj [ 1 ] ) , int ( orMj [ 2 ] ) )  , (  dX , dZ , dY )   , orSm  )
            #id = mc.spawnEntity('Minecart',  int (gdje [0])  ,int (gdje [1]) ,int (gdje [2]) , "{Type:0}" )
            #block = getBlockWithData( int (gdje [0])  ,int (gdje [1]) ,int (gdje [2]))
            myBlock = mc.getBlockWithData( int (gdje [0])  ,int (gdje [1]) ,int (gdje [2]) )
            #myBlock = mc.getBlockWithData( int (gdje [0])  ,int (gdje [1]) ,int (gdje [2]) )
            
            if myBlock.id == 1 : #makni sve stone
               mc.setBlock(int (gdje [0])  ,int (gdje [1]) ,int (gdje [2]) , AIR.id , 0 )  
               myBlock.id = 0      
               #time.sleep ( 0.2 )
               
            
            if myBlock.id in   ( 8 , 9 , 10 , 11 ) : #makni izvore vode
               mc.setBlock(int (gdje [0])  ,int (gdje [1]) ,int (gdje [2]) , AIR.id , 0 )   
               #time.sleep ( 0.2 )

            if myBlock.id in zaObradu :
               a = a + 1
<<<<<<< HEAD
               mc.postToChat("Level: %s  dZ: %s dX: %s count: %s" % ( dY  , dZ ,  dX, a ) )
               #time.sleep ( 0.2 )
=======
               mc.postToChat("Level: %s  dZ: %s dX: %s count: %s what: %s " % ( dY  , dZ ,  dX, a , myBlock.id ) )
               time.sleep ( 0.25 )
>>>>>>> origin/master
               mc.setBlock(int (gdje [0])  ,int (gdje [1]) ,int (gdje [2]) , AIR.id , 0 )
               
               
               if popis.has_key ((  myBlock.id , myBlock.data )):
                  popis [ ( myBlock.id , myBlock.data ) ] += 1
               else:
                  popis [ ( myBlock.id , myBlock.data ) ] = 1
<<<<<<< HEAD
            if a > 9800:
               break
         if a > 9800 :
            break
      if a > 9800 :
=======
            if a > 1000:
               break
         if a > 1000 :
            break
      if a > 1000 :
>>>>>>> origin/master
         break
               
               
   time.sleep ( 20 )            
   for bla in popis.keys () :
         blok = bla [ 0 ]
         modifikacija = bla [ 1 ]
         #prijevodi: 
         #diamond
         #56 : 264,
         if bla [ 0 ] == 56 :
            blok = 264
         #redstone
         #73 : 331 ,
         if bla [ 0 ] == 73 :
            blok = 331
         #lapis
         #21 : 351 , 4 
         if bla [ 0 ] == 21 :
            blok = 351
            modifikacija = 4
         #emerald
         #129 :  388
         if bla [ 0 ] == 129 :
            blok = 388   
         #coal COAL_ORE.id  263
         if bla [ 0 ] == COAL_ORE.id :
            blok = 263   
            modifikacija = 0
            
         mc.postToChat("Key: %s %s " % ( bla [ 0 ] , bla [ 1 ] ) )
         mc.postToChat("Value: %s " % popis [ bla ] )
         while popis [ bla ] > 0 :
            if  popis [ bla ] > 64 :   # preostalo vise od paketa
               sto = ( '{Item:{id:%s,Count:%s,Damage:%s}}' % ( blok , 1  ,  modifikacija ) ) #posalji cijeli paket
               if blok == 1 and modifikacija == 0 :   #ako je stone
                  popis [ bla ] -= 1  # unisti jedan paket i malo vise
            else:
               sto = ( '{Item:{id:%s,Count:%s,Damage:%s}}' % ( blok , popis [ bla ]  ,  modifikacija ) ) #posalji preostalo
            mc.postToChat("-------> : %s  jos: %s " % ( sto , popis [ bla ]  ) )
            gdje = rel2abs ( orMj , (  0 , 0 , 1 )   , orSm  )
            myId = mc.spawnEntity('Item', int (gdje [0])  ,int (gdje [1]) ,int (gdje [2] ) , sto )
            popis [ bla ] -= 64
<<<<<<< HEAD
            time.sleep ( 12 )
=======
            time.sleep ( 10 )
>>>>>>> origin/master
         
   mc.postToChat("Kraj :  XXXXXXXXXXXX")
   return 1
                  
                  
               


if __name__ == "__main__":    #direktan poziv
   orMj = gdjeSam ()
   orSm = gdjeGledam ()
<<<<<<< HEAD
   MegaGrinder ( orMj , orSm ,  dimenzije = 100 , visina = 28)   
=======
   MegaGrinder ( orMj , orSm ,  dimenzije = 5 , visina = 25)   
>>>>>>> origin/master
   #bakljada (dimenzije = 200 , visina = 80)   