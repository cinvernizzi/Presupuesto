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

    def __init__(self, padre):
        """
        
            @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

            @param padre el formulario con la grilla de clientes
            
            Constructor de la clase, abre el diálogo

        """

        # instanciamos la clase 
        self.Consumidor = Clientes()

        # fijamos el padre
        self.Padre = padre

        # definimos el diálogo
        with ui.dialog() as self.dialog:
            with ui.card().style('width: 1300px; height: 320px;'):

                # presentamos la primer fila 
                with ui.row():
                    self.Id = ui.input(label='Id:').tooltip("Clave del registro").classes('w-5')
                    self.Nombre = ui.input(label='Nombre: ').tooltip("Nombre completo del cliente").classes('w-115')

                # la segunda fila
                with ui.row():
                    self.Direccion = ui.input(label='Dirección: ').tooltip("Dirección Postal").classes('w-96')
                    self.Cuil = ui.input(label='CUIL: ').tooltip("Identificación tributaria del cliente").classes('w-32')

                # la tercera fila
                with ui.row():
                    self.Telefono = ui.input(label='Teléfono: ').tooltip("Teléfono del cliente").classes('w-32')
                    self.Mail = ui.input(label='Mail: ').tooltip("Correo electrónico del cliente").classes('w-56')
                    self.Fecha = ui.input(label='Fecha: ').tooltip("Fecha de alta del registro").classes('w-21')

                # definimos la fila de los botones
                with ui.row():
                    ui.button("Grabar", icon='save', on_click=self.verificaCliente).tooltip("Pulse para grabar el registro").classes('w-40')
                    ui.button("Cancelar", icon='cancel', on_click=self.dialog.close).tooltip("Reinicia el formulario").classes('w-40')

        # asignamos la fecha actual por defecto
        ahora = datetime.datetime.now()
        self.Fecha.value = ahora.strftime("%d/%m/%Y")

        # presentamos el diálogo
        self.dialog.open()

    def verificaCliente(self):
        """
        
            @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

            Método llamado al pulsar el botón grabar que verifica 
            los datos del formulario 

        """

        # si está dando un alta
        if self.Id.value == "":
            self.Consumidor.Id = 0
        else:
            self.Consumidor.Id = int(self.Id.value)

        # verifica el nombre
        if self.Nombre.value == "":
            ui.notify("Indique el nombre del cliente", position="top-right", type="negative")
            return
        else:
            self.Consumidor.Nombre = self.Nombre.value

        # verifica la dirección 
        if self.Direccion.value == "":
            ui.notify("Ingrese la dirección postal del cliente", position="top-right", type="negative")
            return
        else:
            self.Consumidor.Direccion = self.Direccion.value

        # verifica el cuil
        if self.Cuil.value == "":
            ui.notify("Ingrese la clave tributaria del cliente", position="top-right", type="negative")
            return
        else:
            self.Consumidor.Identificacion = self.Cuil.value

        # verifica el teléfono
        if self.Telefono.value == "":
            ui.notify("Ingrese el teléfono del cliente", position="top-right", type="negative")
            return
        else:
            self.Consumidor.Telefono = self.Telefono.value

        # verifica el mail 
        if self.Mail.value == "":
            ui.notify("Ingrese la dirección de correo del cliente", position="top-right", type="negative")
            return 
        else:
            self.Consumidor.Mail = self.Mail.value

        # si llegó hasta aquí grabamos
        id = self.Consumidor.grabaCliente()

        # según el resultado
        if id != 0:

            # presenta el mensaje
            ui.notify("Registro grabado", position="top-right", type="info")

            # actualiza la grilla 
            self.Padre.tablaclientes.rows = []
            self.Padre.nominaClientes()

            # cerramos el diálogo 
            self.dialog.close()

        # si ocurrió un error
        else:

            # presenta el mensaje
            ui.notify("Ha ocurrido un error", position="top-right", type="negative")

    def getDatosCliente(self, idcliente: int):
        """
        
            @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

            @param idcliente - clave del registro 

            Método que recibe como parámetro la clave de un registro y 
            obtiene los valores del mismo y los presenta en el formulario

        """

        # obtenemos el registro
        self.Consumidor.getDatosCliente(idcliente)

        # asignamos en el formulario
        self.Id.value = str(self.Consumidor.Id)
        self.Nombre.value = self.Consumidor.Nombre
        self.Direccion.value = self.Consumidor.Direccion
        self.Cuil.value = self.Consumidor.Identificacion
        self.Telefono.value = self.Consumidor.Telefono
        self.Mail.value = self.Consumidor.Mail
