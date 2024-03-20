import sys,time

print(sys.argv) # nos entrega una lista despues de python, basicamente se crean automaticas
print(sys.argv[0])
print(sys.argv[1])

i= int(sys.argv[1])

while i > 0:
    print(f"el valor de i es: {i}")
    time.sleep(1)#tiempo de espera 1 segundo
    i-=1
print(f"perdiste el tiempo llego a: {i} has hecho KA BOOM!")