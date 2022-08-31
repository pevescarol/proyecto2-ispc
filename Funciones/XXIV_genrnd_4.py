from random import randrange

# Función genrnd que retorna una lista 
# con 500.000.000.000.000.000 números aleatorios

def genrnd():
    lista = []
    for i in range(5000000000000000000):
        lista.append(randrange(2))
    return lista


