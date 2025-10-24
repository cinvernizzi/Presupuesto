#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
    Nombre: Verifica.py
    Autor: Lic. Claudio Invernizzi
    Fecha: 16/10/2025
    E-Mail: cinvernizzi@dsgestion.site
    Proyecto: Presupuesto
    Comentarios: Clase que verifica la existencia de las distintas
                 tablas

"""

# importamos las librerías
from sql.Actividades import Actividades
from sql.Clientes import Clientes
from sql.Personal import Personal
from sql.Secciones import Secciones
from sql.Proyectos import Proyectos
from sql.Presupuesto import Presupuesto
from sql.Vistas import Vistas

class Verifica:
    """

        @author Claudio Invernizzi <cinvernizzi@dsgestion.site>
    
        Definición de la clase

    """

    def __init__(self):
        """
        
            @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

            Constructor de la clase que simplemente instancia las 
            distintas verificacions de la base de datos local

        """

        # verificamos los clientes
        Clientes()

        # la tabla de datos personales
        Personal()

        # insertamos las secciones
        Secciones()

        # los datos de los proyectos
        Proyectos()

        # los datos de los presupuestos
        Presupuesto()

        # verificamos las actividades
        Actividades()

        # ahora creamos las vistas
        Vistas()
