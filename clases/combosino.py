# -*- coding: utf-8 -*-

"""
    Nombre: combosino.py
    Autor: Lic. Claudio Invernizzi
    Fecha: 02/02/2020
    E-Mail: cinvernizzi@dsgestion.site
    Licencia: GPL
    Proyecto: Diagnóstico
    Comentarios: Clase que recibe como parámetro un objeto
                 (generalmente un combo) y agrega los elementos
                 si / no en el combo

"""


class comboSino():
    """

        @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

        Definición de la clase
    
    """

    def __init__(self, combo):
        """

            @author Claudio Invernizzi <cinvernizzi@dsgestion.site>

            @parameter: objeto el combo a configurar

            Constructor de la clase, recibe como parámetro el objeto
            y agrega los elementos

        """
        # nos aseguramos de limpiar el combo
        combo.clear()
        
        # agregamos los elementos
        combo.addItem("")
        combo.addItem("Si")
        combo.addItem("No")
        combo.addItem("No Sabe")
