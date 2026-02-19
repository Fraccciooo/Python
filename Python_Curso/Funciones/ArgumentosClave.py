# Se utiliza un argumento unico (identificador unico) para poder darle un valor directo
# a cada argumento, sin importar el orden en el que se encuentren definidos en la funcion

def saludo(nombre, apellido, lenguaje):
    print(f"Buenos dias {nombre}  {apellido}, me alagra que estes aprendiendo {lenguaje}")

# Aqui se colocan los argumentos clave, es decir, 
# se le asigna un valor a cada argumento utilizando su identificador unico
saludo(nombre="Ignacio", apellido="Frachia", lenguaje="Python")