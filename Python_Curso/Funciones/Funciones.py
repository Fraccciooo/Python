# Se utiliza una varible general vacia, para almacenar un valor digitado por el usuario

nombre = ""

# Se usa el "\n" para hacer un salto de linea
def saludo(nombre):
    print(f"Buenos dias, {nombre}... Lo estas haciendo increible!!! \nNO TE RINDAS")

nombre = input("Digita tu nombre: ")
saludo(nombre)