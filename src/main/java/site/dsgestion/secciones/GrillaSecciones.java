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
import javax.swing.table.TableRowSorter;
import java.awt.Dimension;
import java.awt.FlowLayout;
import java.awt.Image;
import java.awt.Toolkit;
import java.sql.ResultSet;
import java.sql.SQLException;
import javax.swing.BoxLayout;
import javax.swing.ImageIcon;
import site.dsgestion.dbApi.Fuentes;
import site.dsgestion.dbApi.RendererTabla;

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

    /**
     * 
     * @author Claudio Invernizzi <cinvernizzi@dsgestion.site>
     * 
     * Constructor de la clase
     * 
     */
    public GrillaSecciones(){

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

        // instanciamos la clase
        this.Secciones = new DbSecciones();

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
				false, false, false, false, false, false
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
                tSeccionesMouseClicked(evt);
            }
        });

        // cargamos los registros 
        this.cargaSecciones();

        // agregamos el scroll al contenedor
        Contenedor.add(scrollSecciones);

        // agregamos el contenedor al formulario
        this.add(Contenedor);

        // mostramos el formulario 
        this.setVisible(true);

    }

    /**
     * 
     * @author Claudio Invernizzi <cinvernizzi@dsgestion.site>
     * 
     * @param evt el evento del mouse
     * 
     * Método llamado al pulsar sobre un registro que recibe como 
     * parámetro el evento del mouse
     * 
     */
    protected void tSeccionesMouseClicked(java.awt.event.MouseEvent evt){

    }

    /**
     * 
     * @author Claudio Invernizzi <cinvernizzi@dsgestion.site>
     * 
     * Método llamado desde el constructor o luego de grabar un registro
     * que carga la nómina de secciones
     * 
     */
    public void cargaSecciones(){

        // obtenemos la nómina 
        ResultSet Nomina = this.Secciones.nominaSecciones();

        // sobrecargamos el renderer de la tabla
        this.tSecciones.setDefaultRenderer(Object.class, new RendererTabla());

        // obtenemos el modelo de la tabla
        DefaultTableModel modeloTabla = (DefaultTableModel)this.tSecciones.getModel();

    	// hacemos la tabla se pueda ordenar
		this.tSecciones.setRowSorter (new TableRowSorter<DefaultTableModel>(modeloTabla));

        // limpiamos la tabla
        modeloTabla.setRowCount(0);

        // definimos el objeto de las filas
        Object [] fila = new Object[6];

        try {

            // iniciamos un bucle recorriendo el vector
            while (Nomina.next()){

                // fijamos los valores de la fila
                fila[0] = Nomina.getInt("id");
                fila[1] = Nomina.getInt("orden");
                fila[2] = Nomina.getString("etapa");
				fila[3] = Nomina.getString("fecha");
                fila[4] = new JLabel(new ImageIcon(getClass().getResource("/imagenes/editar.png")));
                fila[5] = new JLabel(new ImageIcon(getClass().getResource("/imagenes/cancelar.png")));

                // lo agregamos
                modeloTabla.addRow(fila);

            }

        // si hubo un error
        } catch (SQLException ex){

            // presenta el mensaje
            System.out.println(ex.getMessage());

        }

    }

}
