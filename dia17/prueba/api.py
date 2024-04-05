import requests,json

def request_get(url):#crenado la funcion y pasandole el argumento url
    """se conecta a la API

    Args:
        url (string): direccion de API

    Returns:
        Diccionario: retorna informacion en formato texto y imagen
    """
    return json.loads(requests.get(url).text)#pasando una peticion GET a la url y convirtiendola a un texto
