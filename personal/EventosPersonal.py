#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
    Nombre: EventosPersonal.py
    Autor: Lic. Claudio Invernizzi
    Fecha: 16/10/25
    E-Mail: cinvernizzi@dsgestion.site
    Proyecto: Presupuesto
    Comentarios: Clase que controla los eventos del formulario 
                 de datos personales

"""

# importamos las librerías 
from clases.mensaje import Mensaje
from personal.Personal import Personal
from datetime import datetime

class EventosPersonal():
    """
    
        :author: Claudio Invernizzi <cinvernizzi@dsgestion.site>

        Definición de la clase

    """

    def __init__(self, formpersonal):
        """
        
        :author: Claudio Invernizzi <cinvernizzi@dsgestion.site>

        :param: formpersonal el formulario de datos personales

        Constructor de la clase, recibe como parámetro el formulario 
        de datos personales

        """

        # asignamos en la clase
        self.FormPersonal = formpersonal

        # instanciamos la clase
        self.Personal = Personal()

    def cancelaPersonal(self):
        """
        
        :author: Claudio Invernizzi <cinvernizzi@dsgestion.site>

        Método llamado al pulsar el botón cancelar que cierra el 
        formulario
        
        """

        # cerramos 
        self.FormPersonal.close()

    def verificaPersonal(self):
        """
                
        :author: Claudio Invernizzi <cinvernizzi@dsgestion.site>

        Método llamado al pulsar el botón aceptar que verifica 
        el formulario y luego graba el registro 

        """

        # verifica si está insertando
        if not self.FormPersonal.tId.text():
            self.Personal.Id = 0
        else:
            self.Personal.Id = self.FormPersonal.tId.text()

        # si no declaró el nombre
        if not self.FormPersonal.tNombre.text():
            Mensaje(self.FormPersonal, "Ingrese su nombre completo")
            return
        else:
            self.Personal.Nombre = self.FormPersonal.tNombre.text()

        # si no declaró la empresa
        if not self.FormPersonal.tEmpresa.text():
            Mensaje(self.FormPersonal, "Ingrese el nombre de la empresa")
            return
        else:
            self.Personal.Empresa = self.FormPersonal.tEmpresa.text()

        # si no ingresó la dirección 
        if not self.FormPersonal.tDireccion.text():
            Mensaje(self.FormPersonal, "Ingrese la dirección postal")
            return
        else:
            self.Personal.Direccion = self.FormPersonal.tDireccion.text()

        # si no indicó la clave tributaria 
        if not self.FormPersonal.tCuil.text():
            Mensaje(self.FormPersonal, "Ingrese la clave tributaria")
            return
        else:
            self.Personal.Cuil = self.FormPersonal.tCuil.text()

        # si no ingresó el teléfono 
        if not self.FormPersonal.tTelefono.text():
            Mensaje(self.FormPersonal, "Indique un teléfono de contacto")
            return
        else:
            self.Personal.Telefono = self.FormPersonal.tTelefono.text()

        # si no ingresó el mail 
        if not self.FormPersonal.tMail.text():
            Mensaje(self.Personal, "Indique un correo electrónico")
            return
        else:
            self.Personal.Mail = self.FormPersonal.tMail.text()

        # si llegó hasta aquí grabamos
        id = self.Personal.grabaPersonal()

        # si pudo grabar
        if id != 0:

            # si estaba insertando actualiza la fecha
            if not self.FormPersonal.tId.text():
                ahora = datetime.now()
                self.FormPersonal.tAlta.setText(ahora.strftime("%d/%m/%Y"))

            # asignamos en el formulario 
            self.FormPersonal.tId.setText(str(id))
            Mensaje(self.FormPersonal, "Registro grabado ... ")
        
        else:

            # presenta el mensaje
            Mensaje(self.FormPersonal, "Ha ocurrido un error")

    def cargaPersonal(self):
        """
        
        :author: Claudio Invernizzi <cinvernizzi@dsgestion.site>

        Método llamado al cargar el formulario que verifica si 
        existe un registro (siempre hay solo uno) de datos 
        personales y lo carga

        """

