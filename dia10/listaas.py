""" 
LISTAS

()->tuplas
{}->diccionarios
[]->listas

Son contenedores de datos
Son mutables
Conjuntos de datos, separados por coma,ordenanos segun su ingreso
la primera posicion(indice) es 0

variable = [dato,dato,dato,...]
"""
from os import system

lista_pares= [2,4,6,8,10]#-> el tamaño de la lista es 5(cuenta los elemetos(datos) que tiene)
lista_vacia= []#-> esta lista es de 0 por que no tiene elementos(datos)

print("")
print(lista_pares)#-> siempre mostrara con [] para saber que es una lista
print([2,4,6,8,10])#-> siempre mostrara con [] para saber que es una lista

#Mostrando por posicion
print("")
print("Mostrando por posicion")
print(lista_pares[0])#2-> los elementos(datos) no se imprimen con corchete
print(lista_pares[1])#4
print(lista_pares[2])#6
print(lista_pares[3])#8
print(lista_pares[4])#10
# print(lista_pares[5])->IndexError: list index out of range

print("")
print(lista_pares[-1])#-> entrega el ultimo elemento(dato) de la lista, en este caso 10
print(lista_pares[-2])#8

print("")
print(len(lista_pares))#-> imprime el tamaño de la lista, en este caso es de 5
print(len(lista_vacia))#-> imprime el tamaño de la lista, en este caso es de 0

#Metodos de la listas

print("")
print(lista_pares.__dir__)#-> <built-in method __dir__ of list object at 0x00000265EB13D900> es un objeto
print(lista_pares.__dir__())#-> mustran muchos metodos que podemos usar en los objetos

#Metodo append(dato) => agrega un elemento(dato) al final de la lista

print("")
print("Metodo append")
lista_vacia.append("Lunes")#=> se ocupa para 1 dato 
"""
    lista_vacia.append("Lunes").append("Martes")
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AttributeError: 'NoneType' object has no attribute 'append'
"""
lista_vacia.append("Martes")
lista_vacia.append("Miercoles")
print(lista_vacia)

#Metodo insert()
print("")
print("Metodo insert")
lista_vacia.insert(3, "Jueves")#->['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado']
lista_vacia.insert(3, "Viernes")#-> ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Domingo', 'Sabado'] si se ocupa nuevamente la posicion los elementos se desplazan 
lista_vacia[3]="Jueves"#-> ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Sabado'] esto es remplazar
lista_vacia.insert(10, "Sabado")#-> si le asigna una posicion que no existe se agrega en la ultima posicion
print(lista_vacia)

#Metodo pop() => saca el ultimo elemento de la lista si no se espesifica la posicion
listas_eliminados= []
print("")
print("Metodo pop")
lista_vacia.pop(4)#-> si espesificas el dato sacara ese elemento['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Sabado']
listas_eliminados.append(lista_vacia.pop(0))
# eliminado= lista_vacia.pop(0)#-> si no se espesifica la posicion sacara el ultimo elemento
print(f"el elemento eliminado es: {listas_eliminados}")
print(lista_vacia)

#Metodo remove()
print("")
print("Metodo remove")
lista_vacia.remove("Martes")#-> borra el elemento dado
#lista_vacia.remove("a") ValueError: list.remove(x): x not in list
lista_vacia.remove("Jueves")#elimina la primera considencia de izquierda a derecha
lista_vacia.insert(0, "Martes")
lista_vacia.insert(0, "Lunes")
lista_vacia.insert(3, "Jueves")
lista_vacia.insert(4, "Viernes")
lista_vacia.append("Domingo")
print(lista_vacia)

#Metodo reverse() => invierte el orden de los elementos de una lista, el cambio es permanente
print("")
print("Metodo reverse")
lista_vacia.reverse()
print(lista_vacia)#->['Jueves', 'Sabado', 'Miercoles']

#Metodo sort() => ordena los elementos de forma asendente/alfaveticamente, es permanente
print("")
print("Metodo sort")
lista_vacia.sort
lista_pares.sort
print(lista_vacia)#['Domingo', 'Sabado', 'Viernes', 'Jueves', 'Miercoles', 'Martes', 'Lunes']
print(lista_pares)#[2, 4, 6, 8, 10]

#Respaldo de listas
print("")
print("Respaldo de listas")
#no se debe de hacer
lista1= lista_pares#-> no es hace un respaldo
print("Lista pares",lista_pares)

#Si se hace
lista2= lista_pares.copy()#-> asi se respalda una lista
lista3= lista_pares[:]#-> tambien es un respaldo de la lista original
lista4= lista_pares + []#-> otra forma pero no es muy limpea
lista5 =lista_pares*1
lista6= list(lista_pares)
# lista_pares.pop()
print(lista1)
print(lista2)
print(lista3)
print(lista4)
print(lista5)
print(lista6)

#Metodo sorted(lista,reverse= True)=ordena de manera desendente no es permamente
print("")
print("Metodo sorted")
sorted(lista_pares, reverse=True)
print(sorted(lista_pares, reverse=True))
print(lista_pares)

#Metodo index()=> retorna el indece del elemento que se busca en una lista
print("")
print("Metodo index")
print("indice del elemento 8 es: ",lista_pares.index(8))#3 posicion del elemento 8
#print("indice del elemento 13 es: ",lista_pares.index(13))ValueError: 13 is not in list

#Operaciones con las listas
print("")
print("Operaciones con las listas")
lista_final= lista_pares + lista_vacia#-> concatenan las listas
lista_final2= lista_pares*5#-> multiplican los elementos, los repite
print("lista final1: ", lista_final)
print("lista final2: ", lista_final2)