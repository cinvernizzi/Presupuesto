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
import javax.swing.*;
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
        
        // el botón nuevo 
        JButton btnNuevo = new JButton();
        btnNuevo.setFont(Fuente.Normal);
        btnNuevo.setToolTipText("Ingresa un nuevo cliente");
        btnNuevo.setPreferredSize(new Dimension(30, 30));
        Icon icon1 = new ImageIcon(getClass().getResource("/imagenes/nuevo.png"));
        btnNuevo.setIcon(icon1);
        panelFiltros.add(btnNuevo);
        
        // el botón configurar 
        JButton btnConfigurar = new JButton();
        btnConfigurar.setFont(Fuente.Normal);
        btnConfigurar.setToolTipText("Configura la aplicación");
        btnConfigurar.setPreferredSize(new Dimension(30, 30));
        ImageIcon icon2 = new ImageIcon(getClass().getResource("/imagenes/apoyo.png"));
        btnConfigurar.setIcon(icon2);          
        panelFiltros.add(btnConfigurar);
        
        // agregamos al contenedor
        contenedor.add(panelFiltros);
        
    }
    
}
