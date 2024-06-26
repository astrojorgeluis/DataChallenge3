import numpy as np
import pandas as pd
from Planet import Planet
from Star import Star

# Clase para representar un exoplaneta 
class ExoPlanet(Planet):
    # Esta clase hereda de la clase Planet

    # Método para establecer el método de descubrimiento del planeta
    def set_metodo_descubrimiento(self, metodo):
        self.metodo = metodo

    # Método para obtener el método de descubrimiento del planeta
    def metodo_descubrimiento(self):
        return self.metodo
    
    # Método para calcular el parámetro de impacto del planeta en caso de que el método de descubrimiento sea 'Primary Transit'
    def par_impacto(self, star):
        b = (self.get_a()*np.cos(self.get_i())) * (1 - self.get_e()**2) / (star.get_radio()*(1 + self.get_e()*np.sin(self.get_w())))
        if np.isnan(b):
            return 'No se puede calcular por falta de datos.'
        else:
            if 0 < b < 1:
                return b
            elif b <= 0:
                return 0
            else:
                return 1
            
    # Método para obtener la inclinación del planeta
    def inclinacion_de_planeta(self):
        return self.get_i() # Se podria implementar un metodo para convertir la inclinacion a grados o radianes
    
    # Función para verificar si la masa del planeta es mayor a la masa de Júpiter
    def es_mayor_que_tierra(self):
        masa_jupiter = 1.898e27  # Masa de Júpiter en kg
        masa_tierra = 5.972e24  # Masa de la Tierra en kg
        masa_tierra_jupiter = masa_tierra / masa_jupiter
        if self.get_masa() > masa_tierra_jupiter:
            return True
        else:
            return False