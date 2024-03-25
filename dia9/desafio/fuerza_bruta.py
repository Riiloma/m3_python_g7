from string import ascii_lowercase

password= input("Ingrese su contraseña: ").lower()
abc= ascii_lowercase

intentos= 0
lista_convinaciones=[]

# a = [str(letra+conbinacion) for letra in ascii_lowercase for conbinacion in len(ascii_lowercase)]

def convinaciones(long):
    for letra in ascii_lowercase:
        for conbinacion in convinaciones:
            lista_convinaciones.append(letra+conbinacion)
print(lista_convinaciones)

for long in range(1,len(password) + 1):
    for combinacion in convinaciones(long):
        intentos += 1
        if combinacion == password:
                print (combinacion, intentos)

print(f"La contraseña fue encontrada en {intentos}")

#codigo del Edinson
# def brute_force(password):
#     def combinaciones(long):
#         if long == 1: return list(ascii_lowercase)
#         else:
#             resultado = []
#             for letra in ascii_lowercase:
#                 for combinacion in combinaciones(long - 1):
#                     resultado.append(letra + combinacion)
#             return resultado

#     intentos = 0
#     for long in range(1, len(password) + 1):
#         for combinacion in combinaciones(long):
#             intentos += 1
#             #print(combinacion)
#             if combinacion == password:
#                 return combinacion, intentos

# pass_r, intentos = brute_force(password)
# print(f"La contraseña fue forzada en {intentos} intentos.")
# print(f"Tu contraseña es:{pass_r}")

#password = getpass.getpass("Ingrese la contraseña:")
# password = input("Ingrese la contraseña:").lower()

# letras_minusculas = ascii_lowercase
# print(letras_minusculas)
# contador = 0
#gato
#abcdefghijklmnopqrstuvwxyz
#7+1+21+14=43
# for caracter in password:
#     print(caracter)
#     for letra in letras_minusculas:
#         contador+=1
#         if caracter == letra:
#             break

# print(f" La contraseña fue forzada en {contador} intentos")