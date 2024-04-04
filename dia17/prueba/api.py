import requests,json

def request_get(url):
    return json.loads(requests.get(url).text)
    
    # print(type(respuesta))

response = request_get('https://aves.ninjas.cl/api/birds')
