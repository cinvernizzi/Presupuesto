/**
 * 
 * @author Claudio Invernizzi <cinvernizzi@dsgestion.site>
 * @date 27/10/2025
 * @name EventosSecciones
 * @Projecto: Presupuesto
 * @Copyright DsGestion <dsgestion.site>
 * @Licence: GPL
 * Clase que implementa los métodos de la grilla de secciones 
 * de un presupuesto
 * 
 */

// declaración del paquete
package site.dsgestion.secciones;

// importamos las librerías
import java.sql.ResultSet;
import java.sql.SQLException;
import javax.swing.ImageIcon;
import javax.swing.JLabel;
import javax.swing.table.DefaultTableModel;
import javax.swing.table.TableRowSorter;
import site.dsgestion.dbApi.Mensaje;
import site.dsgestion.dbApi.RendererTabla;

/**
 * 
 * @author Claudio Invernizzi <cinvernizzi@dsgestion.site>
 * 
 * Declaración de la clase
 */
public class EventosSecciones {

    // declaración de variables
    protected DbSecciones Secciones;
    protected GrillaSecciones Formulario;

    /**
     * 
     * @author Claudio Invernizzi <cinvernizzi@dsgestion.site>
     * 
     * @param formulario - el formulario de secciones 
     * 
     * Constructor de la clase, instanciamos la conexión con 
     * la base, recibe como parámetro el formulario de secciones
     * 
     */
    public EventosSecciones(GrillaSecciones formulario){

        // instanciamos la clase y asignamos
        this.Secciones = new DbSecciones();
        this.Formulario = formulario;

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

        // obtenemos el modelo de la tabla
        DefaultTableModel modeloTabla = (DefaultTableModel) this.Formulario.tSecciones.getModel();

        // obtenemos la fila y columna pulsados
        int fila = this.Formulario.tSecciones.rowAtPoint(evt.getPoint());
        int columna = this.Formulario.tSecciones.columnAtPoint(evt.getPoint());

        // como tenemos la tabla ordenada nos aseguramos de convertir
        // la fila pulsada (vista) a la fila de datos (modelo)
        int indice = this.Formulario.tSecciones.convertRowIndexToModel (fila);

        // si se pulsó dentro de la tabla 
        if (fila > -1) {

			// obtenemos el protocolo
			int id = (Integer) modeloTabla.getValueAt(indice, 0);
			
            // si se pulsó en editar
            if (columna == 4){
                this.editaSeccion(id);
            } else if (columna == 5){
                this.borraSeccion(id);
            }

		}

    }

    /**
     * 
     * @author Claudio Invernizzi <cinvernizzi@dsgestion.site>
     * 
     * @param idseccion - clave de la sección 
     * 
     * Método que recibe como parámetro la clave de una sección
     * verifica que no tenga registros hijos y ejecuta la consulta
     * de eliminación 
     * 
     */
    protected void borraSeccion(int idseccion){

        // primero verificamos si puede eliminar
        boolean autorizado = this.Secciones.puedeBorrar(idseccion);

        // si puede eliminar 
        if (autorizado){

            // eliminamos
            boolean resultado = this.Secciones.borraSeccion(idseccion);

            // si pudo eliminar
            if (resultado){

                // presenta el mensaje y recarga la grilla
                new Mensaje("Registro eliminado ... ");
                this.cargaSecciones();

            // si ocurrió un error
            } else {

                // presenta el mensaje
                new Mensaje("Ha ocurrido un error .... ");

            }

        // si la sección tiene registros hijos
        } else {

            // presenta el mensaje
            new Mensaje("El registro tiene hijos ... ");

        }
        
    }

    /**
     * 
     * @author Claudio Invernizzi <cinvernizzi@dsgestion.site>
     * 
     * @param idseccion clave de la sección 
     * 
     * Método que recibe como parámetro la clave de una sección 
     * y abre el diálogo emergente presentando el registro 
     * 
     */
    protected void editaSeccion(int idseccion){

    }

    /**
     * 
     * @author Claudio Invernizzi <cinvernizzi@dsgestion.site>
     * 
     * Método llamado al pulsar el botón nueva sección que 
     * abre el diálogo emergente para el alta de un nuevo 
     * registro
     * 
     */
    protected void nuevaSeccion(){

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
        this.Formulario.tSecciones.setDefaultRenderer(Object.class, new RendererTabla());

        // obtenemos el modelo de la tabla
        DefaultTableModel modeloTabla = (DefaultTableModel)this.Formulario.tSecciones.getModel();

    	// hacemos la tabla se pueda ordenar
		this.Formulario.tSecciones.setRowSorter (new TableRowSorter<DefaultTableModel>(modeloTabla));

        // limpiamos la tabla
        modeloTabla.setRowCount(0);

        // definimos las imágenes
        ImageIcon editar = new ImageIcon(getClass().getResource("/imagenes/editar.png"));
        ImageIcon eliminar = new ImageIcon(getClass().getResource("/imagenes/cancelar.png"));
        
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
                fila[4] = new JLabel(editar);
                fila[5] = new JLabel(eliminar);

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
