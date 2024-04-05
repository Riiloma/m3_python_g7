import requests,json

def request_get(url):#crenado la funcion y pasandole el argumento url
    """conecta la la API

    Args:
        url (string): direccion de API

    Returns:
        text: retorna informacion en formato texto y imagen
    """
    return json.loads(requests.get(url).text)#pasando una peticion GET a la url y convirtiendola a un texto
