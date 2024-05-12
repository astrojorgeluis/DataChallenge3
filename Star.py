import numpy as np
import pandas as pd


# Clase para representar una estrella
class Star(object):

    # Constructor de la clase
    def __init__(self, name, masa, radio, teff, distancia, mov_propio):
        self.name = name
        self._masa = masa
        self._radio = radio
        self._teff = teff
        self._distancia = distancia
        self.planets = []  # Lista para almacenar los planetas asociados a la estrella
        self._mov_propio = mov_propio  # Movimiento propio de la estrella en coordenadas (ra, dec)

    # Funciones para obtener los datos de la estrella
    def get_name(self):
        return self.name
    
    def get_masa(self):
        return self._masa
    
    def get_radio(self):
        return self._radio
    
    def get_teff(self):
        return self._teff
    
    def get_distancia(self):
        return self._distancia
    
    def get_mov_propio(self):
        return self._mov_propio

    # Creo una función para agregar planetas a la estrella
    def add_planet(self, planet):
        self.planets.append(planet)

    # Creo un get para obtener los planetas asociados a la estrella
    def get_add_planet(self):
        return self.planets

    # Hago la función para calcular la luminosidad total de la estrella
    def total_luminosidad(self) -> float:
        L = 4*np.pi*(self._radio**2)*self._teff
        return L

    # Hago la función para calcular la luminosidad en la secuencia principal de la estrella
    def luminosidad_sec_principal(self) -> float:
        L_sun = 3.828e26
        M_sun = 1
        L_ms = L_sun * (self._masa / M_sun) ** 3.5
        return L_ms
    
    def comparar_masa_con_sun(self):
        M_sun = 1
        if self._masa > M_sun:
            return True
        else:
            return False
        
    def comparar_radio_con_sun(self):
        R_sun = 1
        if self._radio > R_sun:
            return True
        else:
            return False