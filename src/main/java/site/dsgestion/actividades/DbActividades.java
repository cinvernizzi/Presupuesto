/**
 * 
 * @author Claudio Invernizzi <cinvernizzi@dsgestion.site>
 * @date 21/01/2026
 * @name Actividades
 * @Projecto: Presupuesto
 * @Copyright DsGestion <dsgestion.site>
 * @Licence: GPL
 * Clase que controla las operaciones sobre la tabla de 
 * actividades de un presupuesto
 * 
 */

// definición del paquete
package site.dsgestion.actividades;

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
public class DbActividades {
    
    // declaramos las variables
    protected final Connection Cursor; // puntero a la base
    protected final dbLite Enlace;     // clase dbapi
    protected int Id;                  // clave del registro
    protected int Proyecto;            // clave del proyecto
    protected int Seccion;             // clave de la sección
    protected String Descripcion;      // descripción de la actividad
    protected double Estimado;         // tiempo estimado
    protected double Optimo;           // tiempo optimo
    protected double Pesimista;        // tiempo pesimista
    protected double Total;            // tiempo calculado
    protected int Costo;               // costo de la actividad
    protected String Consideraciones;  // consideraciones del usuario

    /**
     * 
     * @author Claudio Invernizzi <cinvernizzi@dsgestion.site>
     * 
     * Constructor de la clase, establece la conexión con la 
     * base e inicializa las variables
     * 
     */
    public DbActividades(){

        // inicializamos la conexión y las variables
        this.Enlace = new dbLite();
        this.Cursor = this.Enlace.getEnlace();
        this.Id = 0;
        this.Proyecto = 0;
        this.Seccion = 0;
        this.Descripcion = "";
        this.Optimo = 0.00;
        this.Estimado = 0.00;
        this.Pesimista = 0.00;
        this.Total = 0.00;
        this.Costo = 0;
        this.Consideraciones = "";
        
    }
    
    // métodos de asignación de valores
    public void setId(int id){
        this.Id = id;
    }
    public void setProyecto(int proyecto){
        this.Proyecto = proyecto;
    }
    public void setSeccion(int seccion){
        this.Seccion = seccion;
    }
    public void setDescripcion(String descripcion){
        this.Descripcion = descripcion;
    }
    public void setOptimo(double optimo){
        this.Optimo = optimo;
    }
    public void setEstimado(double estimado){
        this.Estimado = estimado;
    }
    public void setPesimista(double pesimista){
        this.Pesimista = pesimista;
    }
    public void setTotal(double total){
        this.Total = total;
    }
    public void setCosto(int costo){
        this.Costo = costo;
    }
    public void setConsideraciones(String consideraciones){
        this.Consideraciones = consideraciones;
    }
    
    // métodos de retorno de valores
    public int getId(){
        return this.Id;
    }
    public int getProyecto(){
        return this.Proyecto;
    }
    public int getSeccion(){
        return this.Seccion;
    }
    public String getDescripcion(){
        return this.Descripcion;
    }
    public double getEstimado(){
        return this.Estimado;
    }
    public double getOptimista(){
        return this.Optimo;
    }
    public double getPesimista(){
        return this.Optimo;
    }
    public double getTotal(){
        return this.Total;
    }
    public int getCosto(){
        return this.Costo;
    }
    public String getConsideraciones(){
        return this.Consideraciones;
    }

