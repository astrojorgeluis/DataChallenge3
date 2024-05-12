import numpy as np
import pandas as pd


# Clase para representar un planeta
class Planet(object):

    # Constructor de la clase
    def __init__(self, star_anfitriona, masa, radio, a, i, e, w, planet_name):
        self._star_anfitriona = star_anfitriona
        self._masa = masa
        self._radio = radio
        self._radiomayor_orb = a
        self._inclinacion_orb = i
        self._excentricidad_orb = e
        self._periastron = w
        self.planet_name = planet_name
        star_anfitriona.add_planet(self)  # Agrega este planeta a la lista de planetas de la estrella anfitriona

    # Funciones para obtener los datos del planeta
    def get_star_anfitriona(self):
        return self._star_anfitriona

    def get_masa (self):
        return self._masa
    
    def get_radio (self):
        return self._radio
    
    def get_a(self):
        return self._radiomayor_orb
    
    def get_i(self):
        return self._inclinacion_orb
    
    def get_e(self):
        return self._excentricidad_orb
    
    def get_w(self):
        return self._periastron
    
    def get_planet_name(self):
        return self.planet_name
    
    # Función para calcular el periodo de rotación kepleriana del planeta
    def periodo_rotacion_kepleriana(self) -> float:
        G = 6.67408e-11
        T = 2 * np.pi * np.sqrt((self.get_a()**3) / (G * self.get_masa()))
        return T