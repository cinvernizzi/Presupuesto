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
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.io.File;

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
        
        // verificamos que exista el directorio temporal
        try {

            // definimos la ruta
            String path = "temp";
            Path dirPath = Paths.get(path);
            boolean isDirectory = Files.isDirectory(dirPath);

            // si no existe lo creamos
            if (!isDirectory) {
                File directorio = new File(path);
                directorio.mkdirs();
            }

        // capturamos el error
        } catch (Exception e) {
            System.out.println(e);
        }        

        // verificamos la base de datos 
        new Verifica();
        
        // aquí lanzamos la interfaz
        new Inicio();
        
    }
    
}
