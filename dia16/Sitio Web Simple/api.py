import requests
import json
from string import Template

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


img_template = Template('<img src="$teRemplazo">')

html_template = Template('''<!DOCTYPE html>
<html>
<head>
<title>Título de la Página</title>
</head>
<body>

<h1>Nuestra página Web</h1>

$teRemplazo

</body>
</html>
''')

lista_url = [elemento['url'] for elemento in response]
texto_img = ''

for url in lista_url:
    texto_img += img_template.substitute(teRemplazo= url)+'\n'
print(texto_img)

with open("dia17/prueba/index4.html", "a") as file:
    file.write(texto_img)


""" 
with open("index4.html", "a") as file:
    file.write(texto_img)

with open("index4.html", "a") as file: -> crea el archivo index4.html  y el "a" es para añadir el "w" es para escribir
    file.write(texto_img) -> mustra en pagina lo que esta en la api

"""
