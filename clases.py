import pprint
from funciones import *

class Tablero:
    def __init__(self):
        self.tablero =  [[" " for _ in range(TAMANO)] for _ in range(TAMANO)]
       
    def poner_barco(self, orientacion, posicion_inicial_fila, posicion_inicial_columna, tamano_barco):
        indice_inicial_fila = posicion_inicial_fila - 1
        indice_inicial_columna = posicion_inicial_columna - 1
        for i in range(tamano_barco):
            if orientacion == "H":
                self.tablero[indice_inicial_fila][indice_inicial_columna + i] = "B"
            elif orientacion == "V":
                self.tablero[indice_inicial_fila + i][indice_inicial_columna] = "B"
                        
    def recibir_disparo(self, fila, columna):
        valor_coordenada = self.tablero[fila - 1][columna - 1]
        if valor_coordenada == "B":
            self.tablero[fila - 1][columna - 1] = "X"
            print(f"Acierto! (fila: {fila} columna: {columna})")
            return True
        else:
            print(f"Agua! (fila: {fila} columna: {columna})")
            return False
        
    def registrar_disparo(self, fila, columna, impacto):
        self.tablero[fila - 1][columna - 1] = "X" if impacto else "O"
        
    def imprimir_tablero(self):
        pprint.pprint(self.tablero)
        
    def contador_de_aciertos(self):
        contador = 0
        for i in range(TAMANO):
            for j in range(TAMANO):
                if self.tablero[i][j] == "X":
                    contador += 1 
        return contador
    

class Jugador:
        
    def __init__(self):
        self.tablero_propio = Tablero()
        self.tablero_oponente = Tablero()
            
    # Para iniciar partida, primero limpiamos los tableros y ya colocamos los barcos del jugador
    def inicializar(self): 
        # poner barcos propios fijos
        #barco de 4
        self.tablero_propio.poner_barco("H", 1, 1, 4)
        # 2 barcos de 3
        # self.tablero_propio.poner_barco("V", 3, 2, 3)
        # self.tablero_propio.poner_barco("V", 7, 9, 3)
        # # 3 barcos de 2
        # self.tablero_propio.poner_barco("H", 6, 5, 2)
        # self.tablero_propio.poner_barco("V", 7, 3, 2)
        # self.tablero_propio.poner_barco("H", 10, 5, 2)
        # # 4 barcos de 1
        # self.tablero_propio.poner_barco("H", 2, 7, 1)
        # self.tablero_propio.poner_barco("V", 9, 1, 1)
        # self.tablero_propio.poner_barco("H", 4, 8, 1)
        # self.tablero_propio.poner_barco("V", 3, 10, 1)
    
    def imprimir_estado_jugador(self):
        print("Tablero propio:")
        self.tablero_propio.imprimir_tablero()
        print()
        print("Tablero oponente:")
        self.tablero_oponente.imprimir_tablero()
        
    # Devuelve si ha dado en barco o no (False=agua)
    def recibir_disparo(self, fila, columna):
        return self.tablero_propio.recibir_disparo(fila, columna)
    
    # Inventario de disparos hechos sobre el oponente
    def registrar_disparo(self, fila, columna, impacto):
        self.tablero_oponente.registrar_disparo(fila, columna, impacto)

    def he_ganado(self):
        return self.tablero_oponente.contador_de_aciertos() == TOTAL_UNIDADES_BARCO
        
    