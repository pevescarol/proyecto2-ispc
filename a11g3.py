from Funciones import I_welcome, II_ing2i, III_ing2s
from Funciones import IV_sum,V_rest,VI_product,VII_quotient,VIII_module,IX_power,X_rationalization
from Funciones import XI_P1, XII_P1_2,XIII_P1_3
from Funciones import XIV_genrnd,XV_genrnd_1,XVI_genrnd_2,XXIV_genrnd_4
from Funciones import XVIII_media,XIX_median,XX_range,XXI_variation,XXII_min,XXIII_max
from Funciones import XXV_media_1,XXVI_median_1,XXVII_range_1,XXVIII_variation_1,XXIX_min_1,XXX_max_1
from Funciones import XXXI_time_1,XXXII_time_2

# Se muestra el cartel de presentacion
I_welcome.presentacion()

#
flag = True

###### funcion para preguntar si desea seguir viendo el menu
def sigue():
    resp = input("¿Deseas seguir? si / no\n>>> ")
    if resp.lower() == "si":
        flag = True
    elif resp.lower() == "no":
        flag = False
    else:
        print("Debes ingresar si o no!!")
    return flag
#############################

# mostrar menu
while flag:
    print("""
    ===============================
   =        MENU DE FUNCIONES      =
    ===============================""")
    print("""
    \t1 - Ingresar dos valores String
    \t2 - Función Suma
    \t3 - Función Resta
    \t4 - Función Producto
    \t5 - Función Cociente
    \t6 - Función Módulo
    \t7 - Función Potencia
    \t8 - Función Radicación
    \t9 - Función P1, producto y suma
    \t10 - Función P1, suma y producto
    \t11 - Función P1, resta y producto
    \t12 - Función genrnd, lista con 50 números aleatorios
    \t13 - Función suma de las combinaciones de genrnd
    \t14 - Función producto de las combinaciones de genrnd
    \t15 - Función calcular la media de genrnd
    \t16 - Función calcular la mediana de genrnd
    \t17 - Función calcular el rango de genrnd
    \t18 - Función calcular la varianza de genrnd
    \t19 - Función calcular el mínimo de genrnd
    \t20 - Función calcular el máximo de genrnd
    \t21 - Función genrnd 2, lista 500.000.000.000.000.000 números aleatorios
    \t22 - Función calcular la media de genrnd 2
    \t23 - Función calcular la mediana de genrnd 2
    \t24 - Función calcular el rango de genrnd 2
    \t25 - Función calcular la varianza de genrnd 2
    \t26 - Función calcular el mínimo de genrnd 2
    \t27 - Función calcular el máximo de genrnd 2
    \t28 - Calcular tiempo de ejecucion desde 15 y 20
    \t29 - Calcular tiempo de ejecucion desde 21 a 27
    \t0 - Salir
    """)
    opcion = int(input(">>> Selecciona una opción:"))

    if opcion == 1:
        # Pedir al usuario que ingres dos valores string
        v1, v2 = III_ing2s.ing2i()
        print(v1,v2)
        flag = sigue()
    elif opcion == 2:
        # Pedir al usuario que ingrese dos numeros enteros y los guardo en 2 variables
        n1, n2 = II_ing2i.ing2i()
        print(IV_sum.suma(n1,n2))
        flag = sigue()
    elif opcion == 3:
        n1, n2 = II_ing2i.ing2i()
        print(V_rest.resta(n1,n2))
        flag = sigue()
    elif opcion == 4:
        n1, n2 = II_ing2i.ing2i()
        print(VI_product.producto(n1,n2))
        flag = sigue()
    elif opcion == 5:
        n1, n2 = II_ing2i.ing2i()
        print(VII_quotient.cociente(n1,n2))
        flag = sigue()
    elif opcion == 6:
        n1, n2 = II_ing2i.ing2i()
        print(VIII_module.modulo(n1,n2))
        flag = sigue()
    elif opcion == 7:
        n1, n2 = II_ing2i.ing2i()
        print(IX_power.potencia(n1,n2))
        flag = sigue()
    elif opcion == 8:
        n1, n2 = II_ing2i.ing2i()
        print(X_rationalization.radicacion(n1,n2))
        flag = sigue()
    elif opcion == 9:
        n1, n2 = II_ing2i.ing2i()
        n3 = int(input("Ingresa otro numero más: "))
        print(XI_P1.p1(n1,n2,n3))
        flag = sigue()
    elif opcion == 10:
        n1, n2 = II_ing2i.ing2i()
        n3 = int(input("Ingresa otro numero más: "))
        print(XII_P1_2.p1(n1,n2,n3))
        flag = sigue()
    elif opcion == 11:
        n1, n2 = II_ing2i.ing2i()
        n3 = int(input("Ingresa otro numero más: "))
        print(XIII_P1_3.p1(n1,n2,n3))
        flag = sigue()
    elif opcion == 12:
        print(XIV_genrnd.genrnd())
        flag = sigue()
    elif opcion == 13:
        lista = XIV_genrnd.genrnd()
        print(XV_genrnd_1.genrnd_suma(lista))
        flag = sigue()
    elif opcion == 14:
        lista = XIV_genrnd.genrnd()
        print(XVI_genrnd_2.genrnd_producto(lista))
        flag = sigue()
    elif opcion == 15:
        lista = XIV_genrnd.genrnd()
        print(XVIII_media.media(lista))
        flag = sigue()
    elif opcion == 16:
        lista = XIV_genrnd.genrnd()
        print(XIX_median.mediana(lista))
        flag = sigue()
    elif opcion == 17:
        lista = XIV_genrnd.genrnd()
        print(XX_range.rango(lista))
        flag = sigue()
    elif opcion == 18:
        lista = XIV_genrnd.genrnd()
        print(XXI_variation.varianza(lista))
        flag = sigue()
    elif opcion == 19:
        lista = XIV_genrnd.genrnd()
        print(XXII_min.minimo(lista))
        flag = sigue()
    elif opcion == 20:
        lista = XIV_genrnd.genrnd()
        print(XXIII_max.maximo(lista))
        flag = sigue()
    elif opcion == 21:
        print(XXIV_genrnd_4.genrnd())
        flag = sigue()
    elif opcion == 22:
        lista2 = XXIV_genrnd_4.genrnd()
        print(XXV_media_1.media(lista2))
        flag = sigue()
    elif opcion == 23:
        lista2 = XXIV_genrnd_4.genrnd()
        print(XXVI_median_1.mediana(lista2))
        flag = sigue()
    elif opcion == 24:
        lista2 = XXIV_genrnd_4.genrnd()
        print(XXVII_range_1.rango(lista2))
        flag = sigue()
    elif opcion == 25:
        lista2 = XXIV_genrnd_4.genrnd()
        print(XXVIII_variation_1.varianza(lista2))
        flag = sigue()
    elif opcion == 26:
        lista2 = XXIV_genrnd_4.genrnd()
        print(XXIX_min_1.minimo(lista2))
        flag = sigue()
    elif opcion == 27:
        lista2 = XXIV_genrnd_4.genrnd()
        print(XXX_max_1.maximo(lista2))
        flag = sigue()
    elif opcion == 28:
        print(XXXI_time_1.tiempo())
        flag == sigue()
    elif opcion == 29:
        print(XXXII_time_2.tiempo())
        flag == sigue()
    elif opcion == 0:
        print("Uh que pena, adios!")
    else:
        print("La opción ingresada no es correcta! Ingresa de nuevo.")
        flag = False
