#Modulos
import eventos

#Librerias
import time

Nombre= input("Introduse su nombre de explorador: ")
time.sleep(0.5)

while True:
    menu=  int(input("""
Menu:
---------------------------
1. Caminar  2. Invitario
3. Pezcar   4. Comer
5. Dormir
-> """))
    if menu == 0 or menu >5:
        print("")
        print("opcion no valida")
        time.sleep(0.5)
    else:
        break
time.sleep(0.5)

print("")
if menu == 1:
    print("----------------------")
    eventos.caminar()
    print("----------------------")
else:
    print("Opcion no valida")