import random
import pprint
import os

def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")

def crear_tablero(tamano):
    return [[" " for _ in range(tamano)] for _ in range(tamano)]

def visualizar(tablero):
    pprint.pprint(tablero)

def imprimir_tablero(tablero):
    for fila in tablero:
        print(' '.join(fila))
    print()
    
    
def posicionar_barcos_fijos(tablero):
    # Ejemplo de posiciones fijas
    barcos = [(3,3), (4,3), (5,3), (6,3), (1,0), (1,1), (1,2), (1,3)]
    for x, y in barcos:
        tablero[x][y] = 'B'



def colocar_barcos(tablero, num_barcos=5):
    barcos_colocados = 0
    tamano = len(tablero)
    while barcos_colocados < num_barcos:
        x = random.randint(0, tamano - 1)
        y = random.randint(0, tamano - 1)
        if tablero[x][y] == " ":  # Si la casilla está vacía
            tablero[x][y] = "B"  # Colocamos un barco
            barcos_colocados += 1

def disparar(tablero, tablero_mostrar, x, y):
    if tablero[x][y] == "B":  # Acertamos un barco
        print("¡Tocado!")
        tablero[x][y] = "X"
        tablero_mostrar[x][y] = "X"
        return True
    elif tablero[x][y] == " ":  # Fallamos
        print("¡Agua!")
        tablero[x][y] = "O"
        tablero_mostrar[x][y] = "O"
        return False
    else:
        print("Ya disparaste aquí. Intenta en otra casilla.")
        return False
