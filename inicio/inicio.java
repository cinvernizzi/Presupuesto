/**
 * @author Claudio Invernizzi <cinvernizzi@dsgestion.site>
 * @date 10/09/2025
 * @Projecto: UploadSitracha
 * @Copyright DsGestion <dsgestion.site>
 * @Licence: GPL
 * Clase principal de la aplicación, pide la acreditación 
 * del usuario
 * 
 */

// definimos el paquete
package inicio;

// importamos las librerías
import sql.verifica;

// declaramos la clase
public class inicio {

    // constructor de la clase
    public static void main(String[] args){

        // verificamos las bases de datos
        new verifica();
        
    }

}