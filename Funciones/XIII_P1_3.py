import V_rest as resta
import VI_product as producto 

def p1(a,b,c):
    # Retorna la resta de los 2 primeros 
    # por el 3er parámetro.
    res = resta.resta(a,b)
    resultado = producto.producto(res,c)
    return resultado