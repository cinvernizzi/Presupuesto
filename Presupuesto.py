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
import sys
import os
from PySide6 import QtCore, QtGui, QtWidgets
from sql.Verifica import Verifica
from clases.fuentes import Fuentes

class Inicio(QtWidgets.QMainWindow):
    """
    
        @author Claudio Invernizzi <cinvernizzi@dsgestion.site>
        
        Definición de la clase principal

    """

    def __init__(self):
        """ 
        
            @author Claudio Invernizzi <cinvernizzi@dsgestion.site>
            
            Constructor de la clase

        """

        # llama al constructor del padre
        super(Inicio, self).__init__()

        # verificamos que exista el directorio temporal
        if not os.path.exists("temp"):
            os.makedirs("temp")

        # verificamos que existan las bases de datos
        Verifica()

        # lanzamos la interfaz
        self.setupUi()

    def setupUi(self):
        """
        
            @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

            Método llamado desde el inicio de la aplicación que 
            configura la interfaz principal del sistema

        """

        # instanciamos las fuentes
        fuentes = Fuentes()

        # fijamos el título y la geometría de la ventana
        self.setGeometry(250, 80, 950, 600)
        self.setWindowTitle('Gestión de Presupuestos')
        self.setWindowIcon(QtGui.QIcon('recursos/logo.png'))

        # definimos la barra de herramientas y agregamos las acciones
        toolbar = self.addToolBar("Barra de Herramientas")
        toolbar.addAction(QtGui.QIcon("recursos/logo.png"), "&Nuevo Proyecto", self.nuevoProyecto)
        toolbar.addAction(QtGui.QIcon("recursos/logo.png"), "Nuevo &Cliente", self.nuevoCliente)
        toolbar.addAction(QtGui.QIcon("recursos/logo.png"), "&Etapas de un Presupuesto", self.Etapas)
        toolbar.addAction(QtGui.QIcon("recursos/logo.png"), "S&alir", self.close)
        toolbar.setFont(fuentes.normal)

        # definimos el tabulador 
        self.Tabulador = QtWidgets.QTabWidget(self)
        self.Tabulador.setGeometry(QtCore.QRect(5, 45, 935, 550))
        self.Tabulador.setFont(fuentes.normal)

        # definimos el tabulador de proyectos
        tProyectos = QtWidgets.QWidget()
        self.Tabulador.addTab(tProyectos, QtGui.QIcon('recursos/logo.png'), "Proyectos")

        # el tabulador de clientes
        tClientes = QtWidgets.QWidget()
        self.Tabulador.addTab(tClientes, QtGui.QIcon('recursos/logo.png'), "Clientes")

        # mostramos el formulario
        self.show()

    def nuevoProyecto(self):
        pass

    def nuevoCliente(self):
        pass

    def Etapas(self):
        pass

# lanzamos la aplicación
app = QtWidgets.QApplication([])
application = Inicio()
sys.exit(app.exec())
