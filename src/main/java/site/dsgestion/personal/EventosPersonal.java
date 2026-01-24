/**
 * 
 * @author Claudio Invernizzi <cinvernizzi@dsgestion.site>
 * @date 24/01/2026
 * @name EventosGrillaClientes
 * @Projecto: Presupuesto
 * @Copyright DsGestion <dsgestion.site>
 * @Licence: GPL
 * Clase define el formulario de los datos personales
 * 
 */

// definimos el paquete
package site.dsgestion.personal;

/**
 * 
 * @author Claudio Invernizzi <cinvernizzi@dsgestion.site>
 * 
 * Definición de la clase
 */
public class EventosPersonal {

    // declaramos las variables
    protected DbPersonal Personal;          // controlador de la base 
    protected FormPersonal Formulario;      // el formulario de datos

    /**
     * 
     * @author Claudio Invernizzi <cinvernizzi@dsgestion.site>
     * 
     * @param formulario el formulario de datos personales
     * 
     * Constructor de la clase, recibe como parámetro el formulario 
     * de datos personales
     * 
     */
    public EventosPersonal(FormPersonal formulario){

        // asignamos en la clase
        this.Formulario = formulario;

    }

    /**
     * 
     * @author Claudio Invernizzi <cinvernizzi@dsgestion.site>
     * 
     * Método llamado al pulsar el botón cancelar
     * 
     */
    public void cancelaPersonal(){

    }

    /**
     * 
     * @author Claudio Invernizzi <cinvernizzi@dsgestion.site>
     * 
     * Método llamado al pulsar el botón grabar que verifica 
     * los datos antes de enviarlo al servidor
     * 
     */
    public void verificaPersonal(){

    }

    /**
     * 
     * @author Claudio Invernizzi <cinvernizzi@dsgestion.site>
     * 
     * Método llamado desde el constructor que verifica si existe
     * un registro de datos personales y lo carga
     * 
     */
    protected void getDatosPersonal(){

    }

    /**
     * 
     * @author Claudio Invernizzi <cinvernizzi@dsgestion.site>
     * 
     * Método llamado al pulsar el botón de secciones que abre
     * la grilla con la nómina de secciones de un presupuesto
     * 
     */
    public void verSecciones(){

    }

    /**
     * 
     * @author Claudio Invernizzi <cinvernizzi@dsgestion.site>
     * 
     * Método llamado al pulsar sobre el botón del logo que 
     * abre el diálogo emergente para cargar la imagen 
     * 
     */
    public void cargaLogo(){

    }
    
}
