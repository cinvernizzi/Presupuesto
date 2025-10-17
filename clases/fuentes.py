# -*- coding: utf-8 -*-

"""
    Nombre: ingreso.py
    Autor: Lic. Claudio Invernizzi
    Fecha: 15/03/2020
    E-Mail: cinvernizzi@gmail.com
    Licencia: GPL
    Proyecto: Diagnóstico
    Comentarios: Procedimiento que define las fuentes del sistema

"""

# importamos las librerías
from PyQt6 import QtGui


class Fuentes():
    """
    
        @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

        Definición de la clase

    """

    def __init__(self):
        """ 
        
            @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

            Constructor de la clase define la fuente a utilizar

        """

        # definimos la fuente de los labels
        self.negrita = QtGui.QFont()
        self.negrita.setFamily("Arial")
        self.negrita.setPointSize(9)
        self.negrita.setBold(True)
        self.negrita.setWeight(75)

        # la fuente normal
        self.normal = QtGui.QFont()
        self.normal.setFamily("Arial")
        self.normal.setPointSize(9)
        self.normal.setBold(False)
        self.normal.setWeight(50)
