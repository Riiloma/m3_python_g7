import requests
import json

def request_get(url):
    return json.loads(requests.get(url).text)#hace un pedido a la API y lo vuleve un .txt

response = request_get('https://jsonplaceholder.typicode.com/photos')#Almacena la API y trabaja con la funcion request_get
print(len(response))#Entrega lo largo de la lista

print("")
print("----Mostrando claves----")
print(response[0].keys())#Entrega la clave de la lista
print(type(response))

print("")
print("----Mostrando el contenido de cada clave----")
print(response[0])

# from string import Template
# img_template = Template('<img src="$url">')

# html_template = Template('''<!DOCTYPE html>
# <html>
# <head>
# <title>Título de la Página</title>
# </head>
# <body>
# <h1>Nuestra página Web</h1>
# $body
# </body>
# </html>
# ''')

# lista_url = [elemento['url'] for elemento in response]
# texto_img = ''
# for url in lista_url:
#     texto_img += img_template.substitute(url = url)+'\n'
# print(texto_img)
