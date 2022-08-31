import IV_sum as suma
import VI_product as producto

# Retorna el producto de los 2 primeros 
# más el 3er parámetro, usando las funciones anteriores

def p1(a,b,c):
    sum = suma.suma(a,b)
    resultado = producto.producto(sum,c)
    return resultado

