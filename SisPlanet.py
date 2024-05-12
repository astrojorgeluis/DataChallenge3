import numpy as np
import pandas as pd


# Clase para representar un sistema planetario    
class SisPlanet(object):
    # Esta clase se utiliza para almacenar las estrellas y sus planetas asociados
    def __init__(self):
        self.estrellas_con_planetas = {}  # Diccionario para almacenar las estrellas y sus planetas asociados
        
    # Función para agregar un planeta a una estrella 
    def add_planeta(self, estrella, planeta):
        if estrella in self.estrellas_con_planetas:
            self.estrellas_con_planetas[estrella].append(planeta)
        else:
            self.estrellas_con_planetas[estrella] = [planeta]

    # Creo una función para obtener los planetas asociados a una estrella
    def planetasxstar(self, estrella):
        return self.estrellas_con_planetas.get(estrella, [])

    # Creo una función para obtener la cantidad de planetas asociados a una estrella
    def num_planetasxstar(self, estrella):
        return len(self.planetasxstar(estrella))

    # Creo una función para ordenar los planetas de una estrella por radio
    def ordenar_planetas_por_radio(self, estrella):
        planetas = self.planetasxstar(estrella)
        planetas_ordenados = sorted(planetas, key=lambda x: x.get_a())
        nombres_planetas_ordenados = [planeta.get_planet_name() for planeta in planetas_ordenados]
        return nombres_planetas_ordenados
 