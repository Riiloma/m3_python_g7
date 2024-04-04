import requests,json

def request_get(url):
    """conecta la la API

    Args:
        url (string): direccion de API

    Returns:
        text: retorna informacion en formato texto y imagen
    """
    return json.loads(requests.get(url).text)


response = request_get('https://aves.ninjas.cl/api/birds')
