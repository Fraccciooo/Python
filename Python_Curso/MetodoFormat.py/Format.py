# Antes de usar el metodo format(), se utilizaba 
# la concatenacion de cadenas para mostrar un mensaje,
nombre = "Ignacio"
apellido = "Frachia"
lenguaje = "Python"
print(f"Hola {nombre} {apellido}, estas aprendiendo {lenguaje}")

# Ejemplo de uso de format()
nombre = "Ignacio"
apellido = "Frachia"
lenguaje = "Python"
# Se resume en que se colocan las varibales al final para poder mostar el mensaje

print("Hola {} {}, estas aprendiendo {}".format(nombre, apellido, "Python"))

# Igualmente funciona sin usar variables, es decir, 
# se pueden colocar los valores directamente dentro del metodo format()
print("Hola {} {}, estas aprendiendo {}".format("Ignacio", "Frachia", "Python"))

# Por otro lado, se puede usar el indice en el que se encuentran las variables con el 
# metodo format(), es decir, se le asigna un numero a cada variable, 
# y luego se coloca ese numero dentro de los corchetes para mostrar el mensaje
print("Hola {0} {1}, estas aprendiendo {2}".format(nombre, apellido, lenguaje))
