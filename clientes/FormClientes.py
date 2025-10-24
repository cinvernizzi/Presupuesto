#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
    Nombre: FormClientes.py
    Autor: Lic. Claudio Invernizzi
    Fecha: 21/10/2025
    E-Mail: cinvernizzi@dsgestion.site
    Proyecto: Presupuesto
    Comentarios: Clase que define la grilla de los clientes
                 registrados

"""

# importamos las librerías
from nicegui import ui
from clientes.EditClientes import EditClientes
from clientes.Clientes import Clientes

class FormClientes:
    """
    
        @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

        Definición de la clase

    """

    def __init__(self):
        """
        
            @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

            Constructor de la clase, carga en el tabulador la 
            definición de la grilla

        """

        # abrimos la columna 
        with ui.row():

            # los títulos de las columnas
            columnas = [{'name': 'id', 'label': 'Id', 'field': 'id','align':'center'},
                        {'name': 'nombre', 'label': 'Nombre', 'field': 'nombre','align':'left'},
                        {'name': 'identificacion', 'label': 'Id.Tributaria', 'field': 'identificacion','align':'center'},
                        {'name': 'telefono', 'label': 'Teléfono', 'field': 'telefono','align':'right'},
                        {'name': 'mail', 'label': 'E-Mail', 'field': 'mail','align':'left'},
                        {'name': 'fecha', 'label': 'Fecha', 'field': 'fecha','align':'center'}]

            # agregamos la tabla de clientes
            self.tablaclientes = ui.table(columns=columnas, 
                                          rows=[], 
                                          title='Clientes Registrados',
                                          row_key='id',
                                          selection='single',
                                          on_select=lambda e: self.cargaCliente(e.selection),
                                          pagination={'rowsPerPage': 5}).props('virtual-scroll').classes('w-260')

            # presentamos el menú 
            with ui.column():
                ui.input('Buscar...').bind_value(self.tablaclientes, 'filter').props('clearable').classes('w-40')
                ui.button("Nuevo", icon='add', on_click=self.nuevoCliente).tooltip("Pulse para insertar un cliente").classes('w-40')
                ui.button("Ayuda", icon='help', on_click=self.ayudaCliente).tooltip("Muestra la ayuda del sistema").classes('w-40')

        # cargamos la nómina de clientes
        self.nominaClientes()

    def nominaClientes(self):
        """
        
            @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

            Método llamado desde el constructor que carga en la grilla 
            la nómina de clientes

        """
        # instanciamos la clase y obtenemos la nómina
        clientes = Clientes()
        nomina = clientes.nominaClientes()

        # si no hay registros
        if not nomina:
            return
        else:

            # recorremos el vector
            for registro in nomina:

                # agregamos a la tabla 
                self.tablaclientes.add_row({'id': registro["id"], 
                                            'nombre': registro["nombre"],
                                            'identificacion': registro["identificacion"],
                                            'telefono': registro["telefono"],
                                            'mail': registro["mail"],
                                            'fecha' : registro["fecha"]})
        
    def nuevoCliente(self):
        """
        
            @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

            Método que abre el diálogo con el formulario de carga
            de nuevo cliente

        """

        # abrimos el diálogo
        EditClientes(self)
        
    def cargaCliente(self, e):
        """
        
            @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

            @param e el vector con los datos de la fila 

            Método llamado al seleccionar una fila de la grilla 
            que recibe como parámetro el vector con los datos 
            de la misma

        """

        # obtenemos la clave del registro
        id = int(e[0]["id"])

        # abrimos el formulario 
        formulario = EditClientes(self)

        # cargamos el registro
        formulario.getDatosCliente(id)

    def ayudaCliente(self):
        """
        
            @authhor Claudio Invernizzi <cinvernizzi@dsgestion.site>

            Método que presenta la ventana de ayuda 

        """