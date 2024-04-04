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

import http.client

conn = http.client.HTTPSConnection("jsonplaceholder.typicode.com")
payload = ''
headers = {}
conn.request("GET", "/posts", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))