#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
    Nombre: FormPresupuestos.py
    Autor: Lic. Claudio Invernizzi
    Fecha: 24/10/2025
    E-Mail: cinvernizzi@dsgestion.site
    Proyecto: Presupuesto
    Comentarios: Clase que define la grilla de con los 
                 presupuestos realizados

"""

# importamos las librerías
from nicegui import ui

class FormPresupuestos:
    """
    
        @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

        Definición de la clase

    """

    def __init__(self):
        """
        
            @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

            Constructor de la clase, carga en el tabulador la 
            definición de la grilla

        """

        # instanciamos la clase 

        # abrimos la columna 
        with ui.row():

            # los títulos de las columnas
            columnas = [{'name': 'id', 'label': 'Id', 'field': 'id','align':'center'},
                        {'name': 'proyecto', 'label': 'Proyecto', 'field': 'proyecto','align':'left'},
                        {'name': 'cliente', 'label': 'cliente', 'field': 'cliente', 'align':'left'},
                        {'name': 'fecha', 'label': 'Fecha', 'field': 'fecha', 'align':'center'},
                        {'name': 'importe', 'label': 'Importe', 'field': 'importe', 'align':'center'}]

            # agregamos la tabla de clientes
            self.tablapresupuestos = ui.table(columns=columnas, 
                                           rows=[], 
                                           title='Presupuestos Presentados',
                                           row_key='id',
                                           selection='single',
                                           on_select=lambda e: self.verPresupuesto(e.selection),
                                           pagination={'rowsPerPage': 5}).props('virtual-scroll').classes('w-260')

            with ui.column():
                ui.input('Buscar...').bind_value(self.tablapresupuestos, 'filter').props('clearable').classes('w-40')
                ui.button("Nuevo", icon='add', on_click=self.nuevoPresupuesto).tooltip("Pulse para ingresar un registro").classes('w-40')
                ui.button("Ayuda", icon='help', on_click=self.ayudaPresupuestos).tooltip("Ayuda del sistema").classes('w-40')

        # cargamos los registros 
        self.cargaPresupuestos()

    def cargaPresupuestos(self):
        """
        
            @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

            Método llamado desde el constructor o luego de editar 
            un registro que carga la grilla con los presupuestos 
            presentados 

        """

    def nuevoPresupuesto(self):
        """
        
            @author Claudio Invernizzi <cinvernizzi@dsgestion.siteX

            Método llamado al pulsar el botón nuevo que abre el 
            layer emergente con el formulario de carga

        """

    def verPresupuesto(self, e):
        """
        
            @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

            @param e vector con los datos de la fila seleccionada

            Método llamado al seleccionar una fila que recibe el 
            vector con los datos de esa fila y abre el diálogo 
            emergente con el formulario para la edición del 
            registro

        """

    def ayudaPresupuestos(self):
        """
        
            @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

            Método que abre el layer emergente con la ayuda del 
            sistema 

        """