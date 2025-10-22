#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
    Nombre: FormProyectos.py
    Autor: Lic. Claudio Invernizzi
    Fecha: 21/10/2025
    E-Mail: cinvernizzi@dsgestion.site
    Proyecto: Presupuesto
    Comentarios: Clase que define la grilla de proyectos 
                 declarados

"""

# importamos las librerías
from nicegui import ui
from proyectos.EditProyectos import EditProyectos

class FormProyectos:
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
                ui.button("Nuevo", icon='add', on_click=self.nuevoProyecto).tooltip("Pulse para grabar el registro").classes('w-40')
                ui.button("Buscar", icon='search', on_click=self.buscaProyecto).tooltip("Pulse para grabar el registro").classes('w-40')
                ui.button("Ayuda", icon='help', on_click=self.ayudaProyecto).tooltip("Pulse para grabar el registro").classes('w-40')
                    
            # los títulos de las columnas de la grilla
            columnas = [
                        {'name': 'id', 'label': 'Id', 'field': 'id'},
                        {'name': 'cliente', 'label': 'Cliente', 'field': 'cliente'},
                        {'name': 'titulo', 'label': 'Título', 'field': 'titulo'},
                        {'name': 'descripcion', 'label': 'Descripción', 'field': 'descripcion'},
                        {'name': 'fecha', 'label': 'Fecha', 'field': 'fecha'},
                        {'name': 'ver', 'label': 'Ver', 'field': 'ver'}
            ]

            # agregamos la grilla 
            tablaproyectos = ui.table(columns=columnas, rows=[], pagination={'rowsPerPage': 15}).props('virtual-scroll')

            # definimos el botón y el evento 
            tablaproyectos.add_slot('body-cell-ver', '''
                <q-td :props="props">
                    <q-btn label="Ver" @click="() => $parent.$emit('notify', props.row.id)" flat />
                </q-td>
            ''')
            tablaproyectos.on('ver', lambda e: ui.notify(f'Hi {e.args["name"]}!'))        

    def nuevoProyecto(self):
        """
        
            @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

            Método que abre el diálogo emergente con el formulario 
            para el abm de proyectos

        """

        # abrimos el formulario
        EditProyectos()

    def buscaProyecto(self):
        """
        
            @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

            Método que abre el diálogo de búsqueda de proyectos

        """

    def ayudaProyecto(self):
        """
        
            @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

            Método que presenta la ayuda emergente 

        """