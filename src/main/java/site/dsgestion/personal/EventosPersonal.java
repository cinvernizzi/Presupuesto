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

// importamos las librerías
import java.awt.Image;
import java.io.File;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.StandardCopyOption;
import javax.swing.ImageIcon;
import javax.swing.JFileChooser;
import javax.swing.filechooser.FileNameExtensionFilter;
import site.dsgestion.dbApi.Mensaje;
import site.dsgestion.dbApi.Utilidades;

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
    protected Utilidades Herramientas;      // utilidades del sistema

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
        this.Herramientas = new Utilidades();
        this.Personal = new DbPersonal();
        
    }

    /**
     * 
     * @author Claudio Invernizzi <cinvernizzi@dsgestion.site>
     * 
     * Método llamado al pulsar el botón cancelar
     * 
     */
    public void cancelaPersonal(){

        // cerramos el formulario
        this.Formulario.dispose();

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

        // si está insertando
        if (this.Formulario.tId.getText().equals("")){
            this.Personal.setId(0);
        } else {
            this.Personal.setId(Integer.parseInt(this.Formulario.tId.getText()));
        }

        // si no indicó el nombre
        if (this.Formulario.tNombre.getText().equals("")){
            new Mensaje("Indique su nombre completo");
            return;
        } else {
            this.Personal.setNombre(this.Formulario.tNombre.getText());
        }

        // si no indicó la empresa
        if (this.Formulario.tEmpresa.getText().equals("")){
            new Mensaje("Indique el nombre de la empresa");
            return;
        } else {
            this.Personal.setEmpresa(this.Formulario.tEmpresa.getText());
        }

        // si no ingresó la clave tributaria
        if (this.Formulario.tCuil.getText().equals("")){
            new Mensaje("Indique la clave tributaria");
            return;
        } else {
            this.Personal.setCuil(this.Formulario.tCuil.getText());
        }

        // si no indicó la dirección 
        if (this.Formulario.tDireccion.getText().equals("")){
            new Mensaje("Indique la dirección de facturación");
            return;
        } else {
            this.Personal.setDireccion(this.Formulario.tDireccion.getText());
        }

        // si ingresó el mail lo verifica
        if (!this.Formulario.tMail.getText().equals("")){

            // verificamos
            if (!this.Herramientas.esEmailCorrecto(this.Formulario.tMail.getText())){
                new Mensaje("El mail parece incorrecto ...");
                return;
            }

        }

        // si no ingresó ni mail ni teléfono
        if (this.Formulario.tTelefono.getText().equals("") &&
            this.Formulario.tMail.getText().equals("")){

            // presenta el mensaje
            new Mensaje("Debe indicar un modo de contacto");
            return;

        }

        // asigna el mail y el teléfono 
        this.Personal.setTelefono(this.Formulario.tTelefono.getText());
        this.Personal.setMail(this.Formulario.tMail.getText());

        // si llegó hasta aquí grabamos
        int id = this.Personal.grabaPersonal();

        // si salió todo bien
        if (id != 0){

            // asignamos la clave y setea el foco 
            this.Formulario.tId.setText(Integer.toString(id));
            new Mensaje("Registro grabado ...");
            this.Formulario.tNombre.requestFocus();

        // si ocurrió un error 
        } else {
            
            // presenta el mensaje
            new Mensaje("Ha ocurrido un error ...");
            
        }

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

        // obtenemos el registro (si existe)
        this.Personal.getDatosPersonal();

        // asignamos en el formulario
        this.Formulario.tId.setText(Integer.toString(this.Personal.getId()));
        this.Formulario.tNombre.setText(this.Personal.getNombre());
        this.Formulario.tEmpresa.setText(this.Personal.getEmpresa());
        this.Formulario.tCuil.setText(this.Personal.getCuil());
        this.Formulario.tDireccion.setText(this.Personal.getDireccion());
        this.Formulario.tTelefono.setText(this.Personal.getTelefono());
        this.Formulario.tMail.setText(this.Personal.getMail());
        this.Formulario.tFecha.setText(this.Personal.getFecha());

        // fijamos el foco
        this.Formulario.tNombre.requestFocus();

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

        // abrimos el cuadro de diálogo
        JFileChooser archivo = new JFileChooser();

        // fijamos el filtro de extensión
        FileNameExtensionFilter filter = new FileNameExtensionFilter("Imágenes PNG", "png");
        archivo.setFileFilter(filter);
        
        // obtenemos la respuesta
        int respuesta = archivo.showOpenDialog(this.Formulario);

        // si se seleccionó un archivo
        if (respuesta == JFileChooser.APPROVE_OPTION) {

            // Creamos un objeto File con el archivo elegido
            File archivoElegido = archivo.getSelectedFile();

            // Obtenemos la ruta de ejecución 
            Path destinoDir = Paths.get(System.getProperty("user.dir"));

            // obtenemos la ruta completa del archivo elegido y 
            // fijamos el destino a partir de la ruta de ejecución
            Path origen = Paths.get(archivoElegido.getAbsolutePath());
            Path destino = Paths.get(destinoDir + "/temp/logo.png");

            // capturamos el error
            try{

                // copiamos 
                Files.copy(origen, destino, StandardCopyOption.REPLACE_EXISTING);

                // si pudo copiar ahora cargamos el archivo en el formulario
                this.mostrarLogo();

            // si hubo un error
            } catch (Exception e){
                System.err.println("Error al copiar el archivo: " + e.getMessage());
            }

        }        

    }

    /**
     * 
     * @author Claudio Invernizzi <cinvernizzi@dsgestion.site>
     * 
     * Método llamado al cargar el formulario o al seleccionar el 
     * archivo que redimensiona el logo y lo muestra en el formulario
     * 
     */
    public void mostrarLogo(){

        // obtenemos la ruta de ejecución
        Path destinoDir = Paths.get(System.getProperty("user.dir"));

        // obtenemos la imagen
        Image originalImage = new ImageIcon(destinoDir + "/temp/logo.png").getImage();
        Image scaledImage = originalImage.getScaledInstance(60, 60, Image.SCALE_SMOOTH);
        ImageIcon icon = new ImageIcon(scaledImage);   
        this.Formulario.btnLogo.setIcon(icon);

    }

    /**
     * 
     * @author Claudio Invernizzi <cinvernizzi@dsgestion.site>
     * 
     * Método que verifica si existe un logo y en este caso lo 
     * carga en el formulario 
     * 
     */
    public void verificaLogo(){

        // Obtenemos la ruta de ejecución 
        Path destinoDir = Paths.get(System.getProperty("user.dir"));
        String destino = destinoDir + "/temp/logo.png";

        // verificamos si existe
        File file = new File(destino);
        if (file.exists()) {
            this.mostrarLogo();
        } 

    }

}
