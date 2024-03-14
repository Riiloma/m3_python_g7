import math

# gravedad = 9.8
# radio= 6371

gravedad = float(input("Ingrese el la gravedad del planeta: "))
radio = int(input("Ingrese el radio en Kilómetros: "))

radio_metros = radio * 1000

resultado = (math.sqrt(2*gravedad*radio_metros))

print(f"La velocidad de Escape es: {round(resultado,1)} [m/s]")
