from api import request_get
import template as t


def pag_ave(url):
    response = request_get(url)
    texto_img = ''
    for elementos in response:
        texto_img+=t.html_informacion.substitute(
            nombre_espanol=elementos["name"]["spanish"],
            nombre_ingles=elementos["name"]["english"],
            url=elementos["images"]["main"])
        
    return t.html_template.substitute(body = texto_img)

a= pag_ave("https://aves.ninjas.cl/api/birds")
with open("dia17/prueba/index2.html", "w") as file:
    file.write(a)