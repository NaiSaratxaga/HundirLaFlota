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
print("Introduce tus coordenadas, fila y columna")
print()


# mensaje_bienvenida()
tablero_computer = crear_tablero(TAMANO)
tablero_computer_visualizar = crear_tablero(TAMANO)
print()

""" print("Tablero vacío")
pprint.pprint(tablero_computer)
 """
imprimir_tablero
pprint.pprint(tablero_computer)

posicionar_barcos_fijos(tablero_computer)
print("Tablero computer con barcos fijos. Te doy 5 segundos para que los memorices...")
visualizar(tablero_computer)
time.sleep(5)
os.system("cls")
print()


while True:
    coordenadas = input("Introduce coordenadas (x y): ")
    
    # Validar entrada
    # Elimina los espacios y verifica si solo hay números.
    try:

        x, y = map(int, coordenadas.split(","))

        if x < 0 or x >= 9 or y < 0 or y >= 9:
            print("Coordenadas fuera del tablero, intenta de nuevo.")
            continue  # Repite el ciclo sin continuar

    # Si las coordenadas son válidas, salir del bucle
        break
    except Exception:
        print("coordenadas no válidas")

    os.system("cls")

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
    
    