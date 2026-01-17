#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
    Nombre: FormPersonal.py
    Autor: Lic. Claudio Invernizzi
    Fecha: 15/10/25
    E-Mail: cinvernizzi@dsgestion.site
    Proyecto: Presupuesto
    Comentarios: Clase que define el formulario de datos 
                 personales

"""

# importamos las librerías 
from clases.fuentes import Fuentes
from personal.EventosPersonal import EventosPersonal
from PySide6.QtWidgets import QDialog, QHBoxLayout, QVBoxLayout, QLabel, QLineEdit, QPushButton
from PySide6 import QtCore
from PySide6 import QtGui
from pathlib import Path


class FormPersonal(QDialog):
    """
    
        :author: Claudio Invernizzi <cinvernizzi@dsgestion.site>

        Definición de la clase

    """

    def __init__(self, parent):
        """
        
        :author: Claudio Invernizzi <cinvernizzi@dsgestion.site>

        :param: parent el formulario padre

        Constructor de la clase, recibe como parámetro el formulario 
        padre


        """

        # instanciamos la fuente
        fuente = Fuentes()

        # instanciamos los eventos 
        self.Eventos = EventosPersonal(self)

        # instanciamos el formulario y lo fijamos como modal
        super(FormPersonal, self).__init__(parent)

        # fijamos el tamaño y el ícono 
        self.setGeometry(200, 200, 700, 250)
        self.setWindowIcon(QtGui.QIcon('recursos/logo.png'))

        # lo establecemos como modal
        self.setModal(True)

        # definimos el layout
        formulario = QVBoxLayout()

        # agregamos el título
        lTitulo = QLabel("Datos Personales")
        lTitulo.setMaximumHeight(30)
        lTitulo.setFont(fuente.negrita)
        lTitulo.setAlignment(QtCore.Qt.AlignCenter)
        formulario.addWidget(lTitulo)

        # abrimos la primer fila 
        fila1 = QHBoxLayout()

        # presenta la clave 
        lId = QLabel("Id:")
        lId.setFont(fuente.normal)
        fila1.addWidget(lId)
        self.tId = QLineEdit()
        self.tId.setFont(fuente.normal)
        self.tId.setToolTip("Clave del registro")
        self.tId.setMaximumWidth(40)
        self.tId.setMinimumHeight(30)
        self.tId.setReadOnly(True)
        fila1.addWidget(self.tId)

        # presenta el nombre 
        lNombre = QLabel("Nombre:")
        lNombre.setFont(fuente.normal)
        fila1.addWidget(lNombre)
        self.tNombre = QLineEdit()
        self.tNombre.setFont(fuente.normal)
        self.tNombre.setToolTip("Su nombre como aparecerá en el presupuesto")
        self.tNombre.setMinimumWidth(200)
        self.tNombre.setMinimumHeight(30)
        fila1.addWidget(self.tNombre)

        # presenta la empresa
        lEmpresa = QLabel("Empresa:")
        lEmpresa.setFont(fuente.normal)
        fila1.addWidget(lEmpresa)
        self.tEmpresa = QLineEdit()
        self.tEmpresa.setFont(fuente.normal)
        self.tEmpresa.setToolTip("La empresa como aparecerá en el presupuesto")
        self.tEmpresa.setMinimumWidth(200)
        self.tEmpresa.setMinimumHeight(30)
        fila1.addWidget(self.tEmpresa)

        # agregamos la fila 
        formulario.addLayout(fila1)

        # abrimos la segunda fila 
        fila2 = QHBoxLayout()

        # presenta la dirección 
        lDireccion = QLabel("Direccion:")
        lDireccion.setFont(fuente.normal)
        fila2.addWidget(lDireccion)
        self.tDireccion = QLineEdit()
        self.tDireccion.setFont(fuente.normal)
        self.tDireccion.setToolTip("El domicilio como aparecerá en el presupuesto")
        self.tDireccion.setMinimumWidth(200)
        self.tDireccion.setMinimumHeight(30)
        fila2.addWidget(self.tDireccion)

        # presenta el cuil 
        lCuil = QLabel("Id Tributaria:")
        lCuil.setFont(fuente.normal)
        fila2.addWidget(lCuil)
        self.tCuil = QLineEdit()
        self.tCuil.setFont(fuente.normal)
        self.tCuil.setToolTip("Su identificación tributaria")
        self.tCuil.setMinimumWidth(120)
        self.tCuil.setMinimumHeight(30)
        fila2.addWidget(self.tCuil)

        # agregamos la segunda fila 
        formulario.addLayout(fila2)

        # define la tercer fila 
        fila3 = QHBoxLayout()

        # presenta el teléfono 
        lTelefono = QLabel("Teléfono:")
        lTelefono.setFont(fuente.normal)
        fila3.addWidget(lTelefono)
        self.tTelefono = QLineEdit()
        self.tTelefono.setFont(fuente.normal)
        self.tTelefono.setToolTip("Teléfono del cliente")
        self.tTelefono.setMaximumWidth(150)
        self.tTelefono.setMinimumHeight(30)
        fila3.addWidget(self.tTelefono)

        # presenta el mail 
        lMail = QLabel("E-Mail:")
        lMail.setFont(fuente.normal)
        fila3.addWidget(lMail)
        self.tMail = QLineEdit()
        self.tMail.setFont(fuente.normal)
        self.tMail.setToolTip("Dirección de correo electrónico")
        self.tMail.setMinimumHeight(30)
        fila3.addWidget(self.tMail)

        # agrega la segunda fila 
        formulario.addLayout(fila3)

        # define la tercer fila 
        fila4 = QHBoxLayout()

        # agregamos un espaciador
        fila4.addStretch()

        # verificamos si existe el logo
        file_path = "temp/logo.png"
        if Path(file_path).is_file():
            icon3 = QtGui.QIcon()
            icon3.addPixmap(QtGui.QPixmap("temp/logo.png"))            
        else:
            icon3 = QtGui.QIcon()
            icon3.addPixmap(QtGui.QPixmap("recursos/imagen_no_disponible.gif"))

        # presenta el logo 
        self.btnLogo = QPushButton()
        self.btnLogo.setFixedHeight(60)
        self.btnLogo.setFixedWidth(60)
        self.btnLogo.setIcon(icon3)
        self.btnLogo.setIconSize(QtCore.QSize(60,60))
        self.btnLogo.setToolTip("Pulse para actualizar su logo")
        fila4.addWidget(self.btnLogo)

        # asignamos el evento
        self.btnLogo.clicked.connect(self.Eventos.seleccionarLogo)

        # presenta la fecha 
        lAlta = QLabel("Alta:")
        lAlta.setFont(fuente.normal)
        fila4.addWidget(lAlta)
        self.tAlta = QLineEdit()
        self.tAlta.setFont(fuente.normal)
        self.tAlta.setToolTip("Fecha de alta del registro")
        self.tAlta.setMaximumWidth(90)
        self.tAlta.setMinimumHeight(30)
        self.tAlta.setReadOnly(True)
        fila4.addWidget(self.tAlta)

        # presenta el botón secciones
        self.btnSecciones = QPushButton("Secciones")
        self.btnSecciones.setFixedHeight(30)
        self.btnSecciones.setFixedWidth(120)
        self.btnSecciones.setToolTip("Edita las secciones de un presupuesto")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("recursos/secciones.png"))
        self.btnSecciones.setIcon(icon4)
        fila4.addWidget(self.btnSecciones)

        # presenta el botón grabar
        self.btnGrabar = QPushButton("Grabar")
        self.btnGrabar.setFixedHeight(30)
        self.btnGrabar.setFixedWidth(120)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("recursos/grabar.png"))
        self.btnGrabar.setIcon(icon1)
        self.btnGrabar.setToolTip("Graba el registro en la base")
        fila4.addWidget(self.btnGrabar)

        # asignamos el evento
        self.btnGrabar.clicked.connect(self.Eventos.verificaPersonal)

        # presenta el botón cancelar 
        self.btnCancelar = QPushButton("Cancelar")
        self.btnCancelar.setFixedWidth(120)
        self.btnCancelar.setFixedHeight(30)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("recursos/cancelar.png"))
        self.btnCancelar.setIcon(icon2)
        self.btnCancelar.setToolTip("Cierra el formulario")
        fila4.addWidget(self.btnCancelar)

        # asignamos el evento
        self.btnCancelar.clicked.connect(self.Eventos.cancelaPersonal)

        # agregamos la tercer fila 
        formulario.addLayout(fila4)

        # fijamos el layout 
        self.setLayout(formulario)

        # mostramos el formulario 
        self.show()

        # cargamos el registro 
        self.Eventos.cargaPersonal()
        