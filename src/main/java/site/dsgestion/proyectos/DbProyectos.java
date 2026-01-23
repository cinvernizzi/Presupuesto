/**
 * 
 * @author Claudio Invernizzi <cinvernizzi@dsgestion.site>
 * @date 22/10/2025
 * @name DbProyectos
 * @Projecto: Presupuesto
 * @Copyright DsGestion <dsgestion.site>
 * @Licence: GPL
 * Clase que provee los métodos para interactar con la base
 * de proyectos
 * 
 */

// definimos el paquete
package site.dsgestion.proyectos;

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
public class DbProyectos {

    // declaramos las variables
    protected final Connection Cursor; // puntero a la base
    protected final dbLite Enlace;     // clase dbapi
    protected int Id;                  // clave del registro
    protected int Cliente;             // clave del cliente
    protected String Titulo;           // título del proyecto
    protected String Descripcion;      // descripción del proyecto
    protected String Fecha;            // fecha de alta del proyecto

    /**
     * 
     * @author Claudio Invernizzi <cinvernizzi@dsgestion.site>
     * 
     * Constructor de la clase, establece la conexión con la 
     * base e inicializa las variables
     * 
     */
    public DbProyectos(){

        // instanciamos la conexión
        this.Enlace = new dbLite();
        this.Cursor = this.Enlace.getEnlace();
        this.Id = 0;
        this.Cliente = 0;
        this.Titulo = "";
        this.Descripcion = "";
        this.Fecha = "";

    }

    // métodos de asignación de valores
    public void setId(int id){
        this.Id = id;
    }
    public void setCliente(int cliente){
        this.Cliente = cliente;
    }
    public void setTitulo(String titulo){
        this.Titulo = titulo;
    }
    public void setDescripcion(String descripcion){
        this.Descripcion = descripcion;
    }

