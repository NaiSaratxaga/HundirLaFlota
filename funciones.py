import random
import os
from variables import *


def generar_numero_aleatorio():
    return random.randint(1, TAMANO)

# validador valor introducido en el input
def es_posicion_coordenada_valida(valor_introducido):
    return valor_introducido.isdigit() and int(valor_introducido) > 0 and int(valor_introducido) <= TAMANO

def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")

    
         