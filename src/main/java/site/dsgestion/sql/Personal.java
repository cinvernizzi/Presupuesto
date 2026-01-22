/**
 * 
 * @author Claudio Invernizzi <cinvernizzi@dsgestion.site>
 * @date 14/10/2025
 * @name Personal
 * @Projecto: Presupuesto
 * @Copyright DsGestion <dsgestion.site>
 * @Licence: GPL
 * Clase que verifica la existencia de la tabla de datos propios
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
public final class Personal {

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
    public Personal(){

        // instanciamos la conexión 
        dbLite Enlace = new dbLite();
        this.Cursor = Enlace.getEnlace();

        // verificamos si existe
        String Consulta = "SELECT COUNT(*) AS registros " + 
                          "FROM sqlite_master WHERE type = 'table' AND " +
                          "     name = 'personal'; ";

        // capturamos el error
        try {

            // ejecutamos la consulta
            PreparedStatement Estado = this.Cursor.prepareStatement(Consulta);
            ResultSet Resultado = Estado.executeQuery();

            // según el resultado
            if (Resultado.getInt("registros") == 0){

                // creamos la tabla
                this.creaPersonal();

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
     * Método que crea la tabla con los datos personales
     * 
     */
    protected void creaPersonal(){

        // componemos la consulta
        String Consulta = "CREATE TABLE personal ( " + 
                          "       id INTEGER NOT NULL, " +
                          "       nombre TEXT NOT NULL, " +
                          "       empresa TEXT NOT NULL, " + 
                          "       direccion TEXT NOT NULL, " +
                          "       cuil TEXT DEFAULT NULL, " +
                          "       telefono TEXT NOT NULL, " +
                          "       mail TEXT NOT NULL, " +
                          "       fecha TEXT NOT NULL, " +
                          "PRIMARY KEY('id' AUTOINCREMENT)); ";

        // capturamos el error
        try {

            // ejecutamos la consulta
            PreparedStatement creaPersonal = this.Cursor.prepareStatement(Consulta);
            creaPersonal.execute();

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
     * Método que crea los índices de la tabla
     * 
     */
    protected void creaIndices(){

        // componemos la consulta
        String Consulta = "CREATE INDEX 'empresa_personal' ON personal('empresa');";

        // capturamos el error
        try {

            // ejecutamos 
            PreparedStatement Indices = this.Cursor.prepareStatement(Consulta);
            Indices.execute();

        // si hubo un error
        } catch (SQLException e){

            // lo presenta
            e.printStackTrace();

        }
    }

}
