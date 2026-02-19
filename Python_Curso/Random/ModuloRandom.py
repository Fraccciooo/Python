import random

# El modulo random se utiliza para generar numeros aleatorios, 
# o para seleccionar elementos de una lista de forma aleatoria
numero = random.randint(1, 100)
print("Numero aleatorio generado:", numero)

# Seleccionar un elemento aleatorio de una lista
colores = ["rojo", "verde", "azul", "amarillo"]
color = random.choice(colores)
print("Color aleatorio seleccionado:", color)

# Mezclar una lista de forma aleatoria
numeros = [1, 2, 3, 4, 5]
random.shuffle(numeros)
print("Lista mezclada de forma aleatoria:", numeros)

# Generar un numero aleatorio entre 0 y 1
decimal = random.random()
print("Numero decimal aleatorio entre 0 y 1:", decimal)

# Generar un numero aleatorio con una distribucion normal
media = 0
desviacion_estandar = 1
normal = random.gauss(media, desviacion_estandar)
print("Numero aleatorio con distribucion normal:", normal)

# Mezcla una cantidad de variables contenidos en una lista
variables = [color, numero, decimal, normal]
random.shuffle(variables)
print("Variables mezcladas de forma aleatoria:", variables)