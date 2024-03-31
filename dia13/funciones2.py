PI=3.14
IVA = 19

suma=4 #variable global

def sumar(numero1,numero2):
    #variable local
    suma = numero1 + numero2 
    return numero1 + numero2

#solo llamado a la funcion
sumar(14,15)

#imprimir el valor de retorno al llamar a la funcion
print(sumar(15,16))# print(31) # 31

#capturar el valor de retorno al llamar a la funcion
valor_retorno = sumar(16,17) # valor_retorno = 33
print(valor_retorno) # 33

print(suma)