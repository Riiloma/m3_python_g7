#las divisiones dan desimanles
print(100/20)

#Simpre que una operacion tenga un desimal, dara como desimal
print(10+3.5)
print(10-3.5)
print(10*3.5)
print(10/3.5)

#String -> se ocupa con " " o con los ' '
print("hola")
nombre='livio'
print(nombre)

#duplicacion
edad="24"
print("texto"*12)
numero=100
print(3*numero) #la diferentcia es que si es numerico hace la operacion
# print("texto"/12) solo se puede con la multiplicacion, ERROR:TypeError: unsupported operand type(s) for /: 'str' and 'int'

#funcion type
print(type(nombre))#<class 'str'>
print(type(numero))#<class 'int'>

#metodo count
print("Elefante".count("Elefante"))#->podriamos usarla para detectar malas palabra por ejemplo y asi controlar comentarios y aun mas

#metodo upper() y lower()
print("Elefante".upper())#Mayusculas
print("Elefante".lower())#minuscula

#metodo title
print("hola".title())#hace que tengan la primera letra de cada palabra sea en mayusculas

#funcion len
print(len("Hola que tal"))
# print(len(123123)) ERROR:TypeError: object of type 'int' has no len()

#metodo join
print("".join(["a","b","c"]))#sirve para unir elementos separados, dentro del "" es el elemeneto separador,si se deja vacio salen todas juntas

#tipos de datos
entero = 7
decimal = 9.5
cadena = "esto es un cadena"
boleanos = True
print(type(entero))#<class 'int'>
print(type(decimal))#<class 'float'>
print(type(cadena))#<class 'str'>
print(type(boleanos))#<class 'bool'>

#manipulacion de variables
numero2=200
#numero2 = numero2 + numero
numero2 += numero # -> el += es mas cortito
print(numero2)

#presicion de datos de la interpolacion
promedio = (4+5+7)/3
print(f"el promedio es {promedio}")
print(f"resulta de la division {1/9:.2f}")
print(f"resulta de la division {round(1/9,2)}")
print(f"resulta de la division {promedio:.2f}")
print(f"resulta de la division {round(promedio,2)}")

#ingresando datos
nombre = input("Ingrese su nombre: ")
print(f"su nombre es: {nombre}")
edad = input("Ingrese su edad: ")
print(f"su edad es: {edad}")



