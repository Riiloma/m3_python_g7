"""
    CONDICIONAL IF  
    
    si se cumple la condicion entonces se ejecuta el codigo
    
    if condicion a evaluar:
        #Codigo a ejecutar si es verdadero
    elfi condicion a evaluar:
        #Codigo a ejecutar si es verdadero
    else:
        #Codigo a ejecutar si es verdadero
"""

edad = int(input("Ingrese su edad: "))

if edad == 18:
    print("Tienes 18")#1 tabulacion, si el mayor tiene una tabulacion de 4 todos tienen de a 4 si tiene 3 todos tienen 3
elif edad >= 19:
    print("Usted tiene mas de 18 años")
else:
    print("Eres menor de edad")

print("")
if edad == 0:
    print("La edad es 0")
elif edad%2 == 0:
    print("La edad es par")
else:
    print("La edad es impar")

print("")
print("Fin del programa")
