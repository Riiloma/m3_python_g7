import requests
import json

url = "https://jsonplaceholder.typicode.com/posts/1"

payload ={
    "userId": 1,
    "title": "Titulo de ejemplo2",
    "body": "Esto es un ejemplo2"
}

response = requests.put(url, json=payload)
if response.status_code == 200:#200 -> CREATE
    print("Insercion exitosa")
    print(response.text)
else:
    print("Error en la cracion de put")