    /**
     * 
     * @author Claudio Invernizzi <cinvernizzi@dsgestion.site>
     * 
     * @return entero con la clave del registro
     * 
     * Método que según el valor de las variables de clase 
     * genera la consulta de inserción o edición, retorna 
     * la clave del registro afectado o cero en caso de error
     * 
     */
    public int grabaActividad(){
    
        // declaramos las variables
        int estado;
        
        // si está insertando
        if (this.Id == 0){
            estado = this.nuevaActividad();
        } else {
            estado = this.editaActividad();
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
     * Método que ejecuta la consulta de inserción y retorna 
     * la clave del nuevo registro o cero en caso de error
     * 
     */
    protected int nuevaActividad(){
     
        // componemos la consulta
        String Consulta = "INSERT INTO actividades " +
                          "       (proyecto, " +
                          "        seccion, " +
                          "        descripcion, " +
                          "        estimado, " +
                          "        optimo, " +
                          "        pesimista, " +
                          "        total, " +
                          "        costo, " + 
                          "        consideraciones) " +
                          "       VALUES " +
                          "       (?, ?, ?, ?, ?, ?, " +
                          "        ?, ?, ?); ";
        
        // capturamos el error
        try {

            // ejecutamos la consulta
            PreparedStatement SqlActividad = this.Cursor.prepareStatement(Consulta);
            SqlActividad.setInt(1, this.Proyecto);
            SqlActividad.setInt(2, this.Seccion);
            SqlActividad.setString(3, this.Descripcion);
            SqlActividad.setDouble(4, this.Estimado);
            SqlActividad.setDouble(5, this.Optimo);
            SqlActividad.setDouble(6, this.Pesimista);
            SqlActividad.setDouble(7, this.Total);
            SqlActividad.setInt(8, this.Costo);
            SqlActividad.setString(9, this.Consideraciones);
            SqlActividad.execute();

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
    protected int editaActividad(){
        
        // componemos la consulta
        String Consulta = "UPDATE actividades SET " +
                          "       seccion = ?, " +
                          "       descripcion = ?, " +
                          "       estimado = ?, " +
                          "       optimo = ?, " +
                          "       pesimista = ?, " +
                          "       total = ?, " +
                          "       costo = ?, " +
                          "       consideraciones = ? " +
                          "WHERE actividades.id = ?; ";

        // capturamos el error
        try {

            // ejecutamos la consulta
            PreparedStatement SqlActividad = this.Cursor.prepareStatement(Consulta);
            SqlActividad.setInt(1, this.Seccion);
            SqlActividad.setString(2, this.Descripcion);
            SqlActividad.setDouble(3, this.Estimado);
            SqlActividad.setDouble(4, this.Optimo);
            SqlActividad.setDouble(5, this.Pesimista);
            SqlActividad.setDouble(6, this.Total);
            SqlActividad.setInt(7, this.Costo);
            SqlActividad.setString(8, this.Consideraciones);
            SqlActividad.setInt(9, this.Id);
            SqlActividad.execute();

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
     * @param idactividad - entero con la clave de la actividad
     * @param actividad - cadena con el nombre de la actividad
     * 
     * @return bool verdadero si puede insertar
     * 
     * Método que recibe como parámetro la clave del registro 
     * y el nombre de la actividad y verifica que no se encuentre
     * declarada, en cuyo caso retorna verdadero
     * 
     */
    public boolean validaActividad(int idactividad, String actividad){
     
        // componemos la consulta
        String Consulta = "SELECT COUNT(actividades.id) AS registros " +
                          "FROM actividades " +
                          "WHERE actividades.id != ? AND " +
                          "      actividades.actividad = ?; ";
        
        // capturamos el error
        try {
        
            // asignamos la consulta y los parámetros 
            PreparedStatement SqlActividad = this.Cursor.prepareStatement(Consulta);
            SqlActividad.setInt(1, idactividad);
            SqlActividad.setString(2, actividad);
            ResultSet Resultado = SqlActividad.executeQuery();
            
            // obtenemos el registro y verificamos
            Resultado.next();
            if (Resultado.getInt(1) == 0){
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
     * @param idactividad - entero con la clave del registro
     * 
     * @return bool resultado de la operación 
     * 
     * Método que recibe como parámetro la clave de un registro
     * y asigna los valores del mismo a las variables de clase, 
     * retorna el resultado de la operación 
     * 
     */
    public boolean getDatosActividad(int idactividad){
     
        // componemos la consulta
        String Consulta = "SELECT actividades.id AS id, " +
                          "       actividades.proyecto AS proyecto, " +
                          "       actividades.seccion AS seccion, " + 
                          "       actividades.descripcion AS descripcion, " +
                          "       actividades.estimado AS estimado, " +
                          "       actividades.optimo AS optimo, " +
                          "       actividades.pesimista AS pesimista, " +
                          "       actividades.total AS total, " +
                          "       actividades.costo AS costo, " +
                          "       actividades.consideraciones AS consideraciones " +
                          "FROM actividades " +
                          "WHERE actividades.id = ?; ";

        // capturamos el error
        try {
        
            // asignamos la consulta y los parámetros 
            PreparedStatement SqlActividad = this.Cursor.prepareStatement(Consulta);
            SqlActividad.setInt(1, idactividad);
            ResultSet Resultado = SqlActividad.executeQuery();
            
            // obtenemos el registro y asignamos
            Resultado.next();
            this.Id = Resultado.getInt("id");
            this.Proyecto = Resultado.getInt("proyecto");
            this.Seccion = Resultado.getInt("seccion");
            this.Descripcion = Resultado.getString("descripcion");
            this.Estimado = Resultado.getDouble("estimado");
            this.Optimo = Resultado.getDouble("optimo");
            this.Pesimista = Resultado.getDouble("pesimista");
            this.Total = Resultado.getDouble("total");
            this.Costo = Resultado.getInt("costo");
            this.Consideraciones = Resultado.getString("consideraciones");
            
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
     * @param idproyecto - clave del proyecto 
     * 
     * @return vector con la nómina de actividades
     * 
     * Método utilizado en los combos que retorna el vector 
     * con la nómina de actividades de un proyecto
     * 
     */
    public ResultSet nominaActividades(int idproyecto){
        
        // declaramos las variables
        ResultSet Resultado = null; 
        
        // realizamos la consulta sobre la vista
        String Consulta = "SELECT v_actividades.id AS id, " + 
                          "       v_actividades.proyecto AS proyecto, " +
                          "       v_actividades.seccion AS seccion, " + 
                          "       v_actividades.descripcion AS descripcion, " +
                          "       v_actividades.total AS total, " +
                          "       v_actividades.costo AS costo " +
                          "FROM v_actividades " + 
                          "WHERE v_actividades.idproyecto = ?; ";
        
        // capturamos el error
        try {
        
            // asignamos la consulta y los parámetros 
            PreparedStatement SqlActividad = this.Cursor.prepareStatement(Consulta);
            SqlActividad.setInt(1, idproyecto);
            Resultado = SqlActividad.executeQuery();
                        
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
     * @param idactividad - entero con la clave del registro
     * 
     * @return bool resultado de la operación 
     * 
     * Método que ejecuta la consulta de eliminación y retorna 
     * el resultado de la operación 
     * 
     */
    public boolean borraActividad(int idactividad){
        
        // definimos la consulta
        String Consulta = "DELETE FROM actividades " +
                          "WHERE actividades.id = ?; ";
        
        // capturamos el error
        try {

            // ejecutamos la consulta
            PreparedStatement SqlActividad = this.Cursor.prepareStatement(Consulta);
            SqlActividad.setInt(1, idactividad);
            SqlActividad.execute();
            return true;

        // si ocurrió un error
        } catch (SQLException e){

            // presenta el mensaje
            e.printStackTrace();
            return false;

        }
        
    }
    
}
