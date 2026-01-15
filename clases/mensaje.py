# -*- coding: utf-8 -*-
# /usr/bin/python3

"""
    Nombre: mensaje.py
    Autor: Lic. Claudio Invernizzi
    Fecha: 30/06/2020
    E-Mail: cinvernizzi@gmail.com
    Licencia: GPL
    Proyecto: Diagnóstico
    Comentarios: Clase que presenta un mensaje emergente y luego se 
                 cierra automáticamente

"""

# importamos las librerías
from PySide6 import QtCore, QtGui, QtWidgets
from threading import Timer


class Mensaje(QtWidgets.QDialog):
    """

        @author Claudio Invernizzi <cinvernizzi@gmail.com>

        Definición de la clase

    """
    
    def __init__(self, parent, mensaje: str):
        """
        
           @author Claudio Invernizzi <cinvernizzi@gmail.com>

           @param parent el formulario padre
           @param mensaje cadena con el mensaje a presentar

           Constructor de la clase, recibe como parámetros el
           formulario padre y el mensaje a presentar

        """

        # llama al constructor del padre
        super(Mensaje, self).__init__(parent)

        # instanciamos el temporizador y lo iniciamos
        t = Timer(5, self.Cerrar)        
        t.start()
        
        # configuramos la interfaz
        self.setupUi(mensaje)
    
    def setupUi(self, mensaje: str):
        """

            @author Claudio Invernizzi <cinvernizzi@gmail.com>

            @param mensaje cadena con el mensaje a presentar

            Método que recibe como parámetro la cadena de texto
            con el mensaje a presentar y configura el aspecto
            y posición del diálogo

        """

        # establecemos la fuente        
        fuente = QtGui.QFont()
        fuente.setFamily("Arial")
        fuente.setPointSize(8)
        fuente.setBold(False)
        fuente.setWeight(50)        
        
        # fijamos las propiedades
        self.setGeometry(1000, 50, 260, 50)        
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.FramelessWindowHint)
        lMensaje = QtWidgets.QLabel(mensaje, self)
        lMensaje.setGeometry(QtCore.QRect(0, 0, 251, 50))
        lMensaje.setFont(fuente)
        lMensaje.setAlignment(QtCore.Qt.AlignCenter)

        # mostramos el formulario
        self.setModal(False)
        self.show()
        
    def Cerrar(self):
        """
            
            @author Claudio Invernizzi <cinvernizzi@gmail.com>
            
            Método llamado por el temporizador que simplemente 
            cierra el diálogo 
 
        """

        # cerramos el diálogo
        self.close()
        