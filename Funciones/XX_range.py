from XXIII_max import maximo
from XXII_min import minimo
# importo las funciones d emaximo y minimo

# Calcular el rango del vector obtenido en genrnd
# R = max - min


def rango(arr):
    rg = maximo(arr) - minimo(arr)
    return rg

