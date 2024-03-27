"""
DICCIONARIOS

Datos de pares, clave:valor

Diferencias de listas y diccionarios

difetencia 1:
    la accediamos a traves de la posiciones
    en los diccionarios a travez de la clave
direfencia 2:
    en las listas importa las posiciones
    en los diccionarios no importa la posicion, si no que la clave, no se genera automanticamente
diferencia 3:
    las listas son ordenadas
    los diccionario no son ordenados
diferencia 4:
    las listas las posiciones solamente numeros
    los diccionarios pueden ser las clases de tipo int string buleano
"""

lista = [25, 31, "hola"]#->aca se mueve por posicion
lista[2] # "hola"

diccionario = {1: "uno", "dos": 2, 3: "tres"}#-> 1: "uno", es 1 elemento, clave: valor(DATO: para organizacion tienes que tener un orden,las claves suelen ser string descriptivo)
diccionario[3] # "tres"

#Diccionario vacio
print("")
print("Diccionario vacio")
notas= {} 
print(len(notas))#muesta 0

notas = {
"Camila": 7,
"Antonio": 5,
"Felipe": 6,
"Daniela": 5,
"Vicente": 7,
"FELIPE": 7,
#"Vicente": 8, cuando se duplican las clave se sobre escribe con el que tenga el ultimo valor
}

print(len(notas))#muesta 5
print(notas)#{'Camila': 7, 'Antonio': 5, 'Felipe': 6, 'Daniela': 5, 'Vicente': 7}

#Acceso a los elemenntos(valores)
print("")
print("Acceso a los elemenntos")
print(notas["Camila"])#7
print(notas["Antonio"])#5
print(notas["Daniela"])#5
print(notas["Felipe"])#6
#print(notas["felipe"])KeyError: 'felipe'
print(notas["Vicente"])#7
print(notas)

print("")
print("Añadiendo dato")
notas["Julio"] = 4
print(notas)

#Modificar par clave:valor
print("")
print("Modificar dato")
notas["Julio"] = 5
print(notas)

#eliminar par clave:valor
print("")
print("Elimianar dato")
del notas["FELIPE"]# del borra completamente el dato
print(notas)

#2 forma pop()-> al eliminar, capturamos el valor
print("")
print("segunda fomra de Elimianar dato")
eliminado = notas.pop("Camila") #notas["Camila"]
print("valor eliminado : ",eliminado)#7
print(notas)
print("")

notas2 = {
    "Mijail":2,
    "Israel":1,
    "Felipe": 7,
    }

#notas.update(notas2)
#print(notas)#
notas2.update(notas)#->juntando 2 diccionarios
print(notas2)#

#COLISIONES: al existir la misma clave en la 2 listas el valor que tomara es el que esta entre (diccionario)

print("")
print("Imprimeindo claves")
print(notas2.keys())

print("")
print("Imprimeindo valor")
print(notas2.values())

print("")
print("Imprimeindo None")
print(type(None))

print("")
print("Imprimeindo items")#entrega una lista en forma de tupla, eso nos permite transformar en un diccionario a lista
print(notas2.items())

print("")
print("Imprimeindo get")#entrega el valor
print(notas2.get('Mijail'))
print(notas2.get('Alexis'))
print(notas2.get('Alexis', "valor no existe"))