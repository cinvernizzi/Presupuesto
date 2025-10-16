#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
    Nombre: Actividades.py
    Autor: Lic. Claudio Invernizzi
    Fecha: 16/10/2025
    E-Mail: cinvernizzi@dsgestion.site
    Proyecto: Presupuesto
    Comentarios: Clase que verifica la existencia de la tabla 
                 de actividades y en todo caso la crea

"""

# importamos las librerías
from clases.dbApi import Conectar
import sqlite3

class Actividades:
    """
    
        @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

        Definición de la clase

    """

    def __init__(self):
        """
        
            @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

            Constructor de la clase, instancia la conexión y verifica
            si existe la tabla, en caso de no existir la crea

        """

        Lite = Conectar()
        self.Cursor = Lite.getConexion()

        # verificamos si existe
        Consulta = ("SELECT COUNT(*) AS registros " 
                    "FROM sqlite_master WHERE type = 'table' AND "
                    "     name = 'actividades'; ")

        # capturamos el error
        try:

            # ejecutamos la consulta
            self.Cursor.execute(Consulta)
            Resultado = self.Cursor.fetchone()

            # según el resultado
            if Resultado["registros"] == 0:

                # creamos la tabla
                self.creaActividades()

        # si ocurrió un error
        except sqlite3.error as e:

            # lo presenta 
            print("Error " + e.args[1])

    def __del__(self):
        """
        
            @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

            Destructor de la clase, simplemente elimina el puntero

        """

        # eliminamos el puntero 
        del self.Cursor

    def creaActividades(self):
        """
        
            @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

            Método que crea la tabla de actividades

        """

        # componemos la consulta
        Consulta = ("CREATE TABLE actividades ("
                    "       id INTEGER NOT NULL, " 
                    "       proyecto INTEGER NOT NULL, " 
                    "       seccion INTEGER NOT NULL, " 
                    "       descripcion TEXT, " 
                    "       estimado REAL, " 
                    "       optimo REAL, " 
                    "       pesimista REAL, " 
                    "       costo INTEGER NOT NULL, " 
                    "       consideraciones BLOB DEFAULT NULL, "
                    "FOREIGN KEY(proyecto) REFERENCES proyectos(id), "
                    "FOREIGN KEY(seccion) REFERENCES secciones(id), " 
                    "PRIMARY KEY ('id' AUTOINCREMENT)); ")

        # capturamos el error
        try:

            # asignamos y ejecutamos
            self.Cursor.execute(Consulta)

            # creamos los índices
            self.creaIndices()

        # si ocurrió un error
        except sqlite3.Error as e:

            # lo presenta
            print ("Error " + e.args[0])

    def creaIndices(self):
        """
        
            @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

            Método que crea los índices de las actividades

        """

        # capturamos el error
        try:

            # definimos la consulta
            Consulta = "CREATE INDEX proyecto_actividad ON actividades('proyecto'); "

            # ejecutamos
            self.Cursor.execute(Consulta);

            # ahora sobre la clave de la sección 
            Consulta = "CREATE INDEX seccion_actividad ON actividades('seccion'); "

            # ejecutamos
            self.Cursor.execute(Consulta)

        # si ocurrió un error
        except sqlite3.Error as e:

            # lo presenta
            print("Error " + e.arg[0])
        
