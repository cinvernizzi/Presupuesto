#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""

    Nombre: FormClientes.py
    Autor: Lic. Claudio Invernizzi
    Fecha: 15/01/2026
    E-Mail: cinvernizzi@dsgestion.site
    Licencia: GPL
    Proyecto: Presupuesto
    Comentarios: Clase que recibe como parámetro el contenedor de 
                 el formulario de clientes y agrega los elementos 
                 al mismo 

"""

# importamos las librerías
from clases.fuentes import Fuentes
from clientes.EventosClientes import EventosClientes
from PySide6 import QtGui
from PySide6 import QtCore
from PySide6.QtWidgets import QLabel, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton

class FormClientes:
    """
    
        :Author: Claudio Invernizzi <cinvernizzi@dsgestion.site>

        Definición de la clase 

    """

    def __init__(self, contenedor):
        """

        :author: Claudio Invernizzi <cinvernizzi@dsgestion.site>        
        :param self: la clase contenedora
        :param contenedor: el layout contenedor del formulario 

        Constructor de la clase, recibe como parámetro el layout
        contenedor del formulario 

        """

        # instanciamos la clase de eventos
        self.Eventos = EventosClientes(self)

        # instanciamos la fuente
        fuente = Fuentes()

        cTitulo = QVBoxLayout()
        cTitulo.setAlignment(QtCore.Qt.AlignTop)
        lForm = QLabel("Datos del Cliente")
        lForm.setFont(fuente.normal)
        lForm.setAlignment(QtCore.Qt.AlignTop)
        cTitulo.addWidget(lForm)

        # definimos la primer fila 
        fila1 = QHBoxLayout()
        fila1.setAlignment(QtCore.Qt.AlignTop)

        # agregamos la clave
        lId = QLabel("Id:")
        lId.setFont(fuente.normal)
        fila1.addWidget(lId)
        self.tId = QLineEdit()
        self.tId.setFont(fuente.normal)
        self.tId.setToolTip("Clave del Registro")
        self.tId.setMaximumWidth(40)
        self.tId.setMinimumHeight(30)
        self.tId.setReadOnly(True)
        fila1.addWidget(self.tId)

        # agregamos el nombre
        lNombre = QLabel("Nombre:")
        lNombre.setFont(fuente.normal)
        fila1.addWidget(lNombre)
        self.tNombre = QLineEdit()
        self.tNombre.setFont(fuente.normal)
        self.tNombre.setToolTip("Nombre completo del cliente")
        self.tNombre.setMinimumWidth(200)
        self.tNombre.setMinimumHeight(30)
        fila1.addWidget(self.tNombre)

        # agregamos la dirección 
        lDireccion = QLabel("Domicilio:")
        lDireccion.setFont(fuente.normal)
        fila1.addWidget(lDireccion)
        self.tDireccion = QLineEdit()
        self.tDireccion.setFont(fuente.normal)
        self.tDireccion.setToolTip("Dirección postal del cliente")
        self.tDireccion.setMinimumWidth(200)
        self.tDireccion.setMinimumHeight(30)
        fila1.addWidget(self.tDireccion)

        # agregamos la primer fila 
        cTitulo.addLayout(fila1)

        # definimos la segunda fila 
        fila2 = QHBoxLayout()
        fila2.setAlignment(QtCore.Qt.AlignTop)

        # agregamos la clave tributaria
        lTributaria = QLabel("Id Tributaria:")
        lTributaria.setFont(fuente.normal)
        fila2.addWidget(lTributaria)
        self.tTributaria = QLineEdit()
        self.tTributaria.setFont(fuente.normal)
        self.tTributaria.setToolTip("Clave tributaria del cliente")
        self.tTributaria.setMaximumWidth(120)
        self.tTributaria.setMinimumHeight(30)
        fila2.addWidget(self.tTributaria)

        # agregamos el teléfono 
        lTelefono = QLabel("Teléfono:")
        lTelefono.setFont(fuente.normal)
        fila2.addWidget(lTelefono)
        self.tTelefono = QLineEdit()
        self.tTelefono.setFont(fuente.normal)
        self.tTelefono.setToolTip("Teléfono del cliente")
        self.tTelefono.setMaximumWidth(150)
        self.tTelefono.setMinimumHeight(30)
        fila2.addWidget(self.tTelefono)

        # agregamos el mail 
        lMail = QLabel("E-Mail:")
        lMail.setFont(fuente.normal)
        fila2.addWidget(lMail)
        self.tMail = QLineEdit()
        self.tMail.setFont(fuente.normal)
        self.tMail.setToolTip("Dirección de correo electrónico")
        self.tMail.setMinimumHeight(30)
        fila2.addWidget(self.tMail)

        # agregamos la fecha de alta
        lAlta = QLabel("Alta:")
        lAlta.setFont(fuente.normal)
        fila2.addWidget(lAlta)
        self.tAlta = QLineEdit()
        self.tAlta.setFont(fuente.normal)
        self.tAlta.setToolTip("Fecha de alta del registro")
        self.tAlta.setMaximumWidth(90)
        self.tAlta.setMinimumHeight(30)
        self.tAlta.setReadOnly(True)
        fila2.addWidget(self.tAlta)

        # agregamos la segunda fila 
        cTitulo.addLayout(fila2)

        # definimos la tercer fila 
        fila3 = QHBoxLayout()
        fila3.setAlignment(QtCore.Qt.AlignTop)

        # agregamos un espaciador
        fila3.addStretch()
        
        # agregamos el botón grabar
        self.btnGrabar = QPushButton("Grabar")
        self.btnGrabar.setFixedHeight(30)
        self.btnGrabar.setFixedWidth(120)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("recursos/grabar.png"))
        self.btnGrabar.setIcon(icon1)
        self.btnGrabar.setToolTip("Graba el registro en la base")
        fila3.addWidget(self.btnGrabar)

        # agregamos el botón cancelar
        self.btnCancelar = QPushButton("Cancelar")
        self.btnCancelar.setFixedWidth(120)
        self.btnCancelar.setFixedHeight(30)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("recursos/cancelar.png"))
        self.btnCancelar.setIcon(icon2)
        self.btnCancelar.setToolTip("Reinicia el formulario")
        fila3.addWidget(self.btnCancelar)

        # agregamos la tercer fila 
        cTitulo.addLayout(fila3)

        # agregamos al contenedor
        contenedor.addLayout(cTitulo)

    def nuevoCliente(self):
        """

        :author: Claudio Invernizzi <cinvernizzi@dsgestion.site>

        Método llamado al pulsar el botón nuevo cliente que 
        desencadena la limpieza del formulario 

        """

        # llamamos al método de la clase
        self.Eventos.nuevoCliente()

    def grabaCliente(self):
        """
        
        :author: Claudio Invernizzi <cinvernizzi@dsgestion.site>

        Método llamado al pulsar el botón grabar que verifica 
        los datos del formulario 

        """

        # llamamos al método de la clase
        self.Eventos.verificaCliente()

    def cancelaCliente(self):
        """
        
        :author: Claudio Invernizzi <cinvernizzi@dsgestion.site>

        Método llamado al pulsar el botón cancelar que recarga el 
        registro o limpia el formulario según corresponda

        """

        # llamamos al método
        self.Eventos.cancelaCliente()
    
    def verCliente(self, idcliente):
        """

        :author: Claudio Invernizzi <cinvernizzi@dsgestion.site>

        :param idcliente: clave del registro

        Método que recibe como parámetro la clave de un cliente y llama
        al evento para mostrarlo en pantalla 
        
        """

        # llamamos el evento
        self.Eventos.getDatosCliente(idcliente)
