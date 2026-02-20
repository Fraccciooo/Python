import os

origen = "texto_2.txt"
destino = "folder/texto_2.txt"

try:
    os.rename(origen, destino)
    print("Archivo movido exitosamente.")
except FileNotFoundError:
    print("El archivo no se encontró.")
except Exception as e:
    print("Ocurrió un error:", e)