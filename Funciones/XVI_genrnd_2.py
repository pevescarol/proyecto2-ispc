import random

"""
función que devuelva el producto de las combinaciones posibles de los números
generados por la función genrnd tomados de a dos.
"""

def genrnd_producto(lista):
    for a in range(10):
        num = random.randint(1,50)
        num1 = random.randint(1,50)
        lista_2 = num * num1
        lista.append(lista_2)
    return lista

