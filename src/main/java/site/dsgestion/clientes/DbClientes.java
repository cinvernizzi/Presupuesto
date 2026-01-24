/**
 * 
 * @author Claudio Invernizzi <cinvernizzi@dsgestion.site>
 * @date 21/10/2025
 * @name DbClientes
 * @Projecto: Presupuesto
 * @Copyright DsGestion <dsgestion.site>
 * @Licence: GPL
 * Clase que provee los métodos para interactar con la base
 * de datos de clientes
 * 
 */

// definición del paquete
package site.dsgestion.clientes;

// importamos las librerías
import site.dsgestion.dbApi.dbLite;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

// definición de la clase
public class DbClientes {

    // definimos las variables
    protected final Connection Cursor; // puntero a la base
    protected final dbLite Enlace;     // clase dbapi
    protected int Id;                  // clave del registro
    protected String Nombre;           // nombre del cliente
    protected String Direccion;        // domicilio del cliente
    protected String Identificacion;   // clave tributaria
    protected String Telefono;         // número de teléfono
    protected String Mail;             // dirección de correo electrónico
    protected String Fecha;            // fecha de alta del registro

    /*
     *
     * @author Claudio Invernizzi <cinvernizzi@dsgestion.site>
     *
     * Método que verifica la existencia de la tabla de 
     * secciones
     *
     */
    public DbClientes(){

        // instanciamos la conexión 
        this.Enlace = new dbLite();
        this.Cursor = this.Enlace.getEnlace();

        // inicializamos las variables
        this.Id = 0;
        this.Nombre = "";
        this.Direccion = "";
        this.Identificacion = "";
        this.Telefono = "";
        this.Mail = ""; 
        this.Fecha = "";
        
    }
    
    // métodos de asignación de valores
    public void setId(int id){
        this.Id = id;
    }
    public void setNombre(String nombre){
        this.Nombre = nombre;
    }
    public void setDireccion(String direccion){
        this.Direccion = direccion;
    }
    public void setIdentificacion(String identificacion){
        this.Identificacion = identificacion;
    }
    public void setTelefono(String telefono){
        this.Telefono = telefono;
    }
    public void setMail(String mail){
        this.Mail = mail; 
    }
    
