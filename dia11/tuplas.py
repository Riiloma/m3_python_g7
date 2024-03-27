""" 
Tuplas
Conjunto de datos e inmutable
se escriben con parentecis
"""

tupla1= (1,2,3,4)
print(tupla1)
print(type(tupla1))#<class 'tuple'>

tupla2=("nombre","Mijail")
nom, texto= tupla2
print(nom)
print(texto)
print(tupla2[0])
print(tupla2[1])
#print(tupla2[2]) si no existe da error
#tupla2[1]= "hola" da error no se puede modificar

#iterar tupla
for num  in tupla1:
    print(num)
    
dicc1 = list({"nota1":5,"nota2":6}.items())#para transformar un diccionario a una lista ocupamos el metodo list
print(dicc1)#[('nota1', 5), ('nota2', 6)]
print(dicc1[0])