print("ADVERTENCIA: Porfavor ingresar Mayor a 0, no ingresar signos, no ingresar letras ")

#variables que piden valores
precio_sus = float(input("Ingrese el precio de las suscripciones: "))
numero_usuario = int(input("Ingrese le numero de Usuario: "))
numero_usuario_primium = int(input("Ingrese le numero de Usuario premium: "))
gastos_totales = float(input("Ingrese sus gastos totales: "))

#Calculo
utilidades_con_usuariosPremium = (precio_sus * 1.5 * numero_usuario_primium) * numero_usuario - gastos_totales
utilidades_con_usuariosnormales = precio_sus * numero_usuario - gastos_totales

#Mostras datos
print(f"las utilidades con los usuarios premiun son son: {utilidades_con_usuariosPremium}")
print(f"las utilidades con los usuarios normales son son: {utilidades_con_usuariosnormales}")