import random

lista_1 = []

def genrnd_suma(lista):
    for a in range(10):
        num = random.randint(1,50)
        num1 = random.randint(1,50)
        lista_2 = num + num1
        lista.append(lista_2)
    return lista