from XVIII_media import media

def varianza(arr):
    med = media(arr) #llamo a la funcion media
    n = len(arr)
    suma = 0
    for dato in arr:
        suma += (dato-med)**2
    varianza = suma/n
    return varianza