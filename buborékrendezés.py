import random
elemek = []
for lista_i in range(0, 20):
    elemek.append(random.randint(0, 100))
print(elemek)
#rendezés
for ismetles_i in range(1, len(elemek)):
    for csere_i in range(len(elemek)-1):
        if elemek[csere_i] > elemek[csere_i+1]:
            segedvalt=elemek[csere_i]
            elemek[csere_i] = elemek[csere_i+1]
            elemek[csere_i+1] = segedvalt
print(elemek)