/**
 * 
 * @author Claudio Invernizzi <cinvernizzi@dsgestion.site>
 * @date 21/01/2026
 * @name Inicio
 * @Projecto: Presupuesto
 * @Copyright DsGestion <dsgestion.site>
 * @Licence: GPL
 * Clase llamada luego de verificar la exisencia de las bases de datos
 * que configura el frame principal de la aplicación
 * 
 */

// definimos el paquete
package site.dsgestion.presupuesto;

// importamos las librerías
import com.formdev.flatlaf.FlatLightLaf;
import java.awt.*;
import javax.swing.*;
import site.dsgestion.dbApi.Fuentes;
import site.dsgestion.clientes.GrillaClientes;
import site.dsgestion.clientes.FormClientes;
import site.dsgestion.proyectos.GrillaProyectos;

/**
 * 
 * @author Claudio Invernizzi <cinvernizzi@dsgestion.site>
 * 
 * Declaración de la clase
 * 
 */
public final class Inicio extends JFrame{

    // declaramsos el serial id
    private static final long serialVersionUID = 1L;

    /**
     * 
     * @author Claudio Invernizzi <cinvernizzi@dsgestion.site>
     * 
     * Constructor de la clase, instanciamos la interfaz
     * 
     */
    public Inicio(){

        // mejoramos el renderizado de fuentes, este código debe ir 
        // antes que cualquier comando swing
        System.setProperty("awt.useSystemAAFontSettings", "lcd");
        System.setProperty("swing.aatext", "true");
    
        // fijamos el tamaño
        this.setSize(1100, 650);

        // podemos redimensionar
        this.setResizable(true);

        // fijamos el título
        this.setTitle("Cálculo de Presupuestos");

        // fijamos el evento por defecto al cerrar
        this.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);

        // centramos la ventana
        Toolkit miPantalla = Toolkit.getDefaultToolkit();
        Dimension tamanioPantalla = miPantalla.getScreenSize();

        // ahora lo convertimos a alto y ancho
        int ancho = tamanioPantalla.width;
        int alto = tamanioPantalla.height;

        // y ahora lo movemos para centrarlo
        this.setLocation((ancho - 1000)/2, (alto - 650)/2);

        // fijamos el ícono
        Image icono = new ImageIcon(getClass().getResource("/imagenes/logo.png")).getImage();
        this.setIconImage(icono);

        // configuramos la interfaz
        this.setupUi();

        // mostramos el formulario 
        this.setVisible(true);

    }

    /**
     * 
     * @author Claudio Invernizzi <cinvernizzi@dsgestion.site>
     * 
     * Método llamado desdel el constructor que configura el layout
     * y los contenedores del formulario 
     * 
     */
    protected void setupUi(){

        // fijamos el laf
        FlatLightLaf.setup();
        
        // los controles serán rectangulares
        UIManager.put( "Button.arc", 0 );
        UIManager.put( "Component.arc", 0 );
        UIManager.put( "CheckBox.arc", 0 );
        UIManager.put( "ProgressBar.arc", 0 );

        // el tipo de flecha (triangle o chevron)
        UIManager.put( "Component.arrowType", "chevron" );
        
        // el tamaño de la sombra del control con foco
        UIManager.put( "Component.focusWidth", 1 );
        
        // muestra la barra de desplazamiento
        UIManager.put( "ScrollBar.showButtons", true );
        
        // muestra un separador en los tabuladores
        UIManager.put( "TabbedPane.showTabSeparators", true );

        // fijamos el layout
        this.setLayout(new BorderLayout());

        // instanciamos las fuentes
        Fuentes Fuente = new Fuentes();
        
        // definimos el contenedor del título
        JPanel pTitulo = new JPanel(new FlowLayout(FlowLayout.CENTER, 10, 10));
        
        // agregamos el título
        JLabel lTitulo = new JLabel("Gestión de Presupuestos");
        lTitulo.setFont(Fuente.Titulo);
        pTitulo.add(lTitulo);
        
        // agregamos al contenedor
        this.add(pTitulo, BorderLayout.NORTH);

        // definimos el contenedor de la lista de clientes
        JPanel grillaClientes = new JPanel();

        // configuramos el panel
        new GrillaClientes(grillaClientes);

        // lo agregamos al layout
        this.add(grillaClientes, BorderLayout.WEST);

        // definimos el contenedor del formulario y la grilla
        JPanel contenedorDatos = new JPanel();

        // definimos el layout del contenedor
        contenedorDatos.setLayout(new BoxLayout(contenedorDatos, BoxLayout.Y_AXIS));

        // definimos el panel del formulario de datos 
        JPanel formClientes = new JPanel();

        // configuramos el formulario de clientes
        new FormClientes(formClientes);
        
        // lo agregamos al panel contenedor
        contenedorDatos.add(formClientes);

        // definimos el panel de la grilla de proyectos
        JPanel grillaProyectos = new JPanel();

        // configuramos la grilla de proyectos 
        new GrillaProyectos(grillaProyectos);

        // lo agregamos al contenedor
        contenedorDatos.add(grillaProyectos);

        // agregamos el contenedor
        this.add(contenedorDatos, BorderLayout.CENTER);

        // el contenedor del pié 
        JPanel pPie = new JPanel(new FlowLayout(FlowLayout.CENTER, 10, 10));
        
        // definimos el pié de página
        JLabel lPie = new JLabel("Lic. Claudio Invernizzi cinvernizzi@dsgestion.site / http://dsgestion.site");
        lPie.setFont(Fuente.Chica);
        
        // lo agregamos 
        pPie.add(lPie);
        this.add(pPie, BorderLayout.SOUTH);

    }

}
