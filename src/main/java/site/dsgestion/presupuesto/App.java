/**
 * 
 * @author Claudio Invernizzi <cinvernizzi@dsgestion.site>
 * @date 21/01/2026
 * @name App
 * @Projecto: Presupuesto
 * @Copyright DsGestion <dsgestion.site>
 * @Licence: GPL
 * Método principal que verifica la existencia de las 
 * bases de datos e inicializa la interfaz
 * 
 */

// definimos el paquete
package site.dsgestion.presupuesto;

// importamos las librerías 
import site.dsgestion.sql.Verifica;

/**
 * 
 * @author: Claudio Invernizzi <cinvernizzi@dsgestion.site>
 * 
 * Definición de la clase
 * 
 */
public class App {
    
    /**
     * 
     * @author Claudio Invernizzi <cinvernizzi@dsgestion.site>
     * 
     * @param args array con los argumentos
     * 
     * Constructor de la clase, verifica las bases de 
     * datos y lanza la interfaz
     * 
     */
    public static void main(String[] args) {
        
        // verificamos la base de datos 
        new Verifica();
        
        // aquí lanzamos la interfaz
        new Inicio();
        
    }
    
}
