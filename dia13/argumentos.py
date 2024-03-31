def funcion_tuplas(*parametros): # (1, [2, 3], 'hola', {'clave': [4]})
    print(parametros)
    return parametros

output = funcion_tuplas(1,[2,3],'hola',{'clave':[4]})
print(type(output))#<class 'tuple'>


def funcion_dicc(**parametros):#{'valor': 1, 'texto': 'hola', 'lista_nombres': [4, 5, 6, 7]}
    print(parametros)
    return parametros

output = funcion_dicc(valor = 1, texto = 'hola', lista_nombres= [4,5,6,7])
print(type(output))