import requests
import json
url = "https://reqres.in/api/users/2"

payload = {
    "name": "morpheus",
    "residence": "zion"
}
updated_user = requests.put(url, json=payload)

print(updated_user.text)
