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

    def __init__(self, padre):
        """
        
            @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

            @param padre el formulario con la grilla de secciones

            Constructor de la clase, abre el diálogo

        """

        # instanciamos la clase 
        self.Items = Secciones()

        # fijamos el formulario padre
        self.Padre = padre

        # definimos el diálogo
        with ui.dialog() as self.dialog:
            with ui.card().classes('w-230 h-56'):
                with ui.row():
                    self.Id = ui.input(label='Id').tooltip("Clave del registro").classes('w-5')
                    self.Orden = ui.input(label='Orden').tooltip("Número de Orden").classes('w-20')
                with ui.row():
                    self.Seccion = ui.input(label='Sección').tooltip("Nombre de la Sección").classes('w-96')
                    self.Fecha = ui.input(label='Fecha').tooltip("Fecha de alta").classes('w-21')
                with ui.row():
                    ui.button("Grabar", icon='save', on_click=self.verificaSeccion).tooltip("Pulse para grabar el registro").classes('w-40')
                    ui.button("Cancelar", icon='cancel', on_click=self.dialog.close).tooltip("Reinicia el formulario").classes('w-40')

        # asignamos la fecha actual por defecto
        ahora = datetime.datetime.now()
        self.Fecha.value = ahora.strftime("%d/%m/%Y")

        # presentamos el diálogo
        self.dialog.open()

    def verificaSeccion(self):
        """
        
            @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

            Método llamado al pulsar el botón grabar que verifica 
            los datos antes de enviarlo al servidor

        """

        # si está insertando 
        if self.Id.value == "":
            self.Items.Id = 0
        else:
            self.Items.Id = int(self.Id.value)

        # si no ingresó el orden
        if self.Orden.value == "":
            ui.notify("Ingrese el orden de la sección", position="top-right", type="negative")
            return
        else:
            self.Items.Orden = int(self.Orden.value)

        # si no indicó la descripción
        if self.Seccion.value == "":
            ui.notify("Ingrese la descripción de la sección", position="top-right", type="negative")
            return 
        else:
            self.Items.Etapa = self.Seccion.value

        # grabamos el registro
        id = self.Items.grabaSeccion()

        # si pudo grabar
        if id != 0:

            # presenta el mensaje
            ui.notify("Registro grabado", position="top-right", type="info")

            # actualizamos la grilla
            self.Padre.tablasecciones.rows = []
            self.Padre.cargaSecciones()
            
            # cerramos el formulario
            self.dialog.close()

        # si ocurrió un error
        else:

            # presenta el mensaje
            ui.notify("Ha ocurrido un error", position="top-right", type="negative")