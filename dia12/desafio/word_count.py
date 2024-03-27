import sys

archivo= sys.argv[1]

with open(archivo, "r") as file:
    texto=file.read()
    
    #usando set para quitar los caracteres repetidos y las palabras repetidas
    caracteres= set(texto)
    palabras= set(texto.split(" "))
    
    #comprobando resultados
    contando_caracteres= len(caracteres)
    contando_palabras= len(palabras)
    print("")
    print(f"la candidad de caracteres es: {contando_caracteres} y la cantidad de palabra es {contando_palabras}")