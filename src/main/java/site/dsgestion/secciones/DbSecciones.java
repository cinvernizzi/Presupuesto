/**
 * 
 * @author Claudio Invernizzi <cinvernizzi@dsgestion.site>
 * @date 23/10/2025
 * @name DbSecciones
 * @Projecto: Presupuesto
 * @Copyright DsGestion <dsgestion.site>
 * @Licence: GPL
 * Clase que provee los métodos para interactar con la base
 * de secciones de un proyecto
 * 
 */

// definimos el paquete
package site.dsgestion.secciones;

// importamos las librerías
import site.dsgestion.dbApi.dbLite;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

/**
 * 
 * @author Claudio Invernizzi <cinvernizzi@dsgestion.site>
 * 
 * Definición de la clase
 * 
 */
public class DbSecciones {

    // declaramos las variables
    protected final Connection Cursor; // puntero a la base
    protected final dbLite Enlace;     // clase dbapi
    protected int Id;                  // clave del registro
    protected int Orden;               // orden de impresión
    protected String Etapa;            // denominación de la etapa
    protected String Fecha;            // fecha de alta 

    /**
     * 
     * @author Claudio Invernizzi <cinvernizzi@dsgestion.site>
     * 
     * Constructor de la clase, instanciamos la conexión con la 
     * base e inicializamos las variables
     * 
     */
    public DbSecciones(){

        // instanciamos la conexión 
        this.Enlace = new dbLite();
        this.Cursor = this.Enlace.getEnlace();

        // inicializamos las variables
        this.Id = 0;
        this.Orden = 0;
        this.Etapa = "";
        this.Fecha = "";

    }

    // métodos de asignación de valores
    public void setId(int id){
        this.Id = id;
    }
    public void setOrden(int orden){
        this.Orden = orden;
    }
    public void setEtapa(String etapa){
        this.Etapa = etapa;
    }

    // métodos de retorno de valores
    public int getId(){
        return this.Id;
    }
    public int getOrden(){
        return this.Orden;
    }
    public String getEtapa(){
        return this.Etapa;
    }
    public String getFecha(){
        return this.Fecha;
    }

    /**
     * 
     * @author Claudio Invernizzi <cinvernizzi@dsgestion.site>
     * 
     * @return entero con la clave del registro
     * 
     * Método que según el estado de las variables de clase 
     * genera la consulta de edición o inserción, retorna la 
     * clave del registro afectado o cero en caso de error
     * 
     */
    public int grabaSeccion(){

        // declaramos las variables
        int estado;

        // si está insertando
        if (this.Id == 0){
            estado = this.nuevaSeccion();
        } else {
            estado = this.editaSeccion();
        }

        // retornamos 
        return estado;

    }

    /**
     * 
     * @author Claudio Invernizzi <cinvernizzi@dsgestion.site>
     * 
     * @return entero con la clave del nuevo registro
     * 
     * Método que ejecuta la consulta de inserción y retorna la 
     * clave del nuevo registro
     * 
     */
    protected int nuevaSeccion(){

        // componemos la consulta
        String Consulta = "INSERT INTO secciones " +
                          "       (orden, " + 
                          "        etapa, " +
                          "        fecha) " +
                          "       VALUES " +
                          "       (?, ?, date('now')); ";

        // capturamos el error
        try {

            // ejecutamos la consulta
            PreparedStatement SqlSecciones = this.Cursor.prepareStatement(Consulta);
            SqlSecciones.setInt(1, this.Orden);
            SqlSecciones.setString(2, this.Etapa);
            SqlSecciones.execute();

            // obtenemos la clave y retornamos
            this.Id = this.Enlace.ultimoInsertado();
            return this.Id;
            
        // si ocurrió un error
        } catch (SQLException e){

            // presenta el mensaje
            e.printStackTrace();
            return 0;

        }
                          
    }

    /**
     * 
     * @author Claudio Invernizzi <cinvernizzi@dsgestion.site>
     * 
     * @return entero con la clave del registro afectado
     * 
     * Método que ejecuta la consulta de edición, retorna la 
     * clave del registro afectado o cero en caso de error
     * 
     */
    protected int editaSeccion(){

        // componemos la consulta
        String Consulta = "UPDATE secciones SET " +
                          "       orden = ?, " +
                          "       etapa = ? " +
                          "WHERE secciones.id = ?; ";

        // capturamos el error
        try {

            // ejecutamos la consulta
            PreparedStatement SqlSecciones = this.Cursor.prepareStatement(Consulta);
            SqlSecciones.setInt(1, this.Orden);
            SqlSecciones.setString(2, this.Etapa);
            SqlSecciones.setInt(3, this.Id);
            SqlSecciones.execute();

            // retornamos
            return this.Id;
            
        // si ocurrió un error
        } catch (SQLException e){

            // presenta el mensaje
            e.printStackTrace();
            return 0;

        }
                          
    }

