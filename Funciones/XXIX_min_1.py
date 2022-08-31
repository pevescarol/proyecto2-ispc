# Devuelve el mínimo del vector obtenido en genrnd

def minimo(arr):
    min = arr[0]
    for i in arr:
        if i < min:
            min = i
    return min
