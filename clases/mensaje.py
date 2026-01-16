# -*- coding: utf-8 -*-
# /usr/bin/python3

"""
    Nombre: mensaje.py
    Autor: Lic. Claudio Invernizzi
    Fecha: 30/06/2020
    E-Mail: cinvernizzi@dsgestion.site
    Licencia: GPL
    Proyecto: Diagnóstico
    Comentarios: Clase que presenta un mensaje emergente y luego se 
                 cierra automáticamente

"""

# importamos las librerías
from PySide6 import QtCore, QtWidgets
from PySide6.QtCore import QTimer
from clases.fuentes import Fuentes


class Mensaje(QtWidgets.QDialog):
    """

        @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

        Definición de la clase

    """
    
    def __init__(self, parent, mensaje: str):
        """
        
           @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

           @param parent el formulario padre
           @param mensaje cadena con el mensaje a presentar

           Constructor de la clase, recibe como parámetros el
           formulario padre y el mensaje a presentar

        """

        # llama al constructor del padre
        super(Mensaje, self).__init__(parent)
        
        # configuramos la interfaz
        self.setupUi(mensaje)
    
    def setupUi(self, mensaje: str):
        """

            @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

            @param mensaje cadena con el mensaje a presentar

            Método que recibe como parámetro la cadena de texto
            con el mensaje a presentar y configura el aspecto
            y posición del diálogo

        """

        # establecemos la fuente        
        fuente = Fuentes()
        
        # fijamos las propiedades
        self.setGeometry(1000, 50, 260, 50)        
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.FramelessWindowHint)
        layout = QtWidgets.QVBoxLayout()
        lMensaje = QtWidgets.QLabel(mensaje, self)
        lMensaje.setFont(fuente.normal)
        lMensaje.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(lMensaje)
        self.setLayout(layout)

        # mostramos 
        self.show()

        # cerramos luego de cinco seguntos
        QTimer.singleShot(3000, self.close)        
