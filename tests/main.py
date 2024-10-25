# Cuando hemos movido el archivo main a la carpeta test
# las rutas ya no son correctas

from ..src.kkpaqueteJoseMiguel import suma, resta
#from src/kkpaqueteJoseMiguel.extra import otras



print(suma.suma(1,2)) # Porque en el init tengo disponible esa función.
# Si no, tendríamos que hacer suma.suma(...)
#print(otras.multiplicacion(1,2))