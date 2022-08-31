from XXX_max_1 import maximo
from XXIX_min_1 import minimo
# importo las funciones d emaximo y minimo

# Calcular el rango del vector obtenido en genrnd
# R = max - min


def rango(arr):
    rg = maximo(arr) - minimo(arr)
    return rg
