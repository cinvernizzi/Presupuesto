#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
    Nombre: FormSecciones.py
    Autor: Lic. Claudio Invernizzi
    Fecha: 21/10/2025
    E-Mail: cinvernizzi@dsgestion.site
    Proyecto: Presupuesto
    Comentarios: Clase que define la grilla de administración 
                 del sistema

"""

# importamos las librerías
from nicegui import ui
from secciones.Secciones import Secciones
from secciones.EditSecciones import EditSecciones

class FormSecciones:
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
        self.Items = Secciones()

        # abrimos la columna 
        with ui.row():

            # los títulos de las columnas
            columnas = [{'name': 'id', 'label': 'Id', 'field': 'id','align':'center'},
                        {'name': 'orden', 'label': 'Orden', 'field': 'orden','align':'center'},
                        {'name': 'etapa', 'label': 'Etapa', 'field': 'etapa', 'align':'left'},
                        {'name': 'fecha', 'label': 'Fecha', 'field': 'fecha', 'align':'center'}]

            # agregamos la tabla de clientes
            self.tablasecciones = ui.table(columns=columnas, 
                                           rows=[], 
                                           title='Secciones de un Presupuesto',
                                           row_key='id',
                                           selection='single',
                                           on_select=lambda e: self.cargaSeccion(e.selection),
                                           pagination={'rowsPerPage': 5}).props('virtual-scroll').classes('w-180')

            with ui.column():
                ui.input('Buscar...').bind_value(self.tablasecciones, 'filter').props('clearable').classes('w-40')
                ui.button("Nuevo", icon='add', on_click=self.nuevaSeccion).tooltip("Pulse para ingresar un registro").classes('w-40')
                ui.button("Ayuda", icon='help', on_click=self.nuevaSeccion).tooltip("Ayuda del sistema").classes('w-40')

        # cargamos los elementos de la tabla
        self.cargaSecciones()

    def cargaSecciones(self):
        """
        
            @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

            Método llamado desde el constructor que carga la grilla
            de secciones de un presupuesto

        """

        # obtenemos la nómina 
        Nomina = self.Items.nominaSecciones()

        # si ocurrió un error 
        if not Nomina:

            # presenta el mensaje 
            ui.notify("No hay registros de Secciones", position="top-right", type="negative")
            return

        # si retornó un vector
        else:

            # recorremos el vector 
            for registro in Nomina:

                # agregamos el elemento
                self.tablasecciones.add_row({'id': registro["id"], 
                                             'orden': registro["orden"],
                                             'etapa': registro["etapa"],
                                             'fecha': registro["fecha"]})
                
    def nuevaSeccion(self):
        """
        
            @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

            Método llamado al pulsar la opción nueva sección del menú 
            que abre el diálogo emergente con el formulario
            
        """

        # abrimos el diálogo
        EditSecciones(self)

    def cargaSeccion(self, e):
        """

            @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

            @param vector con los datos del registro

            Método llamado al seleccionar una fila de la grilla 
            que abre el formulario para edición        
        
        """

        # abrimos el formulario
        formulario = EditSecciones(self)

        # asignamos los valores en el formulario
        formulario.Id.value = e[0]["id"]
        formulario.Orden.value = e[0]["orden"]
        formulario.Seccion.value = e[0]["etapa"]
        formulario.Fecha.value = e[0]["fecha"]
        