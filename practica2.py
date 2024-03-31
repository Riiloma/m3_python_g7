""" 
Analizando el codigo para comprender como funcionan las funciones y argumentos

"""


#asignando los ** en el agumento para poder trabajar con mas de 1
def calcular (**args):
    def cal_factorial(numero_fact):
            if numero_fact == 0:
                return 1
            else:
                #asignandole a una variable el argumento dado por si mismo -1 
                calculo_fact= numero_fact*cal_factorial(numero_fact-1)
                return calculo_fact
            
    def cal_productoria(datos):
        numero_multiplicador= 1
        #multiplicando por el numero dado
        for dato in datos:
            numero_multiplicador*=dato
        return numero_multiplicador
    
    #utilizando .item para recorrer cada argumento
    for clave, valor in args.items():
        if "fact" in clave:
            print(f"El factorial de {valor} es {cal_factorial(valor)}")
        elif "prod" in clave:
            print(f"La productoria de {valor} es {cal_productoria(valor)}")
    print("")

#Forma de invocar pasandole los argumentos 
calcular (fact_1 = 5, prod_1 = [4, 6, 7, 4, 3], fact_2 = 6)
calcular (fact_1 = 5, prod_1 = [3, 6, 4, 2, 8], fact_2 = 6)