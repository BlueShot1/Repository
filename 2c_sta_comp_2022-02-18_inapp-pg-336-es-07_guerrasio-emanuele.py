lenList = 10
lista = []
print(f"dovrai inserire un insieme di numeri per {lenList} volte")
for i in range(lenList):
    temp = ""
    while not type(temp) == int:
        try:
            temp = int(input("Inserisci un numero: "))
        except:
            print("puoi solo inserire numeri interi...")
    if not lista.__contains__(temp):
        lista.append(temp)

print(f"\ni valori inseriti non ripetuti sono: {lista}")

input("processo finito premi invio per uscire...")

#Guerrasio Emanuele 2C