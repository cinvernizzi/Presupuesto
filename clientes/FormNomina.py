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
from clientes.EventosNomina import EventosNomina
from PySide6 import QtGui
from PySide6 import QtCore
from PySide6.QtWidgets import QLabel, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QTableWidget


class NominaClientes:
    """
    
        :Author: Claudio Invernizzi <cinvernizzi@dsgestion.site>

        Definición de la clase 

    """

    def __init__(self, contenedor, padre):
        """
        
        :author: Claudio Invernizzi <cinvernizzi@dsgestion.site>
        :param self: la propia clase
        :param contenedor: contenedor del formulario 

        Constructor de la clase, recibe como parámetro el 
        layout contenedor 

        """

        # instanciamos la fuente
        fuente = Fuentes()

        # fijamos el padre
        self.Padre = padre

        # agregamos el título
        layoutTitulo = QVBoxLayout()
        lLista = QLabel("Clientes Registrados")        
        lLista.setFont(fuente.normal)
        lLista.setAlignment(QtCore.Qt.AlignTop)
        layoutTitulo.addWidget(lLista)

        # ahora definimos un layout horizontal
        layoutFiltro = QHBoxLayout()

        # agregamos el filtro 
        self.tFiltro = QLineEdit()
        self.tFiltro.setFixedWidth(150)
        self.tFiltro.setFixedHeight(30)
        self.tFiltro.setFont(fuente.normal)
        layoutFiltro.addWidget(self.tFiltro)

        # agregamos el botón nuevo cliente
        self.btnNuevo = QPushButton()
        self.btnNuevo.setFixedHeight(30)
        self.btnNuevo.setFixedWidth(30)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("recursos/nuevo.png"))
        self.btnNuevo.setIcon(icon1)
        self.btnNuevo.setToolTip("Agrega un nuevo cliente")
        layoutFiltro.addWidget(self.btnNuevo)

        # agregamos el botón configurar
        self.btnConfigurar = QPushButton()
        self.btnConfigurar.setFixedWidth(30)
        self.btnConfigurar.setFixedHeight(30)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("recursos/apoyo.png"))
        self.btnConfigurar.setIcon(icon2)
        self.btnConfigurar.setToolTip("Configura la aplicación")
        self.btnConfigurar.setEnabled(True)
        layoutFiltro.addWidget(self.btnConfigurar)

        # la tabla de clientes
        self.tClientes = QTableWidget()
        self.tClientes.setColumnCount(2)
        self.tClientes.setFixedWidth(220)
        self.tClientes.setRowCount(0)
        self.tClientes.setFont(fuente.normal)

        # fija los títulos de las columnas
        self.tClientes.setHorizontalHeaderLabels(('Id',
                                                  'Nombre'))

        # fijamos la alineación de las columnas
        self.tClientes.horizontalHeaderItem(0).setTextAlignment(QtCore.Qt.AlignCenter)
        self.tClientes.horizontalHeaderItem(1).setTextAlignment(QtCore.Qt.AlignLeft)

        # fijmos el tamaño de las columnas
        self.tClientes.setColumnWidth(0, 0)
        self.tClientes.setColumnWidth(1, 210)

        # fijamos la fuente
        self.tClientes.setFont(fuente.chica)

        self.tClientes.verticalHeader().hide()

        # permitimos reordenar
        self.tClientes.setSortingEnabled(True)

        # instanciamos la clase de eventos
        self.Eventos = EventosNomina(self.tClientes)

        # cargamos todos los clientes por defecto
        self.Eventos.filtraClientes()

        # agregamos los elementos al contenedor
        layoutTitulo.addLayout(layoutFiltro)
        layoutTitulo.addWidget(self.tClientes)
        contenedor.addLayout(layoutTitulo)

    def filtraCliente(self):
        """
        
        :author: Claudio Invernizzi <cinvernizzi@dsgestion.site>
        
        Método llamado al cambiar el texto del filtro, obtiene el 
        texto ingresado y se lo pasa al filtro

        """

        # filtramos 
        self.Eventos.filtraClientes(self.tFiltro.text())
