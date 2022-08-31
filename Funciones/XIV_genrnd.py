from random import randrange

# Esta función retorna una lista con 50
#  números aleatorios.

def genrnd():
    lista = []
    for i in range(50):
        lista.append(randrange(100))
    return lista
