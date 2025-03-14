from funciones import *
from variables import *
import pprint
import time

print("\n¡Hola marinero! Bienvenido al juego de Hundir la Flota 🚢💥⚓️\n")
print("Instrucciones del juego:")
print("Introduce tus coordenadas para disparar.\n")

# Crear los tableros del juego
tablero_computer = crear_tablero(TAMANO)
tablero_computer_visualizar = crear_tablero(TAMANO)
tablero_jugador = crear_tablero(TAMANO)
tablero_jugador_visualizar = crear_tablero(TAMANO)

print("Tablero vacío del ordenador:")
pprint.pprint(tablero_computer)

posicionar_barcos_fijos(tablero_computer)
print("\nTablero del ordenador con barcos fijos. Memorízalo en 5 segundos...\n")
visualizar(tablero_computer)
time.sleep(5)
limpiar_pantalla()

print("Tablero vacío del jugador:")
pprint.pprint(tablero_jugador)

# Colocar barcos en ambos tableros
colocar_barcos(tablero_jugador)
colocar_barcos(tablero_computer)

# Mostrar los tableros
print("Tablero del Jugador:")
imprimir_tablero(tablero_jugador)
print("Tablero del Ordenador (oculto):")
imprimir_tablero(tablero_computer_visualizar)

# Bucle principal del juego
while True:
    try:
        i = int(input("Introduce la fila, por favor: "))
        j = int(input("Introduce la columna, por favor: "))
        if i < 0 or i >= TAMANO or j < 0 or j >= TAMANO:
            print("Coordenadas fuera de rango. Intenta de nuevo.")
            continue
    except ValueError:
        print("Por favor, ingresa números válidos.")
        continue  # Volver a pedir los datos

    acierto = disparar(tablero_computer, tablero_computer_visualizar, i, j)

    if acierto:
        print("¡Acertaste!")
    else:
        print("¡Fallaste! Intenta nuevamente.")

    limpiar_pantalla()