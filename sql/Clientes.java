/**
 * 
 * @author Claudio Invernizzi <cinvernizzi@dsgestion.site>
 * @date 14/10/2025
 * @name Clientes
 * @Projecto: Presupuesto
 * @Copyright DsGestion <dsgestion.site>
 * @Licence: GPL
 * Clase que verifica la existencia de la tabla de clientes
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

// definición de la clase
public class Clientes {

    // definimos las variables
    protected final Connection Cursor;

    /*
     * @author Claudio Invernizzi <cinvernizzi@dsgestion.site>
     * Método que verifica la existencia de la tabla de 
     * secciones
     */
    public Clientes(){

        // instanciamos la conexión 
        dbLite Enlace = new dbLite();
        this.Cursor = Enlace.getEnlace();

        // verificamos si existe
        String Consulta = "SELECT COUNT(*) AS registros " + 
                          "FROM sqlite_master WHERE type = 'table' AND " +
                          "     name = 'clientes'; ";

        // capturamos el error
        try {

            // ejecutamos la consulta
            PreparedStatement Estado = this.Cursor.prepareStatement(Consulta);
            ResultSet Resultado = Estado.executeQuery();

            // según el resultado
            if (Resultado.getInt("registros") == 0){

                // creamos la tabla
                this.creaClientes();

            }

        // si ocurrió un error
        } catch (SQLException e){

            // lo presenta 
            e.printStackTrace();

        }

    }

    /**
     * @author Claudio Invernizzi <cinvernizzi@dsgestion.site>
     * Método que crea la tabla de clientes
     */
    protected void creaClientes(){

        // componemos la consulta
        String Consulta = "CREATE TABLE clientes (" +
                          "       id INTEGER NOT NULL, " + 
                          "       nombre TEXT NOT NULL, " +
                          "       direccion TEXT DEFAULT NULL, " +
                          "       identificacion TEXT DEFAULT NULL, " +
                          "       telefono TEXT DEFAULT NULL, " + 
                          "       mail TEXT DEFAULT NULL, " + 
                          "       fecha TEXT NOT NULL, " + 
                          "PRIMARY KEY ('id' AUTOINCREMENT)); ";

        // capturamos el error
        try {

            // componemos la consulta 
            PreparedStatement datosCliente = this.Cursor.prepareStatement(Consulta);
            datosCliente.execute();

            // creamos los índices
            this.creaIndices();

        // si ocurrió un error
        } catch (SQLException e){

            // lo presenta
            e.printStackTrace();

        }

    }

    /**
     * @author Claudio Invernizzi <cinvernizzi@dsgestion.site>
     * Método que crea los índices
     */
    protected void creaIndices(){

        // componemos la consulta
        String Consulta = "CREATE INDEX 'nombre_cliente' ON clientes('nombre');";

        // capturamos el error
        try {

            // ejecutamos la consulta
            PreparedStatement Indices = this.Cursor.prepareStatement(Consulta);
            Indices.execute();
            
        // si ocurrió un error
        } catch (SQLException e){

            // presenta el mensaje
            e.printStackTrace();

        }

    }

}
