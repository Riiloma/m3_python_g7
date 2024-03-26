print("ADVERTENCIA: Porfavor ingresar Mayor a 0, no ingresar signos, no ingresar letras ")

#variables que piden valores
precio_sus = float(input("Ingrese el precio de las suscripciones: "))
numero_usuario = int(input("Ingrese le numero de usuario normales: "))
gastos_totales = float(input("Ingrese sus gastos totales: "))
utilidades_pasadas = float(input("Ingrese sus utilidades pasadas: "))

#Calculo
utilidades = precio_sus * numero_usuario - gastos_totales

#Mostras datos
print(f"la utilidad es de {utilidades} y la razon entre la Utilidad actual y la Utilidad pasada es de: {round(utilidades/utilidades_pasadas,2)}")