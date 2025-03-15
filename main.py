from clases import *

#Estoy creando instancia de la clase jugador
usuario = Jugador()
ordenador = Jugador()

#inicializamos los jugador con el metodo de la clase jugador
usuario.inicializar() 
ordenador.inicializar() 

turno = "usuario"
ganador = ""

while True:
    print("Estado del usuario:")
    usuario.imprimir_estado_jugador()
    print()
    print("Estado del ordenador:")
    ordenador.imprimir_estado_jugador()
    print("--------------------------")
    print()
    
    if turno == "usuario":
        print("Turno usuario:")
        
        fila = int(input("Introduce la fila:"))
        columna = int(input("Introduce la columna:"))
        
        # dispara el usuario
        impacto = ordenador.recibir_disparo(fila, columna)
        usuario.registrar_disparo(fila, columna, impacto)
        
        if usuario.he_ganado():
            ganador = "usuario"
            break
        
        # dependerá de si ha acertado o no
        if impacto:
            print("El usuario ha impactado en un barco, sigue disparando!")
            continue
        else:
            turno = "ordenador"
    else:
        print("Turno ordenador:")
        
        fila_ordenador = generar_numero_aleatorio()
        columna_ordenador = generar_numero_aleatorio()
        print(f"El ordenador dispara  (fila: {fila_ordenador} columna: {columna_ordenador})")
        
        # dispara el ordenador
        impacto_ordenador = usuario.recibir_disparo(fila_ordenador, columna_ordenador)
        ordenador.registrar_disparo(fila_ordenador, columna_ordenador, impacto_ordenador)
        
        if ordenador.he_ganado():
            ganador = "ordenador"
            break
        
        if impacto_ordenador:
            print("El ordenador ha impactado en un barco, sigue disparando")
            continue
        else:
            turno = "usuario"
        
print(f"El ganador es: {ganador}")