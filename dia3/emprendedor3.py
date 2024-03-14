print("ADVERTENCIA: Porfavor ingresar Mayor a 0, no ingresar signos, no ingresar letras ")

#variables que piden valores
Precio_sus = float(input("Ingrese el precio de las suscripciones: "))
Numero_usuario = int(input("Ingrese le numero de usuario normales: "))
Gastos_totales = float(input("Ingrese sus gastos totales: "))
Utilidades_pasadas = float(input("Ingrese sus utilidades pasadas: "))

#Calculo
Utilidades = Precio_sus * Numero_usuario - Gastos_totales

#Mostras datos
print(f"la razon entre la Utilidad actual y la Utilidad pasada es de: {round(Utilidades/Utilidades_pasadas,2)}")