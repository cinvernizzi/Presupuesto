#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
    Nombre: Clientes.py
    Autor: Lic. Claudio Invernizzi
    Fecha: 16/10/2025
    E-Mail: cinvernizzi@dsgestion.site
    Proyecto: Presupuesto
    Comentarios: Clase que verifica la existencia de la tabla 
                 de clientes y en todo caso la crea

"""

# importamos las librerías
from clases.dbApi import Conectar
import sqlite3

class Clientes:
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
                    "     name = 'clientes'; ")

        # capturamos el error
        try:

            # ejecutamos la consulta
            self.Cursor.execute(Consulta)
            Resultado = self.Cursor.fetchone()

            # según el resultado
            if Resultado["registros"] == 0:

                # creamos la tabla
                self.creaClientes()

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

    def creaClientes(self) -> None:
        """
        
            @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

            Método que crea la tabla de clientes

        """

        # componemos la consulta
        Consulta = ("CREATE TABLE clientes ("
                    "       id INTEGER NOT NULL, " 
                    "       nombre TEXT NOT NULL, "
                    "       direccion TEXT DEFAULT NULL, "
                    "       identificacion TEXT DEFAULT NULL, "
                    "       telefono TEXT DEFAULT NULL, " 
                    "       mail TEXT DEFAULT NULL, " 
                    "       fecha TEXT NOT NULL, " 
                    "PRIMARY KEY ('id' AUTOINCREMENT)); ")

        # capturamos el error
        try:

            # ejecutamos
            self.Cursor.execute(Consulta)

            # creamos los índices
            self.creaIndices()

        # si ocurrió un error
        except sqlite3.Error as e:

            # lo presenta
            print("Error " + e.args[0])

    def creaIndices(self) -> None:
        """

            @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

            Método que crea los índices de los clientes

        """

        # componemos la consulta
        Consulta = "CREATE INDEX 'nombre_cliente' ON clientes('nombre');"

        # capturamos el error
        try:

            # ejecutamos la consulta
            self.Cursor.execute(Consulta)
            
        # si ocurrió un error
        except sqlite3.Error as e:

            # presenta el mensaje
            print("Error " + e.args[0]) 
