

mascotas = {}

cant_mascotas = int(input("Ingrese cantidad de mascotas a ingresas"))#3

for i in range(cant_mascotas):#0,1,2
    
    mascota = {
        "nombre":"",
        "raza":"",
        "peso":0.0,
        "chip": False,
    }

    #Recorrer un diccionario default
    """for clave in mascota:
        #print(clave)
        mascota[clave] = input(f"Ingrese la {clave} de su mascota> ")
    """

    for key in mascota.keys():
        #print(key)
        mascota[key] = input(f"Ingrese la {key} de su mascota> ")

    print(mascota)

    print("")
    #Accedemos a los valores en nuestro diccionario
    for valor in mascota.values():
        print(valor)

    print("")
    for clave,valor in mascota.items():
        print(f"clave {clave} - valor {valor}")


    mascotas[mascota["nombre"]] = mascota
    #mascotas["zoe"] = mascota


print(mascotas)#
{
    'Zoe': {'nombre': 'Zoe', 'raza': 'bull', 'peso': '9', 'chip': 'si'}, 
    'ayun': {'nombre': 'ayun', 'raza': 'bull', 'peso': '12', 'chip': 'si'}, 
    'negrito': {'nombre': 'negrito', 'raza': 'chilenzis', 'peso': '30', 'chip': 'si'}
}

#acceder a un diccionario dentro de un diccionario
#mascotas["ayun"]            => {'nombre': 'ayun', 'raza': 'bull', 'peso': '12', 'chip': 'si'}
#mascotas["ayun"]["nombre"]  => "ayun"

#mascotas["ayun"].pop("nombre")

"""
mascotas= {
    1: {'nombre': 'zoe', 'raza': 'bull', 'peso': '9', 'chip': 'si'},
    2: {'nombre': 'ayun', 'raza': 'bull', 'peso': '12', 'chip': 'si'},
    
}
"""