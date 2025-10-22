#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
    Nombre: EditClientes.py
    Autor: Lic. Claudio Invernizzi
    Fecha: 22/10/2025
    E-Mail: cinvernizzi@dsgestion.site
    Proyecto: Presupuesto
    Comentarios: Clase que define el formulario para el abm 
                 de los clientes

"""

# importamos las librerías
from nicegui import ui
from clientes.Clientes import Clientes
import datetime

class EditClientes:
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
        self.Consumidor = Clientes()

        # definimos el diálogo
        with ui.dialog() as dialog:
            with ui.card().style('width: 1300px; height: 370px;'):

                # presentamos la primer fila 
                with ui.row():
                    self.Id = ui.input(label='Id:').tooltip("Clave del registro").classes('w-5')
                    self.Nombre = ui.input(label='Nombre: ').tooltip("Nombre completo del cliente").classes('w-115')

                # la segunda fila 
                with ui.row():
                    self.Empresa = ui.input(label='Empresa: ').tooltip("Nombre completo de la empresa").classes('w-130')

                with ui.row():
                    self.Direccion = ui.input(label='Dirección: ').tooltip("Dirección Postal").classes('w-96')
                    self.Cuil = ui.input(label='CUIL: ').tooltip("Identificación tributaria del cliente").classes('w-32')

                with ui.row():
                    self.Telefono = ui.input(label='Teléfono: ').tooltip("Teléfono del cliente").classes('w-32')
                    self.Mail = ui.input(label='Mail: ').tooltip("Correo electrónico del cliente").classes('w-56')
                    self.Fecha = ui.input(label='Fecha: ').tooltip("Fecha de alta del registro").classes('w-21')

                # definimos la fila de los botones
                with ui.row():
                    ui.button("Grabar", icon='save', on_click=self.verificaCliente).tooltip("Pulse para grabar el registro").classes('w-40')
                    ui.button("Cancelar", icon='cancel', on_click=dialog.close).tooltip("Reinicia el formulario").classes('w-40')

        # asignamos la fecha actual por defecto
        ahora = datetime.datetime.now()
        self.Fecha.value = ahora.strftime("%d/%m/%Y")

        # presentamos el diálogo
        dialog.open()

    def verificaCliente(self):
        pass
