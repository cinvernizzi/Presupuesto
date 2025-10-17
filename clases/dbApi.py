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
            # los datos como un diccionario
            self.Lite = sqlite3.connect("presupuesto.db")
            self.Lite.row_factory = sqlite3.Row
            self.Cursor = self.Lite.cursor()

        # si ocurrió un error
        except sqlite3.Error as e:
            
            # presenta el error
            print("Error " + e.args[1])

    def __del__(self):
        """
        
            @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

            Destructor de la clase, simplemente cierra la conexión 

        """

        # cerramos el puntero y la conexión
        self.Cursor.close()
        self.Lite.close()

    def getConexion(self):
        """
        
            @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

            Método que simplemente retorna la conexión a la base

        """

        # retornamos
        return self.Cursor    

    def getPuntero(self):
        """
        
            @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

            Método que retorna el puntero al archivo

        """

        # retornamos el puntero
        return self.Lite
