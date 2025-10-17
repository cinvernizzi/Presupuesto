# este target genera el archivo ejecutable
build:
	echo "Removiendo Basura"
	rm -rf build
	rm -rf dist
	echo "Generando Ejecutable ..."
	# en el caso de linux usamos el compilador gcc
	nuitka --onefile --standalone --enable-plugin=pyside6 --windows-icon-from-ico="recursos/logo.png" Presupuesto.py
	# en el caso de windows nos conviene usar el mingw64 con el plugin clang porque
	# si instalamos el visual c para que no de errores ocupa 20 GB de disco
	# el windows defender
	# la versión de Python recomendada es la 3.10 la 3.11 solo tiene soporte experimental
	# y la versión 3.12 no es soportada
	# nuitka --onefile --standalone --mingw64 --clang --windows-console-mode=enable main.py

# este target limpia la basura del sistema
clean:
	echo "Limpiando estructura ..."
	rm -rf build
	rm -rf dist
	rm -rf clases/__pycache__
	rm -rf sql/__pycache__
	