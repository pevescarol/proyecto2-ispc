def mediana(arr):
    #arr = funcion12.genrnd() # el vector obtenido de la funcion genrnd
    arr.sort() # lo ordenamos
    longitud = len(arr)
    mitad = int(longitud/2)
    
    # si es par, promedio los elemenos del medio
    if longitud % 2 == 0:
        mediana = (arr[mitad-1] + arr[mitad]) / 2 
    else:
        # sino es la del medio
        mediana = arr[mitad]
        
    return mediana