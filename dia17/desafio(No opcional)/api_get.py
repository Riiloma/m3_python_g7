import requests,json

url = "https://reqres.in/api/users"

payload = {}
headers = {}

response= requests.get(url)
users_data = response.json()


print(users_data["data"])#mostrando la informacion de los usuarios




# users_data = response.json()
# print(response[0].keys())
# print(type(users_data))
# # for clave, valor in users_data.items():
# #     print(f"Clave: {clave} Valor {valor}")
# # # print(users_data)