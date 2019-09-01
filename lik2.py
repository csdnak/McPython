#definicija objekta i poziv rutine za crtanje PROBA LOSHE NERADI
from crtanje import *		#tu je funkcija koju zovem
from mc import *			

mc = Minecraft() #inicijalizacija sustava za rad sa Minecraftom

#strelica
lik=[
[2,0,-1,STONE ,0],
[3,0,-1,STONE,0],
[4,-1,-1,STONE,0],
[4,0,-1,STONE,0],
[4,1,-1,STONE,0],
[5,0,-1,STONE,0],
]

#"neshto" :)
lik2=[
[2,0,-1,STONE,0],
[3,0,-1,STONE,0],
[4,-1,-1,STONE,0],
[4,0,-1,STONE,0],
[4,0,1,STONE,0],
[4,1,-1,STONE,0],
[5,0,-1,STONE,0],
[6,0,0,GOLD_BLOCK,0],
]


#zid sa prozorom
zid_prozor=[
[4,-1,0,1,0],
[4,0,0,1,0],
[4,1,0,1,0],
[4,-1,1,1,0],
[4,0,1,102,0],
[4,1,1,1,0],
[4,-1,2,1,0],
[4,0,2,1,0],
[4,1,2,1,0],

]

#zid sa vratima 

zid_ulaz = [
[4,-1,0,1,0],	#prvo nacrtamo zid sa rupom za vrata
[4,1,0,1,0],
[4,-1,1,1,0],
[4,1,1,1,0],
[4,-1,2,1,0],
[4,0,2,1,0],
[4,1,2,1,0],
[4,0,0,195,0], #i na kraju postavimo vrata prvo doljnji dio
[4,0,1,195,8], #8 govori da je ovo gornji dio vrata
]

brlog = [
[4,-1,0,1,0],	#prvo nacrtamo zid sa rupom za vrata
[4,1,0,1,0],
[4,-1,1,1,0],
[4,1,1,1,0],
[4,-1,2,1,0],
[4,0,2,1,0],
[4,1,2,1,0],
[4,0,0,195,0], #i na kraju postavimo vrata prvo doljnji dio
[4,0,1,195,8], #8 govori da je ovo gornji dio vrata
[5,-1,0,1,0],	#bocni zidovi
[5,1,0,1,0],
[5,-1,1,1,0],
[5,1,1,1,0],
[5,-1,2,1,0],
[5,1,2,1,0],
[6,-1,0,1,0],	#zadnji zid
[6,0,0,1,0],
[6,1,0,1,0],
[6,-1,1,1,0],
[6,0,1,1,0],
[6,1,1,1,0],
[6,-1,2,1,0],
[6,0,2,1,0],
[6,1,2,1,0],
[5,0,3,1,0],		# "Krov"
]

crtanje ( brlog )