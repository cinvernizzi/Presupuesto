/**
 * 
 * @author Claudio Invernizzi <cinvernizzi@dsgestion.site>
 * @name: verifica
 * @date 14/10/2025
 * @Projecto: Presupuesto
 * @Copyright DsGestion <dsgestion.site>
 * @Licence: GPL
 * Clase que verifica la existencia de las distintas bases de 
 * datos y en todo caso las crea
 * 
 */

// definición del paquete
package sql;

// definición de la clase
public class verifica {

    /**
     * @author Claudio Invernizzi <cinvernizzi@dsgestion.site>
     * Constructor de la clase, abrimos la conexión y verifica
     * que existan las distintas tablas
     * 
     * Tenemos que tener en cuenta el orden porque sqlite si bien 
     * soporta las claves foráneas, solo las podemos definir en 
     * el momento de su creación, así debemos crear primero los 
     * diccionarios 
     */
    public verifica(){

        // verificamos la tabla de clientes que no tiene 
        // referencias externas
        new Clientes();

        // verificamos los datos propios que no tiene 
        // referencias externas
        new Personal();

        // verificamos la tabla de secciones que no tiene 
        // referencias externas
        new Secciones();

        // la tabla de proyectos que tiene como referencia
        // externa los clientes
        new Proyectos();

        // la tabla de presupuestos que tiene como referencia
        // la tabla de proyectos
        new Presupuesto();

        // verificamos la tabla de actividades que tiene como 
        // referencia la tabla de proyectos, la tabla de 
        // secciones 
        new Actividades();
        
        // ahora creamos las vistas
        new Vistas();

    }

}
