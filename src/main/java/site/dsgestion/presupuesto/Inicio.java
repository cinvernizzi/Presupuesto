/**
 * 
 * @author Claudio Invernizzi <cinvernizzi@dsgestion.site>
 * @date 21/01/2026
 * @name App
 * @Projecto: Presupuesto
 * @Copyright DsGestion <dsgestion.site>
 * @Licence: GPL
 * Método principal que verifica la existencia de las 
 * bases de datos e inicializa la interfaz
 * 
 */

// definimos el paquete
package site.dsgestion.presupuesto;

// importamos las librerías
import java.awt.*;
import javax.swing.*;

/**
 * 
 * @author Claudio Invernizzi <cinvernizzi@dsgestion.site>
 * 
 * Declaración de la clase
 * 
 */
public class Inicio extends JFrame{

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

        // fijamos el tamaño
        setSize(1000, 650);

        // podemos redimensionar
        setResizable(true);

        // fijamos el título
        setTitle("Cálculo de Presupuestos");

        // fijamos el evento por defecto al cerrar
        setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);

        // centramos la ventana
        Toolkit miPantalla = Toolkit.getDefaultToolkit();
        Dimension tamanioPantalla = miPantalla.getScreenSize();

        // ahora lo convertimos a alto y ancho
        int ancho = tamanioPantalla.width;
        int alto = tamanioPantalla.height;

        // y ahora lo movemos para centrarlo
        setLocation((ancho - 1000)/2, (alto - 650)/2);

        // fijamos el ícono
        Image icono = new ImageIcon(getClass().getResource("/imagenes/logo.png")).getImage();
        setIconImage(icono);

        // mostramos el formulario 
        setVisible(true);

    }

}
