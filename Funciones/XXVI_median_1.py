
"""
función que calcule la mediana del vector obtenido en genrnd.
"""

def mediana(lista_numeros):
    lista_numeros.sort() # lo ordenamos
    longitud = len(lista_numeros)
    mitad = int(longitud/2)
    
    # si es par, promedio los elemenos del medio
    if longitud % 2 == 0:
        mediana = (lista_numeros[mitad+1] + lista_numeros[mitad]) / 2 
    else:
        # sino es la del medio
        mediana = lista_numeros[mitad]
    return mediana

