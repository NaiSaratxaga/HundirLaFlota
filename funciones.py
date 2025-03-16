import random
import os
from variables import *


# Utiliza la función randint del módulo random para obtener un número aleatorio dentro de los límites definidos.
def generar_numero_aleatorio():
    '''
    Genera y devuelve un número aleatorio entre 1 y TAMANO (inclusive).
    Esta función se utiliza para generar un número aleatorio dentro de un rango definido.
    '''
    # Genera un número aleatorio entre 1 y TAMANO
    return random.randint(1, TAMANO)

# Validador valor introducido en el input
def es_posicion_coordenada_valida(valor_introducido):
    '''
    Esta función verifica si el valor introducido por el usuario es una posición válida para colocar un barco.
    Verifica que el valor sea un número entero positivo dentro del rango de 1 a TAMANO (inclusive).
    
    Parámetros:
    - valor_introducido: el valor que el usuario intenta ingresar como coordenada.
    
    Devuelve:
    - True si el valor es un número válido dentro del rango.
    - False si el valor no es un número o no está dentro del rango permitido.
    '''
    return valor_introducido.isdigit() and int(valor_introducido) > 0 and int(valor_introducido) <= TAMANO

# Esta función limpia la pantalla de la consola, proporcionando una interfaz más limpia para el usuario.
def limpiar_pantalla():
    '''
    Dependiendo del sistema operativo, la función ejecuta el comando adecuado:
    - En Windows, usa el comando "cls" para limpiar la consola.
    - En sistemas basados en Unix (como Linux y macOS), usa el comando "clear".
    '''
    # Ejecuta el comando adecuado según el sistema operativo
    os.system("cls" if os.name == "nt" else "clear")

    
         