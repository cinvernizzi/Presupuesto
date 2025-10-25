#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
    Nombre: Vistas.py
    Autor: Lic. Claudio Invernizzi
    Fecha: 17/10/2025
    E-Mail: cinvernizzi@dsgestion.site
    Proyecto: Presupuesto
    Comentarios: Clase que una vez verificadas las tablas 
                 del proyecto, se asegura de crear las 
                 vistas correspondientes

"""

# importamos las librerías
from clases.dbApi import Conectar
import sqlite3

class Vistas:
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

        # crea la vista de presupuesto
        self.creaPresupuesto()

        # crea la vista de actividades
        self.creaActividades()

        # crea la vista de proyectos
        self.creaProyectos()
     
    def __del__(self):
        """
        
            @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

            Destructor de la clase, simplemente elimina el puntero

        """

        # eliminamos el puntero 
        del self.Cursor

    def creaPresupuesto(self) -> None:
        """
        
            @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

            Método que crea la vista de presupuesto

        """

        # componemos la consulta
        Consulta = ("CREATE VIEW IF NOT EXISTS v_presupuesto AS " 
                    "       SELECT presupuesto.id AS id, "
                    "              presupuesto.fecha AS fecha, "
                    "              presupuesto.validez AS validez, "
                    "              presupuesto.proyecto AS idproyecto, " 
                    "              proyectos.titulo AS proyecto, " 
                    "              proyectos.cliente AS idcliente, "
                    "              clientes.nombre AS cliente, " 
                    "              clientes.direccion AS direccion, " 
                    "              clientes.identificacion AS identificacion, " 
                    "              clientes.telefono AS telefono, " 
                    "              clientes.mail AS mail, " 
                    "              presupuesto.importe AS importe "
                    "        FROM presupuesto INNER JOIN proyectos ON presupuesto.proyecto = proyectos.id " 
                    "                         INNER JOIN clientes ON proyectos.cliente = clientes.id; ")

        # capturamos el error
        try:

            # asignamos y ejecutamos
            self.Cursor.execute(Consulta);

        # si ocurrió un error
        except sqlite3.Error as e:

            # presenta el mensaje
            print("Error " +  e.args[0])

    def creaActividades(self) -> None:
        """
        
            @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

            Método que crea la vista de actividades

        """

        # componemos la consulta
        Consulta = ("CREATE VIEW IF NOT EXISTS v_actividades AS "
                    "       SELECT actividades.id AS id, " 
                    "              actividades.proyecto AS idproyecto, "
                    "              proyectos.titulo AS proyecto, "
                    "              actividades.seccion AS idseccion, " 
                    "              secciones.orden AS orden, "
                    "              secciones.etapa AS seccion, "
                    "              actividades.descripcion AS descripcion, " 
                    "              actividades.estimado AS estimado, "
                    "              actividades.optimo AS optimo, "
                    "              actividades.pesimista AS pesimista, " 
                    "              actividades.costo AS costo, " 
                    "              actividades.consideraciones AS consideraciones " 
                    "        FROM actividades INNER JOIN proyectos ON actividades.proyecto = proyectos.id " 
                    "                         INNER JOIN secciones ON actividades.seccion = secciones.id; ")

        # capturamos el error
        try:

            # asignamos y ejecutamos
            self.Cursor.execute(Consulta);

        # si ocurrió un error
        except sqlite3.Error as e:

            # presenta el mensaje
            print("Error " + e.args[0])

    def creaProyectos(self) -> None:
        """
        
            @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

            Método que crea la vista de proyectos

        """

        # componemos la consulta
        Consulta = ("CREATE VIEW IF NOT EXISTS v_proyectos AS "
                    "       SELECT proyectos.id AS id, " 
                    "              proyectos.cliente AS idcliente, "
                    "              clientes.nombre AS cliente, " 
                    "              clientes.direccion AS direccion, " 
                    "              clientes.identificacion AS identificacion, " 
                    "              clientes.telefono AS telefono, " 
                    "              clientes.mail AS mail, "
                    "              proyectos.titulo AS titulo, " 
                    "              proyectos.descripcion AS descripcion, " 
                    "              proyectos.fecha AS fecha " 
                    "       FROM proyectos INNER JOIN clientes ON proyectos.cliente = clientes.id; ")
        
        # capturamos el error
        try:

            # asignamos y ejecutamos
            self.Cursor.execute(Consulta);
            
        # si ocurrió un error
        except sqlite3.Error as e:

            # presenta el mensaje
            print("Error " + e.args[0])
