#Devuelve el mínimo del vector obtenido en genrnd

def minimo(lista):
    min = lista[0]
    for i in lista:
        if i < min:
            min = i
    return min