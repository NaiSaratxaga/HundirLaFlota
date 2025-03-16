from clases import *
from variables import *
from funciones import *

# Limpiar pantalla para dar un comienzo a la partida
limpiar_pantalla()

# Menú principal con bienvenida e instrucciones del juego
print("\n¡Hola marinero! Bienvenido al juego de Hundir la Flota 🚢💥⚓️\n")
print("Instrucciones del juego:")
print("En cada turno, el jugador debe introducir las coordenadas (fila y columna) donde cree que se encuentra un barco enemigo.")
print("Luego, por turnos, disparan a coordenadas para intentar hundir los barcos enemigos.")
print("El objetivo es hundir todos los barcos del adversario antes de que ellos hundan los tuyos.")
print()
print("Introduce tus coordenadas para disparar.\n")

# Estoy creando instancia de la clase jugador
usuario = Jugador()
ordenador = Jugador()

# Inicializamos los jugadores con el método de la clase Jugador
# Creación de una instancia de la clase Jugador para el usuario humano
# Esto inicializa un jugador con su propio tablero y métodos relacionados con el juego
usuario.inicializar() 
# Creación de una instancia de la clase Jugador para el ordenador (oponente)
# Este objeto representa al oponente controlado por el programa
ordenador.inicializar() 

# Inicialización de la variable 'turno' para indicar quién comienza el juego
# El valor "usuario" significa que el jugador humano comenzará el primer turno
turno = "usuario"
# Inicialización de la variable 'ganador' como una cadena vacía
# Esta variable se usará para almacenar el nombre del jugador ganador una vez terminado el juego
ganador = ""


# Bucle principal del juego que se ejecuta hasta que un jugador gane
while True:
    # Muestra el estado de ambos jugadores (tableros)
    print("Estado del usuario:")
    usuario.imprimir_estado_jugador()
    print()
    print("Estado del ordenador:")
    ordenador.imprimir_estado_jugador()
    print()
    print("--------------------------")
    print()
    # Si es el turno del usuario
    if turno == "usuario":
        print("Turno usuario:")
        
        # Solicita la fila y columna al usuario y valida que estén dentro del rango permitido
        fila = input("Introduce la fila:")
        if not es_posicion_coordenada_valida(fila):
            print(f"Coordenada para la fila invalida, introduce un número entre 1 y {TAMANO}")
            continue
        
        # Columna
        columna = input("Introduce la columna:")
        if not es_posicion_coordenada_valida(columna):
            print(f"Coordenada para la columna invalida, introduce un número entre 1 y {TAMANO}")
            continue
        
        # El usuario dispara al ordenador y se registra el impacto
        impacto = ordenador.recibir_disparo(fila, columna)
        usuario.registrar_disparo(fila, columna, impacto)
        
        # Si el usuario gana, termina el juego
        if usuario.he_ganado():
            ganador = "usuario"
            break
        
        # Si el disparo fue exitoso, el usuario sigue disparando, sino, pasa el turno al ordenador
        if impacto:
            print("El usuario ha impactado en un barco, sigue disparando!")
            continue
        else:
            turno = "ordenador"
    # Si es el turno del ordenador        
    else:
        print("Turno ordenador:")
        
        # El ordenador genera coordenadas aleatorias para disparar
        fila_ordenador = generar_numero_aleatorio()
        columna_ordenador = generar_numero_aleatorio()
        print(f"El ordenador dispara  (fila: {fila_ordenador} columna: {columna_ordenador})")
        
        # El ordenador dispara y se registra el impacto
        impacto_ordenador = usuario.recibir_disparo(fila_ordenador, columna_ordenador)
        ordenador.registrar_disparo(fila_ordenador, columna_ordenador, impacto_ordenador)
        
        # Si el ordenador gana, termina el juego
        if ordenador.he_ganado():
            ganador = "ordenador"
            break
        
        # Si el disparo del ordenador fue exitoso, sigue disparando, sino, pasa el turno al usuario
        if impacto_ordenador:
            print("El ordenador ha impactado en un barco, sigue disparando")
            continue
        else:
            turno = "usuario"
            
# Muestra el ganador        
print(f"El ganador es: {ganador}")