#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
    Nombre: Clientes.py
    Autor: Lic. Claudio Invernizzi
    Fecha: 18/10/2025
    E-Mail: cinvernizzi@dsgestion.site
    Proyecto: Presupuesto
    Comentarios: Clase que controla las operaciones sobre 
                 la tabla de clientes

"""

# importamos las librerías
from clases.dbApi import Conectar
import sqlite3
import datetime

class Clientes:
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
        self.Nombre = ""                # nombre del cliente
        self.Empresa = ""               # nombre de la empresa
        self.Direccion = ""             # dirección del cliente
        self.Identificacion = ""        # identificación tributaria
        self.Telefono = ""              # número de teléfono
        self.Mail = ""                  # dirección de email
        self.Fecha = ""                 # fecha de alta del registro

    def __del__(self):
        """
        
            @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

            Destructor de la clase 

        """

        # eliminamos la conexión 
        del self.Cursor

    def grabaCliente(self) -> int:
        """
        
            @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

            @return entero con la clave del registro

            Método que según el estado de las variables de clase 
            genera la consulta de edición o inserción, luego retorna 
            la clave del registro afectado o cero en caso de error

        """

        # según el estado de la clave
        if self.Id == 0:
            resultado = self.nuevoCliente()
        else:
            resultado = self.editaCliente()

        return resultado
    
    def nuevoCliente(self) -> int: 
        """
        
            @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

            @return entero con la clave del registro

            Método que genera la consulta de inserción y retorna la 
            clave del nuevo registro o cero en caso de error

        """

        # obtenemos la fecha actual y la pasamos a cadena porque 
        # sqlite no maneja campos de tipo fecha 
        self.Fecha = datetime.datetime.now()
        self.Fecha = self.Fecha.strftime("%d/%m/%Y")

        # componemos la consulta
        Consulta = ("INSERT INTO clientes "
                    "       (nombre, " 
                    "        direccion, " 
                    "        identificacion, " 
                    "        telefono, " 
                    "        mail, " 
                    "        fecha) "
                    "       VALUES "
                    "       (?, ?, ?, ?, ?, ?);")

        # asignamos los parámetros
        parametros = (self.Nombre, 
                      self.Direccion,
                      self.Identificacion, 
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

    def editaCliente(self) -> int:
        """
        
            @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

            @return entero con la clave del registro

            Método que genera la consulta de edición y luego retorna
            la clave del registro afectado o cero en caso de error

        """

        # componemos la consulta
        Consulta = ("UPDATE clientes SET "
                    "       nombre = ?, "
                    "       direccion = ?, "
                    "       identificacion = ?, "
                    "       telefono = ?, "
                    "       mail = ? "
                    "WHERE clientes.id = ?; ")
        
        # asignamos los parámetros
        parametros = (self.Nombre, 
                      self.Direccion, 
                      self.Identificacion, 
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

            # presenta el error y retorna
            print ("Error " + e.args[0])
            return 0
        
    def validaCliente(self, nombre: str, idcliente: int) -> bool:
        """
        
            @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

            @param nombre cadena con el nombre del cliente
            @param idcliente entero con la clave del registro 
                   (0 en caso de alta)

            @return bool verdadero si puede insertar, borrar

            Método llamado antes de insertar / editar que recibe 
            como parámetro el nombre del cliente y la clave del
            registro (que será cero en caso de alta) y verifica 
            que no se encuentre declarado, retorna verdadero 
            si puede insertar / editar

        """

        # componemos la consulta
        Consulta = ("SELECT COUNT(clientes.id) AS registros "
                    "FROM clientes "
                    "WHERE clientes.nombre = ? AND "
                    "      clientes.id != =?; ")
        
        # asignamos los parámetros
        parametros = (nombre, idcliente)

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
        
    def getDatosCliente(self, idcliente: int) -> bool:
        """
        
            @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

            @param idcliente - clave del registro

            @return bool resultado de la operación 

            Método que recibe como parámetro la clave de un registro
            y asigna los valores del mismo a las variables de clase
            retorna el resultado de la operación 

        """

        # componemos la consulta
        Consulta = ("SELECT clientes.id AS id, "
                    "       clientes.nombre AS nombre, "
                    "       clientes.direccion AS direccion, "
                    "       clientes.identificacion AS identificacion, "
                    "       clientes.telefono AS telefono, "
                    "       clientes.mail AS mail, "
                    "       clientes.fecha AS fecha "
                    "FROM clientes "
                    "WHERE clientes.id = ?; ")
        
        # asignamos
        parametros = (idcliente, )

        # capturamos el error
        try:

            # ejecutamos y obtenemos el registro
            self.Cursor.execute(Consulta, parametros)
            resultado = self.Cursor.fetchone()

            # asignamos en la clase
            self.Id = resultado["id"]
            self.Nombre = resultado["nombre"]
            self.Direccion = resultado["direccion"]
            self.Identificacion = resultado["identificacion"]
            self.Telefono = resultado["telefono"]
            self.Mail = resultado["mail"]
            self.Fecha = resultado["fecha"]

            # retornamos
            return True
        
        # si ocurrió un error
        except sqlite3.Error as e:

            # lo presenta y retorna
            print ("Error " + e.args[0])
            return False

    def buscaCliente(self, texto: str) -> list | bool:
        """

            @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

            @param texto cadena a buscar

            @return lista con los registros coincidentes

            Método que recibe como parámetro una cadena de texto y 
            busca la ocurrencia de la misma en el nombre del cliente
            retorna la lista con los registros coincidentes o falso
            en caso de error

        """

        # componemos la consulta
        Consulta = ("SELECT clientes.id AS id, "
                    "       clientes.nombre AS nombre, "
                    "       clientes.telefono AS telefono, "
                    "       clientes.mail AS mail "
                    "FROM clientes "
                    "WHERE clientes.nombre LIKE '%?%' "
                    "ORDER BY clientes.nombre; ")
        
        # asignamos los parámetros
        parametros = (texto, )

        # capturamos el error
        try: 

            # ejecutamos y retornamos
            self.Cursor.execute(Consulta, parametros)
            return self.Cursor.fetchall()
        
        # si ocurrió un error
        except sqlite3.Error as e:

            # presenta el mensaje y retorna
            print ("Error " + e.args[0])
            return False
        

    def nominaClientes(self) -> list | bool:
        """
        
            @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

            @return lista con la nómina de clientes

            Método que simplemente retorna la nómina completa de los 
            clientes registrados ordenados alfabéticamente o falso 
            en caso de error

        """

        # componemos la consulta
        Consulta = ("SELECT clientes.id AS id, "
                    "       clientes.nombre AS nombre, "
                    "       clientes.direccion AS direccion, "
                    "       clientes.telefono AS telefono, "
                    "       clientes.mail AS mail "
                    "FROM clientes "
                    "ORDER BY clientes.nombre; ")

        # capturamos el error
        try: 

            # ejecutamos y retornamos
            self.Cursor.execute(Consulta)
            return self.Cursor.fetchall()
        
        # si ocurrió un error
        except sqlite3.Error as e:

            # presenta el mensaje y retorna
            print ("Error " + e.args[0])
            return False


    def puedeBorrar(self, idcliente: int) -> bool:
        """
        
            @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

            @param idcliente - clave del registro

            @return bool si puede eliminar

            Método que recibe como parámetro la clave de un registro 
            y verifica que no tenga registros hijos, si bien existen 
            claves foráneas, verificamos antes para informar al 
            usuario en vez de lanzar una excepción.
            Retorna verdadero si puede eliminar 

        """

        # componemos la consulta
        Consulta = ("SELECT COUNT(proyectos.id) AS registros "
                     "FROM proyectos "
                     "WHERE proyectos.cliente = ?; ")
        
        # asignamos
        parametros = (idcliente, )

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
            print("Error " + e.args[0])
            return False
        
    def borraCliente(self, idcliente: int) -> bool:
        """
        
            @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

            @param idcliente - clave del registro

            @return bool - resultado de la operación 

            Método que recibe como parámetro la clave de un registro 
            y ejecuta la consulta de eliminación, retorna el resultado
            de la operación 

        """

        # componemos la consulta y asignamos
        Consulta = "DELETE FROM clientes WHERE id = ?;"
        parametros = (idcliente, )

        # capturamos el error
        try:

            # ejecutamos 
            self.Cursor.execute(Consulta, parametros)
            return True
        
        # si hubo un error
        except sqlite3.Error as e:

            # presenta el error y retorna
            print("Error " + e.args[0])
            return False
        