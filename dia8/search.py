import sys,random

numero_buscar = int(sys.argv[1])
lista = [1,2,3,4,5,6,7,8,9,0]

random.shuffle(lista)#shuffle desordena la lista

print(lista)

for posicion, numero in enumerate(lista):# siempre con enumerate tiene que ir la variable posicion
    if numero_buscar == numero:
        print("")
        print("Numero encontrado")
        print(f"El numero {numero_buscar} esta en la posicion {posicion}")
        print("")
        break
    else:
        print(f"El numero no se encuentra en la posicion: {posicion}")

print("Fuera del for")

