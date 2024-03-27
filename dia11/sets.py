""" 
conjunto de datos  que no permiten duplicados
no son ordenadnos y se escriben ocn llaves
mustran las posisiones distintas
"""

muchos_animales = {'Gato', 'Perro', 'Tortuga',
'Gato', 'Perro', 'Tortuga',
'Gato', 'Perro', 'Tortuga',
'Gato', 'Perro', 'Tortuga',
'Hurón', 'Hamster', 'Erizo de Tierra'}
print(muchos_animales)

for elemento in muchos_animales:
    print(elemento)

muchos_animales.add("chancho")#añade un elemento
print("")
print(muchos_animales)
#muchos_animales.remove("leon")#da error si no encuentra el elemente
print(muchos_animales)

muchos_animales.discard("leon")#le da igual si no esta
print("")
print(muchos_animales)

muchos_animales.pop()#elimina un elemento al azar
print(muchos_animales)
muchos_animales.clear()#limpia todo
print("")
print(muchos_animales)

print(muchos_animales.__dir__())
print(dir(muchos_animales))