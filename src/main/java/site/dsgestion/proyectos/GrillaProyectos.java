/**
 * 
 * @author Claudio Invernizzi <cinvernizzi@dsgestion.site>
 * @date 23/01/2026
 * @name GrillaProyectos
 * @Projecto: Presupuesto
 * @Copyright DsGestion <dsgestion.site>
 * @Licence: GPL
 * Clase que configura la grilla con la nómina de proyectos
 * 
 */

// definimos el paquete
package site.dsgestion.proyectos;

// importamos las librerías
import java.awt.*;
import javax.swing.*;
import site.dsgestion.dbApi.Fuentes;

/**
 *
 * @author Claudio Invernizzi <cinvernizzi@dsgestion.site>
 * 
 * Declaración de la clase
 * 
 */
public class GrillaProyectos {
   
    // declaración de controles
    public JTextField tFiltroProyectos;
    
    /**
     * 
     * @author Claudio Invernizzi <cinvernizzi@dsgestion.site>
     * 
     * @param contenedor panel contenedor 
     * 
     * Constructor de la clase, recibe como parámetro el panel 
     * contenedor donde agregan los componentes
     * 
     */
    public GrillaProyectos(JPanel contenedor){

        // definimos las fuentes
        Fuentes Fuente = new Fuentes();
        
        // definimos el layout
        contenedor.setLayout(new BoxLayout(contenedor, BoxLayout.Y_AXIS));
        
        // agregamos el título
        JPanel pTitulo = new JPanel(new FlowLayout(FlowLayout.LEFT, 5, 5));        
        JLabel lTitulo = new JLabel("Proyectos del Cliente");
        lTitulo.setFont(Fuente.Negrita);
        pTitulo.add(lTitulo);
        contenedor.add(pTitulo);
        
        // definimos la primer fila 
        JPanel fila1 = new JPanel(new FlowLayout(FlowLayout.LEFT, 5, 5));
        
        // agregamos el filtro
        JLabel lProyecto = new JLabel("Proyecto:");
        lProyecto.setFont(Fuente.Normal);
        fila1.add(lProyecto);
        this.tFiltroProyectos = new JTextField();
        this.tFiltroProyectos.setFont(Fuente.Normal);
        this.tFiltroProyectos.setToolTipText("Ingrese un texto para filtrar");
        this.tFiltroProyectos.setPreferredSize(new Dimension(250, 30));
        fila1.add(this.tFiltroProyectos);
        
        // el botón agregar
        JButton btnNuevo = new JButton("Nuevo");
        btnNuevo.setFont(Fuente.Normal);
        btnNuevo.setToolTipText("Pulse para agregar un proyecto");
        btnNuevo.setPreferredSize(new Dimension(120,30));
        Icon icon1 = new ImageIcon(getClass().getResource("/imagenes/nuevo.png"));
        btnNuevo.setIcon(icon1);
        fila1.add(btnNuevo);
        
        // agregamos la fila al contenedor
        contenedor.add(fila1);
        
    }
    
}
