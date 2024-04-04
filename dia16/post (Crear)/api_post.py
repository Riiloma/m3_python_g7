import requests
import json

url = "https://jsonplaceholder.typicode.com/posts"

payload ={
    "userId": 1,
    "title": "Titulo de ejemplo",
    "body": "Esto es un ejemplo"
}

response = requests.post(url, json=payload)
if response.status_code == 201:#201 -> CREATE
    print("Insercion exitosa")
    print(response.text)
else:
    print("Error en la cracion de posts")
