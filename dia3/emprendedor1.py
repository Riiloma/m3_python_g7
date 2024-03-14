print("ADVERTENCIA: si pone una letra en los valores dara ERROR")
Precio_sus = float(input("Ingrese el precio de las suscripciones: "))
Numero_usuario = int(input("Ingrese le numero de Usuario: "))
Gastos_totales = float(input("Ingrese sus gastos totales: "))

Utilidades = Precio_sus * Numero_usuario - Gastos_totales

print(Utilidades)