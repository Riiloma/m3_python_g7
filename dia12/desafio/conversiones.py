import sys


#pidiendo datos
sol= float(sys.argv[1])
peso_argentino= float(sys.argv[2])
dolar_americano= float(sys.argv[3])
peso_chileno= float(sys.argv[4])

#operacion matematica
conversion_sol= sol*peso_chileno
conversion_peso_argentino= peso_argentino*peso_chileno
conversion_dolar_americano= dolar_americano*peso_chileno

print(f" el sol esta a: {conversion_sol}\n el peso argentino a: {conversion_peso_argentino} \n el dolar esta a: {conversion_dolar_americano} ")