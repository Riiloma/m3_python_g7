import math

#Datos de prueba
# gravedad = 9.8
# radio= 6371

#Pidiendo datos
gravedad = float(input("Ingrese la gravedad del planeta: "))
radio = int(input("Ingrese el radio en Kilómetros: "))

#Pasndo radio de kilometros a metros
radio_metros = radio * 1000

#Formula para saber la velocidad de escape
resultado = (math.sqrt(2*gravedad*radio_metros))

#Mostrandole al usuario la velocidad de escape al usuario
print(f"La velocidad de Escape es: {round(resultado,1)} [m/s]")
