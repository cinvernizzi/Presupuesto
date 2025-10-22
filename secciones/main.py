#!/usr/bin/env python3
from nicegui import ui
import sqlite3

Lite = sqlite3.connect("presupuesto.db", isolation_level=None)
Lite.row_factory = sqlite3.Row
Cursor = Lite.cursor()

def cargaSecciones():
    """
    
        @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

        Método llamado desde el constructor que carga la grilla
        de secciones de un presupuesto

    """

    # componemos la consulta
    Consulta = ("SELECT secciones.id AS id, "
                "       secciones.orden AS orden, "
                "       secciones.etapa AS etapa, "
                "       secciones.fecha AS fecha "
                "FROM secciones "
                "ORDER BY secciones.orden; ")

    # ejecutamos y obtenemos los registros
    Cursor.execute(Consulta)
    Nomina = Cursor.fetchall()

    # recorremos el vector 
    for registro in Nomina:

        aggrid.options['rowData'].append({'id': registro["id"], 
                                          'orden': registro["orden"], 
                                          'etapa': registro["etapa"],
                                          'fecha': registro["fecha"]})

aggrid = ui.aggrid({
    'columnDefs': [
        {'field': 'id', 'editable': False, 'sortable': True},
        {'field': 'orden', 'editable': False},
        {'field': 'etapa'},
        {'field': 'fecha'}
    ],
    'rowData': [],
}).on('cellClicked', lambda event: ui.notify(f'Cell value: {event.args["value"]}'))

cargaSecciones()


ui.run()