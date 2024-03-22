import sys
ventas = {
    "Enero": 15000,
    "Febrero": 22000,
    "Marzo": 12000,
    "Abril": 17000,
    "Mayo": 81000,
    "Junio": 13000,
    "Julio": 21000,
    "Agosto": 41200,
    "Septiembre": 25000,
    "Octubre": 21500,
    "Noviembre": 91000,
    "Diciembre": 21000,
}

argumento= int(sys.argv[1])
print("")
print(argumento)
print("")

nuevo_diccionario={}

for clave,valor in ventas.items():
    if valor > argumento:
        nuevo_diccionario[clave]=valor

print(nuevo_diccionario)

diccionario2={clave:valor for clave,valor in ventas.items() if valor > argumento}
print(diccionario2)

print("")
print("Fuera del for")