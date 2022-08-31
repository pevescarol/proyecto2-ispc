import IV_sum
import VI_product
# Retorna el producto de los 2 primeros 
# más el 3er parámetro, usando las funciones anteriores

def p1(a,b,c):
    prod = VI_product.producto(a,b)
    resultado = IV_sum.suma(prod,c)
    return resultado

