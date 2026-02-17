# Los bucles anidados requieren de que se pueda usar dos iterables
# En el cual, se entienden entre si, cuando uno termina una condicion,
# el otro empieza a realizar su iteracion

fila = int(input("¿Cuantas filas desea? "))
columnas = int(input("¿Cuantas columnas desea? "))
simbolo = input("¿Que simbolo desea usar? ")
i = 0
j = 0

# En este caso, la logica se aplica en el que, cuando el iterable "J", termine de iterar una vez
# se ejecuta el iterable "I", y asi sucesivamente, 
# hasta que ambos iterables terminen de iterar, en este caso, se termina el bucle dependiendo
# de cuantas filas y columnas haya ingresado el usuario.

for i in range(fila):
    for j in range(columnas):
        print(f"{simbolo}", end="")
    print()  # Se usa un salto de línea después de cada fila 