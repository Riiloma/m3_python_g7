print("ADVERTENCIA: Porfavor ingresar Mayor a 0, no ingresar signos, no ingresar letras ")

#variables que piden valores
precio_sus = float(input("Ingrese el precio de las suscripciones: "))
numero_usuario = int(input("Ingrese le numero de Usuario: "))
gastos_totales = float(input("Ingrese sus gastos totales: "))

#Calculo
utilidades = precio_sus * numero_usuario - gastos_totales

#Mostras datos
print(f"las urilidades son: {utilidades}")