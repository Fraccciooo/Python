# En este ejercicio, se muestra cómo manipular cadenas de caracteres 
# utilizando índices para extraer partes específicas de la cadena.
# La idea es que se cuenta desde el indice 0 (I) y termine en el indice 7 (o)
# pero el indice 7 no se incluye, por eso se obtiene "Ignacio" y no "Ignacio " 
# (con espacio al final)

nombre = "Ignacio Frachia"
primer_nombre = nombre[0:7] # El primer número indica el índice de inicio (inclusive) y el segundo número indica el índice de fin (exclusive)
apellido = nombre[8:15] # El primer número indica el índice de inicio (inclusive) y el segundo número indica el índice de fin (exclusive)
print("Primera forma de obtener el mismo resultado:")
print(primer_nombre)
print(apellido)
# ------------------------------------------------------------------------------------------------------------------------------

# Otra forma de obtener el mismo resultado 
# es omitiendo el índice de inicio o el índice de fin, dependiendo del caso.
print("Segunda forma de obtener el mismo resultado:")
primer_nombre = nombre[:7] # Si el índice de inicio es 0, se puede omitirlo
apellido = nombre[8:] # Si el índice de fin es el último índice de la cadena
print(primer_nombre)
print(apellido)

# ---------------------------------------------------------------------------------------------------------------------------------------
# Con esta manera, imprimimos la cadena saltandonos caracteres
nombre_dos = nombre
nombre_dos = nombre_dos[::2] # El primer número indica el índice de inicio (inclusive), el segundo número indica el índice de fin (exclusive) y el tercer número indica el paso (en este caso, 2)
print(nombre_dos) # Imprime "JnCrls" (se obtiene cada segundo

# ---------------------------------------------------------------------------------------------------------------------------------------
# Con esta manera, imprimimos la cadena al revés
nombre_tres = nombre
nombre_tres = nombre_tres[::-1] # El primer número indica el índice de inicio
# el segundo número indica el índice de fin (exclusive) 
# y el tercer número indica el paso (en este caso, -1)
print(nombre_tres) # Imprime "aihcarF oicangI" (se obtiene la cadena al revés)

# ---------------------------------------------------------------------------------------------------------------------------------------
