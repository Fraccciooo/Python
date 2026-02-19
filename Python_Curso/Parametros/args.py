def suma(a, b):
    return a + b

print(suma(2, 3)) # Se muestra el resultado de la suma, que es 5

# En el caso anterior se hace lo que se requiere, pero
# cuando se quiere añadir un tercer, cuarto o quinto elemento,
# ya se vuelve tedioso, colocando variable tras varible
# ahi es donde entrarn los "*args", que es una forma de decirle a la funcion que puede 
# recibir una cantidad indeterminada de argumentos, es decir, 
# que no se sabe cuantas variables se van
# a colocar, y que la funcion se encargara de sumarlas todas

def suma(*args): # El nomber "*args" puede cambiarse por cualquier otro
    # *cosas, *numeros, *valores, etc... 
    return sum(args)

print(suma(2, 3, 44, 23, -5)) # Se muestra el resultado de la suma, que es 5
print(suma(2, 3, 4)) # Se muestra el resultado de la suma, que es 9
print(suma(2, 3, 4, 5)) # Se muestra el resultado de la suma, que es 14