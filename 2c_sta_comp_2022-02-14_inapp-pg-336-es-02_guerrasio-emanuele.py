import random
nNumeri = 30
nPari = []
nDispari = []

for i in range(nNumeri):
    nGenerato = random.randint(10, 110)
    if nGenerato % 2 == 0:
        nPari.append(nGenerato)
    else:
        nDispari.append(nGenerato)
print("sono stati generati casualmente 30 numeri\n")
print("la lista di numeri pari è: ", nPari)
print("\nmentre la lista di numeri dispari è: ", nDispari)

input("\nprocesso terminato premere invio per continuare...")
#Guerrasio Emanuele 2C