#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
    Nombre: Secciones.py
    Autor: Lic. Claudio Invernizzi
    Fecha: 18/10/2025
    E-Mail: cinvernizzi@dsgestion.site
    Proyecto: Presupuesto
    Comentarios: Clase que controla las operaciones sobre 
                 la tabla de secciones de un presupuesto

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

            Constructor de la clase, instancia la conexión y las 
            variables de clase

        """

        # abrimos la conexión
        Lite = Conectar()
        self.Cursor = Lite.getConexion()

        # definimos las variables
        self.Id = 0                 # clave del registro
        self.Orden = 0              # orden de la presentación
        self.Etapa = ""             # nombre de la etapa
        self.Fecha = ""             # fecha de alta del registro

    def __del__(self):
        """
        
            @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

            Destructor de la clase 

        """

        # eliminamos la conexión 
        del self.Cursor

    def grabaSeccion(self) -> int: 
        """
        
            @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

            @return entero con la clave del registro

            Método que según el estado de las variables de clase 
            ejecuta la consulta de edición o inserción, retorna 
            la clave del registro afectado o cero en caso de 
            error

        """

        # si está insertando 
        if self.Id == 0:
            self.Id = self.nuevaSeccion()
        else:
            self.Id = self.editaSeccion()

        # retornamos
        return self.Id
    
    def nuevaSeccion(self) -> int: 
        """
        
            @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

            @return entero con la clave del registro

            Método que ejecuta la consulta de inserción y retorna la 
            clave del nuevo registro o cero en caso de error

        """

        # obtenemos la fecha actual y la pasamos a cadena porque 
        # sqlite no maneja campos de tipo fecha 
        self.Fecha = datetime.datetime.now()
        self.Fecha = self.Fecha.strftime("%d/%m/%Y")

        # componemos la consulta
        Consulta = ("INSERT INTO secciones "
                    "       (orden, " 
                    "        etapa, " 
                    "        fecha) "
                    "       VALUES "
                    "       (?, ?, ?);")
        
        # asignamos los parámetros
        parametros = (self.Orden, 
                      self.Etapa, 
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

            # presenta el mensaje y retorna
            print("Error " + e.args[0])
            return 0
        
    def editaSeccion(self) -> int:
        """
        
            @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

            @return entero con la clave del registro

            Método que ejecuta la consulta de edición y retorna 
            la clave del registro afectado o cero en caso de 
            error

        """

        # componemos la consulta
        Consulta = ("UPDATE secciones SET "
                    "       orden = ?, "
                    "       etapa = ? "
                    "WHERE secciones.id = ?; ")
        
        # asignamos los parámetros
        parametros = (self.Orden, self.Etapa, self.Id)

        # capturamos el error
        try:

            # ejecutamos y retornamos
            self.Cursor.execute(Consulta, parametros)
            return self.Id
    
        # si ocurrió un error
        except sqlite3.Error as e:

            # presenta el error y retorna
            print ("Error " + e.args[0])
            return 0

    def validaSeccion(self, seccion: str, idseccion: int) -> bool: 
        """
        
            @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

            @param seccion cadena con el nombre de la sección
            @param idseccion entero con la clave de la sección

            @return bool si puede editar / insertar verdadero

            Método que recibe como parámetro el nombre de una sección 
            y la clave (que será cero en caso de un alta) y verifica
            que no se encuentre repetida, si puede insertar / borrar
            retorna verdadero 

        """

        # componemos la consulta
        Consulta = ("SELECT COUNT(secciones.id) AS registros "
                    "FROM secciones "
                    "WHERE secciones.etapa = ? AND "
                    "      secciones.id != ?; ")
        
        # asignamos los parámetros
        parametros = (seccion, idseccion)

        # capturamos el error
        try:

            # ejecutamos y obtenemos el registro
            self.Cursor.execute(Consulta, parametros)
            resultado = self.Cursor.fetchone()

            # según los registros
            if resultado["registros"] == 0:
                return True
            else:
                return False
            
        # si ocurrió un error
        except sqlite3.Error as e:

            # presenta el error y retorna
            print("Error " + e.args[0])
            return False
        
    def getDatosSeccion(self, idseccion: int) -> bool:
        """
        
            @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

            @param idseccion entero con la clave de un registro

            @return bool resultado de la operación 

            Método que recibe como parámetro la clave de una sección 
            y asigna en las variables de clase los valores del registro
            retorna el resultado de la operación 

        """

        # componemos la consulta
        Consulta = ("SELECT secciones.id AS id, "
                    "       secciones.orden AS orden, "
                    "       secciones.etapa AS etapa, "
                    "       secciones.fecha AS fecha "
                    "FROM secciones "
                    "WHERE secciones.id = ?; ")
        
        # asignamos los parámetros
        parametros = (idseccion, )

        # capturamos el error
        try:

            # ejecutamos y obtenemos el registro
            self.Cursor.execute(Consulta, parametros)
            resultado = self.Cursor.fetchone()

            # asignamos en la clase
            self.Id = resultado["id"]
            self.Orden = resultado["orden"]
            self.Etapa = resultado["etapa"]
            self.Fecha = resultado["fecha"]

            # retornamos
            return True
        
        # si ocurrió un error
        except sqlite3.Error as e:

            # presenta el error y retorna
            print("Error " + e.args[0])
            return False
        
    def nominaSecciones(self) -> list | bool:
        """
        
            @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

            @return lista con los registros o falso en caso de error

            Método que obtiene la nómina completa de secciones y 
            la retorna como un diccionario

        """

        # componemos la consulta
        Consulta = ("SELECT secciones.id AS id, "
                    "       secciones.orden AS orden, "
                    "       secciones.etapa AS etapa, "
                    "       secciones.fecha AS fecha "
                    "FROM secciones "
                    "ORDER BY secciones.etapa; ")
        
        # capturamos el error
        try:

            # ejecutamos y obtenemos los registros
            self.Cursor.execute(Consulta)
            resultado = self.Cursor.fetchall()
            return resultado

        # si ocurrió un error
        except sqlite3.Error as e:

            # presenta el error y retorna
            print("Error " + e.args[0])
            return False

    def puedeBorrar(self, idseccion: int) -> bool:
        """
        
            @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

            @param idseccion entero con la clave del registro

            @return bool verdadero si puede eliminar

            Método que recibe como parámetro la clave de un registro 
            y verifica que no tenga registros hijos en la tabla de 
            actiovidades de los proyectos, retorna verdadero si puede 
            eliminar

        """

        # componemos la consulta
        Consulta = ("SELECT COUNT(actividades.id) AS registros "
                    "FROM actividades "
                    "WHERE actividades.seccion = ?; ")
        
        # asignamos los parámetros
        parametros = (idseccion, )

        # capturamos el error
        try:

            # ejecutamos y retornamos
            self.Cursor.execute(Consulta, parametros)
            resultado = self.Cursor.fetchone()

            # según los registros 
            if resultado["registros"] == 0:
                return True
            else:
                return False
        
        # si ocurrió un error
        except sqlite3.Error as e:
            
            # presenta el error y retorna
            print ("Error " + e.args[0])
            return False
        
    def borraSeccion(self, idseccion: int) -> bool:
        """
        
            @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

            @param entero con la clave del registro

            @return bool resultado de la operación 

            Método que recibe como parámetro la clave de un registro 
            y ejecuta la consulta de eliminación, retorna el resultado
            de la operación 

        """

        # componemos la consulta
        Consulta = "DELETE FROM secciones WHERE secciones.id = ?;"

        # asignamos los parámetros 
        parametros = (idseccion, )

        # capturamos el error 
        try: 

            # ejecutamos 
            self.Cursor.execute(Consulta, parametros)
            return True
        
        # si ocurrió un error
        except sqlite3.Error as e:

            # presenta el mensaje y retorna
            print ("Error " + e.args[0])
            return False
