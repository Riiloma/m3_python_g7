""" 
Según el número con el que se inicia la             Algunos de los códigos de respuesta más relevantes son:
respuesta, será de distinto tipo:
● 1xx: Información.                                 ● 200: Ok.
● 2xx: Solicitudes exitosas.                        ● 401: Unauthorized.
● 3xx: Redireccionamiento.                          ● 403: Forbidden.
● 4xx: Error del cliente (no hizo la                ● 404: Not Found.
request correctamente). 
● 5xx: Error del servidor (no puede dar             ● 500: Server error.
una respuesta).

"""

import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

payload = {}#datos a enviar
headers = {}#formato o tipo de datos que enviaremos

# response = requests.request("GET", url, headers=headers, data=payload)

response= requests.get(url)

print("")
print(response)#<Response [200]>

if response.status_code == 200:#el 200 significa OK
    # print(response.text)#convierte la respuesta en un string
    print(response.json())#convierte la respuesta en un json
    respuesta = response.json()
    print("")
    print(respuesta["title"])
    
    for clave, valor in respuesta.items():#no sale items() por que no sabe que es un diccionario, tienes que escribirlo tu
        print(f"clave: {clave} - valor: {valor}")
else:
    print(f"Error {response.status_code}")