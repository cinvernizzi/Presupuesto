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
from PySide6.QtWidgets import QDialog, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QLineEdit, QPushButton
from PySide6 import QtCore
from PySide6 import QtGui
from personal.Personal import Personal

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
        tId = QLineEdit()
        tId.setFont(fuente.normal)
        tId.setToolTip("Clave del registro")
        tId.setMaximumWidth(40)
        tId.setMinimumHeight(30)
        tId.setReadOnly(True)
        fila1.addWidget(tId)

        # presenta el nombre 
        lNombre = QLabel("Nombre:")
        lNombre.setFont(fuente.normal)
        fila1.addWidget(lNombre)
        tNombre = QLineEdit()
        tNombre.setFont(fuente.normal)
        tNombre.setToolTip("Su nombre como aparecerá en el presupuesto")
        tNombre.setMinimumWidth(200)
        tNombre.setMinimumHeight(30)
        fila1.addWidget(tNombre)

        # presenta la empresa
        lEmpresa = QLabel("Empresa:")
        lEmpresa.setFont(fuente.normal)
        fila1.addWidget(lEmpresa)
        tEmpresa = QLineEdit()
        tEmpresa.setFont(fuente.normal)
        tEmpresa.setToolTip("La empresa como aparecerá en el presupuesto")
        tEmpresa.setMinimumWidth(200)
        tEmpresa.setMinimumHeight(30)
        fila1.addWidget(tEmpresa)

        # agregamos la fila 
        formulario.addLayout(fila1)

        # abrimos la segunda fila 
        fila2 = QHBoxLayout()

        # presenta la dirección 
        lDireccion = QLabel("Direccion:")
        lDireccion.setFont(fuente.normal)
        fila2.addWidget(lDireccion)
        tDireccion = QLineEdit()
        tDireccion.setFont(fuente.normal)
        tDireccion.setToolTip("El domicilio como aparecerá en el presupuesto")
        tDireccion.setMinimumWidth(200)
        tDireccion.setMinimumHeight(30)
        fila2.addWidget(tDireccion)

        # presenta el cuil 
        lCuil = QLabel("Id Tributaria:")
        lCuil.setFont(fuente.normal)
        fila2.addWidget(lCuil)
        tCuil = QLineEdit()
        tCuil.setFont(fuente.normal)
        tCuil.setToolTip("Su identificación tributaria")
        tCuil.setMinimumWidth(120)
        tCuil.setMinimumHeight(30)
        fila2.addWidget(tCuil)

        # agregamos la segunda fila 
        formulario.addLayout(fila2)

        # define la tercer fila 
        fila3 = QHBoxLayout()

        # presenta el teléfono 
        lTelefono = QLabel("Teléfono:")
        lTelefono.setFont(fuente.normal)
        fila3.addWidget(lTelefono)
        tTelefono = QLineEdit()
        tTelefono.setFont(fuente.normal)
        tTelefono.setToolTip("Teléfono del cliente")
        tTelefono.setMaximumWidth(150)
        tTelefono.setMinimumHeight(30)
        fila3.addWidget(tTelefono)

        # presenta el mail 
        lMail = QLabel("E-Mail:")
        lMail.setFont(fuente.normal)
        fila3.addWidget(lMail)
        tMail = QLineEdit()
        tMail.setFont(fuente.normal)
        tMail.setToolTip("Dirección de correo electrónico")
        tMail.setMinimumHeight(30)
        fila3.addWidget(tMail)

        # agrega la segunda fila 
        formulario.addLayout(fila3)

        # define la tercer fila 
        fila4 = QHBoxLayout()

        # agregamos un espaciador
        fila4.addStretch()

        # presenta la fecha 
        lAlta = QLabel("Alta:")
        lAlta.setFont(fuente.normal)
        fila4.addWidget(lAlta)
        tAlta = QLineEdit()
        tAlta.setFont(fuente.normal)
        tAlta.setToolTip("Fecha de alta del registro")
        tAlta.setMaximumWidth(90)
        tAlta.setMinimumHeight(30)
        tAlta.setReadOnly(True)
        fila4.addWidget(tAlta)

        # presenta el botón grabar
        btnGrabar = QPushButton("Grabar")
        btnGrabar.setFixedHeight(30)
        btnGrabar.setFixedWidth(120)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("recursos/grabar.png"))
        btnGrabar.setIcon(icon1)
        btnGrabar.setToolTip("Graba el registro en la base")
        fila4.addWidget(btnGrabar)

        # presenta el botón cancelar 
        btnCancelar = QPushButton("Cancelar")
        btnCancelar.setFixedWidth(120)
        btnCancelar.setFixedHeight(30)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("recursos/cancelar.png"))
        btnCancelar.setIcon(icon2)
        btnCancelar.setToolTip("Reinicia el formulario")
        fila4.addWidget(btnCancelar)

        # agregamos la tercer fila 
        formulario.addLayout(fila4)

        # fijamos el layout 
        self.setLayout(formulario)

        # mostramos el formulario 
        self.show()
        