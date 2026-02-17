# Listas 2D: es una lista dentro de otra
# se puede visualizar como un bucle anidado

bebidas = ['cafe', 'refresco', 'te']
cena = ['pizza', 'Hamburguesa', 'Perro Caliente']
postre = ['torta', 'helado']

comidas = [bebidas, cena, postre]

print(comidas)
print(comidas[0]) # Imprime solo el indice 0 de cada lista
print(comidas[0][0]) # Imprime el primer indice de la primera lista