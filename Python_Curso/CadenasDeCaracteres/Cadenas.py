nombre = "Ignacio" # String (cadena de texto)

print(len(nombre)) # Imprime la longitud de la cadena de texto (cantidad de caracteres)
print(nombre*6) # Multiplica la variable la cantidad de veces que sea requerida (en este caso, 6 veces)
print(nombre.upper()) # Convierte la cadena de texto a mayúsculas
print(nombre.lower()) # Convierte la cadena de texto a minúsculas
print(nombre.capitalize()) # Convierte la primera letra de la cadena de texto a mayúscula y el resto a minúsculas
print(nombre.replace("a", "o")) # Reemplaza todas las apariciones de "a" por "o" en la cadena de texto
print(nombre.startswith("I")) # Verifica si la cadena de texto comienza con "I"
print(nombre.endswith("o")) # Verifica si la cadena de texto termina con "o"
print(nombre.isalpha()) # Verifica si la cadena de texto solo contiene letras
print(nombre.isdigit()) # Verifica si la cadena de texto solo contiene dígitos
print(nombre.istitle()) # Verifica si la cadena de texto está en formato de título (primera letra de cada palabra en mayúscula)
print(nombre.split()) # Divide la cadena de texto en una lista de palabras (en este caso, solo hay una palabra)
print(nombre.strip()) # Elimina los espacios en blanco al inicio y al final de la cadena de texto (en este caso, no hay espacios)
print(nombre.count("i")) # Cuenta cuántas veces aparece la letra "i" en la cadena de texto
print(nombre.find("g")) # Devuelve el índice de la primera aparición de la letra "g" en la cadena de texto (en este caso, 1)
print(nombre.rfind("i")) # Devuelve el índice de la última aparición de la letra "i" en la cadena de texto (en este caso, 3)
