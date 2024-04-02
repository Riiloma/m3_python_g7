
def validate(opciones, eleccion):
    """Capta el valor del usuario y luego lo compara
        si no esta en la opciones, entra en bucle hasta que elija un numero valido

    Args:
        opciones (string): almacena el valor en este caso 0 o 1
        eleccion (string): alamacena el valor que ingreso el usuario

    Returns:
        string: entrega la eleccion que ingreso el usuario 
    """
    # Definir validación de eleccion
    ##########################################################################
    while eleccion not in opciones:
        print(f"Opción no válida. Ingrese una de las opciones válidas: {opciones}")
        eleccion = input("Por favor, ingrese su elección: ").lower()
    
    ##########################################################################
    return eleccion


if __name__ == '__main__':
    
    eleccion = input('Ingresa una Opción: ').lower()
    # letras = ['a','b','c','d'] # pueden probar con letras también para verificar su funcionamiento.
    numeros = ['0','1']
    # Si se ingresan valores no validos a eleccion debe seguir preguntando
    validate(numeros, eleccion)