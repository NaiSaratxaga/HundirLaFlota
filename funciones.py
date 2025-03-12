
import pprint
from clases import *


def crear_tablero(tamano):
    tablero = [[" " for i in range(tamano)] for j in range(tamano)]
    return tablero


def posicionar_barcos_fijos(tablero):
    tablero[3][3] = 'B'
    tablero[4][3] = 'B'
    tablero[5][3] = 'B'
    tablero[6][3] = 'B'

    tablero[1][0] = 'B'
    tablero[1][1] = 'B'
    tablero[1][2] = 'B'
    tablero[1][3] = 'B'
    
    
    
def disparo(tablero,tablero_mostrar,i,j):
    if tablero[i][j] == 'B':
        print("Tocado")
        tablero[i][j] = "X"
        tablero_mostrar[i][j] = "X"
        return True
    elif tablero[i][j] == "~":
        print("Agua")
        tablero[i][j] = "O"
        tablero_mostrar[i][j] = "X"
        return False
    else:
        print("¡Fallaste! has desperdiciando un tiro")
        return False
    
    
    
def visualizar(tablero):
    pprint.pprint(tablero)
    
    
    
def mensaje_bienvenida():
    print("Bienvenido al juego de Hundir La Flota 🚢🔥")
    print()
    
    
    
    
    
    
    