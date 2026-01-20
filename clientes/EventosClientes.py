#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
    Nombre: EventosClientes.py
    Autor: Lic. Claudio Invernizzi
    Fecha: 18/10/25
    E-Mail: cinvernizzi@dsgestion.site
    Proyecto: Presupuesto
    Comentarios: Clase que controla las operaciones sobre el 
                 formulario de clientes

"""

# importamos las librerías
from datetime import datetime
from clientes.Clientes import Clientes
from clases.mensaje import Mensaje

class EventosClientes:
    """
    
    :author: Claudio Invernizzi <cinvernizzi@dsgestion.site>

    Definición de la clase 

    """

    def __init__(self, formclientes):
        """

        :author: Claudio Invernizzi <cinvernizzi@dsgestion.site>

        :param: formclientes el formulario de datos de los clientes

        Constructor de la clase, recibe como parámetro el formulario 
        de clientes

        """

        # asignamos en la clase
        self.FormClientes = formclientes

        # instanciamos la clase de la base de datos 
        self.Clientes = Clientes()

    def nuevoCliente(self):
        """

        :author: Claudio Invernizzi <cinvernizzi@dsgestion.site>

        Método que limpia el formulario preparándolo para un nuevo 
        ingreso

        """

        # limpiamos
        self.FormClientes.tId.clear()
        self.FormClientes.tNombre.clear()
        self.FormClientes.tDireccion.clear()
        self.FormClientes.tTributaria.clear()
        self.FormClientes.tTelefono.clear()
        self.FormClientes.tMail.clear()

        # fijamos la fecha de alta
        ahora = datetime.now()
        self.FormClientes.tAlta.setText(ahora.strftime("%d/%m/%Y"))        

        # fijamos el foco
        self.FormClientes.tNombre.setFocus()

    def getDatosCliente(self, idcliente):
        """

        :author: Claudio Invernizzi <cinvernizzi@dsgestion.site>

        :param self: la propia clase
        :param idcliente: entero con la clave del cliente

        Método que recibe como parámetro la clave del cliente y obtiene
        los datos del mismo y los presenta en el formulario

        """

        # obtenemos el registro
        self.Clientes.getDatosCliente(idcliente)

        # asignamos en el formulario
        self.FormClientes.tId.setText(str(self.Clientes.Id))
        self.FormClientes.tNombre.setText(self.Clientes.Nombre)
        self.FormClientes.tDireccion.setText(self.Clientes.Direccion)
        self.FormClientes.tTributaria.setText(self.Clientes.Identificacion)
        self.FormClientes.tTelefono.setText(self.Clientes.Telefono)
        self.FormClientes.tMail.setText(self.Clientes.Mail)
        self.FormClientes.tAlta.setText(self.Clientes.Fecha)        

        # fijamos el foco
        self.FormClientes.tNombre.setFocus()

    def cancelaCliente(self):
        """
        
        :author: Claudio Invernizzi <cinvernizzi@dsgestion.site>
        
        Método llamado al pulsar sobre el botón cancelar que 
        según el estado recarga el registro o lo limpia 

        """

        # si está editando
        if self.FormClientes.tId.text():

            # recargamos el registro
            self.getDatosCliente(self.FormClientes.tId.text())

        # si está insertando
        else:

            # limpiamos el formulario
            self.nuevoCliente()

    def verificaCliente(self):
        """
        
        :author: Claudio Invernizzi <cinvernizzi@dsgestion.site>

        Método llamado al pulsar el botón grabar que verifica 
        los datos del formulario 

        """

        # si está dando de alta
        if not self.FormClientes.tId.text():
            self.Clientes.Id = 0
        else:
            self.Clientes.Id = self.FormClientes.tId.text()

        # verifica el nombre 
        if not self.FormClientes.tNombre.text():
            Mensaje(self.FormClientes, "Ingrese el nombre del cliente")
            return
        else:
            self.Clientes.Nombre = self.FormClientes.tNombre.text()

        # verifica el domicilio 
        if not self.FormClientes.tDireccion.text():
            Mensaje(self.FormClientes, "Indique el domicilio del cliente")
            return
        else:
            self.Clientes.Direccion = self.FormClientes.tDireccion.text()

        # verifica la clave tributaria
        if not self.FormClientes.tTributaria.text():
            Mensaje(self.FormClientes, "Indique la clave tributaria")
            return
        else:
            self.Clientes.Identificacion = self.FormClientes.tTributaria.text()

        # verifica que al menos exista teléfono o mail 
        if not self.FormClientes.tTelefono.text() and not self.FormClientes.tMail.text():
            Mensaje(self.FormClientes, "Indique al menos una forma de contacto")
            return
        else:
            self.Clientes.Telefono = self.FormClientes.tTelefono.text()
            self.Clientes.Mail = self.FormClientes.tMail.text()

        # si llegó hasta aquí grabamos el registro
        if int(self.Clientes.grabaCliente()) != 0:

            # si estaba insertando actualiza la fecha
            if not self.FormClientes.tAlta.text():
                ahora = datetime.now()
                self.FormClientes.tAlta.setText(ahora.strftime("%d/%m/%Y"))

            # asignamos en el formulario 
            self.FormClientes.tId.setText(str(id))
            Mensaje(self.FormClientes, "Registro grabado ... ")
        
        else:

            # presenta el mensaje
            Mensaje(self.FormClientes, "Ha ocurrido un error")
