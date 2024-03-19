import random

#crear un programa para jugar cachipun
opciones = ["piedra", "papel", "tijera"]
juego_pc= random.choice(opciones)
print(juego_pc)

while True:
    juego_usuario= input("ingresar juego cachipun (Debe ser piedra, papel o tijera.): ").lower()
    if juego_usuario in opciones:
        break
    else:
        print(f"opcion no valida")
        
print(f"{juego_usuario}")

print(f"la computadora jugo {juego_pc} y tu jugaste {juego_usuario}")

if juego_pc == juego_usuario:
    
    print("empate")
    
elif (juego_usuario=="piedra" and juego_pc=="tijera") or \
    (juego_usuario=="tijera" and juego_pc=="papel") or \
    (juego_usuario=="papel" and juego_pc=="piedra"):
    
    print("ganaste")
    
else:
    print("perdiste")