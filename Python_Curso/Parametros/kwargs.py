def hola(nombre, apellido, lenguaje):
    print(f"Hola {nombre} {apellido}, me alegra que estes aprendiendo {lenguaje}")

# Aqui se colocan los argumentos clave, es decir,
# se le asigna un valor a cada argumento utilizando su identificador unico
hola(nombre="Ignacio", apellido="Frachia", lenguaje="Python")

# Al igual que los "*args", se puede cambiar el nombre por cualquier otro
# ejemplo: **biblioteca **cocina, **cuarto, **casa

def hola2(**kwargs):
    print(f"Hola {kwargs['nombre']} {kwargs['apellido']}, estes aprendiendo {kwargs['lenguaje']} brother jejejej")
    # Se pueden agregar más argumentos sin problemas
    if 'edad' in kwargs:
        print(f"Tu edad es {kwargs['edad']}")
    if 'pais' in kwargs:
        print(f"Tu pais es {kwargs['pais']}")
        print(f"Tu ciudad es {kwargs['ciudad']}")

hola2(nombre="Ignacio", apellido="Frachia", lenguaje="Python", edad=25, pais="Argentina", ciudad="Buenos Aires")
