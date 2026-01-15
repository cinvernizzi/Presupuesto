#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""

    Nombre: NominaProyectos.py
    Autor: Lic. Claudio Invernizzi
    Fecha: 15/01/2026
    E-Mail: cinvernizzi@dsgestion.site
    Licencia: GPL
    Proyecto: Presupuesto
    Comentarios: Clase que recibe como parámetro el contenedor de 
                 el formulario de clientes y agrega los filtros 
                 y la grilla de proyectos del cliente

"""

# importamos las librerías
from clases.fuentes import Fuentes
from PySide6 import QtGui
from PySide6 import QtCore
from PySide6.QtWidgets import QLabel, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QTableWidget

class NominaProyectos:
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

        # definimos el layout vertical
        cTitulo = QVBoxLayout()
        cTitulo.setAlignment(QtCore.Qt.AlignTop)
        lProyectos = QLabel("Proyectos del Cliente")
        lProyectos.setAlignment(QtCore.Qt.AlignTop)
        lProyectos.setFont(fuente.normal)
        cTitulo.addWidget(lProyectos)

        # agregamos la primer fila 
        fila1 = QHBoxLayout()

        # agregamos el texto 
        lFiltro = QLabel("Proyecto:")
        lFiltro.setFont(fuente.normal)
        fila1.addWidget(lFiltro)
        tFiltro = QLineEdit()
        tFiltro.setFont(fuente.normal)
        tFiltro.setToolTip("Ingrese parte del nombre del proyecto")
        tFiltro.setMinimumHeight(30)
        tFiltro.setMaximumWidth(200)
        fila1.addWidget(tFiltro)

        # agregamos el botón nuevo
        btnNuevo = QPushButton()
        btnNuevo.setFixedHeight(30)
        btnNuevo.setFixedWidth(30)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("recursos/nuevo.png"))
        btnNuevo.setIcon(icon1)
        btnNuevo.setToolTip("Agrega un nuevo proyecto")
        fila1.addWidget(btnNuevo)

        # agregamos un espaciador
        fila1.addStretch()

        # agregamos al layout
        cTitulo.addLayout(fila1)

        # la tabla de clientes
        tProyectos = QTableWidget()
        tProyectos.setColumnCount(5)
        tProyectos.setRowCount(0)
        tProyectos.setFont(fuente.normal)

        # fija los títulos de las columnas
        tProyectos.setHorizontalHeaderLabels(('Id',
                                              'Cliente',
                                              'Título',
                                              'Fecha',
                                              'Ver'))

        # fijamos la alineación de las columnas
        tProyectos.horizontalHeaderItem(0).setTextAlignment(QtCore.Qt.AlignCenter)
        tProyectos.horizontalHeaderItem(1).setTextAlignment(QtCore.Qt.AlignLeft)
        tProyectos.horizontalHeaderItem(2).setTextAlignment(QtCore.Qt.AlignLeft)
        tProyectos.horizontalHeaderItem(3).setTextAlignment(QtCore.Qt.AlignCenter)
        tProyectos.horizontalHeaderItem(4).setTextAlignment(QtCore.Qt.AlignCenter)

        # fijmos el tamaño de las columnas
        tProyectos.setColumnWidth(0, 25)
        tProyectos.setColumnWidth(3, 75)
        tProyectos.setColumnWidth(4, 25)

        # permitimos reordenar
        tProyectos.setSortingEnabled(True)

        # agregamos el widget
        cTitulo.addWidget(tProyectos)

        # agregamos al contenedor principal
        contenedor.addLayout(cTitulo)

