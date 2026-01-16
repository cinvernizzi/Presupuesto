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
        tId = QLineEdit()
        tId.setFont(fuente.normal)
        tId.setToolTip("Clave del Registro")
        tId.setMaximumWidth(40)
        tId.setMinimumHeight(30)
        tId.setReadOnly(True)
        fila1.addWidget(tId)

        # agregamos el nombre
        lNombre = QLabel("Nombre:")
        lNombre.setFont(fuente.normal)
        fila1.addWidget(lNombre)
        tNombre = QLineEdit()
        tNombre.setFont(fuente.normal)
        tNombre.setToolTip("Nombre completo del cliente")
        tNombre.setMinimumWidth(200)
        tNombre.setMinimumHeight(30)
        fila1.addWidget(tNombre)

        # agregamos la dirección 
        lDireccion = QLabel("Domicilio:")
        lDireccion.setFont(fuente.normal)
        fila1.addWidget(lDireccion)
        tDireccion = QLineEdit()
        tDireccion.setFont(fuente.normal)
        tDireccion.setToolTip("Dirección postal del cliente")
        tDireccion.setMinimumWidth(200)
        tDireccion.setMinimumHeight(30)
        fila1.addWidget(tDireccion)

        # agregamos la primer fila 
        cTitulo.addLayout(fila1)

        # definimos la segunda fila 
        fila2 = QHBoxLayout()
        fila2.setAlignment(QtCore.Qt.AlignTop)

        # agregamos la clave tributaria
        lTributaria = QLabel("Id Tributaria:")
        lTributaria.setFont(fuente.normal)
        fila2.addWidget(lTributaria)
        tTributaria = QLineEdit()
        tTributaria.setFont(fuente.normal)
        tTributaria.setToolTip("Clave tributaria del cliente")
        tTributaria.setMaximumWidth(120)
        tTributaria.setMinimumHeight(30)
        fila2.addWidget(tTributaria)

        # agregamos el teléfono 
        lTelefono = QLabel("Teléfono:")
        lTelefono.setFont(fuente.normal)
        fila2.addWidget(lTelefono)
        tTelefono = QLineEdit()
        tTelefono.setFont(fuente.normal)
        tTelefono.setToolTip("Teléfono del cliente")
        tTelefono.setMaximumWidth(150)
        tTelefono.setMinimumHeight(30)
        fila2.addWidget(tTelefono)

        # agregamos el mail 
        lMail = QLabel("E-Mail:")
        lMail.setFont(fuente.normal)
        fila2.addWidget(lMail)
        tMail = QLineEdit()
        tMail.setFont(fuente.normal)
        tMail.setToolTip("Dirección de correo electrónico")
        tMail.setMinimumHeight(30)
        fila2.addWidget(tMail)

        # agregamos la fecha de alta
        lAlta = QLabel("Alta:")
        lAlta.setFont(fuente.normal)
        fila2.addWidget(lAlta)
        tAlta = QLineEdit()
        tAlta.setFont(fuente.normal)
        tAlta.setToolTip("Fecha de alta del registro")
        tAlta.setMaximumWidth(90)
        tAlta.setMinimumHeight(30)
        tAlta.setReadOnly(True)
        fila2.addWidget(tAlta)

        # agregamos la segunda fila 
        cTitulo.addLayout(fila2)

        # definimos la tercer fila 
        fila3 = QHBoxLayout()
        fila3.setAlignment(QtCore.Qt.AlignTop)

        # agregamos un espaciador
        fila3.addStretch()
        
        # agregamos el botón grabar
        btnGrabar = QPushButton("Grabar")
        btnGrabar.setFixedHeight(30)
        btnGrabar.setFixedWidth(120)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("recursos/grabar.png"))
        btnGrabar.setIcon(icon1)
        btnGrabar.setToolTip("Graba el registro en la base")
        fila3.addWidget(btnGrabar)

        # agregamos el botón cancelar
        btnCancelar = QPushButton("Cancelar")
        btnCancelar.setFixedWidth(120)
        btnCancelar.setFixedHeight(30)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("recursos/cancelar.png"))
        btnCancelar.setIcon(icon2)
        btnCancelar.setToolTip("Reinicia el formulario")
        fila3.addWidget(btnCancelar)

        # agregamos la tercer fila 
        cTitulo.addLayout(fila3)

        # agregamos al contenedor
        contenedor.addLayout(cTitulo)
