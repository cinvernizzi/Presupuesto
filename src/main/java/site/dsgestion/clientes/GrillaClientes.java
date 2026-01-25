/**
 * 
 * @author Claudio Invernizzi <cinvernizzi@dsgestion.site>
 * @date 23/01/2026
 * @name GrillaClientes
 * @Projecto: Presupuesto
 * @Copyright DsGestion <dsgestion.site>
 * @Licence: GPL
 * Clase que configura la grilla de clientes 
 * 
 */

// definimos el paquete
package site.dsgestion.clientes;

// importamos las librerías
import java.awt.*;
import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;
import javax.swing.*;
import javax.swing.table.DefaultTableModel;
import site.dsgestion.dbApi.Fuentes;


/**
 *
 * @author Claudio Invernizzi <cinvernizzi@dsgestion.site>
 * 
 * Definición de la clase
 * 
 */
public class GrillaClientes {
   
    // declaramos los objetos 
    public JTextField tFiltro;
    public JTable tClientes;
    protected EventosGrillaClientes Eventos;
    
    /**
     * 
     * @author Claudio Invernizzi <cinvernizzi@dsgestion.site>
     * 
     * @param contenedor el panel contenedor 
     * 
     * Método que configura la grilla de clientes, recibe como 
     * parámetro el panel contenedor de la grilla 
     * 
     */
    public GrillaClientes(JPanel contenedor){
        
        // instanciamos la clase de eventos
        this.Eventos = new EventosGrillaClientes(this);
        
        // configuramos el layout
        contenedor.setLayout(new BoxLayout(contenedor, BoxLayout.Y_AXIS));

        // definimos las fuentes
        Fuentes Fuente = new Fuentes();
        
        // agregamos el título
        JLabel lTitulo = new JLabel("Clientes");
        lTitulo.setFont(Fuente.Normal);
        contenedor.add(lTitulo);
        
        // definimos un panel para los filtros
        JPanel panelFiltros = new JPanel(new FlowLayout(FlowLayout.LEFT, 5, 5));
        
        // definimos el texto a buscar
        this.tFiltro = new JTextField();
        this.tFiltro.setFont(Fuente.Normal);
        this.tFiltro.setToolTipText("Ingrese parte del nombre del cliente");
        this.tFiltro.setPreferredSize(new Dimension(200, 30));
        panelFiltros.add(this.tFiltro);
        
        // agregamos el evento keypress
        this.tFiltro.addKeyListener(new KeyAdapter() {
            @Override
            public void keyTyped(KeyEvent e) {
                Eventos.cargaClientes();
            }           
        });

        // el botón nuevo 
        JButton btnNuevo = new JButton();
        btnNuevo.setFont(Fuente.Normal);
        btnNuevo.setToolTipText("Ingresa un nuevo cliente");
        btnNuevo.setPreferredSize(new Dimension(30, 30));
        Icon icon1 = new ImageIcon(getClass().getResource("/imagenes/nuevo.png"));
        btnNuevo.setIcon(icon1);
        btnNuevo.addActionListener(e -> Eventos.nuevoCliente());
        panelFiltros.add(btnNuevo);
        
        // el botón configurar 
        JButton btnConfigurar = new JButton();
        btnConfigurar.setFont(Fuente.Normal);
        btnConfigurar.setToolTipText("Configura la aplicación");
        btnConfigurar.setPreferredSize(new Dimension(30, 30));
        ImageIcon icon2 = new ImageIcon(getClass().getResource("/imagenes/apoyo.png"));
        btnConfigurar.setIcon(icon2);   
        btnConfigurar.addActionListener(e -> Eventos.verConfiguracion());
        panelFiltros.add(btnConfigurar);
        
        // agregamos al contenedor
        contenedor.add(panelFiltros);

        // definimos un panel para la grilla
        JPanel panelGrilla = new JPanel(new FlowLayout(FlowLayout.LEFT, 5, 5));
        
        // ahora definimos la grilla de clientes
        JScrollPane scrollClientes = new JScrollPane();
        scrollClientes.setPreferredSize(new Dimension(270, 480));

        // definimos la tabla de resultados
        this.tClientes = new JTable();
        this.tClientes.setModel(new DefaultTableModel(
            new Object[][] {
                    {null, null},
            },
            new String[] {
                    "Id",
                    "Nombre"
                }
            ) {
                @SuppressWarnings("rawtypes")
                Class[] columnTypes = new Class[] {
                        Integer.class,
                        String.class
                };
                @SuppressWarnings({ "unchecked", "rawtypes" })
                public Class getColumnClass(int columnIndex) {
                    return columnTypes[columnIndex];
                }
                boolean[] columnEditables = new boolean[] {
                        false, false
                };
                public boolean isCellEditable(int row, int column) {
                        return columnEditables[column];
                }
        });

        // fijamos el tooltip
        this.tClientes.setToolTipText("Pulse para seleccionar el cliente");

        // definimos la fuente
        this.tClientes.setFont(Fuente.Normal);

        // fijamos el ancho de las columnas
        this.tClientes.getColumn("Id").setMaxWidth(0);

        // fijamos el evento click
        this.tClientes.addMouseListener(new java.awt.event.MouseAdapter() {
            @Override
            public void mouseClicked(java.awt.event.MouseEvent evt) {
                Eventos.cargaCliente(evt);
            }
        });
        
        // agregamos la tabla al scroll
        scrollClientes.setViewportView(this.tClientes);
        
        // agregamos el scroll
        panelGrilla.add(scrollClientes);
        
        // agregamos el scroll al contenedor
        contenedor.add(panelGrilla);
        
        // cargamos la grilla de clientes
        Eventos.cargaClientes();
        
    }

    /**
     * 
     * @author Claudio Invernizzi <cinvernizzi@dsgestion.site>
     * 
     * Método que recibe como parámetro el formulario de clientes
     * y lo asigna a la variable de clase
     * 
     */
    public void setFormClientes(FormClientes formulario){

        // asignamos en los eventos
        this.Eventos.FormClientes = formulario;

    }

}
