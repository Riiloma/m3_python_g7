import getpass# libreria que hace que cuando se escriba la contraseña no se vea
#password= getpass.getpass("Ingrese su contraseña")

password = input("Ingrese su contraseña")

if password == "12345":
    print("Password incorrecta")
elif len(password)<6:
    print("El password es demaciado corto")
