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
    def par_impacto(self):
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