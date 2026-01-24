/**
 * 
 * @author Claudio Invernizzi <cinvernizzi@dsgestion.site>
 * @date 23/01/2026
 * @name EventosGrillaClientes
 * @Projecto: Presupuesto
 * @Copyright DsGestion <dsgestion.site>
 * @Licence: GPL
 * Clase controla los eventos de la grilla de clientes
 * 
 */

// definimos el paquete
package site.dsgestion.clientes;

// importamos las librerías
import java.awt.event.MouseEvent;
import java.sql.ResultSet;
import java.sql.SQLException;
import javax.swing.table.DefaultTableModel;
import javax.swing.table.TableRowSorter;
import site.dsgestion.dbApi.RendererTabla;
import site.dsgestion.personal.FormPersonal;

/**
 *
 * @author Claudio Invernizzi <cinvernizzi@dsgestion.site>
 * 
 * Definición de la clase
 */
public class EventosGrillaClientes {
    
    // definimos la clase 
    protected DbClientes Clientes;
    protected GrillaClientes Formulario;
    
    /**
     * 
     * @author Claudio Invernizzi <cinvernizzi@dsgestion.site>
     * 
     * @param formulario - el formulario con la grilla
     * 
     * Constructor de la clase, recibe como parámetro el formulario
     * con la grilla 
     * 
     */
    public EventosGrillaClientes(GrillaClientes formulario){
        
        // asignamos en la clase
        this.Formulario = formulario;
        
        // instanciamos la clase
        this.Clientes = new DbClientes();
        
    }
       
    /**
     * 
     * @author Claudio Invernizzi <cinvernizzi@dsgestion.site>
     * 
     * Método llamado al pulsar el botón configuración que abre 
     * el diálogo de datos personales
     * 
     */
    public void verConfiguracion(){
        
        // instanciamos el formulario
        new FormPersonal();
        
    }
    
    /**
     * 
     * @author Claudio Invernizzi <cinvernizzi@dsgestion.site>
     * 
     * Método llamado al cargar la grilla o al pulsar una tecla
     * en el campo de filtro que obtiene el texto del campo y 
     * recarga la grilla con los clientes
     * 
     */
    public void cargaClientes(){

        // obtenemos el filtro
        String filtro = this.Formulario.tFiltro.getText();
        
        // obtenemos la nómina 
        ResultSet nomina = this.Clientes.nominaClientes(filtro);
        
        // sobrecargamos el renderer de la tabla
        this.Formulario.tClientes.setDefaultRenderer(Object.class, new RendererTabla());

        // obtenemos el modelo de la tabla
        DefaultTableModel modeloTabla = (DefaultTableModel)this.Formulario.tClientes.getModel();

    	// hacemos la tabla se pueda ordenar
        this.Formulario.tClientes.setRowSorter (new TableRowSorter<>(modeloTabla));

        // limpiamos la tabla
        modeloTabla.setRowCount(0);

        // definimos el objeto de las filas
        Object [] fila = new Object[8];

        try {

            // iniciamos un bucle recorriendo el vector
            while (nomina.next()){

                // fijamos los valores de la fila
                fila[0] = nomina.getInt("id");
                fila[1] = nomina.getString("nombre");

                // lo agregamos
                modeloTabla.addRow(fila);

            }

        // si hubo un error
        } catch (SQLException ex){

            // presenta el mensaje
            ex.printStackTrace();			

        }

    }
    
    /**
     * 
     * @author Claudio Invernizzi <cinvernizzi@dsgestion.site>
     * 
     * @param evt el evento del mouse
     * 
     * Método llamado al pulsar sobre la grilla que recibe el 
     * evento del mouse, obtiene la clave del registro y lo 
     * presenta
     * 
     */
    public void cargaCliente(MouseEvent evt){

        // obtenemos el modelo de la tabla
        DefaultTableModel modeloTabla = (DefaultTableModel) this.Formulario.tClientes.getModel();

        // obtenemos la fila y columna pulsados
        int fila = this.Formulario.tClientes.rowAtPoint(evt.getPoint());

        // como tenemos la tabla ordenada nos aseguramos de convertir
        // la fila pulsada (vista) a la fila de datos (modelo)
        int indice = this.Formulario.tClientes.convertRowIndexToModel (fila);

        // obtenemos la clave
        int idcliente = (Integer) modeloTabla.getValueAt(indice, 0);
        System.out.println(idcliente);
        
    }
    
}
