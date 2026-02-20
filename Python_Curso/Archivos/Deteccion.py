import os

path = "C:\\Users\\ignac\\OneDrive\\Desktop\\Lenguajes\\Python\\Python_Curso\\Archivos\\text.txt"
path_2 = "C:\\Users\\ignac\\OneDrive\\Desktop\\Lenguajes\\Python\\Python_Curso\\Archivos\\folder"

# Prueba con un archivo de texto
if os.path.exists(path):
    print("El archivo existe.")
    if os.path.isfile(path):
        print("Es un archivo.")
else:    
    print("El archivo no existe.")

# Prueba con un directorio
if os.path.exists(path_2):
    print("El archivo existe.")
    if os.path.isdir(path_2):
        print("Es un directorio.")
else:
    print("El archivo no existe.")