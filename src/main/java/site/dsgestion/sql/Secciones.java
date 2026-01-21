/**
 * 
 * @author Claudio Invernizzi <cinvernizzi@dsgestion.site>
 * @date 14/10/2025
 * @name Secciones
 * @Projecto: Presupuesto
 * @Copyright DsGestion <dsgestion.site>
 * @Licence: GPL
 * Clase que verifica la existencia de la tabla de secciones
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
public class Secciones {

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
    public Secciones(){

        // instanciamos la conexión 
        dbLite Enlace = new dbLite();
        this.Cursor = Enlace.getEnlace();

        // verificamos si existe
        String Consulta = "SELECT COUNT(*) AS registros " + 
                          "FROM sqlite_master WHERE type = 'table' AND " +
                          "     name = 'secciones'; ";

        // capturamos el error
        try {

            // ejecutamos la consulta
            PreparedStatement Estado = this.Cursor.prepareStatement(Consulta);
            ResultSet Resultado = Estado.executeQuery();

            // según el resultado
            if (Resultado.getInt("registros") == 0){

                // creamos la tabla
                this.creaSecciones();

            }

        // si ocurrió un error
        } catch (SQLException e){

            // lo presenta 
            e.printStackTrace();

        }

    }

    /**
     * 
     * @author Claudio Invernizzi <cinvernizzi@gsgestion.site>
     * 
     * Método que crea la tabla de secciones
     * 
     */
    protected void creaSecciones(){

        // definimos la consulta
        String Consulta = "CREATE TABLE secciones ( " +
                          "       id INTEGER NOT NULL, " +
                          "       orden INTEGER NOT NULL, "  +
                          "       etapa TEXT NOT NULL, " +
                          "       fecha TEXT NOT NULL, " +
                          "PRIMARY KEY ('id' AUTOINCREMENT)); ";
        
        // capturamos el error
        try {

            // ejecutamos la consulta
            PreparedStatement Creacion = this.Cursor.prepareStatement(Consulta);
            Creacion.execute();

            // ahora creamos los índices
            this.creaIndices();

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
     * Método que crea los índices de la tabla de secciones
     * 
     */
    protected void creaIndices(){

        // componemos la consulta
        String Consulta = "CREATE INDEX 'orden_seccion' ON secciones('orden')";

        // capturamos el error
        try {

            // preparamos y ejecutamos
            PreparedStatement Indices = this.Cursor.prepareStatement(Consulta);
            Indices.execute();

            // insertamos las secciones por defecto
            this.insertaSecciones();

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
     * Método que inserta las secciones por defecto 
     * 
     */
    protected void insertaSecciones(){

        // componemos la consulta
        String Consulta = "INSERT INTO secciones " + 
                          "       (orden, " + 
                          "        etapa, " + 
                          "        fecha) " +
                          "       VALUES " +
                          "       (?, ?, date('now'); ";

        // instanciamos los valores como de clase
        Registro[] Vector = new Registro[6];
        Vector[0] = new Registro(1, "Análisis y Diseño");
        Vector[1] = new Registro(2, "Desarrollo Backend");
        Vector[2] = new Registro(3, "Desarrollo Frontend");
        Vector[3] = new Registro(4, "Testing");
        Vector[4] = new Registro(5, "Deploy y Configuración");
        Vector[5] = new Registro(6, "Hosting y Licencias");

        // capturamos el error
        try {

            // preparamos
            PreparedStatement Insertar = this.Cursor.prepareStatement(Consulta);

            for (Registro Elemento : Vector){

                // asignamos en la consulta
                Insertar.setInt(1, Elemento.Orden);
                Insertar.setString(2, Elemento.Etapa);

                // ejecutamos
                Insertar.execute();
                
            }

        // si hubo un error
        } catch (SQLException e){

            // lo presenta
            e.printStackTrace();

        }

    }

    /**
     * 
     * @author Claudio Invernizzi <cinvernizzi@dsgestion.site>
     * 
     * Clase interna que define la estructura de datos de 
     * cada registro
     * 
     */
    protected class Registro {

        // definimos las variables
        protected int Orden;
        protected String Etapa;

        // constructor de la clase
        public Registro(int orden, String etapa){

            // asignamos en la clase
            this.Orden = orden;
            this.Etapa = etapa;

        }

    }

}
