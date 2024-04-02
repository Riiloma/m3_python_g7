def  sumar(x,y):
    """imprimir la suma de dos numeros

    Args:
        x (float): primer nuemro
        y (float): segundo numero
    """
    print(f"El resultado de la suma es {x+y}")

#lo que este bajo esta validacion solamete se ejecutara cuando se ejecute este archivo
if __name__ == '__main__':
    print("Probando el metodo sumar")
    sumar(4,6)