#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
    Nombre: Actividades.py
    Autor: Lic. Claudio Invernizzi
    Fecha: 19/10/2025
    E-Mail: cinvernizzi@dsgestion.site
    Proyecto: Presupuesto
    Comentarios: Clase que controla las operaciones sobre 
                 la tabla de actividades de un proyecto

"""

# importamos las librerías
from clases.dbApi import Conectar
import sqlite3
import datetime

class Actividades:
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

        # tener en cuenta que el costo de la actividad es el 
        # importe que define el usuario de su costo por hora
        # considerando además su margen de ganancia 

        # definimos las variables
        self.Id = 0                   # clave del registro
        self.Proyecto = 0             # clave del proyecto
        self.Seccion = 0              # clave de la sección 
        self.Descripcion = ""         # descripción de la actividad
        self.Optimo = ""              # tiempo optimo de implementación
        self.Estimado = ""            # tiempo promedio estimado
        self.Pesimista = ""           # peor tiempo posible 
        self.Costo = 0.00             # costo de la actividad
        self.Consideraciones = ""     # anotaciones del usuario

    def __del__(self):
        """
        
            @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

            Destructor de la clase 

        """

        # eliminamos la conexión 
        del self.Cursor

    def grabaActividad(self) -> int:
        """
        
            @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

            @return clave del registro afectado

            Método que ejecuta la consulta de edición / inserción 
            según el estado de las variables de clase, retorna 
            la clave del registro afectado o cero en caso de error

        """

        # si está insertando
        if self.Id == 0:
            estado = self.nuevaActividad()
        else:
            esdtado = self.editaActividad()

        # retornamos
        return estado

    def nuevaActividad(self) -> int:
        """
        
            @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

            @return entero con la clave del nuevo registro

            Método que ejecuta la consulta de inserción y retorna 
            la clave del nuevo registro o cero en caso de error

        """

        # componemos la consulta
        Consulta = ("INSERT INTO actividades "
                    "       (proyecto, "
                    "        seccion, "
                    "        descripcion, "
                    "        estimado, "
                    "        optimo, "
                    "        pesimista, "
                    "        costo, "
                    "        consideraciones)"
                    "       VALUES "
                    "       (?, ?, ?, ?, ?, ?, ?, ?);")
        
        # asignamos los parámetros
        parametros = (self.Proyecto,
                      self.Seccion, 
                      self.Descripcion, 
                      self.Estimado,
                      self.Optimo,
                      self.Pesimista,
                      self.Costo,
                      self.Consideraciones)
        
        # capturamos el error
        try:

            # ejecutamos la consulta
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
            print ("Error " + e.args[0])
            return 0

    def editaActividad(self) -> int:
        """
        
            @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

            @return entero con la clave del registro afectado

            Método que ejecuta la consulta de edición de un registro 
            y retorna la clave del mismo, en caso de error retorna 
            cero

        """

        # componemos la consulta
        Consulta = ("UPDATE actividades SET "
                    "       seccion = ?, "
                    "       descripcion = ?, "
                    "       estimado = ?, "
                    "       optimo = ?, "
                    "       pesimista = ?, "
                    "       costo = ?, "
                    "       consideraciones = ? "
                    "WHERE actividades.id = ?; ")
        
        # asignamos los parámetros
        parametros = (self.Seccion, 
                      self.Descripcion,
                      self.Estimado, 
                      self.Optimo, 
                      self.Pesimista, 
                      self.Costo,
                      self.Consideraciones, 
                      self.Id)
        
        # capturamos el error 
        try: 

            # ejecutamos y retornamos
            self.Cursor.execute(Consulta, parametros)
            return self.Id
        
        # si ocurrió un error
        except sqlite3.Error as e:

            # presenta el mensaje y retorna
            print("Error " + e.args[0])
            return 0

    def getDatosActividad(self, idactividad: int) -> bool:
        """
        
            @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

            @param idactividad entero con la clave del registro

            @return bool resultado de la operación 

            Método que recibe como parámetro la clave de un registro 
            y asigna los valores del mismo a las variables de clase
            retorna el resultado de la operación 

        """

        # componemos la consulta
        Consulta = ("SELECT actividades.id AS id, "
                    "       actividades.proyecto AS proyecto, "
                    "       actividades.seccion AS seccion, "
                    "       actividades.descripcion AS descripcion, "
                    "       actividades.estimado AS estimado, "
                    "       actividades.optimo AS optimo, "
                    "       actividades.pesimista AS pesimista, "
                    "       actividades.costo AS costo, "
                    "       actividades.consideraciones AS consideraciones "
                    "FROM actividades "
                    "WHERE acitivades.id = ?; ")
        parametros = (idactividad, )

        # capturamos el error
        try:

            # obtenemos el registro y asignamos
            self.Cursor.execute(Consulta, parametros)
            resultado = self.Cursor.fetchone()
            self.Id = resultado["id"]
            self.Proyecto = resultado["proyecto"]
            self.Descripcion = resultado["descripcion"]
            self.Estimado = resultado["estimado"]
            self.Pesimista = resultado["pesimista"]
            self.Costo = resultado["costo"]
            self.Consideraciones = resultado["consideraciones"]

            # retornamos
            return True
        
        # si ocurrió un error
        except sqlite3.Error as e:

            # lo presenta y retorna
            print("Error " + e.args[0])
            return False
        
    def validaActividad(self, 
                        idproyecto: int, 
                        description: str, 
                        idactividad: int) -> bool:
        """
        
            @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

            @param idproyecto clave del proyecto
            @param descripcion texto con la descripción de la actividad
            @param idactividad clave de la actividad

            @return verdadero si puede insertar / editar

            Método que recibe como parámetros la clave del proyecto, la 
            descripción de la actividad y la clave de la misma (cero en 
            caso de inserción) y verifica que no se encuentre declarada
            retorna verdadero si puede insertar / editar

        """

        # componemos la consulta y asignamos
        Consulta = ("SELECT COUNT(actividades.id) AS registros "
                    "FROM actividades "
                    "WHERE actividades.proyecto = ? AND "
                    "      actividades.descripcion = ? AND "
                    "      actividades.id != ?; ")
        parametros = (idproyecto, description, idactividad)

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

    def nominaActividades(self, idproyecto: int) -> list | bool:
        """
        
            @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

            @param idproyecto clave del proyecto

            @retorna lista con las actividades del proyecto o falso
                     en caso de error

            Método que recibe como parámetro la clave de un proyecto 
            y consulta la vista retornando la nómina completa de 
            actividades de ese proyecto, ordenadas según el orden 
            establecido en la sección de cada actividad

        """

        # componemos la consulta sobre la vista
        Consulta = ("SELECT v_actividades.id AS id, "
                    "       v_actividades.proyecto AS proyecto, "
                    "       v_actividades.seccion AS seccion, "
                    "       v_actividades.orden AS orden, "
                    "       v_actividades.descripcion AS descripcion, "
                    "       v_actividades.estimado AS estimano, "
                    "       v_actividades.optimo AS optimo, "
                    "       v_actividades.pesimista AS pesimista, "
                    "       v_actividades.costo AS costo, "
                    "       v_actividades.consideraciones AS consideraciones "
                    "FROM v_actividades "
                    "WHERE v_actividades.idproyecto = ? "
                    "ORDER BY v_actividades.orden; ")
        parametros = (idproyecto, )

        # capturamos el error
        try: 

            # ejecutamos y retornamos
            self.Cursor.execute(Consulta, parametros)
            return self.Cursor.fetchall()
        
        # si ocurrió un error
        except sqlite3.Error as e:

            # lo presenta y retorna
            print ("Error " + e.args[0])
            return False
        
    def borraActividad(self, idactividad: int) -> bool: 
        """
        
            @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

            @param int idactividad clave del registro

            @return bool resultado de la operación

            Método que recibe como parámetro la clave de una 
            actividad y ejecuta la consulta de eliminación 
            retorna el resultado de la operación 
            
        """