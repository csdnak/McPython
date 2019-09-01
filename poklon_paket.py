# crtanje automatizirani sorter
#definicija objekta i poziv rutine za crtanje
import time 
import sys
from crtanje import *		#tu je funkcija koju zovem

from mc import *			
mc = Minecraft() #inicijalizacija sustava za rad sa Minecraftom



def paket_opreme ( orMjL ,  orSm ,  iX=0 , iZ=0 , iY=0 ):
   djelovi = (
   '{Items:' ,
   '[{Slot:0b,id:"minecraft:diamond_pickaxe",Count:64b,Damage:0s,},',
   '{Slot:1b,id:"minecraft:diamond_shovel",Count:64b,Damage:0s,},'
   '{Slot:2b,id:"minecraft:diamond_axe",Count:64b,Damage:0s,},',
   '{Slot:3b,id:"minecraft:diamond_sword",Count:64b,Damage:0s,},',
   '{Slot:4b,id:"minecraft:diamond",Count:64b,Damage:0s,},',
   '{Slot:5b,id:"minecraft:diamond_hoe",Count:64b,Damage:0s,},',
   '{Slot:6b,id:"minecraft:diamond_sword",Count:64b,Damage:0s,},',
   '{Slot:7b,id:"minecraft:diamond_helmet",Count:64b,Damage:0s,},',
   '{Slot:8b,id:"minecraft:diamond_chestplate",Count:64b,Damage:0s,},',
   '{Slot:9b,id:"minecraft:diamond_leggings",Count:64b,Damage:0s,},',
   '{Slot:10b,id:"minecraft:log",Count:64b,Damage:0s,},',
   '{Slot:11b,id:"minecraft:diamond_boots",Count:64b,Damage:0s,},'
   '{Slot:12b,id:"minecraft:stone_brick_stairs",Count:64b,Damage:0s,},'
   '{Slot:13b,id:"minecraft:stonebrick",Count:64b,Damage:0s,},'
   '{Slot:14b,id:"minecraft:bed",Count:64b,Damage:0s,},'
   '{Slot:15b,id:"minecraft:iron_ingot",Count:64b,Damage:0s,},'
   '{Slot:16b,id:"minecraft:gold_ingot",Count:64b,Damage:0s,},'
   '{Slot:17b,id:"minecraft:cobblestone",Count:64b,Damage:0s,},'
   '{Slot:18b,id:"minecraft:book",Count:64b,Damage:0s,},'
   '{Slot:19b,id:"minecraft:cooked_porkchop",Count:64b,Damage:0s,},'
   '{Slot:20b,id:"minecraft:apple",Count:64b,Damage:0s,},'
   '{Slot:21b,id:"minecraft:chest",Count:64b,Damage:0s,},'
   '{Slot:22b,id:"minecraft:vine",Count:64b,Damage:0s,},'
   '{Slot:23b,id:"minecraft:shears",Count:64b,Damage:0s,},'
   '{Slot:24b,id:"minecraft:torch",Count:64b,Damage:0s,},'   
   '{Slot:25b,id:"minecraft:torch",Count:64b,Damage:0s,},'   
   '{Slot:26b,id:"minecraft:glowstone",Count:64b,Damage:0s,}],'  
   'id:"minecraft:chest",Lock:""}'
   )

   sadrzaj=""
   for to in djelovi :  
      sadrzaj = sadrzaj + to
   bla = rel2abs ( orMjL , ( iX , iZ , iY  ) , orSm )
   # GENERIRA PUNU KUTIJU
   mc.setBlockWithNBT(bla,54,0, sadrzaj )

def mining_komplet ( orMjL ,  orSm ,  iX=0 , iZ=0 , iY=0 ):
   orMjL = premjesti_origin ( orMj ,  iX , iZ , iY   , orSm )
   paket_opreme ( orMjL ,  orSm ,  iX=0 , iZ=0 , iY=2 )  #oprema
   crtaj_kutiju ( orMjL , (0,-2,0) , (0,-1,1) , orSm , rel_smjer  = "meni" , blok_id = 54     ) #prazne kutije
   crtaj_kutiju ( orMjL , (0,1,0) , (0,2,1) , orSm , rel_smjer  = "meni" , blok_id = 54     )
   crtaj_pec  ( orMjL , (0,0,0) , (0,0,0) , orSm , rel_smjer  = "meni"     ) # topionca
   crtaj_kvadar ( orMjL , (0,0,1) , (0,0,1), orSm , 145 , blok_dv = 0 )# nakovanj 145 



if __name__ == "__main__":    #direktan poziv
   orMj = gdjeSam ()
   orSm = gdjeGledam ()
   mining_komplet ( orMj ,  orSm ,  iX=2 , iZ=0 , iY=0 )

