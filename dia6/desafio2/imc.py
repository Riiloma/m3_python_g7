#Calculando IMC

#Ingresando datos
while True:# true es para que se repita INFINITAMENTE
        peso = float(input("Ingrese el peso en Kg: "))
        if peso == 0:
                print("El Valor no puede ser 0")
        else:
            break# esto hace que se detenga si se cumple la condicion -> (si se pone abajo se detiene el while)
        
while True:         
        altura_cm = float(input("Ingrese la altura en centímetros: "))
        if altura_cm == 0:
                print("El Valor no puede ser 0")
        else:
            break

#ajustando valores de cm a m
altura_m = altura_cm / 100
calculo_imc = peso/(altura_m**2)

print(f"Su IMC es {round(calculo_imc,2)} La clasificación OMS es: ",end="")# el end hace que se detenga y se ejecute el codigo de abajito

if calculo_imc < 18.5:
    print("Bajo peso")
elif 18.5 <= calculo_imc < 25:
    print("Adecuado")
elif 25 <= calculo_imc < 30:
    print("Sobrepeso")
elif 30 <= calculo_imc < 35:
    print("Obesidad Grado I")
elif 35 <= calculo_imc < 40:
    print("Obesidad Grado II")
else:
    print("Obesidad Grado III")

