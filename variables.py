# Configuración del juego 

# Tamaño del tablero 
TAMANO = 10  

# Cada tipo de barco tiene un número determinado de unidades según su eslora (tamaño):
NUM_BARCOS_ESLORA_1 = 4  # Número de barcos en el tablero
NUM_BARCOS_ESLORA_2 = 3  # Número de barcos en el tablero
NUM_BARCOS_ESLORA_3 = 2  # Número de barcos en el tablero
NUM_BARCOS_ESLORA_4 = 1  # Número de barcos en el tablero

# Calcula el total de unidades ocupadas por los barcos del jugador
# El total de unidades es la suma de todas las casillas ocupadas por los barcos en el tablero
TOTAL_UNIDADES_BARCO = NUM_BARCOS_ESLORA_1 + (NUM_BARCOS_ESLORA_2 * 2) + (NUM_BARCOS_ESLORA_3 * 3)+ (NUM_BARCOS_ESLORA_4 * 4)
