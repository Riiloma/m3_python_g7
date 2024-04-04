import requests
import json

url = "https://jsonplaceholder.typicode.com/posts/1"

payload = json.dumps({
    "userId": 1,
    "title": "Titulo de ejemplo2",
    "body": "Esto es un ejemplo2"
})
headers = {
    'Content-Type': 'application/json'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)
