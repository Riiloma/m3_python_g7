import requests
import json

url = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.delete(url)
print("")
print(type(response))
print("")
if response.status_code == 200:#200 -> delete
    print("Eliminacion exitosa")
    print(response.text)
else:
    print("Error en la cracion de put")
