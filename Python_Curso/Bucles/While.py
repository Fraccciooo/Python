# Este programa solicita al usuario que ingrese su nombre y lo muestra en pantalla. 
# Si el usuario no ingresa un nombre, se le volverá a solicitar hasta que lo haga.

nombre = ""

while not nombre or len(nombre) == 0:
    nombre = input("Ingresa tu nombre: ")

print(f"Tu nombre es: {nombre}")