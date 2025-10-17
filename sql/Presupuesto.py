#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
    Nombre: Presupuesto.py
    Autor: Lic. Claudio Invernizzi
    Fecha: 17/10/2025
    E-Mail: cinvernizzi@dsgestion.site
    Proyecto: Presupuesto
    Comentarios: Clase que verifica la existencia de la tabla 
                 de presupuesto y en todo caso la crea

"""

# importamos las librerías
from clases.dbApi import Conectar
import sqlite3

class Presupuesto:
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
                    "     name = 'presupuesto'; ")

        # capturamos el error
        try:

            # ejecutamos la consulta
            self.Cursor.execute(Consulta)
            Resultado = self.Cursor.fetchone()

            # según el resultado
            if Resultado["registros"] == 0:

                # creamos la tabla
                self.creaPresupuesto()

        # si ocurrió un error
        except sqlite3.Error as e:

            # lo presenta 
            print("Error " + e.args[1])

    def __del__(self):
        """
        
            @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

            Destructor de la clase, simplemente elimina el puntero

        """

        # eliminamos el puntero 
        del self.Cursor

    def creaPresupuesto(self) -> None:
        """
        
            @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

            Método que crea la tabla con los datos de los presupuestos

        """

        # definimos la consulta
        Consulta = ("CREATE TABLE presupuesto ( "
                    "       id INTEGER NOT NULL, "
                    "       fecha TEXT NOT NULL, " 
                    "       validez INTEGER NOT NULL, " 
                    "       proyecto INTEGER NOT NULL, "
                    "FOREIGN KEY(proyecto) REFERENCES proyectos(id), "
                    "PRIMARY KEY ('id' AUTOINCREMENT)); ")

        # capturamos el error
        try:

            # asignamos y ejecutamos
            self.Cursor.execute(Consulta);

            # creamos los índices
            self.creaIndices();

        # si ocurrió un error
        except sqlite3.Error as e:

            # lo presenta
            print("Error " + e.args[0])

    def creaIndices(self) -> None:
        """
        
            @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

            Método que crea los índices de los presupuestos

        """

        # definimos la consulta
        Consulta = "CREATE INDEX proyecto_presupuesto ON presupuesto('proyecto'); "

        # capturamos el error
        try:

            # asignamos y ejecutamos
            self.Cursor.execute(Consulta);

        # si hubo un error
        except sqlite3.Error as e:

            # lo presenta
            print("Error " + e.args[0])
