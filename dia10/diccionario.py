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