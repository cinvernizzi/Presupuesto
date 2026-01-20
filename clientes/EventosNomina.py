#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""

    Nombre: EventosNomina.py
    Autor: Lic. Claudio Invernizzi
    Fecha: 19/01/2026
    E-Mail: cinvernizzi@dsgestion.site
    Licencia: GPL
    Proyecto: Presupuesto
    Comentarios: Clase que recibe en el constructor el objeto
                 de la grilla y provee los métodos para filtrar
                 mostrar los clientes declarados
"""

# importamos las librerías
from clases.fuentes import Fuentes
from clientes.Clientes import Clientes
from PySide6.QtWidgets import QTableWidgetItem


class EventosNomina:
    """

    :author: Claudio Invernizzi <cinvernizzi@dsgestion.site>

    Declaración de la clase

    """

    def __init__(self, grillaclientes):
        """

        :author: Claudio Invernizzi <cinvernizzi@dsgestion.site>

        :param grillaclientes: la grilla con los clientes

        Constructor de la clase, recibe como parámetro la grilla
        con la nómina de clientes

        """

        # asignamos en la clase
        self.grillaClientes = grillaclientes
        self.Clientes = Clientes()

    def filtraClientes(self, texto = ""):
        """

        :author: Claudio Invernizzi <cinvernizzi@dsgestion.site>

        :param texto: el texto a buscar

        Método que recibe como parámetro el texto a filtrar (o nulo)
        y obtiene el vector con todos los clientes coincidentes
        y lo carga en la grilla

        """

        # obtenemos la nómina
        nomina = self.Clientes.buscaCliente(texto)

        # limpiamos la grilla
        self.grillaClientes.setRowCount(0)

        # recorremos el vector
        for registro in nomina:

            # insertamos una fila
            fila = self.grillaClientes.rowCount()
            self.grillaClientes.insertRow(fila)

            # fijamos los valores convirtiendo las cadenas
            self.grillaClientes.setItem(fila, 0, QTableWidgetItem(str(registro["id"])))
            self.grillaClientes.setItem(fila, 1, QTableWidgetItem(registro["nombre"]))
