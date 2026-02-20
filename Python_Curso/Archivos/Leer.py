path = "C:\\Users\\ignac\\OneDrive\\Desktop\\Lenguajes\\Python\\Python_Curso\\Archivos\\text.txt"

try:
    with open(path, "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("El archivo no se encontró.")