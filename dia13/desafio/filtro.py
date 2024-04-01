""" 
pruebas:
    python filtro.py 30000
    python filtro.py 30000 menor
    python filtro.py 30000 mayor
    python filtro.py 30000 otro
"""

import sys
#Diccionario
precios = {'Notebook': 700000,
'Teclado': 25000,
'Mouse': 12000,
'Monitor': 250000,
'Escritorio': 135000,
'Tarjeta de Video': 1500000}

#Funcion para la operacion del mayor que 
def filtrar_mayor(precios, umbral):
    filtro_mayor = {}
    for key, valor in precios.items():
        if valor > umbral:
            filtro_mayor[key] = valor
    return filtro_mayor

#Funcion para la operacion del menor que 
def filtrar_menor(precios, umbral):
    filtro_menor = {}
    for key, valor in precios.items():
        if valor < umbral:
            filtro_menor[key] = valor
    return filtro_menor

print(sys.argv)

#Invocando a la funcion filtar_mayor solo con el argumento en el indice 1
if len(sys.argv) == 2:
    umbral= int(sys.argv[1])
    almacenando= filtrar_mayor(precios, umbral)
    print("Los productos mayores al umbral son: " + " ".join(almacenando))
    
elif len(sys.argv) == 3:#detectando el largo de sys.argv
    umbral= sys.argv[1]
    criterio= sys.argv[2]
    
    #Invocando a la funcion filtar_mayor solo con el argumento en el indice 2 y 3
    if criterio == "mayor":
        umbral= int(sys.argv[1])
        almacenando= filtrar_mayor(precios, umbral)
        print("Los productos mayores al umbral son: " + " ".join(almacenando))
    elif criterio == "menor":
        umbral= int(sys.argv[1])
        almacenando= filtrar_menor(precios, umbral)
        print("Los productos menores al umbral son: " + " ".join(almacenando))
    elif criterio != "menor" and criterio != "mayor":
        print("Lo sentimos, no es una operación válida")