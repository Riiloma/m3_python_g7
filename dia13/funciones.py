def imprimir_menu():
    print('Opciones: ')
    print('1). De acuerdo')
    print('2). En desacuerdo')
    print('3). No me interesa')
    
def imprimir_respuestas():
    """
    print(f'La respuesta a la pregunta 1 fue {respuestas[0]}')
    print(f'La respuesta a la pregunta 2 fue {respuestas[1]}')
    print(f'La respuesta a la pregunta 3 fue {respuestas[2]}')
    """
    """for i in range(len(respuestas)):#[0,1,2] len(respuestas)=3
        print(f'La respuesta a la pregunta {i+1} fue {respuestas[i]}')
    """    
    for posicion, respuesta in enumerate(respuestas):
        print(f'La respuesta a la pregunta {posicion+1} fue {respuesta}')



preguntas = ['Enunciado Pregunta 1', 'Enunciado Pregunta 2','Enunciado Pregunta 3','Enunciado Pregunta 4']
respuestas = []

# Hacer preguntas
for pregunta in preguntas:
    print(pregunta)
    #llamado o invocacion
    imprimir_menu()
    respuestas.append(input('> '))
    print("")
    
print("")
#llamado o invocacion a la funcion
imprimir_respuestas()
