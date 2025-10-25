#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
    Nombre: Presupuestos.py
    Autor: Lic. Claudio Invernizzi
    Fecha: 25/10/2025
    E-Mail: cinvernizzi@dsgestion.site
    Proyecto: Presupuesto
    Comentarios: Clase que controla las operaciones sobre 
                 la tabla de presupuestos que está 
                 relacionada con la de actividades

"""

# importamos las librerías
from clases.dbApi import Conectar
import sqlite3
import datetime

class Presupuestos:
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
        self.Id = 0                      # clave del registro
        self.Fecha = ""                  # fecha de alta del registro
        self.Validez = 0                 # validez en días del presupuesto
        self.Proyecto = 0                # clave del proyecto
        self.Importe = 0.00              # importe total del proyecto

    def __del__(self):
        """
        
            @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

            Destructor de la clase 

        """

        # eliminamos la conexión 
        del self.Cursor

    def grabaPresupuesto(self) -> int:
        """
        
            @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

            @return int clave del registro

            Método que según el estado de las variables de clase 
            genera la consulta de inserción o edición y retorna
            la clave del registro afectado o cero en caso de 
            error

        """

        # si está insertando
        if self.Id == 0:
            estado = self.nuevoPresupuesto()
        else:
            estado = self.editaPresupuesto()

        # retornamos
        return estado
    
    def nuevoPresupuesto(self) -> int:
        """
        
            @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

            @return entero con la clave del nuevo registro

            Método que ejecuta la consulta de inserción y retorna 
            la clave del nuevo registro o cero en caso de error

        """
        # obtenemos la fecha actual y la pasamos a cadena porque 
        # sqlite no maneja campos de tipo fecha 
        self.Fecha = datetime.datetime.now()
        self.Fecha = self.Fecha.strftime("%d/%m/%Y")

        # componemos la consulta
        Consulta = ("INSERT INTO presupuesto "
                    "       (fecha, "
                    "        validez, "
                    "        proyecto, "
                    "        importe) "
                    "       VALUES "
                    "       (?, ?, ?, ?); ")

        # asignamos los parámetros
        parametros = (self.Fecha, 
                      self.Validez, 
                      self.Proyecto, 
                      self.Importe)        
        
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
        
    def editaPresupuesto(self) -> int:
        """
        
            @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

            @return entero con la clave del registro afectado

            Método que ejecuta la consulta de edición y retorna 
            la clave del registro afectado o cero en caso de 
            error

        """

        # componemos la consulta
        Consulta = ("UPDATE presupuesto SET " 
                    "       validez = ?, " 
                    "       importe = ? " 
                    "WHERE presupuesto. id = ?; ")
        
        # asignamos los parámetros
        parametros = (self.Validez, 
                      self.Importe,
                      self.Id)
        
        # capturamos el error
        try:
            
            # ejecutamos
            self.Cursor.execute(Consulta, parametros)
            return self.Id
        
        # si ocurrió un error
        except sqlite3.Error as e:

            # presenta el mensaje y retorna
            print("Error " + e.args[0])
            return 0
        
    def validaPresupuesto(self, 
                          idpresupuesto: int, 
                          proyecto: str) -> bool:
        """
        
            @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

            @param idpresupuesto clave del registro
            @param proyecto cadena con el nombre del proyecto

            @return bool si puede insertar / editar

            Método que evita la repetición de registros, recibe como 
            parámetros la clave del proyecto (cero en caso de alta)
            el nombre del proyecto y la clave del cliente, retorna 
            verdadero si puede editar / insertar

        """

        # componemos la consulta
        Consulta = ("SELECT COUNT(presupuesto.id) AS registros "
                    "FROM proyecto "
                    "WHERE presupuesto.id != ? AND "
                    "      presupuesto.proyecto = ?; ")

        # asignamos los parámetros
        parametros = (idpresupuesto, proyecto)

        # capturamsos el error
        try:

            # ejecutamos la consulta
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
        
    def nominaPresupuestos(self):
        """
        
            @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

            @return lista con los registros 

            Método que retorna el listado completo de presupuestos

        """

        # componemos la consulta
        Consulta = ("SELECT v_presupuesto.id AS id, "
                    "       v_presupuesto.fecha AS fecha, "
                    "       v_presupuesto.validez AS validez, "
                    "       v_presupuesto.proyecto AS proyecto, "
                    "       v_presupuesto.cliente AS cliente, "
                    "       v_presupuesto.importe AS importe "
                    "FROM v_presupuesto "
                    "ORDER BY v_presupuesto.proyecto; ")
        
        # capturamos el error
        try: 

            # ejecutamos y retornamos
            self.Cursor.execute(Consulta)
            return self.Cursor.fetchall()
        
        # si ocurrió un error
        except sqlite3.Error as e:

            # presenta el mensaje y retorna
            print("Error " + e.args[0])
            return False
        
    def getDatosPresupuesto(self, idpresupuesto: int) -> bool:
        """
        
            @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

            @param idpresupuesto entero con la clave del registro

            @return bool resultado de la operación 

            Método que recibe como parámetro la clave del registro 
            y asigna en las variables de clase los valores del 
            mismo 

        """

        # componemos la consulta
        Consulta = ("SELECT presupuesto.id AS id, "
                    "       presupuesto.fecha AS fecha, "
                    "       presupuesto.validez AS validez, "
                    "       presupuesto.proyecto AS proyecto, "
                    "       presupuesto.importe AS importe "
                    "FROM presupuesto "
                    "WHERE presupuesto.id = ?; ")
        parametros = (idpresupuesto, )

        # capturamos el error 
        try:

            # ejecutamos la consulta y asignamos en la clase
            self.Cursor.execute(Consulta, parametros)
            resultado = self.Cursor.fetchone()
            self.Id = int(resultado["id"])
            self.Fecha = resultado["fecha"]
            self.Validez = resultado["validez"]
            self.Proyecto = resultado["proyecto"]
            self.Importe = resultado["importe"]

            # retornamos
            return True
        
        # si ocurrió un error
        except sqlite3.Error as e:

            # presenta el error y retorna
            print("Error " + e.args[0])
            return False
        
    def borraPresupuesto(self, idpresupuesto: int) -> bool:
        """
        
            @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

            @param idpresupuesto - clave del registro

            @return bool resultado de la operación 

            Método que recibe como parámetro la clave de un registro 
            y ejecuta la consulta de eliminación, retorna el 
            resultado de la operación 

        """

        # componemos la consulta
        Consulta = "DELETE FROM presupuesto WHERE id = ?;"
        parametros = (idpresupuesto, )

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
        