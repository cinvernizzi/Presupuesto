La plataforma utiliza las siguientes librerías que fueron instaladas usando conda

PyInstaller para la creación de ejecutables (ver makefile)
PySide6     para la implementación de la interfaz
xlsxwriter  para la generación de las hojas de cálculo

Está desarrollado en Python 3.11 ya que el soporte de para garantizar la compatibilidad
con los ejecutables generados

Sistema sencillo de gestión de presupuestos para un desarrollador Freelance

Lo he desarrollado porque tenía infinidad de presupuestos destinados a distintos clientes y 
realmente necesitaba alguna aplicación sencilla que me permitiera encontrar rápidamente la 
información, generar el presupuesto, actualizarlo, etc.

Si bien está orientado al desarrollo de software puede ser fácilmente adaptado a otras finalidades.

Ver la carpeta sql en la cual se describe la estructura de las distintas tablas

Consideraciones sobre el PyInstaller, funciona perfectamente en Linux pero al crearlo en 
Windows en este caso el Defender pone el ejecutable en cuarentena, he revisado la 
documentación y aparentemente se debe al empaquetado que realiza el PyInstaller

En el caso de Windows recomiendo utilizar el Nuitka que es un poco mas complejo pero 
el funcionamiento es distinto, traduce a C++ el código Python y luego genera el 
ejecutable (debemos tener instalado en Windows el Visual C o correr Nuitka con 
la opción --clang) en estos casos el ejecutable no da ningún tipo de error.

En Linux en cambio el uso de Nuitka es un poco mas completo y siempre he tenido 
problemas con las dependencias de las librerías
