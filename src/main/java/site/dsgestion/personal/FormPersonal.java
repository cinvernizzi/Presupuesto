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

// definición del paquete
package site.dsgestion.personal;

// importamos las librerías
import java.awt.Dimension;
import java.awt.FlowLayout;
import java.awt.Image;
import java.awt.Toolkit;
import javax.swing.BoxLayout;
import javax.swing.Icon;
import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.JDialog;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JTextField;
import site.dsgestion.dbApi.Fuentes;

/**
 *
 * @author Claudio Invernizzi <cinvernizzi@dsgestion.site>
 * 
 * Definición de la clase
 * 
 */
public final class FormPersonal extends JDialog {
    
    // declaración de variables
    public JTextField tId;               // clave del registro
    public JTextField tNombre;           // nombre del usuario
    public JTextField tEmpresa;          // nombre fantasía de la empresa
    public JTextField tDireccion;        // dirección postal
    public JTextField tCuil;             // clave tributaria
    public JTextField tTelefono;         // número de teléfono
    public JTextField tMail;             // correo electrónico
    public JTextField tFecha;            // fecha de alta del registro
    public JButton btnLogo;              // botón con el logo
    protected EventosPersonal Eventos;   // clase de eventos
    
    /**
     * 
     * @author Claudio Invernizzi <cinvernizzi@dsgestion.site>
     * 
     * Constructor de la clase
     * 
     */
    public FormPersonal(){

        // instanciamos la clase de eventos
        this.Eventos = new EventosPersonal(this);

        // fijamos el tamaño
        this.setSize(850, 250);

        // podemos redimensionar
        this.setResizable(true);

        // fijamos el título
        this.setTitle("Datos Personales");
        
        // centramos la ventana
        Toolkit miPantalla = Toolkit.getDefaultToolkit();
        Dimension tamanioPantalla = miPantalla.getScreenSize();

        // ahora lo convertimos a alto y ancho
        int ancho = tamanioPantalla.width;
        int alto = tamanioPantalla.height;

        // y ahora lo movemos para centrarlo
        this.setLocation((ancho - 800)/2, (alto - 350)/2);

        // fijamos el ícono
        Image icono = new ImageIcon(getClass().getResource("/imagenes/logo.png")).getImage();
        this.setIconImage(icono);

        // configuramos la interfaz
        this.setupUi();
        
    }
    
