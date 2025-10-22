#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
    Nombre: Personal.py
    Autor: Lic. Claudio Invernizzi
    Fecha: 16/10/2025
    E-Mail: cinvernizzi@dsgestion.site
    Proyecto: Presupuesto
    Comentarios: Clase que verifica la existencia de la tabla 
                 datos personales y en todo caso la crea

"""

# importamos las librerías
from clases.dbApi import Conectar
import sqlite3

class Personal:
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
                    "     name = 'personal'; ")

        # capturamos el error
        try:

            # ejecutamos la consulta
            self.Cursor.execute(Consulta)
            Resultado = self.Cursor.fetchone()

            # según el resultado
            if Resultado["registros"] == 0:

                # creamos la tabla
                self.creaPersonal()

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

    def creaPersonal(self) -> None:
        """
        
            @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

            Método que crea la tabla de datos personales

        """

        # componemos la consulta
        Consulta = ("CREATE TABLE personal ( "
                    "       id INTEGER NOT NULL, " 
                    "       nombre TEXT NOT NULL, "
                    "       empresa TEXT NOT NULL, " 
                    "       direccion TEXT NOT NULL, " 
                    "       cuil TEXT DEFAULT NULL, " 
                    "       telefono TEXT NOT NULL, " 
                    "       mail TEXT NOT NULL, " 
                    "       fecha TEXT NOT NULL, " 
                    "PRIMARY KEY('id' AUTOINCREMENT)); ")

        # capturamos el error
        try:

            # ejecutamos la consulta
            self.Cursor.execute(Consulta)

            # creamos los índices
            self.creaIndices();

        # si ocurrió un error
        except sqlite3.Error as e:

            # lo presenta
            print("Error " + e.args[0])

    def creaIndices(self) -> None:
        """
        
            @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

            Método que crea los índices de la tabla 

        """

        # componemos la consulta
        Consulta = "CREATE INDEX 'empresa_personal' ON personal('empresa');"

        # capturamos el error
        try:

            # ejecutamos 
            self.Cursor.execute(Consulta)

        # si hubo un error
        except sqlite3.Error as e:

            # lo presenta
            print("Error " + e.args[0])
            
