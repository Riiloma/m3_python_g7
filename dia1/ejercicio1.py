#esto es un comentario de una linea
""" 
comentario
de mas de 
una
linea 
"""

print("Hola mundo")
print(2+2)
print(2-2)
print(2*0)
#print(20/0) ERROR -> ZeroDivisionError: division by zero
print(20/5)
numero = 23
print(numero)
print("texto",numero)
#Python no permite sumar letras y numeros
#print("texto"+12) -> ERROR: TypeError: can only concatenate str (not "int") to str

#INTERPOLACION
print(f"el numero es {numero}")
nombre="livio"
#string.format
print("Tu nombre es {} y tu edad es {}".format(nombre,numero))
# formato con %: %s para string y %d para numeros
print("Tu nombre es %s y tu edad es %d" % (nombre,numero))
#metodo con cadena
apellido ="gutierrez valdebenito"#entrega con la primera letra en mayuscula aun que ponga una mayuscula al medio lo arregla
print(apellido.title())