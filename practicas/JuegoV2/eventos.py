import random

def caminar():
    """Hace la funcion de señalar una direccion hacia donde caminar
    """
    direcciones=["Norte", "Sur", "Este", "Oeste"]
    direccion= random.choice(direcciones)
    print(f"Caminaras hacia el: {direccion}")

def eventos_ruta():
    eventos_camino = [
    "Aparece un lago",
    "Encuentras un ladrón",
    "Te caes por un barranco",
    "Encuentras una cueva misteriosa",
    "Encuentras un cofre del tesoro",
    "Te encuentras con un comerciante ambulante",
    "Encuentras una bifurcación en el camino",
    "Encuentras un animal salvaje",
    "Encuentras una casa abandonada",
    "Te enfrentas a una tormenta",
    "Encuentras una fuente de agua fresca",
    "Te encuentras con un grupo de viajeros",
    "Encuentras un puente roto",
    "Encuentras un campo de flores silvestres",
    "Encuentras un antiguo templo",
    "Te encuentras con un anciano sabio",
    "Encuentras una cascada impresionante",
    "Te encuentras con un grupo de bandidos",
    "Encuentras una señal misteriosa",
    "Te enfrentas a un desafío de acertijos",
    "Encuentras un oasis en el desierto",
    "Te encuentras con una criatura mágica",
    "Encuentras un campamento de exploradores",
    "Te topas con una trampa",
    "Encuentras un río que bloquea tu camino",
    "Encuentras una planta medicinal",
    "Te encuentras con un viajero solitario",
    "Encuentras una estatua antigua",
    "Te enfrentas a una horda de monstruos",
    "Encuentras un mirador con vistas panorámicas",
    "Te encuentras con un mensajero misterioso"
]
if __name__ == "__main__":
    caminar()