    // métodos de retorno de valores
    public int getId(){
        return this.Id;
    }
    public String getNombre(){
        return this.Nombre;
    }
    public String getDireccion(){
        return this.Direccion;
    }
    public String getIdentificacion(){
        return this.Identificacion;
    }
    public String getTelefono(){
        return this.Telefono;
    }
    public String getMail(){
        return this.Mail;
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
     * genera la consulta de edición o inserción y retorna 
     * la clave del registro afectado o cero en caso de error
     * 
     */
    public int grabaCliente(){
    
        // declaración de variables
        int estado; 
        
        // si está insertando
        if (this.Id == 0){
            estado = this.nuevoCliente();
        } else {
            estado = this.editaCliente();
        }
        
        // retornamos
        return estado;
        
    }
    
    /**
     * 
     * @author Claudio Invernizzi <cinvernizzi@dsgestion.site>
     * 
     * @return entero con la clave del registro
     * 
     * Método que ejecuta la consulta de inserción y retorna la 
     * clave del nuevo registro o cero en caso de error
     * 
     */
    protected int nuevoCliente(){

        // componemos la consulta
        String Consulta = "INSERT INTO clientes " +
                          "       (nombre, " +
                          "        direccion,  " + 
                          "        identificacion, " +
                          "        telefono, " + 
                          "        mail, " + 
                          "        fecha) " +
                          "       VALUES " + 
                          "       (?, ?, ?, ?, ?, date('now')); ";
        
        // capturamos el error
        try {

            // ejecutamos la consulta
            PreparedStatement SqlClientes = this.Cursor.prepareStatement(Consulta);
            SqlClientes.setString(1, this.Nombre);
            SqlClientes.setString(2, this.Direccion);
            SqlClientes.setString(3, this.Identificacion);
            SqlClientes.setString(4, this.Telefono);
            SqlClientes.setString(5, this.Mail);
            SqlClientes.execute();

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
    protected int editaCliente(){
        
        // componemos la consulta
        String Consulta = "UPDATE clientes SET " +
                          "       nombre = ?, " +
                          "       direccion = ?, " +
                          "       identificacion = ?, " +
                          "       telefono = ?, " + 
                          "       mail = ? " +
                          "WHERE clientes.id = ?; ";

        // capturamos el error
        try {

            // ejecutamos la consulta
            PreparedStatement SqlClientes = this.Cursor.prepareStatement(Consulta);
            SqlClientes.setString(1, this.Nombre);
            SqlClientes.setString(2, this.Direccion);
            SqlClientes.setString(3, this.Identificacion);
            SqlClientes.setString(4, this.Telefono);
            SqlClientes.setString(5, this.Mail);
            SqlClientes.setInt(6, this.Id);
            SqlClientes.execute();

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
     * @param idcliente clave del registro
     * @param idtributaria clave tributaria del cliente
     * 
     * @return bool verdadero si puede grabar
     * 
     * Método que recibe como parámetros la clave del cliente 
     * y la clave tributaria y verifica que no se encuentre 
     * declarado, en cuyo caso retorna verdadero
     * 
     */
    public boolean validaCliente(int idcliente, String idtributaria){

        // componemos la consulta
        String Consulta = "SELECT COUNT(clientes.id) AS registros " +
                          "FROM clientes " +
                          "WHERE clientes.id  != ? AND " +
                          "      clientes.identificacion = ?; ";

        // capturamos el error
        try {
        
            // asignamos la consulta y los parámetros 
            PreparedStatement SqlCliente = this.Cursor.prepareStatement(Consulta);
            SqlCliente.setInt(1, idcliente);
            SqlCliente.setString(2, idtributaria);
            ResultSet Resultado = SqlCliente.executeQuery();
                        
            // obtenemos el registro
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
     * @param cliente - parte del nombre del cliente
     * 
     * @return vector con la nómina de clientes
     * 
     * Método utilizado en la grilla de clientes que recibe como 
     * parámetro una cadena de texto y retorna el vector 
     * con todos los registros coincidentes
     * 
     */
    public ResultSet nominaClientes(String cliente){

        // definimos el resultset
        ResultSet Resultado = null;

        // componemos la consulta
        String Consulta = "SELECT clientes.id AS id, " +
                          "       clientes.nombre AS nombre " +
                          "FROM clientes " +
                          "WHERE clientes.nombre LIKE ? " +
                          "ORDER BY clientes.nombre; ";

        // capturamos el error
        try {
        
            // asignamos la consulta y los parámetros 
            PreparedStatement SqlCliente = this.Cursor.prepareStatement(Consulta);
            SqlCliente.setString(1, "%" + cliente + "%");
            Resultado = SqlCliente.executeQuery();
            
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
     * @return vector con la nómina de clientes
     * 
     * Método utilizado en la grilla de clientes llamado sin 
     * filtro de ningún tipo que retorna la nómina completa 
     * de clientes registrados 
     * 
     */
    public ResultSet nominaClientes(){

        // definimos el resultset
        ResultSet Resultado = null;

        // componemos la consulta
        String Consulta = "SELECT clientes.id AS id, " +
                          "       clientes.nombre AS nombre " +
                          "FROM clientes " +
                          "ORDER BY clientes.nombre; ";

        // capturamos el error
        try {
        
            // asignamos la consulta y los parámetros 
            PreparedStatement SqlCliente = this.Cursor.prepareStatement(Consulta);
            Resultado = SqlCliente.executeQuery();
            
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
     * @param idcliente - clave del registro 
     * 
     * @return bool resultado de la operación 
     * 
     * Método que recibe como parámetro la clave de un registro 
     * y asigna los valores del mismo a las variables de clase, 
     * retorna el resultado de la operación 
     * 
     */
    public boolean getDatosCliente(int idcliente){
     
        // componemos la consulta
        String Consulta = "SELECT clientes.id AS id, " +
                          "       clientes.nombre AS nombre, " +
                          "       clientes.direccion AS direccion, " +
                          "       clientes.identificacion AS identificacion, " + 
                          "       clientes.telefono AS telefono, " + 
                          "       clientes.mail AS mail, " + 
                          "       clientes.fecha AS fecha " + 
                          "FROM clientes " + 
                          "WHERE clientes.id = ?; ";

        // capturamos el error
        try {
        
            // asignamos la consulta y los parámetros 
            PreparedStatement SqlCliente = this.Cursor.prepareStatement(Consulta);
            SqlCliente.setInt(1, idcliente);
            ResultSet Resultado = SqlCliente.executeQuery();
                        
            // obtenemos el registro y asignamos
            Resultado.next();
            this.Id = Resultado.getInt("id");
            this.Nombre = Resultado.getString("nombre");
            this.Direccion = Resultado.getString("direccion");
            this.Identificacion = Resultado.getString("identificacion");
            this.Telefono = Resultado.getString("telefono");
            this.Mail = Resultado.getString("mail");
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
     * @param idcliente - clave del registro 
     * 
     * @return bool - verdadero si puede borrar
     * 
     * Método que recibe como parámetro la clave de un registro 
     * y verifica que este no tenga registros hijos en la tabla 
     * de proyectos en cuyo caso retorna verdadero
     * 
     */
    public boolean puedeBorrar(int idcliente){
        
        // componemos la consulta
        String Consulta = "SELECT COUNT(proyectos.id) AS registros " +
                          "FROM proyectos " +
                          "WHERE proyectos.cliente = ?; ";
        
        // capturamos el error
        try {
        
            // asignamos la consulta y los parámetros 
            PreparedStatement SqlCliente = this.Cursor.prepareStatement(Consulta);
            SqlCliente.setInt(1, idcliente);
            ResultSet Resultado = SqlCliente.executeQuery();
                        
            // obtenemos el registro
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
     * @param idcliente - clave del registro 
     * 
     * @return bool resultado de la operación 
     * 
     * Método que recibe la clave de un registro y ejecuta la 
     * consulta de eliminación, retorna el resultado de la 
     * operación 
     * 
     */
    public boolean borraCliente(int idcliente){
        
        // componemos la consulta
        String Consulta = "DELETE FROM clientes " +
                          "WHERE clientes.id = ?; ";

        // capturamos el error
        try {
        
            // asignamos la consulta y los parámetros 
            PreparedStatement SqlCliente = this.Cursor.prepareStatement(Consulta);
            SqlCliente.setInt(1, idcliente);
            SqlCliente.execute();
                        
            // retorenamos
            return true;
            
        // si ocurrió un error
        } catch (SQLException e){
            
            // imrprime y retorna 
            e.printStackTrace();
            return false;
            
        }
        
    }
    
}