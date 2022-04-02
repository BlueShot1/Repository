import math
import random

#cambia queste 3 variabili a piacimento
baseN = 2
nMin = 0
nMax = 256

nRand = random.randint(nMin, nMax + 1)
nRandSalvato = nRand
nStr = ""
while nRand > 0:
    nStr = f"{nRand % baseN}{nStr}"
    nRand = math.floor(nRand / baseN)

#nStr per ora è un valore stringa ma puo essere convertito in qualsiasi momento

print(f"il valore {nRandSalvato} generato randomicamente tra {nMin} e {nMax} è stato convertito da base decimale a base {baseN} in {nStr}")

input("processo finito premere invio per continuare...")

#Guerrasio Emanuele 2C