import math

# Las listas no solo almacenan nombres (STRINGS), tambien almacenan datos numericos
# y booleanos
comida = ['Pizza', 'Hamburguesa', 'Perro Caliente']
numericos = [0.5, 25.7, 3.14, 54]

# Funciones mas usadas

print(comida.append('Helado')) # Inserte este elemento en la lista
print(comida.remove('Hamburguesa')) # Elimina el elemento que queramos 
print(comida.pop()) # Elimina el ultimo valor de la lista
print(comida.insert(0, 'Torta')) # Insertamos un elemento en la posicion cero (0)
print(comida.sort()) # Ordena de manera alfabetica la lista que queramos
print(comida.clear()) # Limpia toda la lista que queramos

print(numericos.append(35)) # Inserte este elemento en la lista
print(numericos.remove(0.5)) # Elimina el elemento que queramos 
print(numericos.pop()) # Elimina el ultimo valor de la lista
print(numericos.insert(0, 2002)) # Insertamos un elemento en la posicion cero (0)
print(numericos.sort()) # Ordena de manera alfabetica la lista que queramos
print(numericos.clear()) # Limpia toda la lista que queramos

for i in comida:
    print(i)