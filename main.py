from funciones import *
from variables import *
from clases import *
import os
import pprint
import time



mensaje_bienvenida()
tablero_computer = crear_tablero(TAMANO)
tablero_computer_visualizar = crear_tablero(TAMANO)
#print("Tablero vacío")
#pprint.pprint(tablero_computer)
posicionar_barcos_fijos(tablero_computer)
print("Tablero computer con barcos fijos. Te doy 5 segundos para que los memorices...")
visualizar(tablero_computer)
time.sleep(5)
os.system("cls")
print()
while True:
    print("Tus disparos")
    visualizar(tablero_computer_visualizar)
    print("")
    i = int(input("Introduce la fila, por favor: "))
    j = int(input("Introduce la columna, por favor: "))
    acierto =  disparo(tablero_computer,tablero_computer_visualizar,i,j)
    if not acierto:
        break
    os.system("cls")