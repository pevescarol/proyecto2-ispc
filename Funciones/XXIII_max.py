# Devuelve el máximo del vector obtenido en genrnd

def maximo(arr):
    max = arr[0]
    for i in arr:
        if i > max:
            max = i
    return max

