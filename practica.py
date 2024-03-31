""" 
Notas: 
    Si no responde el usuario hacer un elif donde salga un mensaje ¡vamos! es de mala educacion no responderle a alguien
    Agregale un menu a esto xD
"""

import random,time

puntos_cardinarle= ["Norte", "Sur", "Este", "Oeste"]
Objetos= []
hora= ["10:00 a.m."]

print("-----Bienvenido al Juego-----")
time.sleep(0.8)
print("")

nombre_jugador= input("Ingrese su nombre: ")
time.sleep(0.8)

print("")
print(f"-> ¡Bienvenido! {nombre_jugador}")
time.sleep(0.8)
print("")

print("-> Las reglas son simples! solo podras decir si o no todo lo demas lo hara la suerte \n veamos hacia donde te dirigiras")
time.sleep(0.8)

direccion= random.choice(puntos_cardinarle)
print("")
print(f"-> ¡Genial! te toca ir al {direccion}")
time.sleep(0.8)
print("")

respuesta= input(f"-> Obviamente era una prueba... quiere ir de verdad a {direccion}: ").lower()

if respuesta == "si":
    print(f"-> ¡Perfecto! por que no te iba a cambiar la ruta jajajaja... ¡ahora... A EXPLORAR!")
    time.sleep(0.8)
else:
    print(f"-> que pena... por que no te voy a cambiar la ruta jajajaja... ¡ahora... A EXPLORAR!")
    time.sleep(0.8)

print("")
print("* Luego de unas horas caminando *")
time.sleep(0.8)
print("")

respuesta= input(f"-> ¡Mira! ¡una laguna! son solamente las {hora} ¿quieres pescar?: ").lower()

while True:
    if respuesta == "si":
        num_random= random.randint(1,20)
        if num_random > 10:
            print("")
            print(f"-> ¡FANTASTICO! ¡has pescado algo!" )
            time.sleep(0.8)
            print("")
            
            Objetos.append("-> pescado")
            print(f"-> El objeto: pescado se a sumado al bolso")
            time.sleep(0.8)
            print(f"tus objetos son: {Objetos}")
            break
        else:
            print("")
            respuesta= input(f"-> No has pescado nada, ¿quieres quedarte mas tiempo?: ").lower()
            if respuesta == "si":
                if num_random > 10:
                    hora=["11:00 a.m."]
                    print(f"-> ¡buena desicion! y solamente son las {hora}")
                    time.sleep(0.8)
                    print("")
                    
                    print(f"-> El objeto: pescado se a sumado al bolso")
                    time.sleep(0.8)
                    print(Objetos)
                    break
                else:
                    print("")
                    print("-> mejor vamos... ya ha pasado una hora")
                    time.sleep(0.8)
                    break
    else:
        print(f"-> Okey, tu te pierdes la aventura")
        time.sleep(0.8)
        break
print("")
print("¡Sigamos!")
time.sleep(0.8)
hora=["12:00 a.m."]
print(hora)