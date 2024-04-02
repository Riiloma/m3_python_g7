import preguntas as p

def print_pregunta(enunciado, alternativas):
    """permite mostrar por consola las arternativvas

    Args:
        enunciado (list): entrega el enunciado
        alternativas (string): muestra las alternativas
    """
    # Imprimir enunciado y alternativas
    ###############################################################
    #pass
    #Alfabeto = ['A','B','C']
    
    print(enunciado[0])
    resultado = [item for item in alternativas if item[1] == 1]
    print(f"Modo Trampa:{resultado}")
    for indice, alternativas in enumerate(alternativas, start=1):
        letra = chr(64 + indice)
        print(f"{letra}. {alternativas[0]}")
    ###############################################################
        
if __name__ == '__main__':
    # Las preguntas y alternativas deben mostrarse según lo indicado
    pregunta = p.pool_preguntas['basicas']['pregunta_1']
    print_pregunta(pregunta['enunciado'],pregunta['alternativas'])
    
    # Enunciado básico 1

    # A. alt_1
    # B. alt_2
    # C. alt_3
    # D. alt_4