    // métodos de retorno de valores
    public int getId(){
        return this.Id;
    }
    public int getCliente(){
        return this.Cliente;
    }
    public String getTitulo(){
        return this.Titulo;
    }
    public String getDescripcion(){
        return this.Descripcion;
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
     * ejecuta la consulta de edición o inserción y luego 
     * retorna la clave del registro afectado o cero en caso
     * de error
     * 
     */
    public int grabaProyecto(){

        // declaramos las variables
        int estado;

        // si está insertando
        if (this.Id == 0){
            estado = this.nuevoProyecto();
        } else {
            estado = this.editaProyecto();
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
     * clave del nuevo registro o cero en caso de error
     * 
     */
    protected int nuevoProyecto(){

        // componemos la consulta
        String Consulta = "INSERT INTO proyectos " +
                          "       (cliente, " + 
                          "        titulo, " + 
                          "        descripcion, " +
                          "        fecha) " + 
                          "       VALUES " + 
                          "       (?, ?, ?, date('now')); ";

        // capturamos el error
        try {

            // ejecutamos la consulta
            PreparedStatement SqlProyectos = this.Cursor.prepareStatement(Consulta);
            SqlProyectos.setInt(1, this.Cliente);
            SqlProyectos.setString(2, this.Titulo);
            SqlProyectos.setString(3, this.Descripcion);
            SqlProyectos.execute();

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
     * Método que ejecuta la consulta de edición y retorna la 
     * clave del registro afectado o cero en caso de error
     * 
     */
    protected int editaProyecto(){

        // componemos la consulta
        String Consulta = "UPDATE proyectos SET " + 
                          "       cliente = ?, " +
                          "       titulo = ?, " +
                          "       descripcion = ? " +
                          "WHERE proyectos.id = ?; ";

        // capturamos el error
        try {

            // ejecutamos la consulta
            PreparedStatement SqlProyectos = this.Cursor.prepareStatement(Consulta);
            SqlProyectos.setInt(1, this.Cliente);
            SqlProyectos.setString(2, this.Titulo);
            SqlProyectos.setString(3, this.Descripcion);
            SqlProyectos.setInt(4, this.Id);
            SqlProyectos.execute();

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
     * @param idproyecto - clave del proyecto
     * @param idcliente - clave del cliente
     * @param titulo - nombre del proyecto
     * 
     * @return bool verdadero si puede grabar
     * 
     * Método que verifica no se ingrese un proyecto repetido
     * recibe como parámetro la clave del proyecto (cero en 
     * caso de un alta), la clave del cliente y el título del
     * proyecto y retorna verdadero si puede grabar 
     * 
     */
    public boolean validaProyecto(int idproyecto, int idcliente, String titulo){

        // componemos la consulta
        String Consulta = "SELECT COUNT(proyectos.id) AS registros " +
                          "FROM proyectos " + 
                          "WHERE proyectos.id != ? AND " +
                          "      proyectos.cliente = ? AND " + 
                          "      proyectos.titulo = ?; ";

        // capturamos el error
        try {
        
            // asignamos la consulta y los parámetros 
            PreparedStatement SqlProyectos = this.Cursor.prepareStatement(Consulta);
            SqlProyectos.setInt(1, idproyecto);
            SqlProyectos.setInt(2, idcliente);
            SqlProyectos.setString(3, titulo);
            ResultSet Resultado = SqlProyectos.executeQuery();
            
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
     * @param idproyecto - clave del proyecto 
     * 
     * @return bool resultado de la operación 
     * 
     * Método que recibe como parámetro la clave de un proyecto 
     * y asigna los valores del registro a las variables de 
     * clase, retorna el resultado de la operación 
     * 
     */
    public boolean getDatosProyecto(int idproyecto){

        // componemos la consulta
        String Consulta = "SELECT proyectos.id AS id, " + 
                          "       proyectos.cliente AS cliente, " +
                          "       proyectos.titulo AS titulo, " +
                          "       proyectos.descripcion AS descripcion, " +
                          "       proyectos.fecha AS fecha " +
                          "FROM proyectos " +
                          "WHERE proyectos.id = ?; ";

        // capturamos el error
        try {
        
            // asignamos la consulta y los parámetros 
            PreparedStatement SqlProyectos = this.Cursor.prepareStatement(Consulta);
            ResultSet Resultado = SqlProyectos.executeQuery();
            
            // obtenemos y asignamos
            Resultado.next();
            this.Id = Resultado.getInt("id");
            this.Cliente = Resultado.getInt("cliente");
            this.Titulo = Resultado.getString("titulo");
            this.Descripcion = Resultado.getString("descripcion");
            this.Fecha = Resultado.getString("fecha");

            // retornamos
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
     * @param idcliente - clave del cliente
     * 
     * @return resultset con la nómina de proyectos
     * 
     * Método que recibe como parámetro la clave de un cliente 
     * y retorna el vector con todos los proyectos de ese cliente
     * 
     */
    public ResultSet nominaProyectos(int idcliente){

        // declaramos las variables
        ResultSet Resultado = null;

        // componemos la consulta
        String Consulta = "SELECT v_proyectos.id AS id, " +
                          "       v_proyectos.titulo AS titulo, " +
                          "       v_proyectos.fecha AS fecha " + 
                          "FROM v_proyectos " +
                          "WHERE v_proyectos.id = ? " +
                          "ORDER BY v_proyectos.titulo; ";

        // capturamos el error
        try {
        
            // asignamos la consulta y los parámetros 
            PreparedStatement SqlProyectos = this.Cursor.prepareStatement(Consulta);
            Resultado = SqlProyectos.executeQuery();
            
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
     * @param idproyecto - clave del proyecto 
     * 
     * @return bool - verdadero si puede borrar
     * 
     * Método que recibe como parámetro la clave de un proyecto 
     * y verifica que este no tenga hijos en la tabla de actividades
     * retorna verdadero si puede eliminar
     * 
     */
    public boolean puedeBorrar(int idproyecto){

        // componemos la consulta
        String Consulta = "SELECT COUNT(actividades.id) AS registros " + 
                          "FROM actividades " +
                          "WHERE actividades.proyecto = ?; ";

        // capturamos el error
        try {
        
            // asignamos la consulta y los parámetros 
            PreparedStatement SqlProyectos = this.Cursor.prepareStatement(Consulta);
            ResultSet Resultado = SqlProyectos.executeQuery();
            
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
     * @param idproyecto - clave del proyecto
     * 
     * @return bool resultado de la operación 
     * 
     * Método que recibe como parámetro la clave de un proyecto y 
     * ejecuta la consulta de eliminación, retorna el resultado de 
     * la operación 
     * 
     */
    public boolean borraProyecto(int idproyecto){

        // componemos la consulta
        String Consulta = "DELETE FROM proyectos " +
                          "WHERE proyectos.id = ?; ";

        // capturamos el error
        try {

            // ejecutamos la consulta
            PreparedStatement SqlProyectos = this.Cursor.prepareStatement(Consulta);
            SqlProyectos.setInt(1, idproyecto);

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
