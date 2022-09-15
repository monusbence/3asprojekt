import random
elemek = []
for lista_i in range(0, 20):
    elemek.append(random.randint(0, 100))
print(elemek)
#rendezés
i = len(elemek)-1
while i >= 1:
    cs= -1
    for j in range(0, i):
        if elemek[j]>elemek[j+1]:
            segedvalt = elemek[j]
            elemek[j] = elemek[j + 1]
            elemek[j + 1] = segedvalt
            cs = j
    i=cs
print(elemek)