import pprint
from funciones import *

# Clase Tablero: representa el tablero del juego
class Tablero:
    def __init__(self):
        # Inicializa un tablero vacío de tamaño 10
        self.tablero =  [[" " for _ in range(TAMANO)] for _ in range(TAMANO)]
        
    # En esta función colocamos los barcos en el tablero   
    def poner_barco(self, orientacion, posicion_inicial_fila, posicion_inicial_columna, tamano_barco):
        '''
         Coloca un barco en el tablero.
        :param orientacion: "H" para horizontal, "V" para vertical.
        :param posicion_inicial_fila: Fila donde inicia el barco.
        :param posicion_inicial_columna: Columna donde inicia el barco.
        :param tamano_barco: Longitud del barco.
        '''
        # Ajustar índices para que coincidan con la matriz (de 0 a TAMANO-1 en lugar de 1 a TAMANO)
        indice_inicial_fila = posicion_inicial_fila - 1
        indice_inicial_columna = posicion_inicial_columna - 1
        # Recorre el tamaño del barco y coloca las partes en el tablero
        for i in range(tamano_barco):
            if orientacion == "H": # Colocar barco en horizontal
                self.tablero[indice_inicial_fila][indice_inicial_columna + i] = "B"
            elif orientacion == "V": # Colocar barco en vertical
                self.tablero[indice_inicial_fila + i][indice_inicial_columna] = "B"
                
    # Recibe un disparo en una casilla del tablero y determina si impacta en un barco ("B") o cae en el agua.                    
    def recibir_disparo(self, fila, columna):
        '''
         Procesa un disparo en una coordenada específica.
        :param fila: Fila del disparo.
        :param columna: Columna del disparo.
        :return: True si el disparo impacta en un barco, False si es agua.
        '''
        # Obtener el valor de la casilla en la posición indicada (ajustamos índices restando 1)
        valor_coordenada = self.tablero[fila - 1][columna - 1]
        # Si la casilla contiene un barco ("B") o ya ha sido impactado antes ("X")
        if valor_coordenada == "B" or valor_coordenada == "X": # Impacto en un barco
            self.tablero[fila - 1][columna - 1] = "X"  # Marcar la casilla como impactada
            print(f"Acierto! (fila: {fila} columna: {columna})") # Mensaje de impacto
            return True # Devuelve True porque fue un disparo exitoso
        else: # Si la casilla está vacía, significa que el disparo cayó en el agua
            print(f"Agua! (fila: {fila} columna: {columna})")
            return False # Devuelve False porque no impactó en un barco
     
    # Registra el resultado de un disparo en el tablero del oponente.
    # Marca "X" si el disparo impactó en un barco, o "O" si cayó en el agua.   
    def registrar_disparo(self, fila, columna, impacto):
        '''
         Marca el resultado del disparo en el tablero.
        :param fila: Fila del disparo.
        :param columna: Columna del disparo.
        :param impacto: True si hubo impacto, False si fue agua.  
        '''
        # Si hubo impacto (impacto == True), se marca con "X" (disparo acertado)
        # Si no hubo impacto (impacto == False), se marca con "O" (agua)
        self.tablero[fila - 1][columna - 1] = "X" if impacto else "O"
        
    # Muestra el tablero en la consola de forma estructurada.   
    def imprimir_tablero(self):
        '''
        Imprime el tablero en consola. 
        '''
        pprint.pprint(self.tablero)
    
    # Recorre el tablero y cuenta las casillas marcadas con 'X' (impactos en barcos)
    def contador_de_aciertos(self):
        '''
        Cuenta el número de impactos en barcos ('X') en el tablero.
        :return: Número total de impactos.
        '''
        contador = 0 # Inicializa el contador de aciertos
        for i in range(TAMANO): # Recorre las filas del tablero
            for j in range(TAMANO): # Recorre las columnas del tablero
                if self.tablero[i][j] == "X": # Si hay un impacto en un barco
                    contador += 1 # Incrementa el contador
        return contador  # Retorna la cantidad total de aciertos
    
    
# Clase Jugador: Representa a un jugador con su propio tablero y el del oponente
class Jugador:
        
    def __init__(self):
        # Cada jugador tiene un tablero propio y uno para registrar los disparos al oponente
        # Se crea un tablero para el jugador, donde podrá colocar sus barcos o elementos
        self.tablero_propio = Tablero() # Inicializa el tablero propio para el jugador.
        # Se crea un segundo tablero para registrar los disparos que el jugador hace al oponente
        self.tablero_oponente = Tablero() # Inicializa el tablero del oponente para registrar los disparos.
            
    # Para iniciar partida, primero limpiamos los tableros y ya colocamos los barcos del jugador
    def inicializar(self): 
        '''
        Configura el tablero del jugador colocando los barcos en posiciones fijas.
        '''
        #barco de 4
        self.tablero_propio.poner_barco("H", 1, 1, 4)
        # 2 barcos de 3
        self.tablero_propio.poner_barco("V", 3, 2, 3)
        self.tablero_propio.poner_barco("V", 7, 9, 3)
        # # 3 barcos de 2
        self.tablero_propio.poner_barco("H", 6, 5, 2)
        self.tablero_propio.poner_barco("V", 7, 3, 2)
        self.tablero_propio.poner_barco("H", 10, 5, 2)
        # # 4 barcos de 1
        self.tablero_propio.poner_barco("H", 2, 7, 1)
        self.tablero_propio.poner_barco("V", 9, 1, 1)
        self.tablero_propio.poner_barco("H", 4, 8, 1)
        self.tablero_propio.poner_barco("V", 3, 10, 1)
    
    # Imprime el estado actual del jugador, mostrando sus tableros.
    def imprimir_estado_jugador(self):
        '''
        Este método muestra al jugador su propio tablero (donde ha colocado sus barcos)
        y el tablero del oponente (donde se registran los disparos realizados al oponente).
        '''
        print("Tablero propio:")
        self.tablero_propio.imprimir_tablero()
        print()
        print("Tablero oponente:")
        self.tablero_oponente.imprimir_tablero()
        
    # Devuelve si el disparo es un impacto o agua.
    def recibir_disparo(self, fila, columna):
        '''
        Recibe un disparo del oponente y devuelve si impactó o no.
        :param fila: Fila del disparo.
        :param columna: Columna del disparo.
        :return: True si impacta en un barco, False si es agua.
        '''
        return self.tablero_propio.recibir_disparo(fila, columna)
    
    # Inventario de disparos hechos sobre el tablero del oponente
    def registrar_disparo(self, fila, columna, impacto):
        '''
        Registra un disparo hecho por el jugador en el tablero del oponente.
        :param fila: Fila donde se disparó.
        :param columna: Columna donde se disparó.
        :param impacto: True si hubo impacto, False si fue agua.
        '''
        self.tablero_oponente.registrar_disparo(fila, columna, impacto)
        
    # Verificamos si un jugador ha alcanzado la victoria
    def he_ganado(self):
        '''
         Verifica si el jugador ha ganado la partida contando los impactos.
        :return: True si ha acertado todas las unidades de los barcos del oponente.
        '''
        return self.tablero_oponente.contador_de_aciertos() == TOTAL_UNIDADES_BARCO
        
    