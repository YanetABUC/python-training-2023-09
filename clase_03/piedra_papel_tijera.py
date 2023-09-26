"""
Jugador -> Piedra
Computadora -> Piedra
Empate

J -> Papel
C -> Piedra
Gané

C -> Tijera
J -> Papel
Perdí
"""
import random

OPCIONES = ["piedra", "papel", "tijeras"]

def obtener_opciones() -> dict:
    opcion_del_jugador = input("Elije una opción: (piedra, papel, tijeras): ")
    opcion_de_la_computadora = random.choice(OPCIONES)
    opciones = {
        "jugador": opcion_del_jugador,
        "computadora": opcion_de_la_computadora
    }
    return opciones

def obtener_resultado(opcion_jugador, opcion_computadora):
    print(opcion_jugador)
    print(opcion_computadora)
    if opcion_jugador == opcion_computadora:
        return "Es un empate!"
    else:
        if (opcion_jugador == "piedra" and opcion_computadora == "tijeras") or (opcion_jugador == "papel" and opcion_computadora == "piedra") or (opcion_jugador == "tijeras" and opcion_computadora == "papel"):
            return "El jugador ganó"           
    
    return "La computadora ganó"


opciones: dict = obtener_opciones()
resultado = obtener_resultado(opciones["jugador"], opciones["computadora"])
print(resultado)

