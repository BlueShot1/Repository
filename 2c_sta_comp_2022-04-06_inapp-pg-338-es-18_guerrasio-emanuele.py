import random

len1 = 10
max, min = 8, 1
vet = []
index = [0] * (max + 1)
vetSort = [0] * len1

for i in range(len1):
    tmp = random.randint(min, max)
    vet.append(tmp)
    index[tmp] = index[tmp] + 1

for i in range(1, max - 1):
    print(i)
    index[i] = index[i] + index[i-1]
print(index)
for i in range(len1):
    vetSort[index[vet[i]]] = vet[i]
    index[vet[i]] = index[vet[i]] - 1
print(vet)
print(vetSort)