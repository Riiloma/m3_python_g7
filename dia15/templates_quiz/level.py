def choose_level(n_pregunta, p_level):
    """_summary_

    Args:
        n_pregunta (int): almacena el numero de preguntas que quiere hacer el usuario
        p_level (int): entrega el nivel de la dificultad

    Returns:
        string: entre el rango del nivel a dependiendo de n_pregunta
    """
    # Construir lógica para escoger el nivel
    ##################################################
    if n_pregunta <= p_level:
        level = 'basicas'
    elif n_pregunta <= 2 * p_level:
        level = 'intermedias'
    else:
        level = 'avanzadas'

    ##################################################
    return level

if __name__ == '__main__':
    # verificar resultados
    print(choose_level(2, 2)) # básicas
    print(choose_level(3, 2)) # intermedias
    print(choose_level(7, 2)) # avanzadas
    print(choose_level(4, 3)) # intermedias