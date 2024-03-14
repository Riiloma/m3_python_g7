print("ADVERTENCIA: Porfavor ingresar Mayor a 0, no ingresar signos, no ingresar letras ")

#variables que piden valores
Precio_sus = float(input("Ingrese el precio de las suscripciones: "))
Numero_usuario = int(input("Ingrese le numero de Usuario: "))
Gastos_totales = float(input("Ingrese sus gastos totales: "))

#Calculo
Utilidades = Precio_sus * Numero_usuario - Gastos_totales

#Mostras datos
print(f"las urilidades son: {Utilidades}")