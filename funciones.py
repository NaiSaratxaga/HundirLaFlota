
import pprint



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
    
    tablero[1][8] = 'B'
    tablero[1][7] = 'B'
    tablero[1][6] = 'B'
    
    tablero[7][1] = 'B'
    tablero[7][2] = 'B'
  
   
    
def disparo(tablero,tablero_mostrar,i,j):
    if tablero[i][j] == 'B':
        print("Tocado")
        tablero[i][j] = "X"
        tablero_mostrar[i][j] = "X"
        return True
    elif tablero[i][j] == "O":
        print("Agua")
        tablero[i][j] = "O"
        tablero_mostrar[i][j] = "X"
        return False
    else:
        print("¡Fallaste! has desperdiciando un tiro")
        return False
    
    
    
def visualizar(tablero):
    pprint.pprint(tablero)
    
def imprimir_tablero(tablero):
    for fila in tablero:
        print(' '.join(fila))
    print() 
    
import random
import pprint



def crear_tablero(tamano):
    tablero = [[" " for i in range(tamano)] for j in range(tamano)]
    return tablero

def visualizar(tablero):
    pprint.pprint(tablero) 
    
# Función para imprimir el tablero
def imprimir_tablero(tablero):
    for fila in tablero:
        print(' '.join(fila))
    print() 

# Función para colocar barcos de manera aleatoria en el tablero
def colocar_barcos(tablero, num_barcos=5):
    barcos_colocados = 0
    tamano = len(tablero)
    while barcos_colocados < num_barcos:
        x = random.randint(0, tamano-1)
        y = random.randint(0, tamano-1)
        if tablero[x][y] == " ":  # Si la casilla está vacía
            tablero[x][y] = "B"  # Colocamos un barco
            barcos_colocados += 1

# Función para simular un disparo
def disparar(tablero, x, y):
    if tablero[x][y] == "B":  # Acertamos un barco
        tablero[x][y] = "X"
        return True
    elif tablero[x][y] == " ":  # Fallamos
        tablero[x][y] = ""
        return False
    return None



    
    
    
    
    
    
    