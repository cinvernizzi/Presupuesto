/**
 * 
 * @author Claudio Invernizzi <cinvernizzi@dsgestion.site>
 * @date 14/10/2025
 * @name Indices
 * @Projecto: Presupuesto
 * @Copyright DsGestion <dsgestion.site>
 * @Licence: GPL
 * Clase que recrea las vistas de todas las tablas
 * 
 */

// definición del paquete
package site.dsgestion.sql;

// importamos las librerías
import site.dsgestion.dbApi.dbLite;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.SQLException;

// definición de la clase
public class Vistas {

    // definimos las variables
    protected final Connection Cursor;

    /*
     *
     * @author Claudio Invernizzi <cinvernizzi@dsgestion.site>
     *
     * Método que verifica la existencia de la tabla de 
     * secciones de un proyecto
     *
     */
    public Vistas(){

        // instanciamos la conexión 
        dbLite Enlace = new dbLite();
        this.Cursor = Enlace.getEnlace();

        // recreamos la vista de presupuesto
        this.creaPresupuesto();

        // recreamos la vista de actividades
        this.creaActividades();

        // la vista de proyectos
        this.creaProyectos();

    }

    /**
     * 
     * @author Claudio Invernizzi <cinvernizzi@dsgestion.site>
     * 
     * Método que recrea la vista de presupuesto
     * 
     */
    protected final void creaPresupuesto(){

        // componemos la consulta
        String Consulta = "CREATE VIEW IF NOT EXISTS v_presupuesto AS " +
                          "       SELECT presupuesto.id AS id, " +
                          "              presupuesto.fecha AS fecha, " +
                          "              presupuesto.validez AS validez, " +
                          "              presupuesto.proyecto AS idproyecto, " + 
                          "              proyectos.cliente AS idcliente, " + 
                          "              clientes.nombre AS nombre, " + 
                          "              clientes.direccion AS direccion, " + 
                          "              clientes.identificacion AS identificacion, " + 
                          "              clientes.telefono AS telefono, " + 
                          "              clientes.mail AS mail, " + 
                          "              proyectos.titulo AS titulo " +
                          "        FROM presupuesto INNER JOIN proyectos ON presupuesto.proyecto = proyectos.id " + 
                          "                         INNER JOIN clientes ON proyectos.cliente = clientes.id; ";

        // capturamos el error
        try {

            // asignamos y ejecutamos
            PreparedStatement Vista = this.Cursor.prepareStatement(Consulta);
            Vista.execute();

        // si ocurrió un error
        } catch (SQLException e){

            // presenta el mensaje
            e.printStackTrace();

        }

    }

    /**
     * 
     * @author Claudio Invernizzi <cinvernizzi@dsgestion.site>
     * 
     * Método que recrea la vista de actividades
     * 
     */
    protected final void creaActividades(){

        // componemos la consulta
        String Consulta = "CREATE VIEW IF NOT EXISTS v_actividades AS " +
                          "       SELECT actividades.id AS id, " + 
                          "              actividades.proyecto AS idproyecto, " +
                          "              proyectos.titulo AS proyecto, " +
                          "              actividades.seccion AS idseccion, " + 
                          "              secciones.etapa AS seccion, " +
                          "              actividades.descripcion AS descripcion, " + 
                          "              actividades.estimado AS estimado, " +
                          "              actividades.optimo AS optimo, " +
                          "              actividades.pesimista AS pesimista, " + 
                          "              actividades.costo AS costo, " + 
                          "              actividades.consideraciones AS consideraciones " +
                          "        FROM actividades INNER JOIN proyectos ON actividades.proyecto = proyectos.id " +
                          "                         INNER JOIN secciones ON actividades.seccion = secciones.id; ";

        // capturamos el error
        try {

            // asignamos y ejecutamos
            PreparedStatement Vista = this.Cursor.prepareStatement(Consulta);
            Vista.execute();

        // si ocurrió un error
        } catch (SQLException e){

            // presenta el mensaje
            e.printStackTrace();

        }

    }
    
    /**
     * 
     * @author Claudio Invernizzi <cinvernizzi@dsgestion.site>
     * 
     * Método que crea la vista de los proyectos
     * 
     */
    protected final void creaProyectos(){

        // componemos la consulta
        String Consulta = "CREATE VIEW IF NOT EXISTS v_proyectos AS " +
                          "       SELECT proyectos.id AS id, " +
                          "              proyectos.cliente AS idcliente, " +
                          "              clientes.nombre AS cliente, " + 
                          "              clientes.direccion AS direccion, " + 
                          "              clientes.identificacion AS identificacion, " + 
                          "              clientes.telefono AS telefono, " + 
                          "              clientes.mail AS mail, " +
                          "              proyectos.titulo AS titulo, " + 
                          "              proyectos.descripcion AS descripcion, " + 
                          "              proyectos.fecha AS fecha " + 
                          "       FROM proyectos INNER JOIN clientes ON proyectos.cliente = clientes.id; ";
        
        // capturamos el error
        try {

            // asignamos y ejecutamos
            PreparedStatement Vista = this.Cursor.prepareStatement(Consulta);
            Vista.execute();
            
        // si ocurrió un error
        } catch (SQLException e){

            // presenta el mensaje
            e.printStackTrace();

        }

    }

}
