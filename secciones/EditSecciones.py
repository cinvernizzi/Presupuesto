#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
    Nombre: EditSecciones.py
    Autor: Lic. Claudio Invernizzi
    Fecha: 21/10/2025
    E-Mail: cinvernizzi@dsgestion.site
    Proyecto: Presupuesto
    Comentarios: Clase que define el formulario para el abm 
                 de las secciones

"""

# importamos las librerías
from nicegui import ui
from secciones.Secciones import Secciones
import datetime

class EditSecciones:
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
        self.Items = Secciones()

        # definimos el diálogo
        with ui.dialog() as dialog:
            with ui.card().classes('w-230 h-56'):
                with ui.row():
                    self.Id = ui.input(label='Id').tooltip("Clave del registro").classes('w-5')
                    self.Orden = ui.input(label='Orden').tooltip("Número de Orden").classes('w-20')
                with ui.row():
                    self.Seccion = ui.input(label='Sección').tooltip("Nombre de la Sección").classes('w-96')
                    self.Fecha = ui.input(label='Fecha').tooltip("Fecha de alta").classes('w-21')
                with ui.row():
                    ui.button("Grabar", icon='save', on_click=self.verificaSeccion).tooltip("Pulse para grabar el registro").classes('w-40')
                    ui.button("Cancelar", icon='cancel', on_click=dialog.close).tooltip("Reinicia el formulario").classes('w-40')

        # asignamos la fecha actual por defecto
        ahora = datetime.datetime.now()
        self.Fecha.value = ahora.strftime("%d/%m/%Y")

        # presentamos el diálogo
        dialog.open()

    def verificaSeccion(self):
        pass
