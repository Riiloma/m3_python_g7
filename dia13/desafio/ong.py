def cal_factorial(num_arg):
        if num_arg == 0:
            return 1
        else:
            #asignandole a una variable el argumento dado por si mismo -1
            res= num_arg*num_arg-1
        return res

def cal_productoria(datos):
    multiplicador=1
    for dato in datos:
        #multiplicando por el numero dado
        multiplicador*=dato
    return multiplicador 

#asignando los ** en el agumento para poder trabajar con mas de 1
def calcular (**args):
    for clave, valor in args.items():
        if "fact" in clave:
            print(f"El factorial de {valor} es {cal_factorial(valor)}")
        elif"prod" in clave:
            print(f"La productoria de {valor} es {cal_productoria(valor)}")

calcular (fact_1 = 5, prod_1 = [4, 6, 7, 4, 3], prod_2 = [3,6,4,2,8], fact_2 = 6)