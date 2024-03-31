import sys
precios = {'Notebook': 700000,
'Teclado': 25000,
'Mouse': 12000,
'Monitor': 250000,
'Escritorio': 135000,
'Tarjeta de Video': 1500000}

def filtrar_mayor(precios, umbral):
    filtro_mayor = {}
    for key, valor in precios.items():
        if valor > umbral:
            filtro_mayor[key] = valor
    return filtro_mayor

def filtrar_menor(precios, umbral):
    filtro_menor = {}
    for key, valor in precios.items():
        if valor < umbral:
            filtro_menor[key] = valor
    return filtro_menor

print(sys.argv)

if len(sys.argv) == 2:
    umbral= int(sys.argv[1])
    almacenando= filtrar_mayor(precios, umbral)
    print("Los productos mayores al umbral son: " + " ".join(almacenando))
    
elif len(sys.argv) == 3:
    umbral= sys.argv[2]
    criterio= sys.argv[2]
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