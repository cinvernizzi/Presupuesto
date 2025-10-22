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

            with ui.column():
                ui.button("Nuevo", icon='add', on_click=self.nuevaSeccion).tooltip("Pulse para grabar el registro").classes('w-40')
                ui.button("Buscar", icon='search', on_click=self.nuevaSeccion).tooltip("Pulse para grabar el registro").classes('w-40')
                ui.button("Ayuda", icon='help', on_click=self.nuevaSeccion).tooltip("Pulse para grabar el registro").classes('w-40')

            # los títulos de las columnas
            columnas = [
                        {'name': 'id', 'label': 'Id', 'field': 'id','align':'center'},
                        {'name': 'orden', 'label': 'Orden', 'field': 'orden','align':'center'},
                        {'name': 'etapa', 'label': 'Etapa', 'field': 'etapa', 'align':'left'},
                        {'name': 'fecha', 'label': 'Fecha', 'field': 'fecha', 'align':'center'},
                        {'name': 'ver', 'label': 'Ver', 'align': 'center'}
            ]

            # agregamos la tabla de clientes
            self.tablasecciones = ui.table(columns=columnas, rows=[], pagination={'rowsPerPage': 6}).props('virtual-scroll')
            
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
                                             'fecha': registro["fecha"],
                                             'ver': 'Ver'})
                # definimos los eventos luego de cargar la tabla 
                self.tablasecciones.add_slot('body-cell-ver', '''
                    <q-td :props="props">
                    <q-btn icon="edit" @click="() => $parent.$emit('edit', props.row)" flat />
                    </q-td>
                ''')
                self.tablasecciones.on('edit', lambda e: ui.notify(f'Hi {e.args["id"]}!'))        

    def nuevaSeccion(self):
        """
        
            @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

            Método llamado al pulsar la opción nueva sección del menú 
            que abre el diálogo emergente con el formulario
            
        """

        # abrimos el diálogo
        EditSecciones()

        