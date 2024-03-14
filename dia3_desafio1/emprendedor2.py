print("ADVERTENCIA: si pone una letra en los valores dara ERROR")

#variables que piden valores
Precio_sus = float(input("Ingrese el precio de las suscripciones: "))
Numero_usuario = int(input("Ingrese le numero de Usuario: "))
Gastos_totales = float(input("Ingrese sus gastos totales: "))

#Calculo
Utilidades = (Precio_sus*1.5) * Numero_usuario - Gastos_totales

#Mostras datos
print(f"las urilidades son: {Utilidades}")