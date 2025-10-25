#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
    Nombre: FormPersonal.py
    Autor: Lic. Claudio Invernizzi
    Fecha: 21/10/2025
    E-Mail: cinvernizzi@dsgestion.site
    Proyecto: Presupuesto
    Comentarios: Clase que define el formulario con los datos 
                 del usuario

"""

# importamos las librerías
from nicegui import ui, events
from nicegui.events import UploadEventArguments
from personal.Personal import Personal
import datetime

class FormPersonal:
    """
    
        @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

        Definición de la clase

    """

    def __init__(self):
        """
        
            @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

            Constructor de la clase, carga en el tabulador la 
            definición del formulario

        """

        # instanciamos la clase 
        self.Datos = Personal()
        
        # presenta un mensaje
        ui.label("Formulario de Datos Personales").style('font-size: 20px; font-weight: bold;')

        # abrimos la fila 
        with ui.row():
            self.Id = ui.input(label='Id').tooltip("Clave del registro").classes('w-5')
            self.Nombre = ui.input(label='Nombre: ').tooltip("Su nombre como aparecerá en el presupuesto").classes('w-64')
            self.Empresa = ui.input(label='Empresa: ').tooltip("Nombre de la empresa").classes('w-64')

        # la segunda fila
        with ui.row():
            self.Direccion = ui.input(label="Direccion: ").tooltip("Dirección postal del presupuesto").classes('w-128')

        # la tercer fila
        with ui.row():
            self.Cuil = ui.input(label="CUIL: ").tooltip("Identificación tributaria").classes('w-32')
            self.Telefono = ui.input(label="Teléfono: ").tooltip("Teléfono de contacto").classes('w-32')
            self.Mail = ui.input(label="E-Mail: ").tooltip("Dirección de Correo Electrónico").classes('w-64')
            self.Fecha = ui.input(label="Fecha: ").tooltip("Fecha de alta del registro").classes('w-21')
            ui.upload(label='Logo del Presupuesto', on_upload=self.handle_upload)

        # la fila de los botones
        with ui.row():
            ui.button("Grabar", icon='save', on_click=self.verificaPersonal).tooltip("Pulse para grabar el registro").classes('w-40')
            ui.button("Cancelar", icon='cancel', on_click=self.cancelaPersonal).tooltip("Reinicia el formulario").classes('w-40')

        # asignamos la fecha actual por defecto
        ahora = datetime.datetime.now()
        self.Fecha.value = ahora.strftime("%d/%m/%Y")
            
        # cargamos los valores iniciales
        self.getDatosPersona()

    # definimos el controlador de la subida de archivos
    def handle_upload(self, e):
        with open('recursos/logositio.png', 'w') as f:
            f.write(e.file.read())

    def verificaPersonal(self):
        """
        
            @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

            Método llamado al pulsar el botón grabar que verifica
            los datos del formulario

        """

        # según la clave
        if self.Id.value == "":
            self.Datos.Id = 0
        else:
            self.Datos.Id = int(self.Id.value)

        # si no ingresó el nombre
        if self.Nombre.value == "":
            ui.notify("Ingrese su nombre", position="top-right", type="negative")
            return 
        else:
            self.Datos.Nombre = self.Nombre.value

        # verificamos el nombre de la empresa
        if self.Empresa.value == "":
            ui.notify("Ingrese el nombre de la empresa", position="top-right", type="negative")
            return 
        else:
            self.Datos.Empresa = self.Empresa.value

        # verificamos la dirección 
        if self.Direccion.value == "":
            ui.notify("Ingrese la dirección de facturación", position="top-right", type="negative")
            return 
        else:
            self.Datos.Direccion = self.Direccion.value

        # la identificación tributaria
        if self.Cuil.value == "":
            ui.notify("Ingrese la identificación tributaria", position="top-right", type="negative")
            return 
        else:
            self.Datos.Cuil = self.Cuil.value

        # el teléfono 
        if self.Telefono.value == "":
            ui.notify("Ingrese un número de teléfono", position="top-right", type="negative")
            return 
        else:
            self.Datos.Telefono = self.Telefono.value

        # el mail 
        if self.Mail.value == "":
            ui.notify("Ingrese la dirección de mail", position="top-right", type="negative")
            return 
        else:
            self.Datos.Mail = self.Mail.value

        # si llegó hasta aquí grabamos
        id = self.Datos.grabaPersonal()

        # si salió todo bien
        if id != 0:
            ui.notify("Registro grabado", position="top-right", type="info")
            self.Id.value = str(id)
        else:
            ui.notify("Ha ocurrido un error", position="top-right", type="negative")

    def cancelaPersonal(self):
        """
        
            @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

            Método llamado al pulsar el botón cancelar que reinicia
            el formulario

        """

        # si está editando 
        if self.Id.value != "":
            self.getDatosPersona()
        else:
            self.limpiaFormulario()

    def limpiaFormulario(self):
        """
        
            @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

            Método que simplemente deja el formulario en blanco 

        """

        # limpiamos los valores
        self.Id.value = ""
        self.Nombre.value = ""
        self.Empresa.value = ""
        self.Direccion.value = ""
        self.Cuil.value = ""
        self.Telefono.value = ""
        self.Mail.value = ""
        ahora = datetime.datetime.now()
        self.Fecha.value = ahora.strftime("%d/%m/%Y")

    def getDatosPersona(self):
        """
        
            @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

            Método llamado al cargar el formulario que verifica si 
            existe un registro y en todo caso lo carga

        """

        # obtenemos los datos del registro
        self.Datos.getDatosPersonal()

        # si hay un registro activo
        if self.Datos.Id > 0:

            # asignamos en el formulario
            self.Id.value = str(self.Datos.Id)
            self.Nombre.value = self.Datos.Nombre
            self.Empresa.value = self.Datos.Empresa
            self.Direccion.value = self.Datos.Direccion
            self.Cuil.value = self.Datos.Cuil
            self.Telefono.value = self.Datos.Telefono
            self.Mail.value = self.Datos.Mail
            self.Fecha.value = self.Datos.Fecha
