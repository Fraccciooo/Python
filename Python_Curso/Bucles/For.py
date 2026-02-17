elemento = [1, 2, 3, 4, 5]
i = 0
y = 1
nombre = ""

# Imprime los datos contenidos en la variables elementos.
for i in elemento:
    print(i)
    i += 1

# Imprime los numeoros del 50 al 100 uno tras otro.
for i in range(50, 100):
    print(i)
    i += 1

# En este caso va a ingresar los numeros del 50 al 100 de 5 en 5.
# 55, 60, 65, 70...
for i in range(50, 100, 5):
    print(i)
    i += 1

print("--------------LETRAS EN ORDEN-----------------")
# Imprime cada letra del nombre en una linea diferente.
nombre = input("Ingresa tu nombre: ")
for i in nombre:
    print(f"Letra: {i}")

print("--------------LETRAS AL REVES-----------------")
# Imprime las letras al reves
for i in range(len(nombre)-1, -1, -1):
    print(f"Letra: {nombre[i]}")

print("--------------NUMEROS AL REVES-----------------")
# Imprime los numeros del 1 al 10 al reves.
for i in range(10, 0, -1):
    print(i)