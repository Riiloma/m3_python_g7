import math

# gravedad = 9.8
# radio= 6371

gravedad = float(input("Ingrese el la gravedad del planeta: "))
radio = int(input("Ingrese el radio: "))

radio_metros = radio * 1000

resultado = (math.sqrt(2*gravedad*radio_metros))

print(f"el resulta: {resultado}")
