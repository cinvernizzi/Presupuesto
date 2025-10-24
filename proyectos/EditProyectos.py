#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
    Nombre: EditProyectos.py
    Autor: Lic. Claudio Invernizzi
    Fecha: 22/10/2025
    E-Mail: cinvernizzi@dsgestion.site
    Proyecto: Presupuesto
    Comentarios: Clase que define el formulario para el abm 
                 de los proyectos

"""

# importamos las librerías
from nicegui import ui
from proyectos.Proyectos import Proyectos
from clientes.Clientes import Clientes
import datetime

class EditProyectos:
    """
    
        @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

        Definición de la clase

    """

    def __init__(self, padre):
        """
        
            @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

            @param el formulario con la grilla de proyectos

            Constructor de la clase, abre el diálogo

        """

        # instanciamos las clases 
        self.Proyecto = Proyectos()
        self.Cliente = Clientes()

        # asignamos el padre
        self.Padre = padre

        # obtenemos la nómina de clientes
        listado = self.listaClientes()

        # definimos el diálogo
        with ui.dialog() as self.dialog:
            with ui.card().style('width: 1300px; height: 390px;'):

                # la primer fila 
                with ui.row():
                    self.Id = ui.input(label='Id:').tooltip("Clave del registro").classes('w-5')
                    self.NombreCliente = ui.select(listado).tooltip("Seleccione el cliente de la lista").classes('w-64')

                # la segunda fila
                with ui.row():
                    self.Titulo = ui.input(label='Titulo:').tooltip("Título del proyecto").classes('w-128')

                # la descripción del proyecto
                with ui.row():
                    self.Descripcion = ui.textarea(label='Descripción').tooltip("Ingrese la descripción detallada").classes('w-128 h.40')

                # la fila de los botones
                with ui.row():
                    self.Fecha = ui.input("Fecha: ").tooltip("Fecha de alta del proyecto").classes('w-21')
                    ui.button("Grabar", icon='save', on_click=self.verificaProyecto).tooltip("Pulse para grabar el registro").classes('w-40')
                    ui.button("Cancelar", icon='cancel', on_click=self.dialog.close).tooltip("Reinicia el formulario").classes('w-40')

        # asignamos la fecha actual por defecto
        ahora = datetime.datetime.now()
        self.Fecha.value = ahora.strftime("%d/%m/%Y")

        # presentamos el diálogo
        self.dialog.open()

    def verificaProyecto(self):
        """

            @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

            Método llamado al pulsar el botón grabar que verifica 
            el formulario antes de enviarlo al servidor 

        """

        # si está insertando 
        if self.Id.value == "":
            self.Proyecto.Id = 0
        else:
            self.Proyecto.Id = int(self.Id.value)

        # si no seleccionó el cliente
        if self.NombreCliente.value == 0:
            ui.notify("Seleccione el cliente del proyecto", position="top-right", type="negative")
            return
        else:
            self.Proyecto.Cliente = self.NombreCliente.value

        # si no ingresó el título
        if self.Titulo.value == "":
            ui.notify("Ingrese el título del proyecto", position="top-right", type="negative")
            return
        else:
            self.Proyecto.Titulo = self.Titulo.value

        # si no ingresó la descripción 
        if self.Descripcion.value == "":
            ui.notify("Ingrese la descripción del proyecto", position="top-right", type="negative")
            return
        else:
            self.Proyecto.Descripcion = self.Descripcion.value

        # si llegó hasta aquí grabamos
        id = self.Proyecto.grabaProyecto()

        # según el valor
        if id != 0:

            # presenta la notificación 
            ui.notify("Registro grabado", position="top-right", type="info")

            # recargamos la grilla
            self.Padre.tablaproyectos.rows=[]
            self.Padre.nominaProyectos()

            # cerramos el diálogo
            self.dialog.close()

        # si ocurrió un error
        else:

            # presenta el mensaje
            ui.notify("Ha ocurrido un error", position="top-right", type="negative")

    def getDatosProyecto(self, idproyecto: int):
        """
        
            @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

            @param idproyecto clave del registro

            Método que recibe como parámetro la clave de un registro y 
            obtiene y presenta los datos del mismo

        """

        # obtenemos el registro
        self.Proyecto.getDatosProyecto(idproyecto)

        # asignamos los valores en el formulario
        self.Id.value = str(self.Proyecto.Id)
        self.NombreCliente.value = int(self.Proyecto.Cliente)
        self.Titulo.value = self.Proyecto.Titulo
        self.Descripcion.value = self.Proyecto.Descripcion
        self.Fecha.value = self.Proyecto.Fecha

    def listaClientes(self):
        """
        
            @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

            Método que obtiene la nómina de clientes y configura 
            la matriz (la cual retorna) con el formato apropiado
            para el select

        """

        # obtenemos el listado
        nomina = self.Cliente.nominaClientes()

        # definimos la variable de retorno
        listado = {}

        # si hay registros 
        if nomina:

            # recorremos el vector
            for registro in nomina:

                listado.update({registro["id"]:registro["nombre"]})

        # retornamos
        return listado
    