import preguntas as p
import random
from shuffle import shuffle_alt

# Opciones dadas para escoger.
###############################################
opciones = {'basicas': [1,2,3],
            'intermedias': [1,2,3],
            'avanzadas': [1,2,3]}
###############################################

def choose_q(dificultad):
    """permite escoger una preguna que no se haya echo

    Args:
        dificultad (int): entrega la dificultad

    Returns:
        list: entrega el enunciado y alternativas desordenadas
    """
    #escoger preguntas por dificultad
    preguntas = p.pool_preguntas[dificultad]
    #print(preguntas)
    # usar opciones desde ambiente global
    global opciones
    opciones_disponibles = opciones[dificultad]
    # escoger una pregunta
    n_elegido = random.choice(list(opciones_disponibles))
    #print(n_elegido)
    # eliminarla del ambiente global para no escogerla de nuevo
    opciones[dificultad].remove(n_elegido)
    
    
    # escoger enunciado y alternativas mezcladas
    pregunta = preguntas["pregunta_"+str(n_elegido)] 
    #print(pregunta)
    #random.shuffle(pregunta['alternativas'])
    alternativas = shuffle_alt(pregunta) #revisar
    alternativas = pregunta['alternativas']
    
    return pregunta['enunciado'], alternativas

if __name__ == '__main__':
    # si ejecuto el programa, las preguntas cambian de orden, pero nunca debieran repetirse
    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')
    
    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')
    
    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')