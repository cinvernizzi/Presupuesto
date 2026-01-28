/**
 * 
 * @author Claudio Invernizzi <cinvernizzi@dsgestion.site>
 * @date 23/10/2025
 * @name GrillaSecciones
 * @Projecto: Presupuesto
 * @Copyright DsGestion <dsgestion.site>
 * @Licence: GPL
 * Clase que implementa la grilla con las secciones de un 
 * presupuesto
 * 
 */

// definición del paquete
package site.dsgestion.secciones;

// importamos las librerías
import javax.swing.JDialog;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JTable;
import javax.swing.table.DefaultTableModel;
import java.awt.Dimension;
import java.awt.FlowLayout;
import java.awt.Image;
import java.awt.Toolkit;
import javax.swing.BoxLayout;
import javax.swing.Icon;
import javax.swing.ImageIcon;
import javax.swing.JButton;
import site.dsgestion.dbApi.Fuentes;

/**
 * 
 * @author Claudio Invernizzi <cinvernizzi@dsgestion.site>
 * 
 * Definición de la clase
 * 
 */
public class GrillaSecciones extends JDialog {

    // declaramos las variables
    protected JTable tSecciones;          // tabla con los datos
    protected DbSecciones Secciones;      // puntero a la base
    protected EventosSecciones Eventos;   // controlador de eventos

    /**
     * 
     * @author Claudio Invernizzi <cinvernizzi@dsgestion.site>
     * 
     * Constructor de la clase
     * 
     */
    public GrillaSecciones(){

        // instanciamos los eventos
        this.Eventos = new EventosSecciones(this);

        // lo fijamos como modal
        this.setModal(true);
        
        // fijamos el tamaño
        this.setSize(450, 250);

        // podemos redimensionar
        this.setResizable(true);

        // fijamos el título
        this.setTitle("Secciones de un presupuesto");
        
        // centramos la ventana
        Toolkit miPantalla = Toolkit.getDefaultToolkit();
        Dimension tamanioPantalla = miPantalla.getScreenSize();

        // ahora lo convertimos a alto y ancho
        int ancho = tamanioPantalla.width;
        int alto = tamanioPantalla.height;

        // y ahora lo movemos para centrarlo
        this.setLocation((ancho - 450)/2, (alto - 350)/2);

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

        // fijamos modal
        this.setModal(true);

        // definimos las fuentes
        Fuentes Fuente = new Fuentes();

        // agregamos un panel y definimos el layout
        JPanel Contenedor = new JPanel();
        Contenedor.setLayout(new BoxLayout(Contenedor, BoxLayout.Y_AXIS));

        // definimos el título
        JPanel pTitulo = new JPanel(new FlowLayout(FlowLayout.LEFT, 5, 5));
        JLabel lTitulo = new JLabel("Secciones de un Presupuesto");
        lTitulo.setFont(Fuente.Negrita);
        pTitulo.add(lTitulo);

        // definimos el botón nuevo
        JButton btnNuevo = new JButton();
        btnNuevo.setFont(Fuente.Normal);
        btnNuevo.setToolTipText("Ingresa una nueva sección");
        btnNuevo.setPreferredSize(new Dimension(30, 30));
        Icon icon1 = new ImageIcon(getClass().getResource("/imagenes/nuevo.png"));
        btnNuevo.setIcon(icon1);
        btnNuevo.addActionListener(e -> Eventos.nuevaSeccion());
        pTitulo.add(btnNuevo);

        // agregamos la fila al contenedor
        Contenedor.add(pTitulo);

		// definimos el scroll
		JScrollPane scrollSecciones = new JScrollPane();

		// definimos la tabla 
		this.tSecciones = new JTable();
		this.tSecciones.setModel(new DefaultTableModel(
			new Object[][] {
				{null, null, null, null, null, null},
			},
			new String[] {
				"Id",
				"Orden",
				"Etapa",
				"Fecha",
				"Ed.",
				"El."
			}
		) {
			@SuppressWarnings("rawtypes")
			Class[] columnTypes = new Class[] {
				Integer.class,
				Integer.class,
				String.class,
				String.class,
                Object.class,
				Object.class
			};
			@SuppressWarnings({ "unchecked", "rawtypes" })
			public Class getColumnClass(int columnIndex) {
				return columnTypes[columnIndex];
			}
			boolean[] columnEditables = new boolean[] {
				false, true, true, false, false, false
			};
			public boolean isCellEditable(int row, int column) {
				return columnEditables[column];
			}
		});

		// fijamos el tooltip
		this.tSecciones.setToolTipText("Pulse para seleccionar el registro");

		// definimos la fuente
		this.tSecciones.setFont(Fuente.Normal);

		// fijamos el ancho de las columnas
		this.tSecciones.getColumn("Id").setMaxWidth(40);
		this.tSecciones.getColumn("Orden").setMaxWidth(60);
		this.tSecciones.getColumn("Etapa").setMaxWidth(180);
		this.tSecciones.getColumn("Fecha").setMaxWidth(85);
		this.tSecciones.getColumn("Ed.").setMaxWidth(30);
		this.tSecciones.getColumn("El.").setMaxWidth(30);

		// agregamos la tabla al scroll
		scrollSecciones.setViewportView(this.tSecciones);

        // fijamos el evento click
        this.tSecciones.addMouseListener(new java.awt.event.MouseAdapter() {
            public void mouseClicked(java.awt.event.MouseEvent evt) {
                Eventos.tSeccionesMouseClicked(evt);
            }
        });

        // cargamos los registros 
        this.Eventos.cargaSecciones();

        // agregamos el scroll al contenedor
        Contenedor.add(scrollSecciones);

        // agregamos el contenedor al formulario
        this.add(Contenedor);

        // mostramos el formulario 
        this.setVisible(true);

    }

}
