import requests
import json

url = "https://jsonplaceholder.typicode.com/posts"

payload = json.dumps({
    "userId": 1,
    "title": "Titulo de ejemplo",
    "body": "Esto es un ejemplo"
})
headers = {
    'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)