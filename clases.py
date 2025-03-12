from funciones import *

class Barco:
    def __init__(self, tamaño):
        self.tamaño = tamaño  # Longitud del barco
        self.posiciones = []  # Lista de coordenadas ocupadas por el barco
        self.tocado = [False] * tamaño  # Estado de cada parte del barco
        
