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

// incluimos las librerías 
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
    protected int Id;                  // clave del registro
    protected int Orden;               // número de orden
    protected String Etapa;            // nombre de la etapa
    protected String Fecha;            // fecha de alta del registro

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
        dbLite Enlace = new dbLite();
        this.Cursor = Enlace.getEnlace();
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
    
}
