/**
 * 
 * @author Claudio Invernizzi <cinvernizzi@dsgestion.site>
 * @date 22/10/2025
 * @name DbPersonal
 * @Projecto: Presupuesto
 * @Copyright DsGestion <dsgestion.site>
 * @Licence: GPL
 * Clase que provee los métodos para interactar con la base
 * de datos personales
 * 
 */

// definición del paquete
package site.dsgestion.personal;

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
 */
public class DbPersonal {

    // declaramos las variables
    protected final Connection Cursor; // puntero a la base
    protected final dbLite Enlace;     // clase dbapi
    protected int Id;                  // clave del registro
    protected String Nombre;           // nombre que figura en el presupuesto
    protected String Empresa;          // nombre de la empresa
    protected String Direccion;        // dirección 
    protected String Cuil;             // identificación tributaria
    protected String Telefono;         // número de teléfono
    protected String Mail;             // mail personal
    protected String Fecha;            // fecha de alta del registro

    /**
     * 
     * @author Claudio Invernizzi <cinvernizzi@dsgestion.site>
     * 
     * Constructor de la clase, instanciamos la conexión con la 
     * base e inicializamos las variables
     * 
     */
    public DbPersonal(){

        // instanciamos la conexión 
        this.Enlace = new dbLite();
        this.Cursor = this.Enlace.getEnlace();
        this.Id = 0;
        this.Nombre = "";
        this.Empresa = "";
        this.Direccion = "";
        this.Cuil = "";
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
    public void setEmpresa(String empresa){
        this.Empresa = empresa;
    }
    public void setDireccion(String direccion){
        this.Direccion = direccion;
    }
    public void setCuil(String cuil){
        this.Cuil = cuil;
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
    public String getEmpresa(){
        return this.Empresa;
    }
    public String getDireccion(){
        return this.Direccion;
    }
    public String getCuil(){
        return this.Cuil;
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
    public int grabaPersonal(){
    
        // declaramos las variables
        int estado; 
        
        // si está insertando
        if (this.Id == 0){
            estado = this.nuevoPersonal();
        } else {
            estado = this.editaPersonal();
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
     * Método que genera la consulta de inserción y retorna la 
     * clave del nuevo registro o cero en caso de error
     * 
     */
    protected int nuevoPersonal(){
    
        // componemos la consulta
        String Consulta = "INSERT INTO personal " +
                          "        nombre, " +
                          "        empresa, " +
                          "        direccion, " +
                          "        cuil, " +
                          "        telefono, " +
                          "        mail, " +
                          "        fecha) " +
                          "       VALUES " +
                          "       (?, ?, ?, ?, ?, ?, date('now'));";
        
        // capturamos el error
        try {

            // ejecutamos la consulta
            PreparedStatement SqlPersonal = this.Cursor.prepareStatement(Consulta);
            SqlPersonal.setString(1, this.Nombre);
            SqlPersonal.setString(2, this.Empresa);
            SqlPersonal.setString(3, this.Direccion);
            SqlPersonal.setString(4, this.Cuil);
            SqlPersonal.setString(5, this.Telefono);
            SqlPersonal.setString(6, this.Mail);
            SqlPersonal.execute();

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
     * @return entero con la clave del registro
     * 
     * Método que genera la consulta de edición y retorna la 
     * clave del registro o cero en caso de error
     * 
     */
    protected int editaPersonal(){
        
        // componemos la consulta
        String Consulta = "UPDATE personal SET " +
                          "       nombre = ?, " +
                          "       empresa = ?, " + 
                          "       direccion = ?, " +
                          "       cuil = ?, " +
                          "       telefono = ?, " +
                          "       mail = ? " +
                          "WHERE personal.id = ?; ";

        // capturamos el error
        try {

            // ejecutamos la consulta
            PreparedStatement SqlPersonal = this.Cursor.prepareStatement(Consulta);
            SqlPersonal.setString(1, this.Nombre);
            SqlPersonal.setString(2, this.Empresa);
            SqlPersonal.setString(3, this.Direccion);
            SqlPersonal.setString(4, this.Cuil);
            SqlPersonal.setString(5, this.Telefono);
            SqlPersonal.setString(6, this.Mail);
            SqlPersonal.execute();

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
     * @return bool resultado de la operación 
     * 
     * Método que obtiene los datos personales y los asigna 
     * a las variables de clase, como hay un solo registro 
     * no recibe la clave del mismo, retorna el resultado 
     * de la operación 
     * 
     */
    public boolean getDatosPersonal(){

        // componemos la consulta
        String Consulta = "SELECT personal.id AS id, " +
                          "       personal.nombre AS nombre, " +
                          "       personal.empresa AS empresa, " +
                          "       personal.direccion AS direccion, " +
                          "       personal.cuil AS cuil, " +
                          "       personal.telefono AS telefono, " +
                          "       personal.mail AS mail, " +
                          "       personal.fecha AS fecha " +
                          "FROM personal; ";

        // capturamos el error
        try {
        
            // asignamos la consulta y los parámetros 
            PreparedStatement SqlPersonal = this.Cursor.prepareStatement(Consulta);
            ResultSet Resultado = SqlPersonal.executeQuery();
            
            // obtenemos el registro y asignamos
            Resultado.next();
            this.Id = Resultado.getInt("id");
            this.Nombre = Resultado.getString("nombre");
            this.Empresa = Resultado.getString("empresa");
            this.Direccion = Resultado.getString("direccion");
            this.Cuil = Resultado.getString("cuil");
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
    
}
