tablero = [[" " for i in range(10)] for j in range(10)]

tablero

tablero
tablero[3][3] = 'B'
tablero[4][3] = 'B'
tablero[5][3] = 'B'
tablero[6][3] = 'B'
tablero


tablero[1][0] = 'B'
tablero[1][1] = 'B'
tablero[1][2] = 'B'
tablero[1][3] = 'B'
tablero


def disparo(tablero,i,j):
    if tablero[i][j] == 'B':
        print("Tocado")
        tablero[i][j] = "X"
        return True
    elif tablero[i][j] == " ":
        print("Agua")
        tablero[i][j] = "O"
        return False
    else:
        print("Ya habías disparado allí, inútil")
        return False
        


disparo(tablero,0,0)
tablero


disparo(tablero,1,0)
tablero

disparo(tablero,1,0)
tablero

while True:
    i = int(input("Introduce la fila, por favor"))
    j = int(input("Introduce la columna, por favor"))
    if not disparo(tablero,i,j):
        break