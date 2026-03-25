import random

print("Selecciona un nombre para tu heroe")

nombre = input()
clases = {
    "soldado": {"vida": 15, "danio": 6, "critico": 3, "energia": 2},
    "medico": {"vida": 12, "danio": 3, "critico": 2, "energia": 5},
    "ingeniero": {"vida": 10, "danio": 4, "critico": 3, "energia": 4},
    "explorador": {"vida": 11, "danio": 5, "critico": 4, "energia": 3}
}

print("Clases disponibles:")
for clase in clases:
    print("-", clase)

tipo = input("Elige la clase ").lower()

while tipo not in clases:
    tipo = input("Clase no válida, elige otra: ").lower()

jugador = {
    "nombre": nombre,
    "vida": clases[tipo]["vida"],
    "danio": clases[tipo]["danio"],
    "critico": clases[tipo]["critico"]
}

print (jugador)

salas = {
    "inicio": {
        "descripcion": "Estás en la entrada de la base lunar abandonada",
        "opciones": {
            "1": "laboratorio",
            "2": "pasillo"
        }
    },
    "laboratorio": {
        "descripcion": "Un laboratorio destruido con luces parpadeantes",
        "opciones": {
            "1": "inicio"
        }
    },
    "pasillo": {
        "descripcion": "Un pasillo oscuro y silencioso",
        "opciones": {
            "1": "inicio",
            "2": "sala_control"
        }
    },
    "sala_control": {
        "descripcion": "La sala de control principal",
        "opciones": {
            "1": "pasillo"
        }
    }
}

sala_actual = "inicio"
while True:
    sala = salas[sala_actual]

    print("\n" + sala["descripcion"])

    for opcion, destino in sala["opciones"].items():
        print(opcion, "->", destino)

    eleccion = input("¿A dónde quieres ir? ")

    if eleccion in sala["opciones"]:
        sala_actual = sala["opciones"][eleccion]
    else:
        print("No puedes ir por ahí")

