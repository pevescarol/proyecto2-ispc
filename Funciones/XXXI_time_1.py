from XIV_genrnd import genrnd
from XVIII_media import media
from XIX_median import mediana
from XX_range import rango
from XXI_variation import varianza
from XXII_min import minimo
from XXIII_max import maximo


import time
# usaremos la libreria time para medir el tiempo de ejecución

def tiempo():
    inicio = time.time()
    lista = genrnd()
    print("La media del vector obtenido es: ", media(lista))
    print("La mediana del vector obtenido es: ",mediana(lista))
    print("El rango del vector obtenido es: ", rango(lista))
    print("La varianza del vector obtenido es: ", varianza(lista))
    print("El mínimo del vector obtenido es: ", minimo(lista))
    print("El máximo del vector obtenido es: ", maximo(lista))
    fin = time.time()
    return "El tiempo de ejecución es de: ", fin - inicio

