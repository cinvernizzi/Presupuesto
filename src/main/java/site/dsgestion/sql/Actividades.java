/**
 * 
 * @author Claudio Invernizzi <cinvernizzi@dsgestion.site>
 * @date 14/10/2025
 * @name Actividades
 * @Projecto: Presupuesto
 * @Copyright DsGestion <dsgestion.site>
 * @Licence: GPL
 * Clase que verifica la existencia de la tabla de datos de las 
 * actividades ligadas a los proyectos
 * 
 */

// definición del paquete
package site.dsgestion.sql;

// importamos las librerías
import site.dsgestion.dbApi.dbLite;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

public class Actividades {

    // definimos las variables
    protected final Connection Cursor;

    /*
     *
     * @author Claudio Invernizzi <cinvernizzi@dsgestion.site>
     *
     * Método que verifica la existencia de la tabla de 
     * secciones
     *
     */
    public Actividades(){

        // instanciamos la conexión 
        dbLite Enlace = new dbLite();
        this.Cursor = Enlace.getEnlace();

        // verificamos si existe
        String Consulta = "SELECT COUNT(*) AS registros " + 
                          "FROM sqlite_master WHERE type = 'table' AND " +
                          "     name = 'actividades'; ";

        // capturamos el error
        try {

            // ejecutamos la consulta
            PreparedStatement Estado = this.Cursor.prepareStatement(Consulta);
            ResultSet Resultado = Estado.executeQuery();

            // según el resultado
            if (Resultado.getInt("registros") == 0){

                // creamos la tabla
                this.creaActividades();

            }

        // si ocurrió un error
        } catch (SQLException e){

            // lo presenta 
            e.printStackTrace();

        }

    }

    /**
     * 
     * @author Claudio Invernizzi <cinvernizzi@dsgestion.site>
     * 
     * Método que genera la tabla de actividades
     * 
     */
    protected void creaActividades(){

        // componemos la consulta
        String Consulta = "CREATE TABLE actividades (" +
                          "       id INTEGER NOT NULL, " +
                          "       proyecto INTEGER NOT NULL, " +
                          "       seccion INTEGER NOT NULL, " +
                          "       descripcion TEXT, " + 
                          "       estimado REAL, " + 
                          "       optimo REAL, " + 
                          "       pesimista REAL, " +
                          "       total REAL, " +
                          "       costo INTEGER NOT NULL, " + 
                          "       consideraciones BLOB DEFAULT NULL, " +
                          "FOREIGN KEY(proyecto) REFERENCES proyectos(id), " +
                          "FOREIGN KEY(seccion) REFERENCES secciones(id), " +
                          "PRIMARY KEY ('id' AUTOINCREMENT)); ";

        // capturamos el error
        try {

            // asignamos y ejecutamos
            PreparedStatement creaActividad = this.Cursor.prepareStatement(Consulta);
            creaActividad.execute();

            // creamos los índices
            this.creaIndices();

        // si ocurrió un error
        } catch (SQLException e){

            // lo presenta
            e.printStackTrace();

        }


    }

    /**
     * 
     * @author Claudio Invernizzi <cinvernizzi@dsgestion.site>
     * 
     * Método que crea los índices de las actividades
     * 
     */
    protected void creaIndices(){

        // capturamos el error
        try {

            // definimos la consulta
            String Consulta = "CREATE INDEX proyecto_actividad ON actividades('proyecto'); ";

            // ejecutamos
            PreparedStatement Indice = this.Cursor.prepareStatement(Consulta);
            Indice.execute();

            // ahora sobre la clave de la sección 
            Consulta = "CREATE INDEX seccion_actividad ON actividades('seccion'); ";

            // ejecutamos
            Indice = this.Cursor.prepareStatement(Consulta);
            Indice.execute();

        // si ocurrió un error
        } catch (SQLException e){

            // lo presenta
            e.printStackTrace();

        }

    }

}
