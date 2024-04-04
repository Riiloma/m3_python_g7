import requests
import json

url = "https://reqres.in/api/users"

payload = json.dumps({
    "name": "Ignacio",
    "job": "Profesor"
})
headers = {
    'Content-Type': 'application/json'
}

created_user = requests.request("POST", url, headers=headers, data=payload)

print(created_user.text)
