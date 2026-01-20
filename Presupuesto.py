#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
    Nombre: Presupuesto.py
    Autor: Lic. Claudio Invernizzi
    Fecha: 15/10/25
    E-Mail: cinvernizzi@dsgestion.site
    Proyecto: Presupuesto
    Comentarios: Script inicial que verifica la existencia de las 
                 tablas y luego inicia la interfaz

"""

# Importamos las librerías
import os
import sys
from sql.Verifica import Verifica
from clientes.FormNomina import NominaClientes
from clientes.FormClientes import FormClientes
from proyectos.NominaProyectos import NominaProyectos
from personal.FormPersonal import FormPersonal
from clases.fuentes import Fuentes
from PySide6.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLabel
from PySide6 import QtCore
from PySide6.QtGui import QIcon

# verificamos que exista el directorio temporal
if not os.path.exists("temp"):
    os.makedirs("temp")

# verificamos que existan las bases de datos
Verifica()

class Inicio(QWidget):
    """
    
        :author: Claudio Invernizzi <cinvernizzi@dsgestion.site>

        Definición de la clase

    """

    def __init__(self):
        """
        
        :author: Claudio Invernizzi <cinvernizzi@dsgestion.site>

        Constructor de la clase, instanciamos el formulario principal

        """

        # inicializamos 
        super().__init__()

        # implementamos la fuente
        fuente = Fuentes()

        # definimos el tamaño inicial y el logo
        self.setGeometry(100, 200, 1050, 650)
        self.setWindowIcon(QIcon('recursos/logo.png'))

        # aquí vamos a definir un layout contenedor
        contenedor = QVBoxLayout()

        # definimos el título
        layoutTitulo = QVBoxLayout()
        lTitulo = QLabel("Gestión de Presupuestos")
        lTitulo.setMaximumHeight(30)
        lTitulo.setFont(fuente.negrita)
        lTitulo.setAlignment(QtCore.Qt.AlignCenter)
        layoutTitulo.addWidget(lTitulo)

        # agregamos el título
        contenedor.addLayout(layoutTitulo)

        # definimos el segundo layout
        datos = QHBoxLayout()
        self.nominaclientes = NominaClientes(datos, self)
        
        # ahora definimos otro contenedor al cual 
        # agregamos el formulario de clientes y 
        # la nómina de proyectos
        contenedor2 = QVBoxLayout()
        self.FormularioClientes = FormClientes(contenedor2)
        NominaProyectos(contenedor2)

        # agregamos el layout 2
        datos.addLayout(contenedor2)

        # agregamos el layout de datos 
        contenedor.addLayout(datos)

        # definimos el pié 
        lPie = QLabel("Lic. Claudio Invernizzi / cinvernizzi@dsgestion.site")        
        lPie.setMaximumHeight(20)
        lPie.setAlignment(QtCore.Qt.AlignCenter)
        contenedor.addWidget(lPie)

        """
        
            Atención, aparentemente al utilizar layout manager anidados
            PySide6 tiene algún tipo de inconveniente al propagar los 
            eventos y nunca se captura el click del mouse o el evento del 
            teclado, por eso declaramos aquí (no es una solución 
            elegante y no me gusta mucho tampoco)
        """
        self.nominaclientes.btnConfigurar.clicked.connect(self.verConfig)
        self.nominaclientes.btnNuevo.clicked.connect(self.FormularioClientes.nuevoCliente)
        self.nominaclientes.tClientes.cellClicked.connect(self.getClaveCliente)
        self.nominaclientes.tFiltro.textChanged.connect(self.nominaclientes.filtraCliente)
        self.FormularioClientes.btnGrabar.clicked.connect(self.FormularioClientes.grabaCliente)
        self.FormularioClientes.btnCancelar.clicked.connect(self.FormularioClientes.cancelaCliente)

        # fijamos el layout
        self.setLayout(contenedor)  
        self.show() 

    def verConfig(self):
        """
                
        :author: Claudio Invernizzi <cinvernizzi@dsgestion.site>

        Método llamado al pulsar sobre el botón configurar que 
        abre el formulario de datos personales

        """

        # instanciamos el formulario 
        FormPersonal(self)

    def getClaveCliente(self, fila, columna):
        """
        
        :author: Claudio Invernizzi <cinvernizzi@dsgestion.site>
        
        :param fila: entero con la clave de la fila 
        :param columna: entero con la clave de la columna 

        Método llamado al pulsar sobre la grilla de clientes que 
        recibe como parámetro la fila y la columna pulsadas, a 
        partir de allí, obtiene la clave del cliente y carga 
        el registro

        """

        # obtenemos la clave
        clave = self.nominaclientes.tClientes.item(fila, 0).text()

        # llamamos el evento
        self.FormularioClientes.verCliente(clave)

# lanzamos la aplicación
app = QApplication([])
application = Inicio()
sys.exit(app.exec())
