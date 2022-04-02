import random
numele = []

#variabili modificabili
nLenght = 15
nMinVal = 10
nMaxVal = 80

#variabili da non toccare
valMax = nMinVal - 1
valMaxPos = 0
valMin = nMaxVal + 1
valMinPos = 0


for i in range(nLenght):
    numele.append(random.randint(nMinVal, nMaxVal + 1))
    if numele[i] >= valMax:
        valMax = numele[i]
        valMaxPos = i
    if numele[i] < valMin:
        valMin = numele[i]
        valMinPos = i

print("L'array con i valori generati casualmente è: ", numele, "\n")

valTemp = numele[valMaxPos]
numele[valMaxPos] = numele[valMinPos]
numele[valMinPos] = valTemp

print("L'array con i valori maggiori e minori scambiati è: ", numele, "\n")
print("si è scambiato il valore '{}' alla posizione '{}' con il valore '{}' alla posizione '{}'".format(numele[valMinPos], valMinPos + 1, numele[valMaxPos], valMaxPos + 1))
input("processo finito clicca invio per continuare...")

#Guerrasio Emanuele 2C