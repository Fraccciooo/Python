import shutil

try:
    shutil.copyfile("texto_2.txt", "text_copy.txt")
    print("Archivo copiado exitosamente.")
except FileNotFoundError:
    print("El archivo no se encontró.")
except Exception as e:
    print("Ocurrió un error:", e)