"""


# origin ispred na sredini 
orMj = gdjeSam ()
orSm = gdjeGledam ()

#oakwood slab
materijal = 126
dv = 8

djelovi = (
'{Items:' ,
'[0:{Slot:0b,id:"minecraft:diamond_pickaxe",Count:64b,Damage:0s,},',
'1:{Slot:1b,id:"minecraft:diamond_shovel",Count:64b,Damage:0s,},'
'2:{Slot:2b,id:"minecraft:diamond_axe",Count:64b,Damage:0s,},',
'3:{Slot:3b,id:"minecraft:diamond_svord",Count:64b,Damage:0s,},'
'4:{Slot:4b,id:"minecraft:diamond",Count:64b,Damage:0s,},',
'5:{Slot:5b,id:"minecraft:diamond_hoe",Count:64b,Damage:0s,},',
'6:{Slot:6b,id:"minecraft:diamond_sword",Count:64b,Damage:0s,},',
'7:{Slot:7b,id:"minecraft:diamond_helmet",Count:64b,Damage:0s,},',
'8:{Slot:8b,id:"minecraft:diamond_chestplate",Count:64b,Damage:0s,},',
'9:{Slot:9b,id:"minecraft:diamond_leggings",Count:64b,Damage:0s,},',
'10:{Slot:10b,id:"minecraft:log",Count:64b,Damage:0s,},',
'11:{Slot:11b,id:"minecraft:diamond_boots",Count:64b,Damage:0s,},'
'12:{Slot:12b,id:"minecraft:glowstone",Count:64b,Damage:0s,},'
'13:{Slot:13b,id:"minecraft:glowstone",Count:64b,Damage:0s,},'
'14:{Slot:14b,id:"minecraft:glowstone",Count:64b,Damage:0s,},'
'15:{Slot:15b,id:"minecraft:glowstone",Count:64b,Damage:0s,},'
'16:{Slot:16b,id:"minecraft:torch",Count:64b,Damage:0s,},'
'17:{Slot:17b,id:"minecraft:torch",Count:64b,Damage:0s,},'
'18:{Slot:18b,id:"minecraft:torch",Count:64b,Damage:0s,},'
'19:{Slot:19b,id:"minecraft:cooked_porkchop",Count:64b,Damage:0s,},'
'20:{Slot:20b,id:"minecraft:torch",Count:64b,Damage:0s,},],'
'id:"Hopper",Lock:"",}'
)

sadrzaj=""
for to in djelovi :  
   sadrzaj = sadrzaj + to

bla = rel2abs ( orMj , ( 2  , 0 ,  0  ) , orSm )

# GENERIRA PUNU KUTIJU
mc.setBlockWithNBT(bla,54,1, sadrzaj )



djelovi2 = (
'{Items:' ,
'[0:{Slot:0b,id:"minecraft:brick",Count:64b,Damage:0s,},',
'1:{Slot:1b,id:"minecraft:redstone_torch",Count:64b,Damage:0s,},'
'2:{Slot:2b,id:"minecraft:chest",Count:64b,Damage:0s,},',
'3:{Slot:3b,id:"minecraft:diamond",Count:64b,Damage:0s,},'
'4:{Slot:4b,id:"minecraft:emerald",Count:64b,Damage:0s,},',
'5:{Slot:5b,id:"minecraft:iron_ingot",Count:64b,Damage:0s,},',
'6:{Slot:6b,id:"minecraft:gold_ingot",Count:64b,Damage:0s,},',
'7:{Slot:7b,id:"minecraft:bone",Count:64b,Damage:0s,},',
'8:{Slot:8b,id:"minecraft:string",Count:64b,Damage:0s,},',
'9:{Slot:9b,id:"minecraft:feather",Count:64b,Damage:0s,},',
'10:{Slot:10b,id:"minecraft:wool",Count:64b,Damage:0s,},',
'11:{Slot:11b,id:"minecraft:chicken",Count:64b,Damage:0s,},'
'12:{Slot:12b,id:"minecraft:porkchop",Count:64b,Damage:0s,},'
'13:{Slot:13b,id:"minecraft:beef",Count:64b,Damage:0s,},'
'14:{Slot:14b,id:"minecraft:glowstone",Count:64b,Damage:0s,},'
'15:{Slot:15b,id:"minecraft:leather",Count:64b,Damage:0s,},'
'16:{Slot:16b,id:"minecraft:vine",Count:64b,Damage:0s,},'
'17:{Slot:17b,id:"minecraft:carrot",Count:64b,Damage:0s,},'
'18:{Slot:18b,id:"minecraft:potato",Count:64b,Damage:0s,},'
'19:{Slot:19b,id:"minecraft:reeds",Count:64b,Damage:0s,},'
'20:{Slot:20b,id:"minecraft:cocoa",Count:64b,Damage:0s,},],'
'id:"Hopper",Lock:"",}'
)

sadrzaj=""
for to in djelovi2 :  
   sadrzaj = sadrzaj + to

bla = rel2abs ( orMj , ( 4  , 0 ,  0  ) , orSm )

# GENERIRA PUNU KUTIJU
mc.setBlockWithNBT(bla,54,1, sadrzaj )

"""

