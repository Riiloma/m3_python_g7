"""
while condicion: -> aca puede ir un True para que se repita infinitamente
    codigo -> pon un break cuando quieres que salga
"""

import  getpass

#password = input("Ingrese su contraseña: \n")\ este slash se crea con AltGr y con el botoncito al lado del 0

# while len(password) < 6:
#     password = input("Ingrese su contraseña nuevamente, tienen que tener 6 caracteres: \n")

# while password != "hola mundo":
#     password = input("Al parecer Ingreso su contraseña incorrectamente, ingresela nuevamente: \n")

# i= 0

# while i < 10:
#     print(f"El valor de i es : {i}")
#     i+=1
# print(f"fuera del while {i}")

saludos = "Hola"
saludos = saludos + " Mundo"
print(saludos)
saludos += "chao"
print(saludos)