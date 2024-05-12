import numpy as np
import pandas as pd
from Star import Star
from Planet import Planet
from SisPlanet import SisPlanet
from Exoplanet import ExoPlanet


# Lectura del archivo CSV
data = pd.read_csv('e1n4AOA4.csv')

# Lista de estrellas que se desean buscar
estrellas_a_buscar = ['HR 8799', 'HD 202206 A', 'TRAPPIST-1', 'TOI-1338', 'HD 188753', 'Kepler-451', 'Kepler-16 (AB)']

# Instancia de la clase para almacenar sistemas planetarios
sistema_planetario = SisPlanet()

# Diccionario para almacenar instancias de estrellas existentes
estrellas_existentes = {} 

# Iteración sobre cada fila del DataFrame 'data'
for index, row in data.iterrows():
    
    # Verifica si el nombre de la estrella en 'star_name' o 'star_alternate_names' está en la lista 'estrellas_a_buscar'
    if row['star_name'] in estrellas_a_buscar or row['star_alternate_names'] in estrellas_a_buscar:
        
        # Verifica si el nombre de la estrella en 'star_name' no está en 'estrellas_mencionadas' pero su nombre alternativo en 'star_alternate_names' sí lo está
        if row['star_name'] not in estrellas_a_buscar and row['star_alternate_names'] in estrellas_a_buscar:
            # Actualiza el nombre de la estrella a su nombre alternativo
            row['star_name'] = row['star_alternate_names']

        # Verifica si el nombre de la estrella no está en el diccionario 'estrellas_existentes'
        if row['star_name'] not in estrellas_existentes:
            # Crea una instancia de la clase 'Star' con los detalles de la estrella y la agrega al diccionario 'estrellas_existentes'
            star = Star(row['star_name'], row['star_mass'], row['star_radius'], row['star_teff'], row['star_distance'], (row['ra'], row['dec']))
            estrellas_existentes[row['star_name']] = star

        else:
            # Si el nombre de la estrella ya está en 'estrellas_existentes', obtiene la instancia de la estrella correspondiente del diccionario
            star = estrellas_existentes[row['star_name']]

        # Crea una instancia de la clase 'ExoPlanet' con los detalles del planeta
        planeta = ExoPlanet(star, row['mass'], row['radius'], row['semi_major_axis'], row['inclination'], row['eccentricity'], row['omega'], row['name'])
        
        # Establece el método de descubrimiento del planeta
        planeta.set_metodo_descubrimiento(row['detection_type'])
        
        # Agrega el planeta al sistema planetario asociado con la estrella
        sistema_planetario.add_planeta(star, planeta)


# Se verifica si alguna de las estrellas mencionadas en 'estrellas_a_buscar' no fue encontrada en la base de datos, y se imprime un mensaje en caso afirmativo
for estrella in estrellas_a_buscar:
    if estrella not in estrellas_existentes:
        print("--------------------------------------------------------------------")
        print(f"La estrella {estrella} no fue encontrada en la base de datos de la Republica Galactica.")
        print("--------------------------------------------------------------------\n")

# Se imprime la información de las estrellas y sus planetas asociados
for star in estrellas_existentes.values():

    print(f"Sistema de la Estrella: {star.get_name()}\n\
        Luminosidad total: {star.total_luminosidad()}\n\
        Luminosidad en la secuencia principal: {star.luminosidad_sec_principal()}\n\
        Cantidad de planetas: {sistema_planetario.num_planetasxstar(star)}\n\
        Planetas ordenados: {sistema_planetario.ordenar_planetas_por_radio(star)}")
        
    print("  Planetas:")
    for planeta in star.get_add_planet():
        print(f"\
        Nombre: {planeta.get_planet_name()}\n\
        Periodo de rotacion kepleriana: {planeta.periodo_rotacion_kepleriana()}\n\
        Metodos de descubrimiento: {planeta.metodo_descubrimiento()}\n\
        Inclinacion del planeta: {planeta.inclinacion_de_planeta()}")
        if planeta.metodo_descubrimiento() == 'Primary Transit':
            print(f"        Parametro de impacto: {planeta.par_impacto(star)}")
        print()

