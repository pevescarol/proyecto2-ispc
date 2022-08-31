from XXIV_genrnd_4 import genrnd
from XXV_media_1 import media
from XXVI_median_1 import mediana
from XXVII_range_1 import rango
from XXVIII_variation_1 import varianza
from XXIX_min_1 import minimo
from XXX_max_1 import maximo


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


