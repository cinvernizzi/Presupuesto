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
from secciones.FormSecciones import FormSecciones
from clientes.FormClientes import FormClientes
from proyectos.FormProyectos import FormProyectos
from personal.FormPersonal import FormPersonal

# verificamos que exista el directorio temporal
if not os.path.exists("temp"):
    os.makedirs("temp")

# verificamos que existan las bases de datos
Verifica()

# definimos el encabezado
with ui.header(fixed=True):
     ui.image("recursos/logo.png").classes('w-16')
     ui.label("Sistema de Presupuesto").style('text-align: center; font-size: 36px; font-weight: bold;')

# definimos los tabuladores
with ui.tabs() as tabs:
    ui.tab('proyectos', label='Proyectos', icon='home').tooltip("Nómina de Proyectos Registrados")
    ui.tab('clientes', label='Clientes', icon='account_box').tooltip("Nómina de Clientes Registrados")
    ui.tab('personal', label='Personal', icon='transcribe').tooltip("Datos que figurarán en el presupuesto")
    ui.tab('administracion', label='Administración', icon='settings').tooltip("Administración del Sistema")

# definimos los paneles 
with ui.tab_panels(tabs, value='proyectos').classes('w-full'):

    # el panel de proyectos
    with ui.tab_panel('proyectos'):

        # cargamos la grilla de proyectos
        FormProyectos()

    # el panel de clientes
    with ui.tab_panel('clientes'):

        # cargamos la grilla de clientes
        FormClientes()

    # el panel de datos personales
    with ui.tab_panel('personal'):

        # cargamos el formulario de datos personales
        FormPersonal()

    # el panel de administración
    with ui.tab_panel('administracion') as formadministracion:

        # instanciamos la clase
        FormSecciones()


# lanzamos la aplicación 
ui.run(host='0.0.0.0',
       port=8080,
       title='Presupuesto',
       reload=True,
       native=False,
       show=True,
       favicon='recursos/logo.png',
       language='es')
