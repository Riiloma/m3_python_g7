def captura_datos():
    """Capturar los numeros ingresados

    Returns:
        tupla: par de numeros capturados
    """
    x=float(input("ingrese su primer numero"))
    y=float(input("ingrese su segundo numero"))
    
    return x,y

if __name__ == '__main__':
    print("Probando la captura de datos")
    print(captura_datos())