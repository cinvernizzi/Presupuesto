/**
 * 
 * @author Claudio Invernizzi <cinvernizzi@dsgestion.site>
 * @date 23/01/2026
 * @name EventosClientes
 * @Projecto: Presupuesto
 * @Copyright DsGestion <dsgestion.site>
 * @Licence: GPL
 * Clase que controla los eventos del formulario de clientes
 * 
 */

// definimos el paquete
package site.dsgestion.clientes;

// importamos las librerías 
import site.dsgestion.dbApi.Utilidades;
import site.dsgestion.dbApi.Mensaje;

/**
 *
 * @author Claudio Invernizzi <cinvernizzi@dsgestion.site>
 * 
 * Definición de la clase
 * 
 */
public class EventosClientes {
   
    // declaramos las variables
    protected DbClientes Clientes;      // controlador de la base de datos
    protected FormClientes Formulario;  // formulario de datos
    protected Utilidades Herramientas;  // utilidades de fechas
    
    /**
     * 
     * @author Claudio Invernizzi <cinvernizzi@dsgestion.site>
     * 
     * @param formulario la clase con la definición del formulario
     * 
     * Constructor de la clase, recibe como parámetro el formulario 
     * con los datos 
     * 
     */
    public EventosClientes(FormClientes formulario){
        
        // asignamos en la clase
        this.Formulario = formulario;
        
        // instanciamos la clase de herramientes y de base de datos
        this.Herramientas = new Utilidades();
        this.Clientes = new DbClientes();
        
    }
    
    /**
     * 
     * @author Claudio Invernizzi <cinvernizzi@dsgestion.site>
     * 
     * Método llamado al pulsar el botón grabar que verifica 
     * los datos del formulario y en todo caso graba el registro
     * 
     */
    public void verificaCliente(){
        
        // si está insertando
        if (this.Formulario.tId.getText().equals("")){
            this.Clientes.setId(0);
        } else {
            this.Clientes.setId(Integer.parseInt(this.Formulario.tId.getText()));
        }
        
        // si no ingresó el nombre
        if (this.Formulario.tNombre.getText().equals("")){
            new Mensaje("Ingrese el nombre del cliente");
            return;
        } else {
            this.Clientes.setNombre(this.Formulario.tNombre.getText());
        }
     
        // si no ingresó la dirección
        if (this.Formulario.tDireccion.getText().equals("")){
            new Mensaje("Indique la dirección del cliente");
            return;
        } else {
            this.Clientes.setDireccion(this.Formulario.tDireccion.getText());
        }
        
        // si no ingresó la id tributaria
        if (this.Formulario.tIdTributaria.getText().equals("")){
            new Mensaje("No hay Id Tributaria, se graba igualmente");
        }
        this.Clientes.setIdentificacion(this.Formulario.tIdTributaria.getText());
        
        // si no ingresó ni teléfono ni mail
        if (this.Formulario.tTelefono.getText().equals("") &&
            this.Formulario.tMail.getText().equals("")){
            
            // presenta el mensaje y retorna
            new Mensaje("Debe indicar una forma de contacto");
            return;
            
        }
        
        // si ingresó el mail verificamos que sea correcto
        if (!this.Formulario.tMail.getText().equals("")){
            
            // verificamos 
            if (!this.Herramientas.esEmailCorrecto(this.Formulario.tMail.getText())){
                
                // presenta el mensaje
                new Mensaje("El mail parece incorrecto");
                return;
            }
            
        }
        
        // fijamos el teléfono y el mail
        this.Clientes.setTelefono(this.Formulario.tTelefono.getText());
        this.Clientes.setMail(this.Formulario.tMail.getText());
        
        // si llegó hasta aquí grabamos
        int id = this.Clientes.grabaCliente();
        
        // si salió todo bien
        if (id != 0){
        
            // fijamos la clave
            this.Formulario.tId.setText(Integer.toHexString(id));
            
            // presenta el mensaje
            new Mensaje("Registro grabado ...");
            
        }
        
    }
    
    /**
     * 
     * @author Claudio Invernizzi <cinvernizzi@dsgestion.site>
     * 
     * Método llamado al pulsar el botón cancelar que según el 
     * estado del formulario lo limpia o recarga el registro
     * 
     */
    public void cancelaCliente(){
        
        // si está insertando
        if (this.Formulario.tId.getText().equals("")){
            this.nuevoCliente();
        } else {
            this.getDatosCliente(Integer.parseInt(this.Formulario.tId.getText()));
        }
        
    }
    
    /**
     * 
     * @author Claudio Invernizzi <cinvernizzi@dsgestion.site>
     * 
     * Método que limpia el formulario de datos 
     * 
     */
    public void nuevoCliente(){
        
        // limpiamos el formulario
        this.Formulario.tId.setText("");
        this.Formulario.tNombre.setText("");
        this.Formulario.tDireccion.setText("");
        this.Formulario.tIdTributaria.setText("");
        this.Formulario.tTelefono.setText("");
        this.Formulario.tMail.setText("");
        this.Formulario.tFecha.setText(this.Herramientas.FechaActual());
        
        // fijamos el foco
        this.Formulario.tNombre.requestFocus();
        
    }
    
    /**
     * 
     * @author Claudio Invernizzi <cinvernizzi@dsgestion.site>
     * 
     * @param idcliente - entero con la clave del registro
     * 
     * Método que recibe como parámetro la clave de un registro 
     * y carga los datos del mismo
     * 
     */
    public void getDatosCliente(int idcliente){

        // obtenemos el registro
        this.Clientes.getDatosCliente(idcliente);
        
        // lo presentamos
        this.Formulario.tId.setText(Integer.toString(this.Clientes.getId()));
        this.Formulario.tNombre.setText(this.Clientes.getNombre());
        this.Formulario.tDireccion.setText(this.Clientes.getDireccion());
        this.Formulario.tIdTributaria.setText(this.Clientes.getIdentificacion());
        this.Formulario.tTelefono.setText(this.Clientes.getTelefono());
        this.Formulario.tMail.setText(this.Clientes.getMail());
        this.Formulario.tFecha.setText(this.Clientes.getFecha());
        
        // fijamos el foco
        this.Formulario.tNombre.requestFocus();
        
    }
    
}
