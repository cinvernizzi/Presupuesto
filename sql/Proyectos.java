/**
 * 
 * @author Claudio Invernizzi <cinvernizzi@dsgestion.site>
 * @date 14/10/2025
 * @name Proyectos
 * @Projecto: Presupuesto
 * @Copyright DsGestion <dsgestion.site>
 * @Licence: GPL
 * Clase que verifica la existencia de la tabla de datos de los 
 * proyectos
 * 
 */

// definición del paquete
package sql;

// importamos las librerías
import dbApi.dbLite;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

public class Proyectos {

    // definimos las variables
    protected final Connection Cursor;

    /*
     * @author Claudio Invernizzi <cinvernizzi@dsgestion.site>
     * Método que verifica la existencia de la tabla de 
     * secciones
     */
    public Proyectos(){

        // instanciamos la conexión 
        dbLite Enlace = new dbLite();
        this.Cursor = Enlace.getEnlace();

        // verificamos si existe
        String Consulta = "SELECT COUNT(*) AS registros " + 
                          "FROM sqlite_master WHERE type = 'table' AND " +
                          "     name = 'proyectos'; ";

        // capturamos el error
        try {

            // ejecutamos la consulta
            PreparedStatement Estado = this.Cursor.prepareStatement(Consulta);
            ResultSet Resultado = Estado.executeQuery();

            // según el resultado
            if (Resultado.getInt("registros") == 0){

                // creamos la tabla
                this.creaProyectos();

            }

        // si ocurrió un error
        } catch (SQLException e){

            // lo presenta 
            e.printStackTrace();

        }

    }

    /**
     * @author Claudio Invernizzi <cinvernizzi@dsgestion.site>
     * Método que crea la tabla de proyectos
     */
    protected void creaProyectos(){

        // componemos la consulta
        String Consulta = "CREATE TABLE proyectos (" +
                          "       id INTEGER NOT NULL, " +
                          "       cliente INTEGER NOT NULL, " +
                          "       titulo TEXT NOT NULL, " +
                          "       descripcion BLOB DEFAULT NULL, " +
                          "       fecha TEXT NOT NULL, " + 
                          "FOREIGN KEY(cliente) REFERENCES clientes(id), " +
                          "PRIMARY KEY ('id' AUTOINCREMENT)); ";

        // capturamos el error
        try {

            // asignamos y ejecutamos
            PreparedStatement creaProyectos = this.Cursor.prepareStatement(Consulta);
            creaProyectos.execute();

            // creamos los índices
            this.creaIndices();

        // si ocurrió un error
        } catch (SQLException e){

            // presenta el mensaje
            e.printStackTrace();

        }

    }

    /**
     * @author Claudio Invernizzi <cinvernizzi@dsgestion.site>
     * Método que crea los índices de la tabla
     */
    protected void creaIndices(){

        // definimos la consulta
        String Consulta = "CREATE INDEX cliente_proyecto ON proyectos('cliente');";

        // capturamos el error
        try {

            // asignamos y ejecutamos
            PreparedStatement Indice = this.Cursor.prepareStatement(Consulta);
            Indice.execute();

        // si ocurrió un error
        } catch (SQLException e){

            // presenta el mensaje
            e.printStackTrace();

        }

    }

}
