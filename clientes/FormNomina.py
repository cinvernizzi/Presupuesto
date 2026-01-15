#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""

    Nombre: FormNomina.py
    Autor: Lic. Claudio Invernizzi
    Fecha: 15/01/2026
    E-Mail: cinvernizzi@dsgestion.site
    Licencia: GPL
    Proyecto: Presupuesto
    Comentarios: Clase que recibe como parámetro el contenedor de 
                 la grilla de clientes, define sus componentes y 
                 la configura

"""

# importamos las librerías
from clases.fuentes import Fuentes
from PySide6 import QtGui
from PySide6 import QtCore
from PySide6.QtWidgets import QLabel, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QTableWidget


class NominaClientes:
    """
    
        :Author: Claudio Invernizzi <cinvernizzi@dsgestion.site>

        Definición de la clase 

    """

    def __init__(self, contenedor):
        """
        
        :author: Claudio Invernizzi <cinvernizzi@dsgestion.site>
        :param self: la propia clase
        :param contenedor: contenedor del formulario 

        Constructor de la clase, recibe como parámetro el 
        layout contenedor 

        """

        # instanciamos la fuente
        fuente = Fuentes()

        # agregamos el título
        layoutTitulo = QVBoxLayout()
        lLista = QLabel("Clientes Registrados")        
        lLista.setFont(fuente.normal)
        lLista.setAlignment(QtCore.Qt.AlignTop)
        layoutTitulo.addWidget(lLista)

        # ahora definimos un layout horizontal
        layoutFiltro = QHBoxLayout()

        # agregamos el filtro 
        tFiltro = QLineEdit()
        tFiltro.setFixedWidth(150)
        tFiltro.setFixedHeight(30)
        tFiltro.setFont(fuente.normal)
        layoutFiltro.addWidget(tFiltro)

        # agregamos el botón nuevo cliente
        btnNuevo = QPushButton()
        btnNuevo.setFixedHeight(30)
        btnNuevo.setFixedWidth(30)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("recursos/nuevo.png"))
        btnNuevo.setIcon(icon1)
        btnNuevo.setToolTip("Agrega un nuevo cliente")
        layoutFiltro.addWidget(btnNuevo)

        # agregamos el botón configurar
        btnConfigurar = QPushButton()
        btnConfigurar.setFixedWidth(30)
        btnConfigurar.setFixedHeight(30)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("recursos/apoyo.png"))
        btnConfigurar.setIcon(icon2)
        btnConfigurar.setToolTip("Configura la aplicación")
        layoutFiltro.addWidget(btnConfigurar)

        # la tabla de clientes
        tClientes = QTableWidget()
        tClientes.setColumnCount(2)
        tClientes.setFixedWidth(220)
        tClientes.setRowCount(0)
        tClientes.setFont(fuente.normal)

        # fija los títulos de las columnas
        tClientes.setHorizontalHeaderLabels(('Id',
                                             'Nombre'))

        # fijamos la alineación de las columnas
        tClientes.horizontalHeaderItem(0).setTextAlignment(QtCore.Qt.AlignCenter)
        tClientes.horizontalHeaderItem(1).setTextAlignment(QtCore.Qt.AlignLeft)

        # fijmos el tamaño de las columnas
        tClientes.setColumnWidth(0, 25)

        # permitimos reordenar
        tClientes.setSortingEnabled(True)

        # agregamos los elementos al contenedor
        layoutTitulo.addLayout(layoutFiltro)
        layoutTitulo.addWidget(tClientes)
        contenedor.addLayout(layoutTitulo)

