"""
Ciclo For

for variable in iterable

"""
#aca empieza asi [0,1,2,3,4,5,6,7,8,9]
for i in range(10):#->el 10 no lo cuenta, no concidera el ultimo elemento que le damos
    print(f"El valor de i es: {i}")

print("")

#aca empieza asi [4,5,6,7,8,9]
for i in range(4,10):# primer numero de donde empieza, segundo numero es donde termina 
    print(f"El valor de i es: {i}")


print("")

#aca empieza asi [4,6,8]
for i in range(4,10,2):#el tercero es el incremento
    print(f"El valor de i es: {i}")

"""
for en js:

for (let index = 4; index < 10; index++) {
    console.log(index);
}

"""
print("")
#Lista

numeros=[2,"4",True,3,"5",[2,5,8],{"clave":"valor"}]
for numero in numeros:#->la variable es singular en este caso "numero"
    print(numero)

print("")

texto= "Hola Mundo"#los string son parecidos a las listas
for caracter in texto:
    print(caracter)

print("")

#Diccionario

print("")

datos_personales= {
    "Nombre": "Livio",#Se componen de elementos (Clave:valor) y una ,
    "Apellido": "Gutierrez",
    "Edad": 24
}# se escribe con llavesitas

for clave in datos_personales:# Si trabajas con un For normal solo tendras la clave
    print(clave)

print("")

for clave in datos_personales:
    print(datos_personales[clave])# asi imprime los valores

print("")

for clave,valor in datos_personales.items():#Imprime clave y valor
    print(f"clave: {clave} - valor: {valor}")

print("")

for clave,valor in datos_personales.items():#Imprime clave y valor
    print(clave,valor)#Solo imprime la informacion sin coma ni nada

print("")

for par in datos_personales.items():#Imprime clave y valor entre parentecis
    print(par)


print("")

for clave in datos_personales.keys():#obtienes las claves
    print(clave)

print("")
for valor in datos_personales.values():#obtienes los valores
    print(valor)

print("")
#ENUMERATE
print("enumerate")
for posicion, caracter in enumerate(texto):
    print(f"la posicion {posicion} del caracter {caracter}")

print("")
for posicion, caracter in enumerate(numeros):
    print(f"la posicion {posicion} del caracter {caracter}")

print("")
for posicion, caracter in enumerate(datos_personales):
    print(f"la posicion {posicion} del caracter {caracter}")

print("")
prefijo = ['La','El','La','El']
frutas = ['manzana', 'platano','frutilla','tomate']
colores = ['verde','amarillo','roja','rojo']

for p, fruta, color in zip(prefijo, frutas, colores):#zip funciona si las listas tienen los mismo tamaños y le da mas importancia a la lista que tiene menos datos
    print(f'{p} {fruta} es de color {color}')

#Break
print("")
numeros=[2,"4",True,3,"5",[2,5,8],{"clave":"valor"}]
for numero in numeros:#->la variable es singular en este caso "numero"
    print(numero)
    if numero == 3:
        break
print("Fuera del for")