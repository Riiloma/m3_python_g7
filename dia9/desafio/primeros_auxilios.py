print("Bienvenido a su consulta medica, por favor solo responda con si y no")
print("")

#ciclo while 
while True:
    
    #Pidiendo datos
    Estimulo= input("¿Responde a estumulos? ").lower()
    
    if Estimulo == "si":
        print("")
        print("Valorar la nesesidad de llavarlo al hospital mas cercano")
        break
    
    elif Estimulo == "no":
        print("Abrir la via Aéra")
        print("")
        
        #Pidiendo datos
        Respira= input("¿respira? ").lower()
        if Respira == "si":
            print("")
            print("Permitirle posicion de suficiente ventilacion")
            break

        elif Respira == "no":
            print("administrar 5 ventilaciones y llamar a Ambulancia")

        while True:
            
            #Pidiendo datos
            signos_de_vida= input("¿Signos de vida? ").lower()
            if signos_de_vida == "si":
                print("")
                print ("Reevalua a la espera de la Ambulancia")
                print("")
                
                #Pidiendo datos
                llego_abmulancia= input("¿Llego la Ambulancia? ").lower()
                if llego_abmulancia == "si":
                    exit()

            elif signos_de_vida == "no":
                print ("Administrar Compresiones Torácicas hasta que llegue ambulancia")
                print("")
                
                #Pidiendo datos
                llego_abmulancia= input("¿Llego la Ambulancia? ").lower()
                print("")
                if llego_abmulancia == "si":
                    exit()
    else:
        print("")
        print("Opcion incorrecta, por favor ingrece 'si' o 'no' ")
        print("")