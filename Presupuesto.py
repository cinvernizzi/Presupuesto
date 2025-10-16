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

        # verficamos que existan las bases de datos
        Verifica()

        # lanzamos la interfaz


# lanzamos la aplicación
app = QtWidgets.QApplication([])
application = Inicio()
sys.exit(app.exec())
