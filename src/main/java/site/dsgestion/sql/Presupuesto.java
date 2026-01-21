/**
 * 
 * @author Claudio Invernizzi <cinvernizzi@dsgestion.site>
 * @date 14/10/2025
 * @name Presupuesto
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

// definición de la clase
public class Presupuesto {

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
    public Presupuesto(){

        // instanciamos la conexión 
        dbLite Enlace = new dbLite();
        this.Cursor = Enlace.getEnlace();

        // verificamos si existe
        String Consulta = "SELECT COUNT(*) AS registros " + 
                          "FROM sqlite_master WHERE type = 'table' AND " +
                          "     name = 'presupuesto'; ";

        // capturamos el error
        try {

            // ejecutamos la consulta
            PreparedStatement Estado = this.Cursor.prepareStatement(Consulta);
            ResultSet Resultado = Estado.executeQuery();

            // según el resultado
            if (Resultado.getInt("registros") == 0){

                // creamos la tabla
                this.creaPresupuesto();

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
     * Método que crea la tabla de presupuestos
     * 
     */
    protected void creaPresupuesto(){

        // definimos la consulta
        String Consulta = "CREATE TABLE presupuesto ( " +
                          "       id INTEGER NOT NULL, " +
                          "       fecha TEXT NOT NULL, " + 
                          "       validez INTEGER NOT NULL, " + 
                          "       proyecto INTEGER NOT NULL, " +
                          "FOREIGN KEY(proyecto) REFERENCES proyectos(id), " +
                          "PRIMARY KEY ('id' AUTOINCREMENT)); ";

        // capturamos el error
        try {

            // asignamos y ejecutamos
            PreparedStatement creaPresupuesto = this.Cursor.prepareStatement(Consulta);
            creaPresupuesto.execute();

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
     * Método que crea los índices de la tabla de presupuesto
     * 
     */
    protected void creaIndices(){

        // definimos la consulta
        String Consulta = "CREATE INDEX proyecto_presupuesto ON presupuesto('proyecto'); ";

        // capturamos el error
        try {

            // asignamos y ejecutamos
            PreparedStatement Indice = this.Cursor.prepareStatement(Consulta);
            Indice.execute();

        // si hubo un error
        } catch (SQLException e){

            // lo presenta
            e.printStackTrace();

        }

    }

}
