cantidad_notas = float(input("Ingresa la cantidad de notas: "))
i= 0
suma_notas= 0

while i <= cantidad_notas:
    nota = float(input("Ingresa tu nota: "))
    suma_notas = suma_notas + nota
    i+=1
print(f"El promedio de notas es: {suma_notas/3}")