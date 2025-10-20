#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
    Nombre: dbApi.py
    Autor: Lic. Claudio Invernizzi
    Fecha: 16/10/2025
    E-Mail: cinvernizzi@dsgestion.site
    Proyecto: Presupuesto
    Comentarios: Clase que establece la conexión con la 
                 base de datos local

"""

# importamos las librerías
import sqlite3

class Conectar:
    """
    
        @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

        Definición de la clase

    """

    def __init__(self):
        """
        
            @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

            Constructor de la clase que establece la conexión con 
            la base y retorna el puntero de la misma

        """

        # capturamos el error
        try: 

            # nos conectamos y establecemos que retorna
            # los datos como un diccionario, el switch 
            # isolation_level realiza el autocommit de 
            # las consultas de inserción
            Lite = sqlite3.connect("presupuesto.db", isolation_level=None)
            Lite.row_factory = sqlite3.Row
            self.Cursor = Lite.cursor()

        # si ocurrió un error
        except sqlite3.Error as e:
            
            # presenta el error
            print("Error " + e.args[1])

    def __del__(self):
        """
        
            @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

            Destructor de la clase, simplemente cierra la conexión 

        """

        # cerramos el puntero
        self.Cursor.close()

    def getConexion(self):
        """
        
            @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

            Método que simplemente retorna la conexión a la base

        """

        # retornamos
        return self.Cursor    
