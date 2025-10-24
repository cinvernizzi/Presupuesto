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
from proyectos.Proyectos import Proyectos

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
                   
            # los títulos de las columnas de la grilla
            columnas = [{'name': 'id', 'label': 'Id', 'field': 'id','align':'center'},
                        {'name': 'cliente', 'label': 'Cliente', 'field': 'cliente','align':'left'},
                        {'name': 'titulo', 'label': 'Título', 'field': 'titulo','align':'left'},
                        {'name': 'telefono', 'label': 'Teléfono', 'field': 'telefono','align':'right'},
                        {'name': 'mail', 'label': 'Mail', 'field': 'mail','align':'left'}]

            # agregamos la grilla 
            self.tablaproyectos = ui.table(title='Proyectos Registrados', 
                                           columns=columnas, 
                                           rows=[],
                                           row_key='id', 
                                           selection='single',
                                           on_select=lambda e: self.cargaProyecto(e.selection),
                                           pagination={'rowsPerPage': 5}).props('virtual-scroll').classes('w-260')
            # presentamos el menú 
            with ui.column():
                ui.input('Buscar...').bind_value(self.tablaproyectos, 'filter').props('clearable').classes('w-40')
                ui.button("Nuevo", icon='add', on_click=self.nuevoProyecto).tooltip("Pulse para ingresar un proyecto").classes('w-40')
                ui.button("Ayuda", icon='help', on_click=self.ayudaProyecto).tooltip("Ayuda del sistema").classes('w-40')

        # cargamos los registros 
        self.nominaProyectos()

    def nominaProyectos(self):
        """
        
            @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

            Método llamado desde el constructor que carga la grilla 
            de proyectos 

        """

        # instanciamos la clase y obtenemos la nómina
        proyectos = Proyectos()
        nomina = proyectos.nominaProyectos()

        # si no hay registros
        if not nomina:
            return
        else:

            # recorremos el vector
            for registro in nomina:

                # agregamos a la tabla 
                self.tablaproyectos.add_row({'id': registro["id"], 
                                             'cliente': registro["cliente"],
                                             'titulo': registro["titulo"],
                                             'telefono': registro["telefono"],
                                             'mail': registro["mail"]})

    def nuevoProyecto(self):
        """
        
            @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

            Método que abre el diálogo emergente con el formulario 
            para el abm de proyectos

        """

        # abrimos el formulario
        EditProyectos(self)

    def cargaProyecto(self, e):
        """
        
            @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

            Método que recibe como parámetro la fila seleccionada 
            de la grilla

        """

        # obtenemos la clave del registro
        id = int(e[0]["id"])

        # abrimos el formulario 
        formulario = EditProyectos(self)

        # cargamos el registro 
        formulario.getDatosProyecto(id)

    def ayudaProyecto(self):
        """
        
            @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

            Método que presenta la ayuda emergente 

        """