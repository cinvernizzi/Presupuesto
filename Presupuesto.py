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
from nicegui import ui
from sql.Verifica import Verifica

# verificamos que exista el directorio temporal
if not os.path.exists("temp"):
    os.makedirs("temp")

# verificamos que existan las bases de datos
Verifica()

ui.run()
