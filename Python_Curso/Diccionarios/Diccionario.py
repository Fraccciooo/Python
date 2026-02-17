# Es un conjunto de datos almacenados por clave/valor
# En este ejemplo se almacenan los paises como paises y como valor el estado

capitales = {'Estados Uiidos': 'Washington D.C',
            'Argentina': 'Buenos Aires',
            'Brasil': 'Brasilia',
            'Uruguay': 'Montevideo'
}

print(capitales.get('Uruguay')) # Se imprime la clave del pais que seleccionamos
print(capitales.keys) # Nos trae todas las llaves de cada pais
print(capitales.values()) # Imprime los valores de las clabes del diccionario
print(capitales.items())
capitales.update({'Alemania': 'Berlin'}) # Agregamos un nuevo pais
capitales.pop('Estados Unidos') # Borra una llave
capitales.clear() # Limpia todo el diccionario


for i, y in capitales.items():
    print(f"{i}: {y}")