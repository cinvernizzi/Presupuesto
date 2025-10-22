#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
    Nombre: EditProyectos.py
    Autor: Lic. Claudio Invernizzi
    Fecha: 22/10/2025
    E-Mail: cinvernizzi@dsgestion.site
    Proyecto: Presupuesto
    Comentarios: Clase que define el formulario para el abm 
                 de los proyectos

"""

# importamos las librerías
from nicegui import ui
from proyectos.Proyectos import Proyectos
import datetime

class EditProyectos:
    """
    
        @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

        Definición de la clase

    """

    def __init__(self):
        """
        
            @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

            Constructor de la clase, abre el diálogo

        """

        # instanciamos la clase 
        self.Proyecto = Proyectos()

        # definimos el diálogo
        with ui.dialog() as dialog:
            with ui.card().style('width: 1300px; height: 390px;'):

                # la primer fila 
                with ui.row():
                    self.Id = ui.input(label='Id:').tooltip("Clave del registro").classes('w-5')
                    self.Cliente = ui.select([]).tooltip("Seleccione el cliente de la lista").classes('w-64')

                # la segunda fila
                with ui.row():
                    self.Titulo = ui.input(label='Titulo:').tooltip("Título del proyecto").classes('w-128')

                # la descripción del proyecto
                with ui.row():
                    self.Descripcion = ui.textarea(label='Descripción').tooltip("Ingrese la descripción detallada").classes('w-128 h.40')

                # la fila de los botones
                with ui.row():
                    self.Fecha = ui.input("Fecha: ").tooltip("Fecha de alta del proyecto").classes('w-21')
                    ui.button("Grabar", icon='save', on_click=self.verificaProyecto).tooltip("Pulse para grabar el registro").classes('w-40')
                    ui.button("Cancelar", icon='cancel', on_click=dialog.close).tooltip("Reinicia el formulario").classes('w-40')

        # asignamos la fecha actual por defecto
        ahora = datetime.datetime.now()
        self.Fecha.value = ahora.strftime("%d/%m/%Y")

        # presentamos el diálogo
        dialog.open()

    def verificaProyecto(self):
        pass
