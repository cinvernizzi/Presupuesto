#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
    Nombre: Personal.py
    Autor: Lic. Claudio Invernizzi
    Fecha: 21/10/2025
    E-Mail: cinvernizzi@dsgestion.site
    Proyecto: Presupuesto
    Comentarios: Clase que provee los métodos para interactuar 
                 con la tabla de datos personales

"""

# importamos las librerías
from clases.dbApi import Conectar
import sqlite3
import datetime

class Personal:
    """
    
        @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

        Definición de la clase

    """

    def __init__(self):
        """
        
            @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

            Constructor de la clase, instancia la conexión y las 
            variables de clase

        """

        # abrimos la conexión
        Lite = Conectar()
        self.Cursor = Lite.getConexion()

        # definimos las variables
        self.Id = 0                     # clave del registro
        self.Nombre = ""                # nombre del usuario
        self.Empresa = ""               # nombre fantasía de la empresa
        self.Direccion = ""             # dirección postal
        self.Cuil = ""                  # identificación tributaria
        self.Telefono = ""              # número telefónico
        self.Mail = ""                  # mail del usuario
        self.Fecha = ""                 # fecha de alta 

    def __del__(self):
        """
        
            @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

            Destructor de la clase 

        """

        # eliminamos la conexión 
        del self.Cursor

    def grabaPersonal(self) -> int:
        """
        
            @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

            @return entero con la clave del registro

            Método que según las variables de clase genera la consulta
            de inserción o edición y retorna la clave del registro 
            afectado o cero en caso de error

        """

        # si está insertando
        if self.Id == 0:
            estado = self.nuevoPersonal()
        else:
            estado = self.editaPersonal()

        # retornamos
        return estado
    
    def nuevoPersonal(self) -> int:
        """
        
            @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

            @return entero con la clave del registro insertado

            Método que ejecuta la consulta de inserción y retorna 
            la clave del nuevo registro o cero en caso de error 

        """

        # obtenemos la fecha actual y la pasamos a cadena porque 
        # sqlite no maneja campos de tipo fecha 
        self.Fecha = datetime.datetime.now()
        self.Fecha = self.Fecha.strftime("%d/%m/%Y")

        # componemos la consulta
        Consulta = ("INSERT INTO personal "
                    "       (nombre, "
                    "        empresa, "
                    "        direccion, "
                    "        cuil, "
                    "        telefono, "
                    "        mail, "
                    "        fecha) "
                    "       VALUES "
                    "       (?, ?, ?, ?, ?, ?, ?); ")

        # asignamos los parámetros 
        parametros = (self.Nombre, 
                      self.Empresa, 
                      self.Direccion, 
                      self.Cuil,
                      self.Telefono, 
                      self.Mail,
                      self.Fecha)        
        
        # capturamos el error
        try:

            # ejecutamos 
            self.Cursor.execute(Consulta, parametros)

            # esta comprobación la hacemos porque lastrowid
            # puede devolver tanto la clave como None si 
            # ocurrió un error
            estado = self.Cursor.lastrowid
            if estado is not None:
                return int(estado)
            else:
                return 0

        # si ocurrió un error
        except sqlite3.Error as e:
    
            # presenta el error y retorna
            print ("Error " + e.args[0])
            return 0


    def editaPersonal(self) -> int:
        """
        
            @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

            @return entero con la clave del registro afectado

            Método que ejecuta la consulta de edición y retorna 
            la clave del registro o cero en caso de error

        """

        # componemos la consulta
        Consulta = ("UPDATE personal SET "
                    "       empresa = ?, "
                    "       nombre = ?, "
                    "       direccion = ?, "
                    "       cuil = ?, "
                    "       telefono = ?, "
                    "       mail = ? "
                    "WHERE personal.id = ?; ")
        
        # asignamos los parámetros 
        parametros = (self.Empresa, 
                      self.Nombre, 
                      self.Direccion,
                      self.Cuil, 
                      self.Telefono, 
                      self.Mail,
                      self.Id)
        
        # capturamos el error
        try:

            # ejecutamos y retornamos
            self.Cursor.execute(Consulta, parametros)
            return self.Id
        
        # si ocurrió un error
        except sqlite3.Error as e:

            # lo presenta y retorna
            print("Error " + e.args[0])
            return 0
        
    def getDatosPersonal(self) -> bool:
        """
        
            @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

            @return bool resultado de la operación 

            Método que obtiene los datos del registro del productor 
            (asumimos que existe un solo registro) y los asigna 
            a las variables de clase

        """

        # componemos la consulta
        Consulta = ("SELECT personal.id AS id, "
                    "       personal.nombre AS nombre, "
                    "       personal.empresa AS empresa, "
                    "       personal.direccion AS direccion, "
                    "       personal.cuil AS cuil, "
                    "       personal.telefono AS telefono, "
                    "       personal.mail AS mail, "
                    "       personal.fecha AS fecha "
                    "FROM personal "
                    "LIMIT 1; ")
        
        # capturamos el error
        try:

            # ejecutamos y asignamos los valores en 
            # las variables de clase
            self.Cursor.execute(Consulta)

            # verificamos si hay registros
            if self.Cursor.rowcount != 0:

                # asignamos en la clase
                resultado = self.Cursor.fetchone()
                self.Id = resultado["id"]
                self.Nombre = resultado["nombre"]
                self.Empresa = resultado["empresa"]
                self.Direccion = resultado["direccion"]
                self.Cuil = resultado["cuil"]
                self.Telefono = resultado["telefono"]
                self.Mail = resultado["mail"]
                self.Fecha = resultado["fecha"]

            # retornamos
            return True
        
        # si ocurrió un error
        except sqlite3.Error as e:

            # presenta el mensaje y retorna
            print("Error " + e.args[0])
            return False
        