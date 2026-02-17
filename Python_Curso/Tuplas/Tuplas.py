# Las tuplas son colecciones ordenable e inamobiles, no se pueden modificar

estudiantes = ('Ignacio', 24, 'M')

print(estudiantes.count('Alex')) # Imprime la cantidad de veces que existe ese elemento
print(estudiantes.index('M')) # Imprime el numoer de indices de dicho elemento

# Mostrar el contenido de una tupla

for i in estudiantes:
    print(i)

if 'Ignacio' in estudiantes:
    print("Ignacio esta presente! NO... TE... RINDAS...")