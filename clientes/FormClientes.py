#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
    Nombre: FormClientes.py
    Autor: Lic. Claudio Invernizzi
    Fecha: 21/10/2025
    E-Mail: cinvernizzi@dsgestion.site
    Proyecto: Presupuesto
    Comentarios: Clase que define la grilla de los clientes
                 registrados

"""

# importamos las librerías
from nicegui import ui
from clientes.EditClientes import EditClientes

class FormClientes:
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

        # abrimos la columna 
        with ui.row():

            # presentamos el menú 
            with ui.column():
                ui.button("Nuevo", icon='add', on_click=self.nuevoCliente).tooltip("Pulse para grabar el registro").classes('w-40')
                ui.button("Buscar", icon='search', on_click=self.buscaCliente).tooltip("Pulse para grabar el registro").classes('w-40')
                ui.button("Ayuda", icon='help', on_click=self.ayudaCliente).tooltip("Pulse para grabar el registro").classes('w-40')

            # los títulos de las columnas
            columnas = [
                        {'name': 'id', 'label': 'Id', 'field': 'id'},
                        {'name': 'nombre', 'label': 'nombre', 'field': 'nombre'},
                        {'name': 'identificacion', 'label': 'Id.Tributaria', 'field': 'identificacion'},
                        {'name': 'telefono', 'label': 'Teléfono', 'field': 'telefono'},
                        {'name': 'mail', 'label': 'E-Mail', 'field': 'mail'},
                        {'name': 'fecha', 'label': 'Fecha', 'field': 'fecha'},
                        {'name': 'ver', 'label': 'Ver', 'field': 'ver'}
            ]

            # agregamos la tabla de clientes
            tablaclientes = ui.table(columns=columnas, rows=[], pagination={'rowsPerPage': 15}).props('virtual-scroll')

            # definimos el evento del botón ver
            tablaclientes.add_slot('body-cell-ver', '''
                <q-td :props="props">
                    <q-btn label="Ver" @click="() => $parent.$emit('notify', props.row.id)" flat />
                </q-td>
            ''')
            tablaclientes.on('ver', lambda e: ui.notify(f'Hi {e.args["name"]}!'))        

    def nuevoCliente(self):
        """
        
            @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

            Método que abre el diálogo con el formulario de carga
            de nuevo cliente

        """

        # abrimos el diálogo
        EditClientes()
        
    def buscaCliente(self):
        """
        
            @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

            Método que abre el díalogo de búsqueda de cliente

        """

    def ayudaCliente(self):
        """
        
            @authhor Claudio Invernizzi <cinvernizzi@dsgestion.site>

            Método que presenta la ventana de ayuda 

        """