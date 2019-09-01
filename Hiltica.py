#ispred lika crta more baklji po tlu

import time
import math
from mc import * #import api-ja
from crtanje import *		#tu je funkcija koju zovem
mc = Minecraft() #inicijalizacija sustava za rad sa Minecraftom
import threading


zaObradu = [  STONE.id , GRASS.id , SANDSTONE.id , SAND.id ,  DIRT.id , GRAVEL.id , COBBLESTONE.id , CLAY.id ,GOLD_ORE.id , IRON_ORE.id , COAL_ORE.id ,  DIAMOND_ORE.id , OBSIDIAN.id , REDSTONE_ORE.id , LAPIS_LAZULI_ORE.id , 129 ] # 129 emerald

popis = {}

def MegaGrinder ( orMj , orSm ,  dimenzije = 5 , visina = 5):
   a = 1
   for dY in range ( visina  , -1 , -1 ):
      mc.postToChat("Level: %s " % dY )
      for dZ  in range ( -dimenzije - 1 * dY , dimenzije + 1 * dY + 1 ):
         for dX in range ( -dimenzije - 1 * dY , dimenzije + 1 * dY + 1 ):
            gdje = rel2abs ( orMj  , (  dX , dZ , dY )   , orSm  )
            myBlock = mc.getBlockWithData( int (gdje [0])  ,int (gdje [1]) ,int (gdje [2]) )
            if myBlock.id in   ( 8 , 9 , 10 , 11 ) : #makni izvore vode
               mc.setBlock(int (gdje [0])  ,int (gdje [1]) ,int (gdje [2]) , AIR.id , 0 )   
               time.sleep ( 0.2 )

            if myBlock.id in zaObradu :
               a = a + 1
               mc.postToChat("Level: %s  dZ: %s dX: %s count: %s what: %s " % ( dY  , dZ ,  dX, a , myBlock.id ) )
               
               mc.setBlock(int (gdje [0])  ,int (gdje [1]) ,int (gdje [2]) , AIR.id , 0 )
               time.sleep ( 0.2 )
               sto = ( '{Item:{id:%s,Count:%s,Damage:%s}}' % ( myBlock.id , 1  ,  myBlock.data ) ) #posalji
               myId = mc.spawnEntity('Item', int (gdje [0])  ,int (gdje [1] + 1 ) ,int (gdje [2] ) , sto )
               
            if a > 1000:
               break
         if a > 1000 :
            break
      if a > 1000 :
         break
               

   mc.postToChat("Kraj :  XXXXXXXXXXXX")
   return 1
                  


class ExplodingBlock(threading.Thread):

    def __init__(self, pos, fuseInSecs, blastRadius):
        #Setup object
        threading.Thread.__init__(self)
        self.pos = pos
        self.fuseInSecs = fuseInSecs
        self.blastRadius = blastRadius

    def run(self):
        #Open connect to minecraft
        mc = minecraft.Minecraft.create()

        #Get values
        pos = self.pos
        blastRadius = self.blastRadius

        #Explode the block!
        # get block type
        blockType = mc.getBlock(pos.x, pos.y, pos.z)
        # flash the block
        for fuse in range(0, self.fuseInSecs):
            mc.setBlock(pos.x, pos.y, pos.z, block.AIR)
            time.sleep(0.5)
            mc.setBlock(pos.x, pos.y, pos.z, blockType)
            time.sleep(0.5)
        # create sphere of air
        for x in range(blastRadius*-1,blastRadius):
            for y in range(blastRadius*-1, blastRadius):
                for z in range(blastRadius*-1,blastRadius):
                    if x**2 + y**2 + z**2 < blastRadius**2:
                        mc.setBlock(pos.x + x, pos.y + y, pos.z + z, block.AIR)
                  
               
class Hiltica(threading.Thread):

   def __init__(self, orMj , orSm ,  dimenzije  , visina ):
      threading.Thread.__init__(self)
      self.orMj = orMj
      self.orSm  = orSm
      self.dimenzije = dimenzije
      self.visina = visina
   
   def run(self):
      zaObradu = [  STONE.id , GRASS.id , SANDSTONE.id , SAND.id ,  DIRT.id , GRAVEL.id , COBBLESTONE.id , CLAY.id ,GOLD_ORE.id , IRON_ORE.id , COAL_ORE.id ,  DIAMOND_ORE.id , OBSIDIAN.id , REDSTONE_ORE.id , LAPIS_LAZULI_ORE.id , 129 ] # 129 emerald
      orMj = self.orMj
      orSm  = self.orSm
      dimenzije = self.dimenzije
      visina = self.visina      
      a = 1
      for dY in range ( visina  , -1 , -1 ):
         mc.postToChat("Level: %s " % dY )
         for dZ  in range ( -dimenzije - 1 * dY , dimenzije + 1 * dY + 1 ):
            for dX in range ( -dimenzije - 1 * dY , dimenzije + 1 * dY + 1 ):
               gdje = rel2abs ( orMj  , (  dX , dZ , dY )   , orSm  )
               myBlock = mc.getBlockWithData( int (gdje [0])  ,int (gdje [1]) ,int (gdje [2]) )
               if myBlock.id in   ( 8 , 9 , 10 , 11 ) : #makni izvore vode
                  mc.setBlock(int (gdje [0])  ,int (gdje [1]) ,int (gdje [2]) , AIR.id , 0 )   
                  time.sleep ( 1 )

               if myBlock.id in zaObradu :
                  a = a + 1
                  mc.postToChat("Level: %s  dZ: %s dX: %s count: %s what: %s " % ( dY  , dZ ,  dX, a , myBlock.id ) )
               
                  mc.setBlock(int (gdje [0])  ,int (gdje [1]) ,int (gdje [2]) , AIR.id , 0 )
                  
                  #sto = ( '{Item:{id:%s,Count:%s,Damage:%s}}' % ( myBlock.id , 1  ,  myBlock.data ) ) #posalji
                  #myId = mc.spawnEntity('Item', int (gdje [0])  ,int (gdje [1]  ) ,int (gdje [2] ) , sto )
                  #time.sleep ( 0.11 )
                  #pos = mc.entity.getPos(myId)
                  #time.sleep ( 1 )
               if a > 100000:
                  break
            if a > 100000 :
               break
         if a > 100000 :
            break
               

      mc.postToChat("Kraj :  XXXXXXXXXXXX")
      #return 1

      
if __name__ == "__main__":    #direktan poziv
   orMj = gdjeSam ()
   orSm = gdjeGledam ()
   #MegaGrinder ( orMj , orSm ,  dimenzije = 1 , visina = 3)  
   hiltica =    Hiltica ( orMj , orSm ,  dimenzije = 6 , visina = 25)  
   hiltica.daemon
   hiltica.start()
   

   """
                       explodingBlock = ExplodingBlock(blockHit.pos, 3, 3)
                    explodingBlock.daemon
                    explodingBlock.start()
   """
   #bakljada (dimenzije = 200 , visina = 80)   