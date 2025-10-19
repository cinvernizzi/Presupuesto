#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
    Nombre: Proyectos.py
    Autor: Lic. Claudio Invernizzi
    Fecha: 19/10/2025
    E-Mail: cinvernizzi@dsgestion.site
    Proyecto: Presupuesto
    Comentarios: Clase que controla las operaciones sobre 
                 la tabla de proyectos

"""

# importamos las librerías
from clases.dbApi import Conectar
import sqlite3
import datetime

class Proyectos:
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
        self.Id = 0                   # clave del registro
        self.Cliente = 0              # clave del cliente
        self.Titulo = ""              # nombre del proyecto
        self.Descripcion = ""         # descripción del proyecto
        self.Fecha = ""               # fecha de alta del registro

    def __del__(self):
        """
        
            @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

            Destructor de la clase 

        """

        # eliminamos la conexión 
        del self.Cursor

    def grabaProyecto(self) -> int:
        """
        
            @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

            @return entero con la clave del registro

            Método que según el valor de las variables de clase 
            ejecuta la consulta de inserción o edición, retorna 
            la clave del registro afectado o cero en caso de error

        """

        # si está insertando
        if self.Id == 0:
            estado = self.nuevoProyecto()
        else:
            estado = self.editaProyecto()

        # retornamos
        return estado
    
    def nuevoProyecto(self) -> int:
        """
        
            @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

            @return entero con la clave del nuevo registro

            Metodo que ejecuta la consulta de inserción en la base
            de datos, retorna la clave del nuevo registro o cero 
            en caso de error

        """

        # obtenemos la fecha actual y la pasamos a cadena porque 
        # sqlite no maneja campos de tipo fecha 
        self.Fecha = datetime.datetime.now()
        self.Fecha = self.Fecha.strftime("%d/%m/%Y")

        # componemos la consulta
        Consulta = ("INSERT INTO proyectos "
                     "      (cliente, "
                     "       titulo, "
                     "       descripcion, "
                     "       fecha) "
                     "      VALUES "
                     "      (?, ?, ?, ?); ")
        
        # asignamos los parámetros
        parametros = (self.Cliente, 
                      self.Titulo, 
                      self.Descripcion, 
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

            # lo presenta y retornamos
            print("Error " + e.args[0])        
            return 0

    def editaProyecto(self) -> int:
        """
        
            @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

            @return entero con la clave del registro afectado

            Método que ejecuta la consulta de edición, retorna la 
            clave del registro afectado o cero en caso de error

        """

        # componemos la consulta
        Consulta = ("UPDATE proyectos SET "
                    "       titulo = ?, "
                    "       descripcion = ? "
                    "WHERE proyectos.id = ?; ")
        
        # asignamos los parámetros
        parametros = (self.Titulo, self.Descripcion, self.Id)

        # capturamos el error
        try: 

            # ejecutamos y retornamos
            self.Cursor.execute(Consulta, parametros)
            return self.Id
        
        # si ocurrió un error
        except sqlite3.Error as e:

            # lo presenta y retornamos
            print("Error " + e.args[0])
            return 0

    def validaProyecto(self, 
                       nombre: str, 
                       idcliente: str,
                       idproyecto: int) -> bool:
        """
        
            @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

            @param nombre cadena con el nombre del proyecto
            @param idcliente entero con la clave del cliente
            @param idproyecto clave del proyecto

            @return bool verdadero si puede insertar

            Método llamado antes de grabar para evitar la inserción 
            edición de registros repetidos, recibe como parámetros 
            el nombre del proyecto, la clave del cliente y la clave
            del proyecto (cero en caso de un alta) y verifica que 
            no se encuentre declarado.
            Si puede insertar / editar retorna verdadero

        """

        # componemos la consulta
        Consulta = ("SELECT COUNT(proyectos.id) AS registros "
                    "FROM proyectos "
                    "WHERE proyectos.nombre = ? AND "
                    "      proyectos.idcliente = ? AND "
                    "      proyectos.id != ?; ")
        
        # asignamos los parámetros
        parametros = (nombre, idcliente, idproyecto)

        # capturamos el error
        try:

            # obtenemos el registro
            self.Cursor.execute(Consulta, parametros)
            resultado = self.Cursor.fetchone()

            # según los registros
            if resultado["registros"] == 0:
                return True
            else:
                return False
            
        # si ocurrió un error
        except sqlite3.Error as e:

            # presenta el mensaje y retorna
            print("Error " + e.args[0])
            return False
        
    def getDatosProyecto(self, idproyecto: int) -> bool:
        """
        
            @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

            @param idproyecto - clave del registro

            @return bool - resultado de la operación 

            Método que recibe como parámetro la clave de un registro 
            y asigna los valores del mismo a las variables de clase

        """

        # componemos la consulta y asignamos los parámetros
        Consulta = ("SELECT proyectos.id AS id, "
                    "       proyectos.cliente AS cliente, "
                    "       proyectos.titulo AS titulo, "
                    "       proyectos.descripcion AS descripcion, "
                    "       proyectos.fecha AS fecha "
                    "FROM proyectos "
                    "WHERE proyectos.id = ?;")
        parametros = (idproyecto, )

        # capturamos el error
        try:

            # ejecutamos y asigmanos en la clase
            self.Cursor.execute(Consulta, parametros)
            resultado = self.Cursor.fetchone()
            self.Id = resultado["id"]
            self.Cliente = resultado["cliente"]
            self.Titulo = resultado["titulo"]
            self.Descripcion = resultado["descripcion"]
            self.Fecha = resultado["fecha"]

            # retornamos
            return True
    
        # si ocurrió un error
        except sqlite3.Error as e:

            # presenta el mensaje y retorna
            print("Error " + e.args[0])
            return False
        
    def proyectosCliente(self, idcliente: int) -> list | bool:
        """
        
            @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

            @param idcliente - clave del cliente

            @return lista con los proyectos del cliente

            Método que recibe como parámetro la clave de un cliente 
            y retorna todos los proyectos de ese cliente, en caso 
            de error retorna falso

        """

        # componemos la consulta
        Consulta = ("SELECT proyectos.id AS id, "
                    "       proyectos.titulo AS titulo, "
                    "       proyectos.descripcion AS descripcion, "
                    "       proyectos.fecha AS fecha "
                    "FROM proyectos "
                    "WHERE proyectos.cliente = ? "
                    "ORDER BY proyectos.titulo;")
        parametros = (idcliente, )

        # capturamos el error
        try: 

            # ejecutamos y retornamos
            self.Cursor.execute(Consulta, parametros)
            return self.Cursor.fetchall()
        
        # si ocurrió un error
        except sqlite3.Error as e:

            # presenta el mensaje y retorna
            print ("Error " +  e.args[0])
            return False

    def buscaProyecto(self, texto: str) -> list | bool:
        """
        
            @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

            @param texto cadena a buscar

            @return lista con los registros coincidentes

            Método que recibe como parámetro una cadena de texto y 
            busca la ocurrencia de la misma en el nombre del 
            proyecto y el nombre del cliente, retorna la lista con 
            los registros coincidentes, en caso de error retorna 
            falso

        """

        # componemos la consulta sobre la vista
        Consulta = ("SELECT v_proyectos.id AS id, "
                    "       v_proyectos.cliente AS cliente, "
                    "       v_proyectos.titulo AS titulo, "
                    "       v_proyectos.telefono AS telefono, "
                    "       v_proyectos.mail AS mail, "
                    "       v_proyectos.fecha AS fecha "
                    "FROM v_proyectos "
                    "WHERE v_proyectos.titulo LIKE '%?%' "
                    "ORDER BY v_proyectos.titulo, "
                    "         v_proyectos.cliente; ")
        
        # definimos los parámetros 
        parametros = (texto, )

        # capturamos el error
        try:

            # ejecutamos la consulta y retornamos
            self.Cursor.execute(Consulta, parametros)
            return self.Cursor.fetchall()
        
        # si ocurrió un error
        except sqlite3.Error as e:

            # presenta el mensaje y retorna
            print ("Error " + e.args[0])
            return False
        
    def puedeBorrar(self, idproyecto: int) -> bool:
        """
        
            @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

            @param idproyecto - clave del registro

            @return verdadero si puede eliminar

            Método llamado antes de eliminar un registro que verifica 
            que no tenga registros hijos (si bien están las claves 
            foráneas, es mejor avisarle al usuario que generar la 
            excepción)

        """

        # componemos sobre la tabla de presupuestos
        Consulta = ("SELECT COUNT(presupuesto.id) AS registros "
                    "FROM presupuesto "
                    "WHERE presupuesto.proyecto = ?; ")
        parametros = (idproyecto, )

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

            # presenta el mensaje y retorna
            print ("Error " + e.args[0])
            return False
        
    def borraProyecto(self, idproyecto) -> bool:
        """
        
            @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

            @param idproyecto - clave del registro

            @return bool resultado de la operación 

            Método que recibe como parámetro la clave de un proyecto 
            y ejecuta la consulta de eliminación, retorna el resultado
            de la operación 

        """
        
        # componemos la consulta y asignamos
        Consulta = "DELETE FROM proyectos WHERE proyectos.id =?;"
        parametros = (idproyecto, )

        # capturamos el error 
        try:

            # ejecutamos y retornamos
            self.Cursor.execute(Consulta, parametros)
            return True
        
        # si ocurrió un error
        except sqlite3.Error as e:

            # presenta el mensaje y retorna
            print("Error " + e.args[0])
            return False
        