    /**
     * 
     * @author Claudio Invernizzi <cinvernizzi@dsgestion.site>
     * 
     * @param idseccion entero con la clave de la sección 
     * @param etapa cadena con el nombre de la etapa 
     * 
     * @return bool verdadero si puede grabar
     * 
     * Método que recibe como parámetro la clave de una sección 
     * y el nombre de la etapa y verifica que no esté repetida
     * retorna verdadero si puede grabar
     * 
     */
    public boolean validaSeccion(int idseccion, String etapa){

        // componemos la consulta
        String Consulta = "SELECT COUNT(secciones.id) AS registros " +
                          "FROM secciones " +
                          "WHERE secciones.id != ? AND " +
                          "      secciones.etapa = ?; ";

        // capturamos el error
        try {
        
            // asignamos la consulta y los parámetros 
            PreparedStatement SqlSecciones = this.Cursor.prepareStatement(Consulta);
            SqlSecciones.setInt(1, idseccion);
            SqlSecciones.setString(2, etapa);
            ResultSet Resultado = SqlSecciones.executeQuery();
            
            // obtenemos el registro y asignamos
            Resultado.next();

            // según los registros 
            if (Resultado.getInt("registros") == 0){
                return true;
            } else {
                return false;
            }

        // si ocurrió un error
        } catch (SQLException e){
            
            // imrprime y retorna 
            e.printStackTrace();
            return false;
            
        }

    }

    /**
     * 
     * @author Claudio Invernizzi <cinvernizzi@dsgestion.site>
     * 
     * @return vector con la nómina de secciones
     * 
     * Método que retorna el vector con la nómina de secciones
     * utilizado en los select 
     * 
     */
    public ResultSet nominaSecciones(){

        // declaramos las variables
        ResultSet Resultado = null; 

        // componemos la consulta
        String Consulta = "SELECT secciones.id AS id, " +   
                          "       secciones.orden AS orden, " +
                          "       secciones.etapa AS etapa, " +
                          "       secciones.fecha AS fecha " +
                          "FROM secciones " +
                          "ORDER BY secciones.orden; ";

        // capturamos el error
        try {
        
            // asignamos la consulta y los parámetros 
            PreparedStatement SqlSecciones = this.Cursor.prepareStatement(Consulta);
            Resultado = SqlSecciones.executeQuery();
            
        // si ocurrió un error
        } catch (SQLException e){
            
            // imrprime y retorna 
            e.printStackTrace();
            
        }

        // retornamos 
        return Resultado;

    }

    /**
     * 
     * @author Claudio Invernizzi <cinvernizzi@dsgestion.site>
     * 
     * @param idseccion clave del registro
     * 
     * @return bool resultado de la operación 
     * 
     * Método que recibe como parámetro la clave de un registro 
     * y asigna los valores del mismo a las variables de clase
     * retorna el resultado de la operación 
     * 
     */
    public boolean getDatosSeccion(int idseccion){

        // componemos la consulta
        String Consulta = "SELECT secciones.id AS id, " +   
                          "       secciones.orden AS orden, " +
                          "       secciones.etapa AS etapa " +
                          "       secciones.fecha AS fecha " +
                          "FROM secciones " +
                          "WHERE secciones.id = ?; ";

        // capturamos el error
        try {
        
            // asignamos la consulta y los parámetros 
            PreparedStatement SqlSecciones = this.Cursor.prepareStatement(Consulta);
            SqlSecciones.setInt(1, idseccion);
            ResultSet Resultado = SqlSecciones.executeQuery();
            
            // obtenemos el registro y retornamos
            Resultado.next();
            this.Id = Resultado.getInt("id");
            this.Orden = Resultado.getInt("orden");
            this.Etapa = Resultado.getString("etapa");
            this.Fecha = Resultado.getString("fecha");
            return true;

        // si ocurrió un error
        } catch (SQLException e){
            
            // imrprime y retorna 
            e.printStackTrace();
            return false;
            
        }

    }

    /**
     * 
     * @author Claudio Invernizzi <cinvernizzi@dsgestion.site>
     * 
     * @param idseccion - entero con la clave del registro
     * 
     * @return bool verdadero si puede eliminar
     * 
     * Método que recibe como parámetro la clave de un registro 
     * y verifica que no tenga registros hijos en la tabla de 
     * proyectos, retorna verdadero si puede eliminar 
     * 
     */
    public boolean puedeBorrar(int idseccion){

        // componemos la consulta
        String Consulta = "SELECT COUNT(actividades.id) AS registros " +
                          "FROM actividades " +
                          "WHERE actividades.seccion = ?;";

        // capturamos el error
        try {
        
            // asignamos la consulta y los parámetros 
            PreparedStatement SqlSecciones = this.Cursor.prepareStatement(Consulta);
            SqlSecciones.setInt(1, idseccion);
            ResultSet Resultado = SqlSecciones.executeQuery();
            
            // obtenemos el registro y verificamos
            Resultado.next();
            if (Resultado.getInt("registros") == 0){
                return true;
            } else {
                return false;
            }

        // si ocurrió un error
        } catch (SQLException e){
            
            // imrprime y retorna 
            e.printStackTrace();
            return false;
            
        }

    }

    /**
     * 
     * @author Claudio Invernizzi <cinvernizzi@dsgestion.site>
     * 
     * @param idseccion entero con la clave del registro
     * 
     * @return bool resultado de la operación 
     * 
     * Método que recibe como parámetro la clave de un registro 
     * y ejecuta la consulta de eliminación, retorna el resultado
     * de la operación 
     * 
     */
    public boolean borraSeccion(int idseccion){

        // componemos la consulta
        String Consulta = "DELETE FROM secciones " +
                          "WHERE secciones.id = ?; ";

        // capturamos el error
        try {

            // ejecutamos la consulta
            PreparedStatement SqlSecciones = this.Cursor.prepareStatement(Consulta);
            SqlSecciones.setInt(1, idseccion);
            SqlSecciones.execute();

            // retornamos
            return true;
            
        // si ocurrió un error
        } catch (SQLException e){

            // presenta el mensaje
            e.printStackTrace();
            return false;

        }
                          
    }
    
}
