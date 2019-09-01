# -*- coding:utf-8 -*-

# debug = True

import io
from collections import defaultdict
from mine import *
import mido
import time
from fallingEntity import FallingBlock
import api_motion
# import input
# import random
# 
# Custom Setting Here
class Cfg(object):
  def __init__(self):

    # self.MidiFile = r'E:\minecraft 1.12.2\.minecraft\saves\CopyNinjaKaKaXi\data\functions\mid\test.mid'
    # self.MidiFile = r'E:\minecraft 1.12.2\.minecraft\saves\CopyNinjaKaKaXi\data\functions\mid\S1.mid'
    # self.MidiFile = r'C:\Users\dell\Desktop\膝盖\小苹果.mid'
    # self.MidiFile = r'C:\Users\dell\Desktop\膝盖\Lemon.mid'
    # self.MidiFile = r'C:\Users\dell\Desktop\膝盖\梁祝完整版.mid'
    # self.MidiFile = r'./mid/梦回还 - 狐妖小红娘王权篇OP.mid'
    self.MidiFile = r'C:\Users\Administrator\Desktop\msDownload\2019-5-11\东方系列神组曲.mid'
    self.RootPos  = Vec3( 32,32,0 )
    self.tickrate = 20
    self.maxfb    = 8



cfg = Cfg()
tickrate = cfg.tickrate
mc = None
mc = Minecraft()
FB = FallingBlock()

# class falling_block_pool:
#   def __init__(self, maxCount):
#     self.maxCount = 100
#     self.freeList = []
#     self.busyList = []
#   def Init(self):
#     pass


port = mido.open_output()
# port.close()
# port = mido.open_output()

def Log( msg ):
  if mc != None:
    mc.postToChat( msg )
  else:
    print( msg )


class FackMc(object):
  def __init__(self):
    self.falling_block_list = []
    self.maxfb              = cfg.maxfb
  def setblock( self, x,y,z, block, data=0 ):
    mc.setBlock( Vec3(x,y,z), Block.byName( ' '.join([str(block), str(data)]) ) )
  def fill( self, x0,y0,z0, x1,y1,z1, block, data=0, replaceBlock=None, replaceData=None ):
    # print(x0,y0,z0, x1,y1,z1, block)
    if replaceBlock == None:
      mc.setBlocks( Vec3(x0,y0,z0), Vec3(x1,y1,z1), Block.byName( ' '.join([str(block), str(data)]) ) )
    elif replaceBlock != None:
      index = 0
      oldBlocks = mc.getBlocksWithData( x0,y0,z0, x1,y1,z1 )
      # print( oldBlocks )
      for y in range(min(y0,y1),max(y0,y1)+1):
        for x in range(min(x0,x1),max(x0,x1)+1):
          for z in range(min(z0,z1),max(z0,z1)+1):
            oldBlock = oldBlocks[index]
            # Log( oldBlock ) 
            index+= 1
            newBlock = Block.byName( ' '.join([str(replaceBlock), str(0 if replaceData == None else replaceData)]) ) 
            # print( newBlock )
            if newBlock.id == oldBlock.id and (replaceData == None or newBlock.data == oldBlock.data):
              self.setblock( x,y,z, block, data )
              # print( f'isEqual: setblock {block} {data}' )
  def fallingblock( self, x,y,z, X,Y,Z, tick, block, data=0 ):
    motion = FB.getMotionBy2PWithT( x,y,z, X,Y,Z, tick, gravity=False )
    vx,vy,vz = motion
    if not 1 <= y <= 255:
      Log(f'[ERROR]:pos y out of range, y:{y}')
      return
    if ( abs(vx) >= 10.0 or abs(vy) >= 10.0 or abs(vz) >=10.0 ):
      Log(f'[ERROR]:vx, vy, vz too large [{vx}, {vy}, {vz}]')
      return
    else:
      _Time  = 600 - ( tick - 1 )
      if _Time < 1:
        Log(f'[Warning]:_Time < 1, _Time:{_Time}, now _Time = 1')
        _Time = 1
      # else:
      try:
        curTime = time.time()
        self.falling_block_list = [ i for i in self.falling_block_list if i > curTime ]
        if len(self.falling_block_list) < self.maxfb:
          self.falling_block_list.append( curTime + tick/tickrate )
          Log( f'summon falling_block {x} {y} {z} {{Motion:[{vx},{vy},{vz}],Time:{_Time},DropItem:0b,Block:"{block}",Data:{data},NoGravity:1b}}' )
          # _NoGravity = 0 if gravity else 1
          mc.spawnEntity( 'FallingSand', x, y, z, f'{{NoGravity:1b,Motion:[{vx},{vy},{vz}],Time:{_Time},DropItem:0b,Block:"{block}",Data:{data}}}' )
        else:
          # Log( f'[ERROR]:falling_block_list is full' )
        # Log( f'summon falling_block {x} {y} {z} {{Motion:[{vx},{vy},{vz}],Time:{_Time},DropItem:0b,Block:"{block}",Data:{data}}}' )
          pass
      except:
        pass

