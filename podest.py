# crtanje automatizirani sorter
#definicija objekta i poziv rutine za crtanje
import time 
import sys
from crtanje import *		#tu je funkcija koju zovem

from mc import *			
mc = Minecraft() #inicijalizacija sustava za rad sa Minecraftom



"""
print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)
print '/give spavle axe'
"""

# origin ispred na sredini 
orMj = gdjeSam ()
orSm = gdjeGledam ()

#oakwood slab
materijal = 126
dv = 8


crtaj_kvadar ( orMj , ( 1  , -1 , -1 ) , ( 3 , 1 , -1 ) , orSm , materijal , dv ) # zrak iznad stepenica

