from api import request_get
import template as t


#crando una funcion que recorral la URL
def pag_ave(url):
    """la funciona hace un for para añadir mediante un template la informacion

    Args:
        url (text): la url de la api

    Returns:
        _type_: retorna la subtitucion de body
    """
    response = request_get(url)# almacenando la funcion que hace la coneccion a la URL
    texto_img = ''
    for elementos in response:# For que recorre "response" y que va cambiando las cards
        #crenado las CARDS
        texto_img+=t.html_informacion.substitute(# aca se esta subtituyendo el template de informacion
            url=elementos["images"]["main"],# la variable url que esta en template "$url" se le asigna el elemento y la clave [images] y el valor [main]
            nombre_espanol=elementos["name"]["spanish"],
            nombre_ingles=elementos["name"]["english"])
        
    return t.html_template.substitute(body = texto_img)#aca se remplaza lo que es la va en "$body" por las "texto_img" que vendria siendo los card

llamando_funcion= pag_ave("https://aves.ninjas.cl/api/birds")#almacenando en una variable la funcion y pasandole la URL de la api
with open("dia17/prueba/index.html", "w", encoding='utf-8' ) as file: #creando la ruta donde se creara el archivo
    file.write(llamando_funcion)