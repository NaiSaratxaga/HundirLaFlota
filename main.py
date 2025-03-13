from funciones import *
from variables import *
from clases import *
import os
import pprint
import time

print()
print("!!Hola marinero!!, Bienvenido al juego de hundir la flota 🚢💥⚓️")

print()
print("Insrucciones del juego")
print("Introduce tus coordenadas,")
print()



tablero_computer = crear_tablero(TAMANO)
tablero_computer_visualizar = crear_tablero(TAMANO)
print()

print("Tablero vacío")
pprint.pprint(tablero_computer)


posicionar_barcos_fijos(tablero_computer)
print("\nTablero computer con barcos fijos. Te doy 5 segundos para que los memorices...\n") 

visualizar(tablero_computer)
time.sleep(5)
os.system("cls")
print()

tamano_tablero = 10

# Crear los tableros de los jugadores
tablero_jugador = crear_tablero(tamano_tablero)
tablero_ordenador = crear_tablero(tamano_tablero)

# Colocar barcos en ambos tableros
colocar_barcos(tablero_jugador)
colocar_barcos(tablero_ordenador)

# Imprimir los tableros
print("Tablero del Jugador:")
imprimir_tablero(tablero_jugador)

print("Tablero del Ordenador:")
imprimir_tablero(tablero_ordenador)

# Ejemplo de disparo del jugador
print("Disparo del jugador a la casilla (2, 3):")
disparo = disparar(tablero_ordenador, 2, 3)
print(f"Disparo acertado: {disparo}")
imprimir_tablero(tablero_ordenador)

while True:
    print("Tus disparos")
    visualizar(tablero_computer_visualizar)
    print("")
    i = int(input("Introduce la fila, por favor: "))
    j = int(input("Introduce la columna, por favor: "))
    acierto = disparo(tablero_computer, tablero_computer_visualizar, i, j)

    if acierto:
        print("¡Acertaste!")
    else:
        print("¡Fallaste! Intenta nuevamente.")
    
    os.system("cls")
    
    