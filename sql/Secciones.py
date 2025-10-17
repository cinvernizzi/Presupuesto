#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
    Nombre: Secciones.py
    Autor: Lic. Claudio Invernizzi
    Fecha: 17/10/2025
    E-Mail: cinvernizzi@dsgestion.site
    Proyecto: Presupuesto
    Comentarios: Clase que verifica la existencia del
                 diccionario de secciones

"""

# importamos las librerías
from clases.dbApi import Conectar
import sqlite3
import datetime

class Secciones:
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
        self.Puntero = Lite.getPuntero()

        # verificamos si existe
        Consulta = ("SELECT COUNT(*) AS registros " 
                    "FROM sqlite_master WHERE type = 'table' AND "
                    "     name = 'secciones'; ")

        # capturamos el error
        try:

            # ejecutamos la consulta
            self.Cursor.execute(Consulta)
            Resultado = self.Cursor.fetchone()

            # según el resultado
            if Resultado["registros"] == 0:

                # creamos la tabla
                self.creaSecciones()

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

    def creaSecciones(self) -> None:
        """
        
            @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

            Método que crea la tabla de secciones

        """

        # definimos la consulta
        Consulta = ("CREATE TABLE secciones ( " 
                    "       id INTEGER NOT NULL, " 
                    "       orden INTEGER NOT NULL, "  
                    "       etapa TEXT NOT NULL, " 
                    "       fecha TEXT NOT NULL, " 
                    "PRIMARY KEY ('id' AUTOINCREMENT)); ")
        
        # capturamos el error
        try:

            # ejecutamos la consulta
            self.Cursor.execute(Consulta);

            # ahora creamos los índices
            self.creaIndices();

        # si ocurrió un error
        except sqlite3.Error as e:

            # presenta el mensaje
            print ("Error " + e.args[0])

    def creaIndices(self) -> None:
        """
        
            @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

            Método que crea los índices de la tabla de secciones

        """

        # componemos la consulta
        Consulta = "CREATE INDEX 'orden_seccion' ON secciones('orden')"

        # capturamos el error
        try:

            # preparamos y ejecutamos
            self.Cursor.execute(Consulta);

            # insertamos las secciones por defecto
            self.insertaSecciones();

        # si ocurrió un error
        except sqlite3.Error as e:

            # presenta el mensaje
            print ("Error " + e.args[0])

    def insertaSecciones(self) -> None:
        """
        
            @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

            Método que inserta las secciones por defecto

        """

        # componemos la consulta
        Consulta = ("INSERT INTO secciones " 
                    "       (orden, " 
                    "        etapa, " 
                    "        fecha) " 
                    "       VALUES " 
                    "       (?, ?, ?); ")

        # creamos una lista con los valores 
        # que vamos a insertar inicialmente
        registros = []
        registros.append("Análisis y Diseño")
        registros.append("Desarrollo y Backend")
        registros.append("Desarrollo y Frontend")
        registros.append("Testing")
        registros.append("Deploy y Configuración")
        registros.append("Hosting y Licencias")

        # definimos el contador
        orden = 1

        # obtenemos la fecha actual
        ahora = datetime.datetime.now()
        ahora = ahora.strftime("%d/%m/%Y")

        # ahora recorremos la lista
        for item in registros:

            # agregamos los parámetros
            parametros = (orden, item, ahora)

            # ejecutamos la consulta y hacemos el commit
            self.Cursor.execute(Consulta, parametros)
            self.Puntero.commit()            

            # incrementamos el contador
            orden += 1
