# Con la Indexacion se logra dividar la cadena de caracteres
# se puede dividir usando el indice de las variables
# se usa upper() o lower() solo para poner en mayuscula o miniscula

nombre = 'ignacio Frachia'

if nombre[0].islower:
    nombre = nombre.capitalize()

print(nombre)

primer_nombre = nombre[0:7].upper()
apellido = nombre[8:].lower()
ultimo_caracter = nombre[-1]

print(primer_nombre)
print(apellido)
print(ultimo_caracter)