    /**
     * 
     * @author Claudio Invernizzi <cinvernizzi@dsgestion.site>
     * 
     * Método llamado desde el constructor que configura la 
     * interfaz
     * 
     */
    protected void setupUi(){
    
        // definimos la fuente
        Fuentes Fuente = new Fuentes();
        
        // agregamos un panel contenedor
        JPanel contenedor = new JPanel();
        contenedor.setLayout(new BoxLayout(contenedor, BoxLayout.Y_AXIS));
        
        // presenta el título 
        JLabel lTitulo = new JLabel("Datos Personales");
        lTitulo.setFont(Fuente.Negrita);
        contenedor.add(lTitulo);
        
        // define la primer fila 
        JPanel fila1 = new JPanel(new FlowLayout(FlowLayout.LEFT, 5, 5));
        
        // presenta la clave del registro
        JLabel lId = new JLabel("Id:");
        lId.setFont(Fuente.Normal);
        fila1.add(lId);
        this.tId = new JTextField();
        this.tId.setFont(Fuente.Normal);
        this.tId.setToolTipText("Clave única del registro");
        this.tId.setPreferredSize(new Dimension(40,30));
        this.tId.setEditable(false);
        fila1.add(this.tId);
        
        // pide el nombre
        JLabel lNombre = new JLabel("Nombre:");
        lNombre.setFont(Fuente.Normal);
        fila1.add(lNombre);
        this.tNombre = new JTextField();
        this.tNombre.setFont(Fuente.Normal);
        this.tNombre.setToolTipText("Nombre como aparecerá en el presupuesto");
        this.tNombre.setPreferredSize(new Dimension(200,30));
        fila1.add(this.tNombre);
        
        // pide el nombre de la empresa
        JLabel lEmpresa = new JLabel("Empresa:");
        lEmpresa.setFont(Fuente.Normal);
        fila1.add(lEmpresa);
        this.tEmpresa = new JTextField();
        this.tEmpresa.setFont(Fuente.Normal);
        this.tEmpresa.setToolTipText("Nombre como aparecerá en el presupuesto");
        this.tEmpresa.setPreferredSize(new Dimension(200,30));
        fila1.add(this.tEmpresa);
        
        // pide la clave tributaria 
        JLabel lIdTributaria = new JLabel("Id Tributaria:");
        lIdTributaria.setFont(Fuente.Normal);
        fila1.add(lIdTributaria);
        this.tCuil = new JTextField();
        this.tCuil.setFont(Fuente.Normal);
        this.tCuil.setToolTipText("Indique su clave tributaria");
        this.tCuil.setPreferredSize(new Dimension(130,30));
        fila1.add(this.tCuil);
        
        // agrega la fila al contenedor
        contenedor.add(fila1);
        
        // define la segunda fila 
        JPanel fila2 = new JPanel(new FlowLayout(FlowLayout.LEFT, 5, 5));
        
        // pide la dirección 
        JLabel lDireccion = new JLabel("Dirección:");
        lDireccion.setFont(Fuente.Normal);
        fila2.add(lDireccion);
        this.tDireccion = new JTextField();
        this.tDireccion.setFont(Fuente.Normal);
        this.tDireccion.setToolTipText("Dirección que figura en el presupuesto");
        this.tDireccion.setPreferredSize(new Dimension(200, 30));
        fila2.add(this.tDireccion);

        // pide el teléfono 
        JLabel lTelefono = new JLabel("Teléfono:");
        lTelefono.setFont(Fuente.Normal);
        fila2.add(lTelefono);
        this.tTelefono = new JTextField();
        this.tTelefono.setFont(Fuente.Normal);
        this.tTelefono.setToolTipText("Número de teléfono que figura en el presupuesto");
        this.tTelefono.setPreferredSize(new Dimension(120,30));
        fila2.add(this.tTelefono);
        
        // pide el mail 
        JLabel lMail = new JLabel("Mail:");
        lMail.setFont(Fuente.Normal);
        fila2.add(lMail);
        this.tMail = new JTextField();
        this.tMail.setFont(Fuente.Normal);
        this.tMail.setToolTipText("Su dirección de correo electrónico");
        this.tMail.setPreferredSize(new Dimension(200,30));
        fila2.add(this.tMail);
        
        // presenta la fecha de alta
        JLabel lAlta = new JLabel("Alta:");
        lAlta.setFont(Fuente.Normal);
        fila2.add(lAlta);
        this.tFecha = new JTextField();
        this.tFecha.setFont(Fuente.Normal);
        this.tFecha.setToolTipText("Fecha de alta del registro");
        this.tFecha.setPreferredSize(new Dimension(90,30));
        this.tFecha.setEditable(false);
        fila2.add(this.tFecha);
        
        // agrega la segunda fila 
        contenedor.add(fila2);
        
        // define la tercer fila 
        JPanel fila3 = new JPanel(new FlowLayout(FlowLayout.RIGHT, 5, 5));        
        
        // presenta al botón con el logo
        this.btnLogo = new JButton();
        this.btnLogo.setFont(Fuente.Normal);
        this.btnLogo.setToolTipText("Pulse para cargar su logo");
        this.btnLogo.setPreferredSize(new Dimension(60,60));
        Icon icon1 = new ImageIcon(getClass().getResource("/imagenes/imagen_no_disponible.png"));
        this.btnLogo.setIcon(icon1);
        this.btnLogo.addActionListener(e -> Eventos.cargaLogo());
        fila3.add(this.btnLogo);
        
        // verifica si existe el logo
        this.Eventos.verificaLogo();
        
        // presenta el botón de secciones
        JButton btnSecciones = new JButton("Secciones");
        btnSecciones.setFont(Fuente.Normal);
        btnSecciones.setToolTipText("Configura las secciones del presupuesto");
        btnSecciones.setPreferredSize(new Dimension(120, 30));
        Icon icon2 = new ImageIcon(getClass().getResource("/imagenes/secciones.png"));
        btnSecciones.setIcon(icon2);
        btnSecciones.addActionListener(e -> Eventos.verSecciones());        
        fila3.add(btnSecciones);
        
        // el botón grabar
        JButton btnGrabar = new JButton("Grabar");
        btnGrabar.setFont(Fuente.Normal);
        btnGrabar.setToolTipText("Graba el registro en la base");
        btnGrabar.setPreferredSize(new Dimension(120, 30));
        Icon icon3 = new ImageIcon(getClass().getResource("/imagenes/grabar.png"));
        btnGrabar.setIcon(icon3);
        btnGrabar.addActionListener(e -> Eventos.verificaPersonal());        
        fila3.add(btnGrabar);
        
        // el botón cancelar
        JButton btnCancelar = new JButton("Cancelar");
        btnCancelar.setFont(Fuente.Normal);
        btnCancelar.setToolTipText("Reinicia el formulario");
        btnCancelar.setPreferredSize(new Dimension(120, 30));
        Icon icon4 = new ImageIcon(getClass().getResource("/imagenes/cancelar.png"));
        btnCancelar.setIcon(icon4);
        btnCancelar.addActionListener(e -> Eventos.cancelaPersonal());
        fila3.add(btnCancelar);
        
        // agrega la tercer fila
        contenedor.add(fila3);

        // agregamos el panel
        this.add(contenedor);
        
        // mostramos el formulario
        this.setVisible(true);
        
    }
    
}
