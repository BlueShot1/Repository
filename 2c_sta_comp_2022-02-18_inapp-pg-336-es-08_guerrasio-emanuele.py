vettore = []
strHas = ""
n = ""

while not type(n) == int:
    try:
        n = int(input("inserisci quanti valori vuoi aggiungere: "))
    except:
        print("puoi inserire solo valori numerici interi...")

for i in range(n):
    vettore.append("")
    while not type(vettore[i]) == int:
        try:
            vettore[i] = int(input(f"inserisci {i + 1}° valore: "))
            strHas = f"{strHas}\n numero {vettore[i]}: "
            for x in range(vettore[i]):
                strHas = f"{strHas}*"
        except:
            print("puoi inserire solo valori numerici interi...")

input(f"{strHas}\n\n processo finito premi invio per uscire...")
#Guerrasio Emanuele 2C