import requests

url = "https://reqres.in/api/users/6"

response = requests.delete(url)
print("")
print(type(response))
print("")

if response.status_code == 204:#200 -> revisar
    print("Eliminacion exitosa")
    print(response.text)
else:
    print("Error en la cracion de put")