fackMc = FackMc()

class Piano:
  def __init__(self):
    self.root = ( cfg.RootPos.x, cfg.RootPos.y, cfg.RootPos.z )
    # self.bIndexs = [1, 4, 6, 9, 11, 13, 16, 18, 21, 23, 25, 28, 30, 33, 35, 37, 40, 42, 45, 47, 49, 
    #                 52, 54, 57, 59, 61, 64, 66, 69, 71, 73, 76, 78, 81, 83, 85]
    # self.kIndexs = [0, 1, 2, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 21, 22, 24, 25,
    #                 26, 27, 28, 29, 30, 32, 33, 34, 35, 36, 38, 39, 40, 41, 42, 43, 44, 46, 47, 48,
    #                 49, 50, 52, 53, 54, 55, 56, 57, 58, 60, 61, 62, 63, 64, 66, 67, 68, 69, 70, 71,
    #                 72, 74, 75, 76, 77, 78, 80, 81, 82, 83, 84, 85, 86, 88, 89, 90, 91, 92, 94, 95,
    #                 96, 97, 98, 99, 100, 102]
    self.bIndexs = [1, 3, 6, 8, 10, 13, 15, 18, 20, 22, 25, 27, 30, 32, 34, 37, 39, 42, 44, 46, 49, 
                    51, 54, 56, 58, 61, 63, 66, 68, 70, 73, 75, 78, 80, 82, 85, 87, 90, 92, 94, 97, 
                    99, 102, 104, 106, 109, 111, 114, 116, 118, 121, 123, 126]
    self.kIndexs = [0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 20, 21, 22, 23, 24, 25, 26, 28, 29, 30, 31, 32, 34, 35, 36, 37, 38, 39, 40, 42, 43, 44, 45, 46, 48, 49, 50, 51, 52, 53, 54, 56, 57, 58, 59, 60, 62, 63, 64, 65, 66, 67, 68, 70, 71, 72, 73, 74, 76, 77, 78, 79, 80, 81, 82, 84, 85, 86, 87, 88, 90, 91, 92, 93, 94, 95, 96, 98, 99, 100, 101, 102, 104, 105, 106, 107, 108, 109, 110, 112, 113, 114, 115, 116, 118, 119, 120, 121, 122, 123, 124, 126, 127, 128, 129, 130, 132, 133, 134, 135, 136, 137, 138, 140, 141, 142, 143, 144, 146, 147, 148]
    self.kBufferL= [ []  for n in range(0, 128)]
    self.kBuffer = [ []  for n in range(0, 128)]
    self.kFlag   = [True for n in range(0, 128)]
  def getKeyType(self, note):
    if note in self.bIndexs:
      return 'black'
    else:
      return 'white'
  def getKeyPos(self, note, channel):
    ln, rn = int(floor(note)), int(ceil(note))
    if rn == note:
      return self._getKeyPos(rn, channel)
    x0,y0,z0 = self._getKeyPos( ln, channel )
    x1,y1,z1 = self._getKeyPos( rn, channel )
    x = x0 + (x1-x0)*(note-ln)/(rn-ln)
    y = y0 + (y1-y0)*(note-ln)/(rn-ln)
    z = z0 + (z1-z0)*(note-ln)/(rn-ln)
    return (x,y,z)
  def _getKeyPos(self, note, channel):
    x,y,z = self.root
    z += self.kIndexs[note]
    x    += 16*( channel // 2 )
    z    += 0 if channel%2 == 0 else 160
    return (x,y,z)

  def keyDown(self, note, channel):
    # self.markNote(note, channel, v=1) # 记录note

    x,y,z   = self.getKeyPos(note, channel)

    x      -= 1
    # x,y,z = cfg.RootPos.x-1, cfg.RootPos.y, cfg.RootPos.z
    keyType = self.getKeyType(note)
    if keyType == 'white':
    #   # mc.setBlocks( root, root + Vec3(-9, 0, 0), block. )
    # #   return f'execute @p {x} {y} {z} function key:whitedown'
      fackMc.fill( x,y,z, x-9,y,z, 'stone_slab', 4, 'brick_block', 0 )
      fackMc.fill( x,y,z-1, x-9,y,z-1, 'quartz_stairs', 3, 'quartz_block', 0 )
      fackMc.fill( x,y,z-1, x-9,y,z-1, 'stone_slab', 7, 'quartz_stairs', 2 )
      fackMc.fill( x,y,z+1, x-9,y,z+1, 'quartz_stairs', 2, 'quartz_block', 0 )
      fackMc.fill( x,y,z+1, x-9,y,z+1, 'stone_slab', 7, 'quartz_stairs', 3 )
    elif keyType == 'black':
      fackMc.setblock( x+1,y+1,z, 'stone_slab', 6 )
      fackMc.fill( x,y+1,z, x-5,y+1,z, 'air', 0, 'nether_brick', 0 )
      fackMc.setblock( x-6,y+1,z, 'air', 0 )
      fackMc.setblock( x-6,y,z, 'nether_brick_stairs', 0 )
    fackMc.setblock( x+3,y+1,z, 'wool', channel%14 + 1 )


    #   return f'execute @p {x} {y} {z} function key:blackdown'
    # else:
    #   return ''

  def keyUp(self, note, channel):
    # self.markNote(note, channel, v=0) # 记录note

    x,y,z   = self.getKeyPos(note, channel)

    x      -= 1
    # x,y,z = cfg.RootPos.x-1, cfg.RootPos.y, cfg.RootPos.z
    keyType = self.getKeyType(note)
    if keyType == 'white':
    #   return f'execute @p {x} {y} {z} function key:whiteup'
      fackMc.fill( x,y,z, x-9,y,z, 'brick_block', 0, 'stone_slab', 4 )
      fackMc.fill( x,y,z-1, x-9,y,z-1, 'quartz_block', 0, 'quartz_stairs', 3 )
      fackMc.fill( x,y,z-1, x-9,y,z-1, 'quartz_stairs', 2, 'stone_slab', 7 )
      fackMc.fill( x,y,z+1, x-9,y,z+1, 'quartz_block', 0, 'quartz_stairs', 2 )
      fackMc.fill( x,y,z+1, x-9,y,z+1, 'quartz_stairs', 3, 'stone_slab', 7 )
      pass
    elif keyType == 'black':
      fackMc.setblock( x+1,y+1,z, 'nether_brick', 6 )
      fackMc.fill( x,y+1,z, x-5,y+1,z, 'nether_brick', 0, 'air', 0 )
      fackMc.setblock( x-6,y+1,z, 'nether_brick_stairs', 0 )
      fackMc.setblock( x-6,y,z, 'nether_brick', 0 )
    fackMc.setblock( x+3,y+1,z, 'air', 0 )


    #   return f'execute @p {x} {y} {z} function key:blackup'
    #   
    # else:
    #   return ''


  # def markNote(self, note, channel, v):
  #   self.kFlag[note] = True
  #   if v > 0:
  #     self.kBuffer[note].append(channel)
  #   else:
  #     self.kBuffer[note].remove(channel)

  # def makeNoteCmd(self):
  #   cmds = []
  #   for i,flag in enumerate(self.kFlag):
  #     if flag:
  #       self.kFlag[i] = False
  #       maxC = 16
  #       last = [-1 for j in range(maxC)]
  #       curr = [-1 for j in range(maxC)]
  #       for j,c in enumerate(self.kBufferL[i]):
  #         last[j] = c
  #       for j,c in enumerate(self.kBuffer[i]):
  #         curr[j] = c
  #       for j in range(maxC):
  #         if curr[j] != last[j]:
  #           x,y,z = self.getKeyPos(i)
  #           x    += (j+2)
  #           c     = curr[j]
  #           if c == -1:
  #             cmds.append(util.SetBlock(x,y,z, 'air').toCmd())
  #           else:
  #             cmds.append(util.SetBlock(x,y,z, 'wool', (c+2)%16).toCmd())

  #       self.kBufferL[i] = self.kBuffer[i][:]

    # return '\n'.join(cmds)

def buildPiano():
  for c in range(16):
    for note in range(0,128):
      x,y,z = p.getKeyPos(note, c)

      kt    = p.getKeyType(note)
      if kt == 'white':
        # buildCmds.append(f'fill {x} {y} {z-1} {x-10} {y} {z+1} quartz_block')
        # buildCmds.append(f'fill {x} {y+1} {z-1} {x} {y+1} {z+1} stone_slab 7')
        # buildCmds.append(f'fill {x} {y} {z} {x-10} {y} {z} brick_block')
        # buildCmds.append(f'setblock {x} {y+1} {z} stone_slab 4')
        # mc.setBlocks( Vec3( x,y,z-1 ), Vec3( x-10,y,z+1 ), Block( block.QUARTZ_BLOCK.id, 0 ) )
        # mc.setBlocks( Vec3( x,y+1,z-1 ), Vec3( x,y+1,z+1 ), Block( block.STONE_SLAB.id, 7 ) )
        # mc.setBlocks( Vec3( x,y,z ), Vec3( x-10,y,z ), Block( block.BRICK_BLOCK.id, 0 ) )
        # mc.setBlock ( Vec3( x,y+1,z ), Block( block.STONE_SLAB.id, 4 ) )
        fackMc.fill( x+1,y,z-1, x+3,y+1,z+1, 'air' )
        fackMc.fill( x,y,z-1, x-10,y,z+1, 'quartz_block' )
        fackMc.fill( x,y+1,z-1, x,y+1,z+1, 'stone_slab', 7 )
        fackMc.fill( x,y,z, x-10,y,z, 'brick_block' )
        fackMc.setblock( x,y+1,z, 'stone_slab', 4 )

    for note in range(0,128):
      x,y,z = p.getKeyPos(note, c)

      kt    = p.getKeyType(note)
      if kt == 'black':
        # buildCmds.append(f'fill {x} {y} {z} {x-7} {y+1} {z} nether_brick')
        # buildCmds.append(f'setblock {x-7} {y+1} {z} nether_brick_stairs 0')
        # mc.setBlocks( Vec3( x,y,z ), Vec3( x-7,y+1,z ), Block( block.NETHER_BRICK.id, 0 ) )
        # mc.setBlock ( Vec3( x-7,y+1,z ), Block( block.NETHER_BRICK_STAIRS.id, 0 ) )
        fackMc.fill( x,y,z, x-7,y+1,z, 'nether_brick' )
        fackMc.setblock( x-7,y+1,z, 'nether_brick_stairs', 0 )

  # util.writeMcFunction('tmp:piano', '\n'.join(buildCmds))

# def buildEnd():
#   buildCmds = []
#   for n in range(21, 108+1):
#     buildCmds.append(p.keyUp(n))
#   x1,y1,z1 = p.root
#   x2,y2,z2 = x1+32, y1, p.getKeyPos(108)[2]
#   x3,y3,z3 = x1, y1+32+2, p.getKeyPos(108)[2]
#   buildCmds.append(f'fill {x1+1} {y1} {z1} {x2} {y2} {z2} air')
#   buildCmds.append(f'fill {x1} {y1+2} {z1} {x3} {y3} {z3} air')
#   buildCmds.append(f'gamerule gameLoopFunction None')
#   util.writeMcFunction('tmp:end', '\n'.join(buildCmds))


p   = Piano()



if __name__ == '__main__':
  # borad = Board2D( mc, 20, 10, distance=10 )

  buildPiano()

  # Log("Cleaning")
  # mc.setBlocks( cfg.RootPos, cfg.RootPos + Vec3(15, 0, 127), block.AIR )
  Log('Loading...')
  mid  = mido.MidiFile( cfg.MidiFile )
  Log('Load Complete...')

  Log('Prepare... pitchwheel ')

  class moveItem:
    def __init__(self, dt, dn):
      self.dt = dt
      self.dn = dn

  class fixMsg:
    def __init__(self, msg, curTime, length=None):
      self.rawMsg = msg
      self.curTime= curTime
      self.length = length
      self.move   = []


  fixMsgList = []
  mem = [[None for note in range(128)] for channel in range(16)]
  timer = 0
  for msg in mid:
    timer += msg.time
    newFixMsg = fixMsg( msg, timer, None )
    fixMsgList.append( newFixMsg )
    if msg.type == 'note_on' and msg.velocity > 0:
      mem[msg.channel][msg.note] = newFixMsg
    elif msg.type == 'note_on' and msg.velocity == 0 or msg.type == 'note_off':
      if mem[msg.channel][msg.note] != None:
        mem[msg.channel][msg.note].length = timer - mem[msg.channel][msg.note].curTime
        mem[msg.channel][msg.note] = None
    elif msg.type == 'pitchwheel':
      for n in range(128):
        if mem[msg.channel][n] != None: 
          mem[msg.channel][n].move.append( moveItem( timer-mem[msg.channel][n].curTime, (msg.pitch-128*64) / 64 / 4 / 2 ) )
    else:
      pass


  class TweenItem:
    def __init__(self, remainTime, p0, p1, fT, block, data=0):
      self.remainTime = remainTime
      self.p0         = p0
      self.p1         = p1
      self.fT         = fT
      self.block      = block
      self.data       = data
    def callback(self):
      fackMc.fallingblock( *self.p0, *self.p1, self.fT, self.block, self.data )

  with open('output.txt', 'w') as f:

    _TweenList = []
    timer = 0
    for fixMsg in fixMsgList:
      msg = fixMsg.rawMsg
      timer += msg.time
      if msg.type == 'note_on' and msg.velocity > 0:
        if fixMsg.length != None and int( fixMsg.length*tickrate ) > 0:
          tick   = int( fixMsg.length*tickrate )
          x,y,z  = p.getKeyPos( msg.note, msg.channel )
          x     += 2
          if len(fixMsg.move) == 0:
            pass
          else:
            _startTick = 0
            _endTick   = tick
            _lastDn    = 0
            moveDict = {}
            moveDict[_startTick] = 0.0

            for m in fixMsg.move:
              moveDict[int(round(m.dt*tickrate))] = m.dn
              _lastDn                             = m.dn
            if not _endTick in moveDict:
              moveDict[_endTick] = _lastDn

            fixMoveList = []
            for t in range( _startTick, _endTick+1 ):
              if t in moveDict:
                fixMoveList.append( moveItem( t, moveDict[t] ) )

            f.write( '--newFixMoveList:' + '\n')
            for i, m in enumerate(fixMoveList):
              f.write( f't:{m.dt}, dn={m.dn}' + '\n' )

            motion = FB.getMotionBy2PWithT( x,y,z, x,y,z, tick, gravity=False )
            # vx,vy,vz = motion
            # if ( abs(vx) >= 10.0 or abs(vy) >= 10.0 or abs(vz) >=10.0 ):
            #   Log(f'vx, vy, vz too large [{vx}, {vy}, {vz}]')
            # else:
            #   _Time  = 600 - tick - 1
            #   if _Time < 1:
            #     Log(f'_Time < 1, _Time:{_Time}')
            #   else:
            #     mc.spawnEntity( 'falling_block', x+0.5, y+0.5, z+0.5, f'{{Motion:[{vx},{vy},{vz}],Time:{_Time},DropItem:0b,Block:"{block}",Data:{data}}}' )


            for i,m in enumerate(fixMoveList):
              # 这是最后一项
              if i == len(fixMoveList)-1:
                # if msg.length > m[0]:
                #   m0 = m
                #   m1 = m
                #   sTick = tick + m0[0]
                #   eTick = tick + msg.length
                #   sNote = note + m0[1]
                #   eNote = note + m1[1]
                #   fT    = eTick - sTick
                #   lastNote = eNote
                # else:
                #   break
                pass

              # 这不是最后一项
              else:
                m0 = m
                m1 = fixMoveList[i+1]
                sTick = m0.dt
                eTick = m1.dt
                sNote = m0.dn + msg.note
                eNote = m1.dn + msg.note
                fT    = eTick - sTick
                # lastNote = eNote

              # p0 = getPos(sTick, sNote, velocity, channel)
              # p1 = getPos(eTick, eNote, velocity, channel)
                
              if fT > 0:
                z0 = p.getKeyPos( sNote, msg.channel )[2]
                z1 = p.getKeyPos( eNote, msg.channel )[2]

                # motion = FB.getMotionBy2PWithT( x,y,z, x,y,z, tick, gravity=True )

                # maxHeight = 8.0
                # for reTick, cmd in FB.getHushCmdsBy2PWithT(*p0, *p1, fT, maxHeight+p0[1], 'wool', channel%14 + 1):
                #   seq.findByTick(sTick+reTick).addCmd(cmd)##
                # # pass
                p0 = FB.getPosBy1PWithV0( x,y,z, *motion, sTick, gravity=False )
                p1 = FB.getPosBy1PWithV0( x,y,z, *motion, eTick, gravity=False )
                p0 = (p0[0]-0.5, p0[1]+3.5, z0+0.5)
                p1 = (p1[0]-0.5, p1[1]+3.5, z1+0.5)

              
                # def getFallingBlockFunction( p0, p1, fT, block, data=0 ):
                #   def fun():
                #     fackMc.fallingblock( *p0, *p1, fT, block, data=0 )
                #   return fun

                _TweenList.append( TweenItem( timer + sTick / tickrate,  p0, p1, fT, 'wool', msg.channel % 14 + 1 ) ) 

  _TweenList.sort( key=lambda item: item.remainTime )

  # with open('log.txt', 'w') as f:
  #   for tween in _TweenList:
  #     f.write(f'time:{tween.remainTime}, p0:{tween.p0}, p1:{tween.p1}, fT:{tween.fT} \n')
            

  def yieldMsg():
    for fixMsg in fixMsgList:
      yield fixMsg

  def yieldTween():
    for Tween in _TweenList:
      yield Tween

  Log("Prepare Ok ...")

  for i in range(3,0,-1):
    Log(i)
    time.sleep(1.0)
  Log('Playing...')

  startTime  = time.time()
  # nextTime  = lastTime
  # nextFixMsg   = None
  # msgGetter = yieldMsg()
  # tweenGetter = yieldTween()
  msgIndex = 0
  tweenIndex = 0


  _noMoreMsgFlag = False



  while True:
    msg = None
    fixMsg = None
    curTime = time.time() - startTime

    # dt = curTime - lastTime
    # lastTime = curTime

    if msgIndex < len(fixMsgList) and curTime >= fixMsgList[msgIndex].curTime:

      fixMsg = fixMsgList[msgIndex]
      msgIndex += 1

    # if curTime >= nextTime:
    #   fixMsg     = nextFixMsg
    #   try:
    #     nextFixMsg = next(msgGetter)
    #   except:
    #     nextFixMsg = None
    #     _noMoreMsgFlag = True
    #   if not nextFixMsg is None:
    #     nextTime = nextTime + nextFixMsg.rawMsg.time

    if not fixMsg is None:
      msg = fixMsg.rawMsg
      if not msg.is_meta:
        lastTime = curTime
        port.send(msg)
        pass
      if msg.type == 'note_on' and msg.velocity > 0:

        p.keyDown(msg.note, msg.channel)

        if fixMsg.length != None and int( fixMsg.length*tickrate ) > 0:
          tick   = int( fixMsg.length*tickrate )
          x,y,z  = p.getKeyPos( msg.note, msg.channel )
          x     += 2
          if len(fixMsg.move) == 0:
            # fackMc.fallingblock( x+0.5,y+1.5,z+0.5, x+0.5,y+0.5,z+0.5, tick, 'redstone_block', data=0 )
            # fackMc.setblock( x,y+1,z, 'redstone_block', 0 )
            pass
          else:
            pass

      elif msg.type == 'note_on' and msg.velocity == 0 or msg.type == 'note_off':

        # fackMc.setblock( x,y+1,z, 'air', 0 )

        p.keyUp(msg.note, msg.channel)

        pass

    if ( tweenIndex < len(_TweenList) and curTime >= _TweenList[tweenIndex].remainTime ):
      _TweenList[tweenIndex].callback()
      tweenIndex += 1
    # while ( tweenIndex < len(_TweenList) and curTime >= _TweenList[tweenIndex].remainTime ):
    #   tweenIndex += 1


    if msgIndex >= len(fixMsgList) and tweenIndex >= len(_TweenList):
      Log("--- End ---")
      Log("[xue]: This is builded with mcpipy")
      time.sleep(3)
      break
    
  
  # Log("--- End ---")
  # Log("---  ---")
  # Log("~~结束啦啦啦~~谢谢观看啦啦啦啦啦~~~~~~")

  # fackMc.fill( 0,4,-1, 0,4,3, 'STAIRS_WOOD', 3, 'dirt', 0 )
  # print( mido.get_output_names() )

  # while True:
  #   Log( mc.player.getTilePos() )

