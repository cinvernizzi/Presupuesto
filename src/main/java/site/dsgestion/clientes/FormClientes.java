/**
 * 
 * @author Claudio Invernizzi <cinvernizzi@dsgestion.site>
 * @date 23/01/2026
 * @name FormClientes
 * @Projecto: Presupuesto
 * @Copyright DsGestion <dsgestion.site>
 * @Licence: GPL
 * Clase que configura el formulario con los datos de los clientes
 * 
 */

// definimos el paquete
package site.dsgestion.clientes;

// importamos las librerías
import java.awt.*;
import javax.swing.*;
import site.dsgestion.dbApi.Fuentes;


/**
 *
 * @author Claudio Invernizzi <cinvernizzi@dsgestion.site>
 * 
 * Definición de la clase
 * 
 */
public class FormClientes {
    
    // definimos los controles
    public JTextField tId;             // clave del registro
    public JTextField tNombre;         // nombre del cliente
    public JTextField tDireccion;      // dirección postal
    public JTextField tIdTributaria;   // identificación tributaria
    public JTextField tTelefono;       // número de teléfono
    public JTextField tMail;           // dirección de correo
    public JTextField tFecha;          // fecha de alta
    protected EventosClientes Eventos; // controlador de eventos
    
    /**
     * 
     * @author Claudio Invernizzi <cinvernizzi@dsgestion.site>
     * 
     * @param contenedor el panel contenedor
     * 
     * Constructor de la clase, recibe como parámetro el panel contenedor
     * del formulario 
     * 
     */
    public FormClientes(JPanel contenedor){
        
        // definimos las fuentes
        Fuentes Fuente = new Fuentes();
        
        // instanciamos la clase de eventos
        this.Eventos = new EventosClientes(this);
        
        // definimos el layout
        contenedor.setLayout(new BoxLayout(contenedor, BoxLayout.Y_AXIS));
        
        // agregamos el título
        JPanel pTitulo = new JPanel(new FlowLayout(FlowLayout.LEFT, 5, 5));
        JLabel lTitulo = new JLabel("Datos del Cliente");
        lTitulo.setFont(Fuente.Negrita);
        pTitulo.add(lTitulo);
        contenedor.add(pTitulo);
        
        // definimos la primer fila 
        JPanel fila1 = new JPanel(new FlowLayout(FlowLayout.LEFT, 5, 5));
        
        // agregamos la clave
        JLabel lId = new JLabel("Id:");
        lId.setFont(Fuente.Normal);
        fila1.add(lId);
        this.tId = new JTextField();
        this.tId.setFont(Fuente.Normal);
        this.tId.setToolTipText("Clave del registro");
        this.tId.setPreferredSize(new Dimension(40,30));
        this.tId.setEditable(false);
        fila1.add(this.tId);
        
        // agregamos el nombre 
        JLabel lNombre = new JLabel("Nombre:");
        lNombre.setFont(Fuente.Normal);
        fila1.add(lNombre);
        this.tNombre = new JTextField();
        this.tNombre.setFont(Fuente.Normal);
        this.tNombre.setToolTipText("Nombre compledo del cliente");
        this.tNombre.setPreferredSize(new Dimension(290, 30));
        fila1.add(this.tNombre);
        
        // agregamos la dirección 
        JLabel lDireccion = new JLabel("Dirección:");
        lDireccion.setFont(Fuente.Normal);
        fila1.add(lDireccion);
        this.tDireccion = new JTextField();
        this.tDireccion.setFont(Fuente.Normal);
        this.tDireccion.setToolTipText("Dirección postal del cliente");
        this.tDireccion.setPreferredSize(new Dimension(290,30));
        fila1.add(this.tDireccion);
        
        // agregamos la fila al contenedor
        contenedor.add(fila1);
        
        // definimos la segunda fila 
        JPanel fila2 = new JPanel(new FlowLayout(FlowLayout.LEFT, 5, 5));
        
        // agregamos la id tributaria
        JLabel lIdTributaria = new JLabel("Id Tributaria:");
        lIdTributaria.setFont(Fuente.Normal);
        fila2.add(lIdTributaria);
        this.tIdTributaria = new JTextField();
        this.tIdTributaria.setFont(Fuente.Normal);
        this.tIdTributaria.setToolTipText("Clave tributaria del cliente");
        this.tIdTributaria.setPreferredSize(new Dimension(130,30));
        fila2.add(this.tIdTributaria);
        
        // agregamos el mail 
        JLabel lMail = new JLabel("Mail:");
        lMail.setFont(Fuente.Normal);
        fila2.add(lMail);
        this.tMail = new JTextField();
        this.tMail.setFont(Fuente.Normal);
        this.tMail.setToolTipText("Correo electrónico del cliente");
        this.tMail.setPreferredSize(new Dimension(200,30));
        fila2.add(this.tMail);
        
        // agregamos el teléfono 
        JLabel lTelefono = new JLabel("Teléfono:");
        lTelefono.setFont(Fuente.Normal);
        fila2.add(lTelefono);
        this.tTelefono = new JTextField();
        this.tTelefono.setFont(Fuente.Normal);
        this.tTelefono.setToolTipText("Teléfono del cliente");
        this.tTelefono.setPreferredSize(new Dimension(120,30));
        fila2.add(this.tTelefono);
        
        // la fecha de alta
        JLabel lAlta = new JLabel("Alta:");
        lAlta.setFont(Fuente.Normal);
        fila2.add(lAlta);
        this.tFecha = new JTextField();
        this.tFecha.setToolTipText("Fecha de alta del registro");
        this.tFecha.setPreferredSize(new Dimension(90,30));
        this.tFecha.setEditable(false);
        fila2.add(this.tFecha);
        
        // agregamos el panel al contenedor
        contenedor.add(fila2);
        
        // definimos el panel de los botones
        JPanel fila3 = new JPanel(new FlowLayout(FlowLayout.RIGHT, 5, 5));
        
        // agregamos el botón grabar
        JButton btnGrabar = new JButton("Grabar");
        btnGrabar.setFont(Fuente.Normal);
        btnGrabar.setToolTipText("Graba el registro en la base");
        btnGrabar.setPreferredSize(new Dimension(120, 30));
        Icon icon1 = new ImageIcon(getClass().getResource("/imagenes/grabar.png"));
        btnGrabar.setIcon(icon1);
        btnGrabar.addActionListener(e -> Eventos.verificaCliente());
        fila3.add(btnGrabar);
        
        // agregamos el botón cancelar
        JButton btnCancelar = new JButton("Cancelar");
        btnCancelar.setFont(Fuente.Normal);
        btnCancelar.setToolTipText("Reinicia el formulario");
        btnCancelar.setPreferredSize(new Dimension(120, 30));
        Icon icon2 = new ImageIcon(getClass().getResource("/imagenes/cancelar.png"));
        btnCancelar.setIcon(icon2);
        btnCancelar.addActionListener(e -> Eventos.cancelaCliente());
        fila3.add(btnCancelar);
        
        // agregamos la fila al contenedor
        contenedor.add(fila3);
        
    }
    
    /**
     * 
     * @author Claudio Invernizzi <cinvernizzi@dsgestion.site>
     * 
     * Método llamado al pulsar sobre el botón nuevo en la grilla de 
     * clientes, solo invoca el método 
     * 
     */
    public void nuevoCliente(){

        // invocamos el método
        this.Eventos.nuevoCliente();

    }

    /**
     * 
     * @author Claudio Invernizzi <cinvernizzi@dsgestion.site>
     * 
     * @param idcliente - entero con la clave del registro
     * 
     * Método llamado al pulsar sobre la grilla de clientes 
     * que recibe como parámetro la clave del registro, 
     * simplemente invoca el evento
     * 
     */
    public void getDatosCliente(int idcliente){

        // invocamos 
        this.Eventos.getDatosCliente(idcliente);

    }
    
}
