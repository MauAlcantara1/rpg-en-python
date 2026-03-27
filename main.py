import random
from salas import salas
import time

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

tipo = input("Elige la clase: ").lower()

while tipo not in clases:
    tipo = input("Clase no válida, elige otra: ").lower()

jugador = {
    "nombre": nombre,
    "vida": clases[tipo]["vida"],
    "vida_max": clases[tipo]["vida"],  
    "danio": clases[tipo]["danio"],
    "critico": clases[tipo]["critico"]
}

print("\nJugador creado:", jugador)

sala_actual = "inicio"

def intro():
    print("…Sistema iniciando…")
    time.sleep(1.2)

    print("\n[ERROR] Memoria corrupta")
    time.sleep(1)

    print("[ERROR] Soporte vital al 32%")
    time.sleep(1.2)

    print("\n—Reiniciando protocolo médico—")
    time.sleep(1.5)

    print("\n…")
    time.sleep(2)

    print("\nAbres los ojos.")
    time.sleep(1.5)

    print("\nEl techo blanco de la sala médica está agrietado.")
    time.sleep(1.5)

    print("Las luces parpadean con un zumbido constante.")
    time.sleep(1.5)

    print("\nTu respiración es irregular.")
    time.sleep(1.5)

    print("Sientes un dolor punzante en el pecho.")
    time.sleep(1.5)

    print("\nIntentas recordar algo… lo que sea.")
    time.sleep(2)

    print("\nPero no hay nada.")
    time.sleep(2)

    print("\nUn monitor cercano emite un pitido:")
    time.sleep(1.5)

    print("“Paciente inestable”")
    time.sleep(2)

    print("\nLa base lunar… está en silencio.")
    time.sleep(2)

    print("\nDemasiado silencio.")
    time.sleep(2.5)

    input("\nPresiona ENTER para continuar...")

intro()
while True:
    sala = salas[sala_actual]

    print("\n", sala["descripcion"])
    print(" Vida:", jugador["vida"], "/", jugador["vida_max"])

    print("\n¿Qué quieres hacer?")
    print("1. Investigar")
    print("2. Curar")
    print("3. Mover")
    print("0. Salir")

    accion = input("Elige una opción: ")

    if accion == "1":
        objetos = sala.get("objetos", {})

        if not objetos:
            print("No hay nada interesante aquí...")
        else:
            print("\n¿Qué quieres revisar?")
            for key, obj in objetos.items():
                print(key, "-", obj["nombre"])

            eleccion = input("Elige un objeto: ")

            if eleccion in objetos:
                obj = objetos[eleccion]
                print("\n" + obj["mensaje"])


                if obj["evento"] == "curar":
                    jugador["vida"] += 3
                    if jugador["vida"] > jugador["vida_max"]:
                        jugador["vida"] = jugador["vida_max"]
                    print(" Recuperas algo de vida")

            else:
                print("No existe esa opción")

    elif accion == "2":
        if jugador["vida"] < jugador["vida_max"]:
            jugador["vida"] += 2
            if jugador["vida"] > jugador["vida_max"]:
                jugador["vida"] = jugador["vida_max"]
            print("Te has curado un poco")
        else:
            print("Ya tienes la vida completa")

    elif accion == "3":
        print("\nOpciones de movimiento:")
        for opcion, datos in sala["opciones"].items():
            print(opcion, "-", datos["texto"])

        eleccion = input("¿A dónde quieres ir? ")

        if eleccion in sala["opciones"]:
            sala_actual = sala["opciones"][eleccion]["destino"]
        else:
            print("No puedes ir por ahí")

    elif accion == "0":
        print("Saliendo del juego...")
        break

    else:
        print("Opción inválida")