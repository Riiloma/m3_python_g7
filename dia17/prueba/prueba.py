

print(type(nombres))
print(type(imagenes))

texto_img = ''
for elementos in imagenes:
    texto_img += html_template.substitute(url_img = elementos)

with open("dia17/prueba/index2.html", "w") as file:
    file.write(texto_img)

""" 
imagenes= [print(valor('full')) for valor in respuesta if valor.get("images")]

print(f"Nombres: {nombres}")
print(f"Imagenes: {imagenes}")

with open("index4.html", "a") as file:
    file.write('<img src="$url">')


# def obteniendo_informacion():
# #    #for para optener el Nombre
#     for clave,valor in enumerate(respuesta):#recorre la lista
#         diccionario= valor#<class 'dict'>
#         nombre= diccionario["name"]
        
#         for clave, valor in nombre.items():
#             if clave == 'spanish':
#                 print(f"Nombre: {valor}")

#     for clave,valor in enumerate(respuesta):    # -> recorre la lista
#         diccionario= valor  # -> Almacena los valores de los diccionarios
#         imagen= diccionario["images"]   # -> busca la clave images
        
#         for clave, valor in imagen.items(): # -> Recorre los i
#             if clave == 'full':
#                 print(f"Imagen: {valor}")

"""
